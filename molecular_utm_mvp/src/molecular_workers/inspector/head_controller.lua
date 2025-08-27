-- Inspector: Molecular Head Controller
-- Manages read/write head operations using closures

local HeadController = {}
HeadController.__index = HeadController

function HeadController:new(tape_manager)
    local head = {
        tape = tape_manager,
        position = 0,
        state = "idle",
        read_history = {},
        write_history = {}
    }
    setmetatable(head, self)
    return head
end

function HeadController:create_reader()
    local tape = self.tape
    return function()
        local symbol = tape:read()
        table.insert(self.read_history, {
            position = tape.position,
            symbol = symbol,
            timestamp = os.clock()
        })
        return symbol
    end
end

function HeadController:create_writer()
    local tape = self.tape
    return function(symbol)
        tape:write(symbol)
        table.insert(self.write_history, {
            position = tape.position,
            symbol = symbol,
            timestamp = os.clock()
        })
        return true
    end
end

function HeadController:create_mover()
    local tape = self.tape
    return {
        left = function() tape:move_left() end,
        right = function() tape:move_right() end
    }
end

function HeadController:get_operation_history()
    return {
        reads = self.read_history,
        writes = self.write_history
    }
end

function HeadController:molecular_scan(radius)
    -- Simulate molecular environment scanning
    local scan_result = {}
    local current_pos = self.tape.position
    
    for offset = -radius, radius do
        local pos = current_pos + offset
        scan_result[pos] = self.tape.data[pos] or 0
    end
    
    return scan_result
end

return HeadController
