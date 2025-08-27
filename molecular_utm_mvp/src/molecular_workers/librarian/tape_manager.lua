-- Librarian: Molecular Tape Manager
-- Manages UTM tape operations using Lua tables

local TapeManager = {}
TapeManager.__index = TapeManager

function TapeManager:new(initial_size)
    local tape = {
        data = {},
        position = 0,
        size = initial_size or 1000,
        bounds = {left = 0, right = 0}
    }
    setmetatable(tape, self)
    return tape
end

function TapeManager:read()
    return self.data[self.position] or 0
end

function TapeManager:write(symbol)
    self.data[self.position] = symbol
    self.bounds.left = math.min(self.bounds.left, self.position)
    self.bounds.right = math.max(self.bounds.right, self.position)
end

function TapeManager:move_left()
    self.position = self.position - 1
end

function TapeManager:move_right()
    self.position = self.position + 1
end

function TapeManager:get_tape_segment(start_pos, end_pos)
    local segment = {}
    for i = start_pos, end_pos do
        segment[i] = self.data[i] or 0
    end
    return segment
end

function TapeManager:optimize_storage()
    -- Molecular memory optimization
    local compacted = {}
    for pos, symbol in pairs(self.data) do
        if symbol ~= 0 then
            compacted[pos] = symbol
        end
    end
    self.data = compacted
end

return TapeManager
