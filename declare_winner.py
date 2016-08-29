class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

def declare_winner(fighter1, fighter2, first_attacker):
    print "Fighters:", fighter1.name, fighter2.name, "\nFirst attacker:", first_attacker
    
    if first_attacker != fighter1.name and first_attacker != fighter2.name:
        return "First attacker has to be part of the fight!"

    

def test_declare_winner():
	assert (declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew"), "Lew") == "Lew"
