from data_loader import loader

example_data = [
    '7 6 4 2 1',
    '1 2 7 8 9',
    '9 7 6 2 1',
    '1 3 2 4 5',
    '8 6 4 4 1',
    '1 3 6 7 9'
]

data = loader.load_day2()
#data = loader.load_day2(example_data)
print(data)

########## Part 1 - safe reports
safe_reports = 0
for line in data:
    index = 1
    safe = True
    last_direction = None
    while len(line) > index:
        distance = line[index] - line[index-1]
        direction = 'dec' if distance < 0 else 'inc'
        distance = abs(distance)
        if last_direction != direction and last_direction is not None:
            safe = False
            break

        if distance<1 or distance>3:
            safe = False
            break
        index += 1
        last_direction = direction

    if safe:
        #print(line)
        safe_reports += 1

print (f"Safe reports: {safe_reports}")

def check_report_safety(line_data):
    differences = []
    for i in range(len(line_data)-1):
        differences.append(line_data[i+1] - line_data[i])

    if not all(1 <= abs(diff) <= 3 for diff in differences):
        return False

    if all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences):
        return True

    return False

def can_be_safe_with_removal(report):
    for i in range(len(report)):
        # Create a sub-report by removing the i-th level
        sub_report = report[:i] + report[i+1:]
        if check_report_safety(sub_report):
            return True
    return False

########## Part 1 - safe reports
safe_reports = 0
#data = loader.load_day2(example_data)
for line in data:
    if check_report_safety(line) or can_be_safe_with_removal(line):
        print(line)
        safe_reports += 1

print (f"Safe reports: {safe_reports}")
