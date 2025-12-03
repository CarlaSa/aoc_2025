from helpers import get_input_lines

test_input = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
R1000
"""
test_input = [r for r in test_input.splitlines() if len(r)> 0]

real_input = get_input_lines(1)

def run_algorithm(lines, verbose=False):
    current = 50
    clicks = 0
    positions = [current]

    if verbose:
        print("The dial starts by pointing at ", current )
    for line in lines:

        dir = line[0]
        num = int(line[1:])

        current_was_zero = current == 0

        if dir == "L":
            current = (current - num)
        elif dir == "R":
            current = (current + num)
        else:
            raise ValueError


        current_is_zero = current % 100 == 0

        if current_was_zero or current_is_zero:
            score = abs(num)//100

        else:
            score = abs(current//100)

        current %= 100
        clicks += score

        if verbose:
            first_sentence = f"The dial is rotated {line} to point at {current}"
            times_words = {1: "once", 2: "twice"}
            get_times_word = lambda x: times_words[x] if x in times_words else f"{x} times"
            second_sentence = f"during this rotation, it points at 0 {get_times_word(score)}."

            if score >0:
                print(first_sentence + "; " + second_sentence)
            else:
                print(first_sentence + ".")

        positions.append(current)

    return positions.count(0), clicks + positions.count(0)

output = run_algorithm(real_input)

print("part one:", output[0], "\npart two:", output[1])

# 4551
# 5660