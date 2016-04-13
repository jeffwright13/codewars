#!/usr/bin/python

def main():
    print count_vegetables('')

def count_vegetables(string):
    """
    Help Suzuki count his vegetables....

    Suzuki is the master monk of his monastery so it is up to him to ensure the kitchen is operating at full capacity to feed his students and the villagers that come for lunch on a daily basis.

    This week there was a problem with his deliveries and all the vegetables became mixed up. There are two important aspects of cooking in his kitchen, it must be done in harmony and nothing can be wasted. Since the monks are a record keeping people the first order of business is to sort the mixed up vegetables and then count them to ensure there is enough to feed all the students and villagers.

    You will be given a string with the following vegetables:

    "cabbage", "carrot", "celery", "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip"

    Return a list of tuples with the count of each vegetable in descending order. If there are any non vegetables mixed in discard them. If the count of two vegetables is the same sort in descending alphabetical order.

    (119, "pepper"),
    (114, "carrot"),
    (113, "turnip"),
    (102, "onion"),
    (101, "tofu"),
    (100, "cabbage"),
    (93, "mushroom"),
    (90, "cucumber"),
    (88, "potato"),
    (80, "celery")
    """
    veg = ("cabbage", "carrot", "celery", "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip")
    veg_dict = dict(zip(list(veg), [0]* len(veg)))
    
    for elem in string.split():
        if elem in veg:
            veg_dict[elem] += 1

    return = [(v, k) for k, v in veg_dict.iteritems()]
    

def test():
    lst1 = [(2, 'tofu'),
       (2, 'potato'),
       (2, 'cucumber'),
       (2, 'cabbage'),
       (1, 'turnip'),
       (1, 'pepper'),
       (1, 'onion'),
       (1, 'mushroom'),
       (1, 'celery'),
       (1, 'carrot')]

    s1 = 'potato tofu cucumber cabbage turnip pepper onion carrot celery mushroom potato tofu cucumber cabbage' 
    
    assert count_vegetables(s1) == lst1

if __name__ == "__main__":
    main()
