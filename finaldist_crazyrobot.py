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
    curr_pos = [init_pos[0], init_pos[1]]

    for move in moves:
        if move[0] == 'R':
            curr_pos[0] += move[1]
        if move[0] == 'L':
            curr_pos[0] -= move[1]
        if move[0] == 'U':
            curr_pos[1] += move[1]
        if move[0] == 'D':
            curr_pos[1] -= move[1]

    print 'Final pos:', curr_pos
    dist_x = curr_pos[0] - init_pos[0]
    dist_y = curr_pos[1] - init_pos[1]
    return round((dist_x**2 + dist_y**2) ** 0.5, 4)

def test_finaldist_crazyrobot():
    assert finaldist_crazyrobot([('R', 2), ('U', 3), ('L', 1), ('D', 6)], (0, 0)) == 3.1623
    assert finaldist_crazyrobot([('R', 32), ('D', 16), ('U', 31), ('L', 26), ('D', 14),('U', 4), ('R', 5), ('L', 16)], (20, 18)) == 7.0711

if __name__ == "__main__":
    main()
