with open('data/02.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

num_valid_passwords = 0

records = []

for line in lines:
    components = line.split(':')
    range_and_letter = components[0].split()

    range = range_and_letter[0].split('-')

    lower_bound = int(range[0])
    upper_bound = int(range[1])
    letter = range_and_letter[1]
    password = components[1].strip()

    records.append((lower_bound, upper_bound, letter, password))

print(sum(lb <= password.count(letter) <= ub for lb, ub, letter, password in records))
print(sum(((password[a - 1] == letter) + (password[b - 1] == letter)) == 1
          for a, b, letter, password in records))
