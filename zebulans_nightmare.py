def main():
    print zebulansNightmare.__doc__

def zebulansNightmare(functionName):
    """
    Zebulan has worked hard to write all his python code in strict compliance to PEP8 rules. In this kata, you are a mischevious hacker that has set out to sabatoge all his good code.

    Your job is to take PEP8 compatible function names and convert them to camelCase. For example:

    zebulansNightmare('camel_case') == 'camelCase'
    zebulansNightmare('zebulans_nightmare') == 'zebulansNightmare'
    zebulansNightmare('get_string') == 'getString'
    zebulansNightmare('convert_to_uppercase') == 'convertToUppercase'
    zebulansNightmare('main') == 'main'
    """
    l = list(functionName)
    underscores = []
    for char in range(len(l)):
        if l[char] == '_':
            underscores.append(char)
    
    underscores.reverse()
    print "underscores:", underscores
    for index in underscores:
        if index + 1 == len(l):
            l.pop(index)
        else:
            l.pop(index)
            l[index] = l[index].upper()
            
    return ''.join(l)

def test_zebulansNightmare():
    assert zebulansNightmare('camel_case_')     == 'camelCase'
    assert zebulansNightmare('mark_as_issue')   == 'markAsIssue'
    assert zebulansNightmare('repeat')          == 'repeat'
    assert zebulansNightmare('main')            == 'main'
    assert zebulansNightmare('copy_paste_pep8') == 'copyPastePep8'
    assert zebulansNightmare('goto_next_kata')  == 'gotoNextKata'

if __name__ == "__main__":
    main()
