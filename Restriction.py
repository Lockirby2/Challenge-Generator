class Restriction(object):
    def __init__(self, yaml_restriction): # Initialize the restriction
        self.name = yaml_restriction.get("name") # Friendly name for the restriction
        self.tags = yaml_restriction.get("tags")
        self.weight = yaml_restriction.get("weight") # If the weight is higher, the restriction is more likely to be applied
        self.difficulty = yaml_restriction.get("difficulty") # The difficulty of this restriction
        self.message = yaml_restriction.get("message")
        self.is_limiting = yaml_restriction.get("limiting")