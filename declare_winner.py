'''
https://www.codewars.com/kata/two-fighters-one-winner

Create a function that returns the name of the winner in a fight between two fighters.

Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.
'''
class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

def declare_winner(Fighter1, Fighter2, first_attacker):
    #print "Fighters:", Fighter1.name, Fighter2.name, "\nFirst attacker:", first_attacker
    
    if first_attacker != Fighter1.name and first_attacker != Fighter2.name:
        return "First attacker has to be part of the fight!"

    current_attacker = first_attacker
    winner = ''
    while (True):
        if current_attacker == Fighter1.name:
            Fighter2.health -= Fighter1.damage_per_attack
            if Fighter2.health <= 0:
                winner = Fighter1.name
                break
            current_attacker = Fighter2.name
        else:
            Fighter1.health -= Fighter2.damage_per_attack
            if Fighter1.health <= 0:
                winner = Fighter2.name
                break
            current_attacker = Fighter1.name
    return winner

def test_declare_winner():
	assert declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew") == "Lew"
	assert declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Harry") == "Harry"
	assert declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry") == "Harald"
	assert declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald") == "Harald"
	assert declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry") == "Harald"
	assert declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald") == "Harald"
