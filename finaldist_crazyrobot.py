def main():
    print finaldist_crazyrobot(None)

def finaldist_crazyrobot(moves, init_pos):
    """
    We want to calculate the final distance from an initial position.
    So we make a function finaldist_crazyrobot() that receives:
    (1) a list of tuples, moves. Each tuple having a direction and the length of the step.
    (2) the initial position, init_pos, that are the coordinates (x0, y0) of the point where the robot is standing before it starts moving.
    
    Ex 1:
    init_pos = (0, 0)
    moves = [('R', 2), ('U', 3), ('L', 1), ('D', 6)]
    finaldist_crazyrobot(moves, init_pos) == 3.16227766017
    
    Ex 2:
    init_pos = (20, 18)
    moves = [('R', 32), ('D', 16), ('U', 31), ('L', 26), ('D', 14),('U', 4), ('R', 5), ('L', 16)]
    finaldist_crazyrobot(moves, init_pos) == 7.07106781187
    # distance from (20, 18) to (15, 23)
    """
    pass

def test_finaldist_crazyrobot():
    assert finaldist_crazyrobot([('R', 2), ('U', 3), ('L', 1), ('D', 6)], (0, 0)) == 3.16227766017
    assert finaldist_crazyrobot([('R', 32), ('D', 16), ('U', 31), ('L', 26), ('D', 14),('U', 4), ('R', 5), ('L', 16)], (20, 18)) == 7.07106781187

if __name__ == "__main__":
    main()
