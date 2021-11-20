from typing import List

def halve_range(range, designator):
    if designator not in ('F', 'B'):
        raise Exception('Designator needs to be `F` or `B`')

    midpoint = int(len(range) / 2)

    if designator == 'F':
        return range[0:midpoint]
    else:
        return range[midpoint:]

def build_row(inclusive_start: int, exclusive_end: int) -> List[int]:
    return [x for x in range(inclusive_start, exclusive_end)]


# with open('data/05.txt', 'r') as f:
#     lines = [line.strip() for line in f.readlines()]

#
# for line in lines:
#     print(line)
