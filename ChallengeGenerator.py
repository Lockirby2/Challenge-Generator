import traceback
import random
from Restriction import Restriction
from Config import Config
from benedict import benedict
from collections import defaultdict

# Manages the generation of the challenge
def main():
    # Starting text
    print("Welcome to the Ultimate Challenge Generator (TM)!")
    print("")
    config = Config(benedict.from_yaml("Config.yaml"))
    
    # Get restrictions from YAML
    yaml_restrictions = benedict.from_yaml(config.game + "/Restrictions.yaml").get("values")
    all_restrictions = list(map(lambda yaml_restriction: Restriction(yaml_restriction), yaml_restrictions))
    
    # Get conflicting tags from YAML
    yaml_tag_conflicts = benedict.from_yaml(config.game + "/Conflicts.yaml").get("values")
    conflicting_tag_dict = defaultdict(list)
    for tag_conflict in yaml_tag_conflicts:
        first = tag_conflict.get("first")
        second = tag_conflict.get("second")
        
        conflicting_tag_dict[first].append(second)
        if first != second:
            conflicting_tag_dict[second].append(first)
    
    chosen_restrictions = []
    total_difficulty = 0
    
    # Determines if restriction should be removed based on the restriction that was last chosen
    def should_remove_restriction(restriction, chosen_restriction):
        conflicting_tags = []
        for tag in chosen_restriction.tags:
            conflicting_tags.extend(conflicting_tag_dict[tag])
    
        return (
            restriction == chosen_restriction or
            any(conflicting_tag in restriction.tags for conflicting_tag in conflicting_tags) or
            restriction.difficulty + total_difficulty > config.target_difficulty
        )
        
    def choose_restriction(restrictions):
        nonlocal total_difficulty
        nonlocal all_restrictions
    
        chosen_restriction = chooseByWeight(restrictions)
        chosen_restrictions.append(chosen_restriction)
        
        total_difficulty += chosen_restriction.difficulty
        all_restrictions = [r for r in all_restrictions if not should_remove_restriction(r, chosen_restriction)]
    
    # Add limiting restriction if necessary
    if config.mandate_limiting:
        limiting_restrictions = [r for r in all_restrictions if r.is_limiting]
        if limiting_restrictions:
            choose_restriction(limiting_restrictions)
        else:
            print("A limiting restriction should have been chosen, but there are no limiting restrictions.")
            print("")
    
    # Choose restrictions
    while len(all_restrictions) > 0 and len(chosen_restrictions) < config.max_restrictions:
        choose_restriction(all_restrictions)
        
    # Print restrictions
    if len(chosen_restrictions) == 0:
        print("You messed something up in the config and no restrictions are valid. Go fix it!")
    else:
        print("Your challenge is as follows:")
        print("")
        for restriction in chosen_restrictions:
            print(restriction.name + " : " + restriction.message)
        
    # Final message
    print("")
    print("Good luck and have fun! Press Enter to exit")
    input()
    
def chooseByWeight(restrictions): # Chooses a restriction randomly; restrictions with a higher weight are more likely to get picked
    weights = map(lambda restriction: restriction.weight, restrictions)
    return random.choices(restrictions, weights=weights, k=1)[0]

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        traceback.print_exc()
        print("")
        print("Something went wrong! Oopsie poopsie! Press Enter to exit.")
        input()