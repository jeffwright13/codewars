def main():
    test_processes = [
        ['gather', 'field', 'wheat'],
        ['bake', 'flour', 'bread'],
        ['mill', 'wheat', 'flour']]
    processes('field', 'bread', test_processes)

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
    end_things = [processes[x][2] for x in range(len(processes))]
    if start == end or end not in end_things:
        return []

    seq = []
    seen = 0
    inp = ''
    out = ''
    do  = ''
    
    for i in range(len(processes)):
        if processes[i][2] == end:
            out = processes[i][2]
            inp = processes[i][1]
            do  = processes[i][0]
            seq.append(do)
            seen += 1
            break

    while seen < len(processes):
        for i in range(len(processes)):
            if processes[i][2] == inp:
                out  = processes[i][2]
                inp  = processes[i][1]
                do   = processes[i][0]
                seq.append(do)
                seen += 1

    seq.reverse()
    return seq

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
