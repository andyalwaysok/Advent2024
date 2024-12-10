new_line1 = []
new_line2 = []

with open("C:\Personal Projects\Advent_of_Code_2024\day1_file.txt") as file:
    for line in file:
        line = line.strip().split()
        new_line1.append(line[0])
        new_line2.append(line[1])

l1 = sorted(new_line1)
l2 = sorted(new_line2)

distance = 0

for d1, d2 in zip(l1, l2):
    distance += abs(int(d1) - int(d2))

similarity = 0

for d1 in l1:
    similarity += l2.count(d1) * int(d1)

print(similarity)