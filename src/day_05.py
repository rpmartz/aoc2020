from typing import List

lower_designators = {'L', 'F'}
upper_designators = {'R', 'B'}
allowed_designators = upper_designators.union(lower_designators)


def binary_search(range, designator):
    if designator not in allowed_designators:
        raise Exception('Designator needs to be `F`, `B`, `L`, or `R`')

    midpoint = int(len(range) / 2)

    if designator in lower_designators:
        return range[0:midpoint]
    else:
        return range[midpoint:]


def build_row(inclusive_start: int, exclusive_end: int) -> List[int]:
    return [x for x in range(inclusive_start, exclusive_end)]


def find_result(num_range, instructions):
    res = num_range
    for instruction in instructions:
        res = binary_search(res, instruction)

    assert len(res) == 1
    return res[0]

# with open('data/05.txt', 'r') as f:
#     lines = [line.strip() for line in f.readlines()]

#
# for line in lines:
#     print(line)
