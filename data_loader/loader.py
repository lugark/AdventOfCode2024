def load_day1():
    list1 = []
    list2 = []
    with open('data/day1.data') as f:
        lines = [line.strip().split() for line in f]
        for line in lines:
            list1.append(int(line.pop()))
            list2.append(int(line.pop()))
    return list1, list2


def load_day2(example_data=None):
    data = []
    if example_data is None:
        with open('data/day2.data') as f:
            data = f.readlines()
    else:
        data = example_data

    lines = [line.strip().split() for line in data]
    data = []
    for line in lines:
        data.append([int(item) for item in line])
    return data


def load_day3():
    with open('data/day3.data') as f:
        return f.readlines()