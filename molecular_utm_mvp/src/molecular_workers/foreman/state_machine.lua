-- Foreman: Molecular State Machine
-- Manages UTM state transitions using closures

local StateMachine = {}
StateMachine.__index = StateMachine

function StateMachine:new(initial_state)
    local machine = {
        current_state = initial_state or "q0",
        transition_table = {},
        state_history = {},
        halted = false,
        step_count = 0
    }
    setmetatable(machine, self)
    return machine
end

function StateMachine:add_transition(state, symbol, new_state, write_symbol, direction)
    local key = state .. ":" .. tostring(symbol)
    self.transition_table[key] = {
        new_state = new_state,
        write_symbol = write_symbol,
        direction = direction
    }
end

function StateMachine:create_transition_function()
    local transition_table = self.transition_table
    local machine = self
    
    return function(current_state, input_symbol)
        local key = current_state .. ":" .. tostring(input_symbol)
        local transition = transition_table[key]
        
        if not transition then
            machine.halted = true
            return nil
        end
        
        -- Record state history
        table.insert(machine.state_history, {
            from_state = current_state,
            input_symbol = input_symbol,
            to_state = transition.new_state,
            write_symbol = transition.write_symbol,
            direction = transition.direction,
            step = machine.step_count
        })
        
        machine.current_state = transition.new_state
        machine.step_count = machine.step_count + 1
        
        return transition
    end
end

function StateMachine:is_halted()
    return self.halted
end

function StateMachine:get_state_statistics()
    local stats = {}
    for _, history_entry in ipairs(self.state_history) do
        local state = history_entry.from_state
        stats[state] = (stats[state] or 0) + 1
    end
    return stats
end

function StateMachine:molecular_state_analysis()
    -- Analyze molecular state configurations
    return {
        total_steps = self.step_count,
        unique_states = self:count_unique_states(),
        transition_complexity = self:calculate_complexity(),
        molecular_efficiency = self:calculate_efficiency()
    }
end

function StateMachine:count_unique_states()
    local unique = {}
    for _, entry in ipairs(self.state_history) do
        unique[entry.from_state] = true
        unique[entry.to_state] = true
    end
    local count = 0
    for _ in pairs(unique) do count = count + 1 end
    return count
end

function StateMachine:calculate_complexity()
    return #self.state_history / math.max(1, self:count_unique_states())
end

function StateMachine:calculate_efficiency()
    if self.step_count == 0 then return 0 end
    return 1.0 / self.step_count
end

return StateMachine
