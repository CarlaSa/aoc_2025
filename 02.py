import time
from collections import defaultdict

from helpers import get_input, time_wrapper

test_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
real_input = get_input(2)
hans_input = "1-4294967296"


def cleanup(inp):
    return [tuple(int(xx) for xx in x.split("-")) for x in inp.split(",")]

test_input = cleanup(test_input)
real_input = cleanup(real_input)
hans_input = cleanup(hans_input)


def is_valid(id):
    id = str(id)
    l = len(id)
    if l%2 != 0:
        return True
    return id[:l//2] != id[l//2:]


def is_valid2(id):
    id = str(id)
    l = len(id)

    for i in range(1, l):
        if l % i == 0:
            j = l // i
            segments = [id[ii * i: (ii+1) * i] for ii in range(j)]
            if len(set(segments)) == 1:
                return False

    return True

@time_wrapper
def task(inp, valid_f):
    num_invs = 0
    sum_invs = 0
    # invs = []

    for (t_min, t_max) in inp:
        for t in range(t_min, t_max+1):
            if not valid_f(t):
                num_invs += 1
                sum_invs += t
                # invs.append(t)

    return num_invs, sum_invs



@time_wrapper
def task_sieb(inp, first_part):
    maximum = max(inp[i][1] for i in range(len(inp)))
    all_invs = set()

    ds = dict()
    for n_zeros in range(0, 10):
        if first_part:
            temp = [int("1" + n_zeros  * "0" + "1")]
        else:
            temp = [int("1" + rep * (n_zeros  * "0" + "1")) for rep in range(1, 10)]

        temp = [t for t in temp if t * 10 ** n_zeros <= maximum]
        for t in temp:
            ds[t] = n_zeros


    for d in ds:
        i = ds[d]
        for j in range(10 ** i , 10**(i + 1)):
            z = d * j
            if z > maximum:
                break

            all_invs.add(z)

    num_invs = 0
    sum_invs = 0

    num_overall_invs = len(all_invs)

    for (t_min, t_max) in inp:
        # decide what to compare to what
        if t_max - t_min > num_overall_invs + 1:
            # go through invs
            for t in all_invs:
                if t_min <= t <= t_max:
                    num_invs += 1
                    sum_invs += t
        else:
            # go through intervall
            for t in range(t_min, t_max+1):
                if not is_valid(t):
                    num_invs += 1
                    sum_invs += t

    return sum_invs







# first part 863
# second part 953
# print(task(real_input, is_valid))
# print(task(real_input, is_valid2))

# print(task_sieb(real_input, first_part= True))
# print(task_sieb(real_input, first_part= False))
# print()

print("Task from Hans")
print(task_sieb(hans_input, first_part= True))
print(task_sieb(hans_input, first_part= False))