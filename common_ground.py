def main():
    print common_ground.__doc__

def common_ground(s1, s2):
    """
    Two samurai generals are discussing dinner plans after a battle, but they can't seem to agree.

    The discussion gets heated and you are cannot risk favoring either of them as this might damage your political standing with either of the two clans the samurai generals belong to. Thus, the only thing left to do is find what the common ground of what they are saying is.

    Compare the proposals using the function commonGround(string a, string b) that outputs a string containing the words in string a that also occur in string b.

    Each word in the resulting string shall occur once, and the order of the words follow the order of the first occurence of each word in the second string.

    If they are saying nothing in common, kill both samurai and blame a ninja. (output "death")
    """
    return None

def test_common_ground():
    assert common_ground("eat chicken", "eat chicken and rice") == 'eat chicken'
    assert common_ground("eat a burger and drink a coke", "drink a coke") == 'drink a coke'
    assert common_ground("i like turtles", "what are you talking about") == 'death'
    assert common_ground("aa bb cc", "bb cc bb aa") == 'bb cc aa'

if __name__ == "__main__":
    main()
