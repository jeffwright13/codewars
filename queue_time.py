def main():
    print queue_time.__doc__

def queue_time(customers, n):
    """
    https://www.codewars.com/kata/the-supermarket-queue

    There is a queue for the self-checkout tills at the supermarket. Your task is write a queue_time to calculate the total time required for all the customers to check out!

    The queue_time has two input variables:

        customers: an array (list in python) of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
        n: a positive integer, the number of checkout tills.

    The queue_time should return an integer, the total time required.

    Assume that the front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free. So, for example:

    queue_time([5,3,4], 1)
    # should return 12
    # because when n=1, the total time is just the sum of the times

    queue_time([10,2,3,3], 2)
    # should return 10
    # because here n=2 and the 2nd, 3rd, and 4th people in the 
    # queue finish before the 1st person has finished.

    N.B. You should assume that all the test input will be valid, as specified above.

    P.S. The situation in this kata can be likened to the more-computer-science-related idea of a thread pool, with relation to running multiple processes at the same time: https://en.wikipedia.org/wiki/Thread_pool
    """
    return n

def test_queue_time():
    assert queue_time([], 1) == 0
    assert queue_time([5], 1) == 5
    assert queue_time([2], 5) == 2
    assert queue_time([1,2,3,4,5], 1) == 15
    assert queue_time([1,2,3,4,5], 100) == 5
    assert queue_time([1,2,3,4,5], 3) == 7
    assert queue_time([2,2,3,3,4,4], 2) == 9

if __name__ == "__main__":
    main()
