-- Shift Supervisor: Molecular Coroutine Scheduler
-- Manages parallel molecular reactions using coroutines

local CoroutineScheduler = {}
CoroutineScheduler.__index = CoroutineScheduler

function CoroutineScheduler:new(max_workers)
    local scheduler = {
        workers = {},
        max_workers = max_workers or 10,
        active_count = 0,
        completed_count = 0,
        failed_count = 0,
        task_queue = {},
        results = {}
    }
    setmetatable(scheduler, self)
    return scheduler
end

function CoroutineScheduler:create_molecular_worker(reaction_function, params)
    return coroutine.create(function()
        local success, result = pcall(reaction_function, params)
        return {success = success, result = result, worker_id = params.worker_id}
    end)
end

function CoroutineScheduler:schedule_reaction(reaction_function, params)
    if self.active_count >= self.max_workers then
        table.insert(self.task_queue, {func = reaction_function, params = params})
        return false
    end
    
    params.worker_id = params.worker_id or ("worker_" .. tostring(#self.workers + 1))
    local worker = self:create_molecular_worker(reaction_function, params)
    
    table.insert(self.workers, {
        coroutine = worker,
        worker_id = params.worker_id,
        status = "running",
        start_time = os.clock()
    })
    
    self.active_count = self.active_count + 1
    return true
end

function CoroutineScheduler:process_reactions()
    local completed_workers = {}
    
    for i, worker_info in ipairs(self.workers) do
        if worker_info.status == "running" then
            local success, result = coroutine.resume(worker_info.coroutine)
            
            if coroutine.status(worker_info.coroutine) == "dead" then
                worker_info.status = "completed"
                worker_info.end_time = os.clock()
                worker_info.execution_time = worker_info.end_time - worker_info.start_time
                
                if success and result then
                    self.results[worker_info.worker_id] = result
                    self.completed_count = self.completed_count + 1
                else
                    self.failed_count = self.failed_count + 1
                end
                
                table.insert(completed_workers, i)
                self.active_count = self.active_count - 1
            end
        end
    end
    
    -- Remove completed workers
    for i = #completed_workers, 1, -1 do
        table.remove(self.workers, completed_workers[i])
    end
    
    -- Process queued tasks
    while self.active_count < self.max_workers and #self.task_queue > 0 do
        local task = table.remove(self.task_queue, 1)
        self:schedule_reaction(task.func, task.params)
    end
    
    return {
        active = self.active_count,
        completed = self.completed_count,
        failed = self.failed_count,
        queued = #self.task_queue
    }
end

function CoroutineScheduler:get_molecular_statistics()
    return {
        total_workers_created = self.completed_count + self.failed_count + self.active_count,
        success_rate = self.completed_count / math.max(1, self.completed_count + self.failed_count),
        average_execution_time = self:calculate_average_execution_time(),
        molecular_throughput = self:calculate_throughput()
    }
end

function CoroutineScheduler:calculate_average_execution_time()
    local total_time = 0
    local count = 0
    for _, result in pairs(self.results) do
        if result.execution_time then
            total_time = total_time + result.execution_time
            count = count + 1
        end
    end
    return count > 0 and (total_time / count) or 0
end

function CoroutineScheduler:calculate_throughput()
    return self.completed_count / math.max(1, os.clock())
end

return CoroutineScheduler
