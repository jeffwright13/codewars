def fibonacci(n):
    if n<0:
        return None
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def test_fibonacci():
    assert fibonacci(-1) == None
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(6) == 8
    assert fibonacci(13) == 233
    assert fibonacci(20) == 6765
    assert fibonacci(38) == 39088169
