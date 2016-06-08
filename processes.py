def main():
    print processes.__doc__

def processes(n):
    """
    In this task you have to code process planner.

    You will be given initial thing, target thing and a set of processes to turn one thing into another (in the form of [process_name, start_thing, end_thing]). You must return names of shortest sequence of processes to turn initial thing into target thing, or empty sequence if it's impossible.

    If start already equals end, return [], since no path is required.

    Example: 
    test_processes = [
        ['gather', 'field', 'wheat'],
        ['bake', 'flour', 'bread'],
        ['mill', 'wheat', 'flour']
    ];

    processes('field', 'bread', test_processes) # should return ['gather', 'mill', 'bake']
    processes('field', 'ferrari', test_processes) # should return []
    processes('field', 'field', test_processes) # should return [], since no processes are needed
    """
    pass


def test_processes():
    assert processes(0) == None
    assert processes(1) == "*\n"
    assert processes(2) == None
    assert processes(3) == " *\n***\n *\n"
    assert processes(4) == None
    assert processes(5) == "   *\n  ***\n*****\n  ***\n   *\n"

if __name__ == "__main__":
    main()
