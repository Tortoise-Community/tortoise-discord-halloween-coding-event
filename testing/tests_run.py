"""
Just put your script/scripts inside the same directory as this one.
Then run this.
"""


import os
from importlib import import_module
from timeit import default_timer as timer


class EliminationFail(Exception):
    pass


def elimination_0(imp):
    try:
        return getattr(imp, "is_vampire_number")
    except AttributeError:
        raise EliminationFail("Elimination 0: is_vampire_number function not found!")


def elimination_1(function):
    try:
        function(-1)
    except ValueError:
        return
    raise EliminationFail("Elimination 1: Negative number did not raise ValueError!")


def elimination_2(function):
    try:
        function(0)
    except ValueError:
        return
    raise EliminationFail("Elimination 2: Zero did not raise ValueError!")


def elimination_3(function):
    valid_vampires = (146137, 150300, 536539, 10025010, 13078260, 46847920, 1000174288)
    for number in valid_vampires:
        try:
            assert function(number)
            assert not function(number - 1)
        except AssertionError:
            raise EliminationFail("Elimination 3: is_vampire_number function returned incorrect result!")


def elimination_4(function):
    start = timer()
    for i in range(1, 7000):
        function(i)
    time = timer() - start
    if time > 10:
        raise EliminationFail("Elimination 4: Iteration took more than 10s!")


submissions = (script.replace(".py", "") for script in os.listdir(".") if script.endswith(".py") and script != "tests_run.py")

for submission in submissions:
    imported = import_module(submission)

    try:
        function_to_run = elimination_0(imported)
        elimination_1(function_to_run)
        elimination_2(function_to_run)
        elimination_3(function_to_run)
        elimination_4(function_to_run)
    except EliminationFail as e:
        print(f"{submission} did not pass {e}")
        continue

    print(f"{submission} passed tests.")
