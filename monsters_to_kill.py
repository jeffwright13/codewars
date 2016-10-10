def main():
    print monsters_to_kill.__doc__

def monsters_to_kill(level, multiplier, exp_per_monster):
    """
    https://www.codewars.com/kata/how-many-monsters

    My knight wants to level up. Create a solution which takes as inputs the knight's current level, the level up multiplier, and experience per monster, and outputs the number of monsters needed to kill in order to level up.

    Important information:
    - Level 1 is ALWAYS 100xp
    - Assume that the knight has the Exact ammount of exp for his current level
    - The level up modifier is a number greater than 1, which is multiplied times the experience of the previous level, in order to get the next level
      (example: modifier = 2, lvl 1 = 100xp, lvl 2 = 100xp*2 = 200xp, lvl 3 = 200xp*2 = 400xp, etc.)
    """
    print "level, multiplier, exp_per_monster:", (level, multiplier, exp_per_monster)
    return round(100 * multiplier ** (level-1) / exp_per_monster)

def test_monsters_to_kill():
    assert monsters_to_kill(32,1.0,20) == 5
    assert monsters_to_kill(3,2.0,50) == 8
    assert monsters_to_kill(15,2.5,1000) == 37253

if __name__ == "__main__":
    main()
