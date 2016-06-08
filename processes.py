def main():
    print processes.__doc__

def processes(start, end, processes):
    """
    In this task you have to code process planner.

    You will be given initial thing, target thing and a set of processes to turn one thing into another (in the form of [process_name, start_thing, end_thing]). You must return names of shortest sequence of processes to turn initial thing into target thing, or empty sequence if it's impossible.

    If start already equals end, return [], since no path is required.

    Example:
    ========
    test_processes = [
        ['gather', 'field', 'wheat'],
        ['bake', 'flour', 'bread'],
        ['mill', 'wheat', 'flour']
    ];

    processes('field', 'bread', test_processes) # should return ['gather', 'mill', 'bake']
    processes('field', 'ferrari', test_processes) # should return []
    processes('field', 'field', test_processes) # should return [], since no processes are needed
    """
    # print "start, end, processes:", start, end, processes
    end_things = [processes[x][2] for x in range(len(processes))]
    if start == end or start not in end_things:
        return []

    seq = []
    want = need = do = ''
    for i in range(len(processes)):
        if processes[i][2] == start:
            want = processes[i][2]
            need = processes[i][1]
            do   = processes[i][0]
            seq.append(do)
            break

    for i in range(len(processes)):
        if processes[i][2] == need:
            want = processes[i][2]
            need = processes[i][1]
            do   = processes[i][0]
            seq.append(do)

    return seq.reverse()

def test_processes():
    test_processes = [
        ['gather', 'field', 'wheat'],
        ['bake', 'flour', 'bread'],
        ['mill', 'wheat', 'flour']]

    assert processes('field', 'field', test_processes) == []
    assert processes('field', 'ferrari', test_processes) == []
    assert processes('field', 'bread', test_processes) == ['gather', 'mill', 'bake']

if __name__ == "__main__":
    main()
