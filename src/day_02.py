with open('data/02.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

num_valid_passwords = 0

for line in lines:

    components = line.split(':')
    range_and_letter = components[0].split()

    range = range_and_letter[0].split('-')

    lower_bound = int(range[0])
    upper_bound = int(range[1])
    letter = range_and_letter[1]
    password = components[1].strip()

    num_occurences = password.count(letter)
    if lower_bound <= num_occurences <= upper_bound:
        num_valid_passwords += 1

print(num_valid_passwords)
