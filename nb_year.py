def main():
    print function.__doc__

def function(p0, percent, aug, p):
    """
    https://www.codewars.com/kata/growth-of-a-population/

    In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater or equal to p = 1200 inhabitants?

    At the end of the first year there will be: 
    1000 + 1000 * 0.02 + 50 => 1070 inhabitants

    At the end of the 2nd year there will be: 
    1070 + 1070 * 0.02 + 50 => 1141 inhabitants (number of inhabitants is an integer)

    At the end of the 3rd year there will be:
    1141 + 1141 * 0.02 + 50 => 1213

    It will need 3 entire years.

    More generally given parameters:

    p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)

    the function nb_year should return n number of entire years needed to get a population greater or equal to p.

    aug is an integer (> 0), percent a positive or null floating number, p0 and p are positive integers (> 0)

    Examples:
    nb_year(1500, 5, 100, 5000) -> 15
    nb_year(1500000, 2.5, 10000, 2000000) -> 10

    Note: Don't forget to convert the percent parameter as a percentage in the body of your function: if the parameter percent is 2 you have to convert it to 0.02.
    """
    current_pop = p0
    n = 0
    while current_pop < p:
        current_pop = int(current_pop + current_pop*(percent/100.0) + aug)
        n += 1
    return n

def test_function():
    assert function(1000, 2, 50, 1200) == 3
    assert function(1500, 5, 100, 5000) == 15
    assert function(1500000, 2.5, 10000, 2000000) == 10
    assert function(1500000, 0.25, 1000, 2000000) == 94

if __name__ == "__main__":
    main()