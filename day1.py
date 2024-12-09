# Testdata
list_left = []
list_right = []

with open('data/day1.data') as f:
    lines = [line.strip().split() for line in f]
    for line in lines:
        list_left.append(int(line.pop()))
        list_right.append(int(line.pop()))
    print(list_left)
    print(list_right)


#### Part 1
# Testdata
#list_left = [3,4,2,1,3,3]
#list_right = [4,3,5,3,9,3]
list_left_part2 = list_left
list_right_part2 = list_right

sum = 0
list_left.sort()
list_right.sort()
while(len(list_left)>0):
    sum += abs(list_left.pop() - list_right.pop())

print(f"Distance Part 1: {sum}")


##### Part 2
for number in list_left_part2:
    counter = list_right_part2.