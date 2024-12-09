from data_loader import loader
# Testdata
list_left, list_right = loader.load_day1()

#### Part 1
# Testdata
#list_left = [3,4,2,1,3,3]
#list_right = [4,3,5,3,9,3]
list_left_part2 = list_left.copy()
list_right_part2 = list_right.copy()

sum = 0
list_left.sort()
list_right.sort()
while(len(list_left)>0):
    sum += abs(list_left.pop() - list_right.pop())

print(f"Distance Part 1: {sum}")

##### Part 2
sum = 0
for number in list_left_part2:
    counter = list_right_part2.count(number)
    sum += number*counter

print(f"Distance Part 2: {sum}")
