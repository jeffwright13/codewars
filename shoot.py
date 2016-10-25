def main():
    print shoot.__doc__

def shoot(results):
    """
    https://www.codewars.com/kata/clay-pigeon-shooting

    Pete and his mate Phil are out in the countryside shooting clay pigeons with a shotgun - amazing fun.

    They decide to have a competition. 3 rounds, 2 shots each. Winner is the one with the most hits.

    Some of the clays have something attached to create lots of smoke when hit, guarenteed by the packaging to generate 'real excitement!' (genuinely this happened). None of the explosive things actually worked, but for this kata lets say they did.

    For each round you will receive the following format:

    [{P1:'XX', P2:'XO'}, true]

    That is an array containing an object and a boolean. Pl represents Pete, P2 represents Phil. X represents a hit and O represents a miss. If the boolean is true, any hit is worth 2. If it is false, any hit is worth 1.

    Find out who won. If it's Pete, return 'Pete Wins!'. If it is Phil, return 'Phil Wins!'. If the scores are equal, return 'Draw!'.

    Note that as there are three rounds, the actual input (x) will look something like this:

    [[{P1:'XX', P2:'XO'}, true], [{P1:'OX', P2:'OO'}, false], [{P1:'XX', P2:'OX'}, true]]
    """
    P1_score = P2_score = 0

    for result in results:
        if result[1] == True:
            mult = 2
        else:
            mult = 1
        P1_score += result[0]['P1'].count('X') * mult
        P2_score += result[0]['P2'].count('X') * mult
    
    if P1_score > P2_score:
        return 'Pete Wins!'
    elif P2_score > P1_score:
        return 'Phil Wins!'
    else:
        return 'Draw!'

def test_shoot():
    assert shoot([[{"P1":"XX", "P2":"XO"}, True], [{"P1":"OX", "P2":"OO"}, False], [{"P1":"XX", "P2":"OX"}, True]]) == "Pete Wins!"
    assert shoot([[{"P1":"XX", "P2":"XO"}, False], [{"P1":"OX", "P2":"XX"}, False], [{"P1":"OO", "P2":"XX"}, True]]) == "Phil Wins!"
    assert shoot([[{"P1":"OO", "P2":"XX"}, False], [{"P1":"OO", "P2":"XX"}, False], [{"P1":"XX", "P2":"OO"}, True]]), "Draw!"

if __name__ == "__main__":
    main()
