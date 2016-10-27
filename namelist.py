def main():
    print namelist.__doc__

def namelist(n):
    """
    https://www.codewars.com/kata/format-a-string-of-names-like-bart-lisa-and-maggie/

    Given: an array containing hashes of names

    Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

    Examples:

    namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
    # returns 'Bart, Lisa & Maggie'
    namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
    # returns 'Bart & Lisa'
    namelist([ {'name': 'Bart'} ])
    # returns 'Bart'
    namelist([])
    # returns ''

    Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.
    """
    print "names:", names
    if len(names) == 0:
        return ''
    if len(names) == 1:
        return names[name[0]]
        
    out = []
    
    return ','.join(out[:-1]) + '&' + out[-1]

def test_namelist():
    assert namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer & Marge'
    assert namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]) == 'Bart, Lisa & Maggie',
    assert namelist([{'name': 'Bart'},{'name': 'Lisa'}]) == 'Bart & Lisa', 
    assert namelist([{'name': 'Bart'}]) == 'Bart'
    assert namelist([]) == ''

if __name__ == "__main__":
    main()
