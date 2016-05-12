def main():
    print winner.__doc__

def winner(contestants):
    """
    Three candidates take part in a TV show. In order to decide who will take part in the final game and probably become rich, they have to roll the Wheel of Fortune!

    The Wheel of Fortune is divided into 20 sections, each with a number from 5 to 100 (only mulitples of 5).

    Each candidate can roll the wheel once or twice and sum up the score of each roll. The winner one that is closest to 100 (while still being lower or equal to 100). In case of a tie, the candidate that rolled the wheel first wins.

    You receive the information about each candidate as an array of objects: each object should have a name and a scores array with the candidate roll values.

    Your solution should return the name of the winner, or false if there is no winner (all scored more than 100).

    Example:

    c1 = {"name": "Bob", "scores": [10, 65]}
    c2 = {"name": "Bill", "scores": [90, 5]}
    c3 = {"name": "Charlie", "scores": [40, 55]}
    winner([c1, c2, c3]) #Returns "Bill"

    Please note that inputs may be invalid: in this case, the function should return false.

    Potential errors derived from the specifications are: - More or less than three candidates take part in the game. - A candidate did not roll the wheel or rolled it more than twice. - Scores are not valid. - Invalid user entry (no name or no score).
    """
    # Check validity of contestants
    if len(contestants) != 3:
        print 'Need exactly 3 contestants; was provided ', len(contestants)
        return False
    for contestant in contestants:
        if not 'name' in contestant:
            print 'Contestant', contestant, 'needs a name'
            return False
        if not 'scores' in contestant:
            print 'Contestant', contestant, 'needs scores'
            return False
        if len(contestant['scores']) not in (1, 2):
            print 'Contestant "' + contestant['name'] + '" needs 1 or 2 scores'
            return False
        if len(contestant['name']) <= 0:
            print 'Contestant', contestant, 'needs a valid name'
            return False
        for score in contestant['scores']:
            if score not in range(5,101,5):
                print 'Contestant', contestant['name'], 'has invalid scores'
                return False

    # Contestant list provided is OK; now process scores and return winner
    high_score = 0
    winner = ''
    for contestant in contestants:
        score = 0
        for s in contestant['scores']:
            score += s
        if score > 100:
            continue
        if score > high_score:
            high_score = score
            winner = contestant['name']
    if winner == '':
        return False
    else:
        return winner

def test_winner():
    c0 = {'name': '', 'scores': []}
    c1 = {'name':"Bob", 'scores':[10, 65] }
    c2 = {'name':"Bill", 'scores':[90, 5] }
    c3 = {'name':"Jennifer", 'scores':[55] }
    c4 = {'name':"John", 'scores':[5, 15] }
    c5 = {'name':"Brad", 'scores':[3, 15] }
    c6 = {'name':"Laurel", 'scores':[5, 12] }
    c7 = {'name':"Charlie", 'scores':[5, 105] }
    c8 = {'name':"Paul", 'scores':[80, 25] }
    c9 = {'name':"Marc", 'scores':[80, 25] }
    c10 = {'name':"Oliver", 'scores':[80, 25] }
    c11 = {'name':"Bruce", 'scores':[] }
    c12 = {'name':"Alfred", 'scores':[10, 15, 20] }
    c13 = {'scores':[10, 20] }
    c14 = {'name':"Cheater" }
    c15 = {'name':"Robert", 'scores':[45] }
    c16 = {'name':"Rob", 'scores':[40, 45] }
    c17 = {'name':"Ned", 'scores':[10] }
    c18 = {'name':"Gandalf", 'scores':[85] }

    assert winner([]) == False
    assert winner([c0, c0, c0]) == False
    assert winner([c1]) == False
    assert winner([c1, c2, c3, c4]) == False
    assert winner([c1, c2, c3]) == 'Bill'
    assert winner([c1, c11, c3]) == False
    assert winner([c8, c9, c10]) == False
    assert winner([c16, c17, c18]) == 'Rob'
    assert winner([c1, c2, c13]) == False
    assert winner([c1, c2, c14]) == False
    assert winner([c5, c6, c7]) == False
    assert winner([c12, c15, c16]) == False
    
if __name__ == "__main__":
    main()
