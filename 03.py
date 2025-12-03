from helpers import get_input_lines, time_wrapper

test_input = """
987654321111111
811111111111119
234234234234278
818181911112111
"""
test_input = test_input.strip().split("\n")

real_input = get_input_lines(3)

def find_highest_voltage(l, num_digits, debug = False):
    vals = [int(l[i]) for i in range(num_digits)]
    idx = list(range(num_digits))
    for i in range(0, len(l)):

        for j in range(0, num_digits):
            if idx[j] > i:
                continue

            # tried to do clever index stuff but confused myself
            if len(l[i:]) < len(vals[j:]):
                continue

            if vals[j] < int(l[i]):
                for k in range(0, num_digits - j):
                    vals[j + k] = int(l[i + k])
                    idx[j + k] = i + k
                break

    score = int("".join(str(v) for v in vals))

    if debug:
        return score, vals
    else:
        return score


@time_wrapper
def task1(lines):
    return sum(find_highest_voltage(l, 2) for l in lines)

@time_wrapper
def task2(lines):
    return sum(find_highest_voltage(l, 12) for l in lines)

print(task1(test_input))
print(task1(real_input))

print(task2(test_input))
print(task2(real_input))


