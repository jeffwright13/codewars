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
    print "Contestants:", contestants, type(contestants)
    def valid(*args):
        print "args:", args, len(args), type(args)
        # ensure exactly 3 candidates are playing
        if len(args) != 3:
            return False
        # ensure each candidate rolled once or twice
        
        # ensure each candidate's scores are valid
        
        # ensure each candidate has valid name

    if not valid(contestants):
        return False

    for contestant in contestants:
        print "contestant:", contestant, type(contestant)
        

def test_winner():
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
    assert winner([c1]) == False
    assert winner([c1, c2, c3, c4]) == False
    assert winner([c1, c2, c3]) == 'Bill'
    
if __name__ == "__main__":
    main()
