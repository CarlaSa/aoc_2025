import time
from time import perf_counter_ns
from pprint import PrettyPrinter

def get_input_lines(i):

    file_name = "inputs/" + f"{i:02}" + ".txt"
    with open(file_name) as f:
        lines = f.readlines()

    return [l.strip() for l in lines if len(l.strip())> 0]

def get_input(i):
    file_name = "inputs/" + f"{i:02}" + ".txt"
    with open(file_name) as f:
        text = f.read()
    return text.strip()




def time_wrapper(func):
    result_file = "temp_outputs.txt"
    result_printer = PrettyPrinter(indent= 8)

    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        result = func(*args, **kwargs)
        end = perf_counter_ns()
        time_elapsed = end - start
        time_elapsed = time_elapsed / 1e9
        result_string = f"{func.__name__:10} --  {time_elapsed: .8f} seconds  -- result: "
        result_string += result_printer.pformat(result)
        with open(result_file, "a") as f:
            time_stamp = time.strftime("%Y/%m/%d-%H/%M/%S")
            f.write(time_stamp + "\n")
            f.write(result_string + "\n")
            f.write("\n")
        return result_string
    return wrapper
