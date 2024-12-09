from data_loader import loader
from typing import List
import re

example_data = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
example_data2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
regex_part1 = r"mul\((\d+),(\d+)\)"
regex_part2 = r"(don't)\(\).*?mul\((\d+),(\d+)\)|(do)\(\).*?mul\((\d+),(\d+)\)"

def mul_strip(stream_text: str, regex_split: regex_part1) -> List:
    return re.findall(regex_split, stream_text, re.MULTILINE)

def mul_sum_list(values_list: List) -> int:
    return sum(a*b for a,b in values_list)

def mul_values_with_check(values_list: List) -> int:
    command, a, b = values_list
    if 'don\'t' == command:
        return 0
    return int(a)*int(b)


data = loader.load_day3()

################# Part 1 - mul
mul_extracted = [(int(a), int(b)) for a, b in mul_strip(" ".join(data), regex_part1)]
#mul_extracted = mul_strip(example_data)
print(mul_extracted)
sum_multiplies = mul_sum_list(mul_extracted)
print(sum_multiplies)

################# Part 2 - mul - example 48
mul_extracted = mul_strip(example_data2, regex_part2)
sum_multiplies = 0
for matches in mul_extracted:
    sum_multiplies += mul_values_with_check([item for item in matches if item != ''])

print(sum_multiplies)


