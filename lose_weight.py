"""
http://www.codewars.com/kata/573b216f5328ffcd710013b3/edit/python

BACKGROUND:
Jacob recently decided to get healthy and lose some weight. He did a lot of reading and research and after focusing on steady exercise and a healthy diet for several months, was able to shed over 50 pounds! Now he wants to share his success, and has decided to tell his friends and family how much weight they could expect to lose if they used the same plan he followed.

Lots of people are really excited about Jacob's program and they want to know how much weight they would lose if they followed his plan. Unfortunately, he's really bad at math, so he's turned to you to help write a program that will calculate the expected weight loss for a particular person, given their weight and how long they think they want to continue the plan.

TECHNICAL DETAILS:
Jacob's weight loss protocol, if followed closely, yields weight loss according to a simple formulae, depending on gender. Men can expect to lose 1.5% of their current body weight each week they stay on plan. Women can expect to lose 1.2%. (Children are advised to eat whatever they want, and make sure to play outside as much as they can!)

TASK:
Write a function that takes as input:
   - The person's gender ('M' or 'F');
   - Their current weight (in pounds);
   - How long they want to stay true to the protocol (in weeks);
and then generates/returns the expected weight loss (in pounds).

NOTES:
Weights (both input and output) should be decimals, rounded to the nearest tenth.
Duration (input) should be a whole number (integer). If it is not, the function should round to the nearest whole number.
"""
def lose_weight(gender, weight, duration):
    if gender not in ('M', 'F'):
        return 'Invalid gender'
    if weight <= 0:
        return 'Invalid weight'
    if duration <= 0:
        return 'Invalid duration'
    
    if gender == 'M':
        multiplier = .015
    elif gender == 'F':
        multiplier = .012

    for i in range(int(duration)):
        weight -= (weight * multiplier)

    return round(weight, 1)


def test_lose_weight():
    assert lose_weight('K', 200, 10) == 'Invalid gender'
    assert lose_weight('M', 0, 10) == 'Invalid weight'
    assert lose_weight('M', -5, 10) == 'Invalid weight'
    assert lose_weight('F', 160, 0) == 'Invalid duration'
    assert lose_weight('F', 160, -10) == 'Invalid duration'
    assert lose_weight('M', 250, 5) == 231.8
    assert lose_weight('F', 190, 8) == 172.5
    assert lose_weight('M', 405, 12) == 337.8
    assert lose_weight('F', 130, 7) == 119.5

"""
CodeWars Kata Tests (Python):

def assert_fuzzy_equals(actual, expected, msg=""):
    import math
    merr = 1e-3  # max error

    if expected == 0:
        inrange = math.fabs(actual) <= merr
    else:
        inrange = math.fabs((actual - expected) / expected) <= merr
    if msg == "":
        msg = "Expected value near {:.12f}, but got {:.12f}"
        msg = msg.format(expected, actual)
    return Test.expect(inrange, msg)

test.describe("Basic Tests - Negative")
test.it("Should reject invalid genders")
test.assert_equals(lose_weight('K', 200, 10), 'Invalid gender')
test.it("Should reject weights less than or equal to zero")
test.assert_equals(lose_weight('M', 0, 10), 'Invalid weight')
test.it("Should reject weights less than or equal to zero")
test.assert_equals(lose_weight('M', -5, 10), 'Invalid weight')
test.it("Should reject negative or zero durations")
test.assert_equals(lose_weight('F', 160, 0), 'Invalid duration')
test.assert_equals(lose_weight('F', 160, -10), 'Invalid duration')
###
test.describe("Basic Tests - Positive")
test.it("Typical male")
test.assert_equals(lose_weight('M', 250, 5), 231.8)
test.it("Typical female")
test.assert_equals(lose_weight('F', 190, 8), 172.5)
test.it("Very heavy male")
test.assert_equals(lose_weight('M', 405, 12), 337.8)
test.it("Light female")
test.assert_equals(lose_weight('F', 130, 7), 119.5)
###
test.describe("Random Tests")
import random

test.it('Should reject invalid genders')
import string
l = string.letters
l = l.replace('F', '')
l = l.replace('M', '')
for i in range(0, 25):
    test.assert_equals(lose_weight(random.choice(l), 100, 1), 'Invalid gender')

test.it('Should reject weights less than or equal to zero')
for i in range(0, 25):
    test.assert_equals(lose_weight(random.choice(['M', 'F']), random.randint(-65535, 0), 1), 'Invalid weight')

test.it('Should reject negative or zero durations')
for i in range(0, 25):
    test.assert_equals(lose_weight(random.choice(['M', 'F']), 200, random.randint(-65535, 0)), 'Invalid duration')

test.it('Should calculate values correctly for men')
g = 'M'
m = 0.015
w = random.randint(1, 65535)
d = random.randint(1, 65535)
wt = w
for i in range(int(d)):
    wt -= (wt * m)
for i in range(0, 25):
    test.assert_equals(round(lose_weight(g, w, d), 1), round(wt, 1))

test.it('Should calculate values correctly for women')
g = 'F'
m = 0.012
w = random.randint(1, 65535)
d = random.randint(1, 65535)
wt = w
for i in range(int(d)):
    wt -= (wt * m)
for i in range(0, 25):
    test.assert_equals(round(lose_weight(g, w, d), 1), round(wt, 1))
"""
