def main():
    """
    http://www.codewars.com/kata/56055244356dc5c45c00001e/train/python

    The Brief
    =========
    Microsoft Excel provides a number of useful functions for counting, summing, and averaging values if they meet a certain criteria. Your task is to write three functions that work similarly to Excel's COUNTIF, SUMIF and AVERAGEIF functions.

    Specifications
    ==============
    Each function will take the same two arguments:

    A list object containing values to be counted, summed, or averaged.
    A criteria in either an integer, float, or string
    Integer or float indicates equality
    Strings can indicate >, >=, <, <= or <> (use the Excel-style "Not equal to" operator) to a number (ex. ">=3"). In the count_if function, a string without an operater indicates equality to this string.
    The tests will all include properly formatted inputs. The test cases all avoid rounding issues associated with floats.

    Examples
    ========
    count_if([1,3,5,7,9], 3)
    1

    count_if(["John","Steve","John"], "John")
    2

    sum_if([2,4,6,-1,3,1.5],">0")
    16.5

    average_if([99,95.5,0,83],"<>0")
    92.5
    """
    pass

def count_if(values, criteria):
    return n

def test_countif():
    assert count_if(1,3,5,7,9], 3) == 1
    assert count_if(["John","Steve","John"], "John") == 2

def sum_if(values, criteria):
    return n

def test_sumif():
    assert sum_if([2,4,6,-1,3,1.5],">0") == 16.5

def average_if(values, criteria):
    return n

def test_averageif():
    assert average_if([99,95.5,0,83],"<>0") == 92.5

if __name__ == "__main__":
    main()
