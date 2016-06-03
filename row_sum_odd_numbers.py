def main():
    print row_sum_odd_numbers.__doc__

def row_sum_odd_numbers(n):
    """
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
