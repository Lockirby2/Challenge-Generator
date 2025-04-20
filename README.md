This is an arbitrary RPG challenge run generator.  You can configure a set of restrictions for any RPG in YAML format and then generate a challenge from those descriptions.  For your game, you'll need to add a folder containing both a set of restrictions and a list of which restrictions conflict with each other.  Then you can generate a challenge with the game or give the restrictions to somebody else for their own challenges.  See the FF6 folder for an example.  The restriction format is as follows:

```
name: "No Weapons" # The short name of the restriction
tags: # List out tags with dashes beforehand (used for determining which restrictions conflict with each other)
    - "Equipment"
weight: 1.0 # Higher weight means that the restriction is more likely to appear; a restriction with a weight of 7.0 is 7 times as likely to show up as one with a weight of 1.0
difficulty: 1.0 # Difficulty of a restriction relative to the other restrictions; total difficulty of all restrictions chosen won't exceed the target difficulty
limiting: false # Whether this restriction limits the amount of EXP grinding that is possible
message: "You cannot equip weapons to any character." # Detailed description of the restriction's rules
```

You also need to define which restrictions conflict with each other.

```
In this first case, any restrictions with the tag "Equipment" will conflict with any restrictions with the tag "Heavy Equipment".
If two restrictions conflict, they can't both be chosen at the same time

-
    first: "Equipment"
    second: "Heavy Equipment"

In this second case, any restrictions with the tag "Heavy Equipment" will conflict with other restrictions with the tag "Heavy Equipment".
This means that two restrictions with this tag cannot be added at the same time. Obviously, restrictions don't conflict with themselves.

-
    first: "Heavy Equipment"
    second: "Heavy Equipment"
```
    
Then, when you go to generate the challenge, you'll be asked three questions:

Q: What game do you want to generate a challenge for?
A: Enter the name of your game.  This needs to exactly match the name of the folder that you added the Restrictions/Conflicts to.

Q: What is the maximum number of restrictions that you want?
A: Enter the number.

Q: What is the difficulty that you're aiming for?
A: You need to enter a number.  This one's a bit trickier to answer because the difficulty of the restrictions is defined relative to each other.  You'll likely need to play around with this a bit to discover a number that seems about right before you formally decide to "go for it" and generate your real challenge.  If I ever work on this again, I'll give the person defining the restrictions a way to define numbers for "easy", "medium", and "hard" difficulties to give the player an idea of what number will fit their tastes.

On top of that, there's a config YAML with some additional options:

```
ask_for_input: true # Set to true if asking the player to specify a game, max number of restrictions, and target difficulty before starting. Otherwise, the values from this config will be used instead.
game: FF6 # The game to generate restrictions for
max_restrictions: 7 # The maximum number of restrictions to generate
target_difficulty: 30 # The total difficulty of the game; the total difficulty of all chosen restrictions will not go over this limit.
limiting_chance: 95.0 # The chance of adding a limiting restriction (i.e., a restriction that prevents unlimited EXP grinding); this is a percent
```