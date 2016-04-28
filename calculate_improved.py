def main():
    print calculate_improved.__doc__

def calculate_improved(students):
    """
    Most Improvd - Puzzles #4

    When being graded in a subject or a course high marks are focused on the most but what about most improved? As a computer science teacher you would like to create a function which calculates the most improved students and rank them in a list.

    Task

    Your task is to compelete the function calculate_improved() to return an array sorted by most improved as percentages.

    Input

    The input you will receive will be an array of students; students will be an object containing a name and array of marks (in order of acheived); the marks will be out of 100, a student can however have a mark of null if the test was not attempted (treat this as 0)
    Example of student Object: {name:'Henry, Johns',marks:[25,50]}

    Output

    The output expected will be an array of objects similar to the student object, containing the name and total improvement percentage out of the first and last mark given to calculate the overall improvement percentage. The output array must be sorted by most improved (round the calculated improvement). If there is a tie in improvements, then order by name.
    Example of return Object: {name:'Henry, Johns', improvement:100}
    """
    return None

def test_calculate_improved():

    students=[{'name': 'Henry, Johns', 'marks': [25, 50]}, {'name': 'Timmy, Bug', 'marks': [100, 98]}, {'name': 'George, King', 'marks': [100, 85]}, {'name': 'Finn, Wish', 'marks': [45, 90]}, {'name': 'Lucy Act', 'marks': [55, 100]}]
    assert calculate_improved(students) == [{"name":"Finn, Wish","improvement":100},
    {"name":"Henry, Johns","improvement":100},
    {"name":"Lucy Act","improvement":82},
    {"name":"Timmy, Bug","improvement":-2},
    {"name":"George, King","improvement":-15}]
    
    students=[{'name': 'Henry, Johns', 'marks': [25, 56, 50]}, {'name': 'Timmy, Bug', 'marks': [100, 67, 98]}, {'name': 'George, King', 'marks': [100, 45, 85]}, {'name': 'Finn, Wish', 'marks': [45, 100, 90]}, {'name': 'Lucy Act', 'marks': [55, 0, 100]}]
    assert calculate_improved(students) == [{"name":"Finn, Wish","improvement":100},
    {"name":"Henry, Johns","improvement":100},
    {"name":"Lucy Act","improvement":82},
    {"name":"Timmy, Bug","improvement":-2},
    {"name":"George, King","improvement":-15}]
    
    students=[{'name': 'Henry, Johns', 'marks': [25, 56, 50, 58]}, {'name': 'Timmy, Bug', 'marks': [100, 67, 98, 100]}, {'name': 'George, King', 'marks': [100, 45, 85, 90]}, {'name': 'Finn, Wish', 'marks': [45, 100, 90, 100]}, {'name': 'Lucy Act', 'marks': [55, 0, 100, 6]}]
    assert calculate_improved(students) == [{"name":"Henry, Johns","improvement":132},
    {"name":"Finn, Wish","improvement":122},
    {"name":"Timmy, Bug","improvement":0},
    {"name":"George, King","improvement":-10},
    {"name":"Lucy Act","improvement":-89}]
    
    students=[{'name': 'Henry, Johns', 'marks': [0]}, {'name': 'Timmy, Bug', 'marks': [0]}, {'name': 'George, King', 'marks': [0]}, {'name': 'Finn, Wish', 'marks': [0]}, {'name': 'Lucy Act', 'marks': [0]}]
    assert calculate_improved(students) == [{"name":"Finn, Wish","improvement":0},
    {"name":"George, King","improvement":0},
    {"name":"Henry, Johns","improvement":0},
    {"name":"Lucy Act","improvement":0},
    {"name":"Timmy, Bug","improvement":0}]
    
    students=[{'name': 'Henry, Johns', 'marks': [0, 100]}, {'name': 'Timmy, Bug', 'marks': [0, 9]}, {'name': 'George, King', 'marks': [0, 0]}, {'name': 'Finn, Wish', 'marks': [0, 76]}, {'name': 'Lucy Act', 'marks': [0, None]}]
    assert calculate_improved(students) == [{"name":"Finn, Wish","improvement":0},
    {"name":"George, King","improvement":0},
    {"name":"Henry, Johns","improvement":0},
    {"name":"Lucy Act","improvement":0},
    {"name":"Timmy, Bug","improvement":0}]

if __name__ == "__main__":
    main()
