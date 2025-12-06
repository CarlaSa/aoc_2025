from functools import reduce

from helpers import get_input

test_input ="""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
real_input = get_input(6)

def parse_input(inp):
     inp = [[ii for ii in i.split(" ") if len(ii)>0] for i in inp.strip().split("\n")]

     n = len(inp[0])
     inp_rev = [
         [inp[i][j] for i in range(len(inp))] for j in range(n)
     ]

     return inp_rev

def task1(inp):
    operation_list = parse_input(inp)
    score = 0
    for eq in operation_list:
        op = eq[-1]
        if op == "+":
            score += sum([int(i) for i in eq[:-1]])
        elif op == "*":
            score += reduce(lambda x, y: int(x) * int(y), eq[:-1])
    return score


def task2(inp):
    lines = inp.split("\n")

    l = max(len(line) for line in lines)
    # pad wrong lines
    lines = [
        line + (l - len(line)) *" " for line in lines
    ]


    num_lines = len(lines)

    blocks = []
    current_block = []
    for i in range(len(lines[0])):
        column = [lines[j][i] for j in range(num_lines)]
        if all(c == " " for c in column):
            blocks.append(current_block)
            current_block = []
        else:
            current_block.append(column)
    blocks.append(current_block)

    score = 0
    for block in blocks:
        op = block[0][-1]
        rev_block = [int("".join(block[i][j] for j in range(len(block[0])-1))) for i in range(len(block))]

        if op == "+":
            score += sum(rev_block)
        elif op == "*":
            score += reduce(lambda x, y: int(x) * int(y), rev_block)

    return score



# print(task1(test_input))
# print(task1(real_input))

print(task2(test_input))
print(task2(real_input))
