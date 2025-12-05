from helpers import get_input, time_wrapper

test_input = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

real_input = get_input(5)


def parse_input(inp):
    fresh, ingredients = inp.split("\n\n")

    def string_to_set(s):
        a, b = s.split("-")
        return set(range(int(a), int(b) + 1))

    fresh = [[int(a) for a in s.split("-")] for s in fresh.strip().split("\n")]
    ingredients = [int(s) for s in ingredients.strip().split("\n")]
    return fresh, ingredients

@time_wrapper
def task1(inp, debug=False):
    fresh, ingredients = parse_input(inp)

    fresh_ingredients = []
    for ing in ingredients:
        for a, b in fresh:
            if a <= ing <= b:
                fresh_ingredients.append(ing)
                break

    if debug:
        return {"result": len(fresh_ingredients), "fresh ingredients" : fresh_ingredients}
    return len(fresh_ingredients)


@time_wrapper
def task2(inp, debug=False):
    fresh, _ = parse_input(inp)

    ranges = []

    for a, b in fresh:
        overlap_idxes = []
        for i, (r,s) in enumerate(ranges):
            if s < a or r > b:
                continue
            overlap_idxes.append(i)
            if len(overlap_idxes) >= 2:
                break

        overlap_ranges= [[a,b]] + [ranges.pop(i) for i in reversed(overlap_idxes)]

        ranges.append([min(r[0] for r in overlap_ranges),
                       max(r[1] for r in overlap_ranges)])


    score = 0
    for a,b in ranges:
        score += b - a + 1

    if debug:
        return {"result": score, "non-overlapping intervals" : ranges}

    return score





print(task1(test_input, debug=True))
print(task1(real_input))

print(task2(test_input, debug=True))
print(task2(real_input))


