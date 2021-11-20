
with open('data/05.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


for line in lines:
    print(line)
