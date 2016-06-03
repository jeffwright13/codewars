def main():
    print row_sum_odd_numbers.__doc__

def row_sum_odd_numbers(n):
    """
    Given the triangle of consecutive odd numbers:

                 1
              3     5
           7     9    11
       13    15    17    19
    21    23    25    27    29
    ...

    Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

    row_sum_odd_numbers(1); # 1
    row_sum_odd_numbers(2); # 3 + 5 = 8
    """
    return n

def test_row_sum_odd_numbers():
    assert row_sum_odd_numbers(0) == 0
    assert row_sum_odd_numbers(1) == 1
    assert row_sum_odd_numbers(2) == 8
    assert row_sum_odd_numbers(3) == 27
    assert row_sum_odd_numbers(4) == 64
    assert row_sum_odd_numbers(19) == 6859

if __name__ == "__main__":
    main()
