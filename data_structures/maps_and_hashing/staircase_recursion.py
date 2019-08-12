'''
Problem Statement
A child is running up a staircase with and can hop either 1 step, 2 steps or 3 steps at a time. If the staircase
has n steps, write a function to count the number of possible ways in which child can run up the stairs.

For e.g.

n == 1 then answer = 1

n == 3 then answer = 4

n == 5 then answer = 13

'''


def staircase(n):
    # Base Case - minimum steps possible and number of ways the child can climb them
    # Inductive Hypothesis - ways to climb rest of the steps
    # Inductive Step - we can use Inductive Hypothesis to formulate a solution

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)


def test_function(test_case):
    answer = staircase(test_case[0])
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")

test_case = [4, 7]
test_function(test_case)

test_case = [5, 13]
test_function(test_case)

test_case = [3, 4]
test_function(test_case)

test_case = [20, 121415]
test_function(test_case)