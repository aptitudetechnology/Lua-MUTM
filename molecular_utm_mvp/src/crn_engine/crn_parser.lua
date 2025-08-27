-- CRN Engine: Chemical Reaction Network Parser
-- Parses and validates CRN specifications

local CRNParser = {}
CRNParser.__index = CRNParser

function CRNParser:new()
    local parser = {
        reactions = {},
        species = {},
        initial_concentrations = {},
        rate_constants = {}
    }
    setmetatable(parser, self)
    return parser
end

function CRNParser:parse_reaction_string(reaction_str)
    -- Parse reaction format: "A + B -> C + D, rate=0.1"
    local reactants_str, products_str, rate_str = reaction_str:match("([^->]+)->([^,]+),?%s*rate=([%d%.]+)")
    
    if not reactants_str or not products_str then
        error("Invalid reaction format: " .. reaction_str)
    end
    
    local reactants = self:parse_species_list(reactants_str)
    local products = self:parse_species_list(products_str)
    local rate = tonumber(rate_str) or 1.0
    
    return {
        reactants = reactants,
        products = products,
        rate = rate,
        id = #self.reactions + 1
    }
end

function CRNParser:parse_species_list(species_str)
    local species = {}
    for species_name in species_str:gmatch("([%w_]+)") do
        species_name = species_name:gsub("^%s+", ""):gsub("%s+$", "")
        table.insert(species, species_name)
        self.species[species_name] = true
    end
    return species
end

function CRNParser:add_reaction(reaction_str)
    local reaction = self:parse_reaction_string(reaction_str)
    table.insert(self.reactions, reaction)
    return reaction
end

function CRNParser:set_initial_concentration(species, concentration)
    self.initial_concentrations[species] = concentration
end

function CRNParser:get_species_list()
    local species_list = {}
    for species in pairs(self.species) do
        table.insert(species_list, species)
    end
    table.sort(species_list)
    return species_list
end

function CRNParser:validate_network()
    local validation_results = {
        valid = true,
        errors = {},
        warnings = {}
    }
    
    -- Check for species without initial concentrations
    for species in pairs(self.species) do
        if not self.initial_concentrations[species] then
            table.insert(validation_results.warnings, 
                "Species '" .. species .. "' has no initial concentration (defaulting to 0)")
            self.initial_concentrations[species] = 0
        end
    end
    
    -- Check for reactions with zero rates
    for _, reaction in ipairs(self.reactions) do
        if reaction.rate <= 0 then
            table.insert(validation_results.errors,
                "Reaction " .. reaction.id .. " has non-positive rate: " .. reaction.rate)
            validation_results.valid = false
        end
    end
    
    return validation_results
end

return CRNParser
