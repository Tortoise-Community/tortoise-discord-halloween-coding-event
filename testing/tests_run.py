"""
Just put your script/scripts inside the same directory as this one.
Then run this.
"""


import os
from importlib import import_module
from timeit import default_timer as timer


class EliminationFail(Exception):
    pass


def elimination_1(imp):
    try:
        return getattr(imp, "is_vampire_number")
    except AttributeError:
        raise EliminationFail("Elimination 0: is_vampire_number function not found!")


def elimination_2(function, number):
    try:
        returned = function(number)
        if returned:
            raise EliminationFail(f"Elimination 2: Invalid number {number} returned True!")
    except ValueError:
        return
    except Exception as err:
        raise EliminationFail(f"Elimination 2: Uncaught exception while passing number {number}: {err}!")


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
        function_to_run = elimination_1(imported)
        for num in range(-5, 1, 1):
            elimination_2(function_to_run, num)
        elimination_3(function_to_run)
        elimination_4(function_to_run)
    except EliminationFail as e:
        print(f"{submission} did not pass {e}")
        continue

    print(f"{submission} passed tests.")
