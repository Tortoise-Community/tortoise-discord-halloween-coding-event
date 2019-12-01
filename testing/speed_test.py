import os
from importlib import import_module
from timeit import default_timer as timer


submissions = (script.replace(".py", "") for script in os.listdir(".") if script.endswith(".py") and
               script not in ("tests_run.py", "speed_test.py"))
times = {}
iterations = 100


def speed_test(function):
    start = timer()
    for i in range(1, 7000):
        function(i)
    return timer() - start


for submission in submissions:
    imported = import_module(submission)
    time = 0
    try:
        function_to_run = getattr(imported, "is_vampire_number")
        for _ in range(iterations):
            time += speed_test(function_to_run)
        times[submission] = time/iterations
        print(f"Done with {submission} : {times[submission]}")
    except Exception:
        continue

sorted_times = sorted(times.items(), key=lambda kv: kv[1])
for time_tuple in sorted_times:
    print(f"'{time_tuple[0]}'\t{time_tuple[1]}")
