with open('task2.txt', 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()

counts = []
for line in lines:
    counts.append(line.count('а'))

sorted_lines = [line for counts, line in sorted(zip(counts, lines), reverse=True)]

print('\n'.join(sorted_lines))

