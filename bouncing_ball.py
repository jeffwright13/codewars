def main():
    print bouncing_ball.__doc__

def bouncing_ball(h, bounce, window):
    """
    https://www.codewars.com/kata/bouncing-balls

    A child plays with a ball on the nth floor of a big building the height of which is known

    (float parameter "h" in meters, h > 0) .

    He lets out the ball. The ball rebounds for example to two-thirds

    (float parameter "bounce", 0 < bounce < 1)

    of its height.

    His mother looks out of a window that is 1.5 meters from the ground

    (float parameters window < h).

    How many times will the mother see the ball either falling or bouncing in front of the window

    (return a positive integer unless conditions are not fulfilled in which case return -1) ?

    Note

    You will admit that the ball can only be seen if the height of the rebouncing ball is stricty greater than the window parameter.

    Example:

        h = 3, bounce = 0.66, window = 1.5, result is 3

        h = 3, bounce = 1, window = 1.5, result is -1

    """
    if (h <= 0) or not (0 < bounce < 1) or (h <= window):
        return -1
    
    count = 0
    while h > window:
        count += 1
        h = h*bounce
        if h<window:
            break
        count += 1

    return count

def test_bouncing_ball():
    assert bouncing_ball(3, 1, 1.5) == -1
    assert bouncing_ball(3, 0.66, 1.5) == 3
    assert bouncing_ball(30, 0.66, 1.5) == 15

if __name__ == "__main__":
    main()
