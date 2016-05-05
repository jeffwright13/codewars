def main():
    print serve.__doc__

def serve(food, flavour, mouths):
    """
    Story:
    ======
    You are a cook in an alien restaurant at a distant planet called Kahumo. These aliens have some specific physiology features:
        Aliens eat only one type of food in one day.
        Each food has a special factor called flavour (let's designate it as k hereafter).
        Each alien has several mouths of different size. The amount of food each mouth eats depends on mouth number. Second mouth must eat exactly k times more than the first, third mouth must eat exactly k times more than the second, etc. (For example, if k is 2, and the first mouth ate 1 kg of food, second mouth must eat 2 * 1 = 2 kg of food, third eats 2 * 2 = 4 kg of food, fourth eats 2 * 4 = 8 kg, etc.)

    Food on Kahumo is very valuable and spoils fast. This means that if a client orders a certain amount of food, you have to serve it all in the exact proportions required for each of your client's mouths. If any of client's mouths eats less or more than requested, client will feel pain in his stomach, and may spray your eyes with his mildly acidic emotion fluid (which also is kahumoling saliva) as a sign of disrespect. (Please, not again, this juice in my eyes makes me sick!)

    Kahumolings have very sensitive tongues, but not absolutely sensitive. They can feel deviations within 9 grams. This means that if you serve your client 100.005 kg of food instead of 100.000, the kahumoling will probably not notice.
    
    Function features:
    ==================
    Arguments:
        food is the amount of food your client has ordered.
        flavour is the k-factor of the food your client ordered.
        mouths is the amount of mouths of your client.

    Return format:
        [x, y, z, ...], where values correspond to the amount of food served to a certain mouth (float; you can round it to 3 decimal places) in ascending order (low to high).

    Tests:
    ======
        Number of served mouths must correspond to the number of mouths your client has.
        Total amount of food must correspond to the amount ordered by your client.
        Each next mouth must receive exactly k times more food than the previous.

    Comments:
    =========
    This problem can be summarized as follows:
    Find the 'seed' amount r such that
    
                  |(m-1)
    f = r*SUM(k^n)|
                  |(n=0)
    
    ==> solving for r:
    
    f / rSUM(k^n)
    """
    f = float(food)
    k = float(flavour)
    m = int(mouths)
    
    sum = 0
    out = []
    for n in range(0, m):
        sum += k ** n
        out.append(k ** n)
    r = f / sum
    return [round(r * elem, 3) for elem in out]

def test_serve():
    assert serve(31, 2, 5)    == [1.0, 2.0, 4.0, 8.0, 16.0]
    assert serve(728, 3, 6)   == [2.0, 6.0, 18.0, 54.0, 162.0, 486.0]
    assert serve(100, 1.5, 3) == [21.053, 31.579, 47.368]

if __name__ == "__main__":
    main()
