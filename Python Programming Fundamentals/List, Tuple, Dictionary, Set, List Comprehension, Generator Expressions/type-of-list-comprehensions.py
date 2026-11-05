# numbers: list[int] = [1, 2, 3, 4, 5]
# squared: list[int] = [pow(number, 2) for number in numbers]
# print(squared)  # Output: [1, 4, 9, 16, 25]

# from typing import Generator

# data: range = range(10_1000)
# squared: Generator[int, None, None] = (pow(n, 2) for n in data)
# print(squared)
# print(next(squared))
# print(next(squared))
# print(next(squared))
# print(next(squared))
# print(next(squared))
# print(next(squared))
# print(next(squared))
# print(next(squared))
# print(next(squared))
# print(next(squared))

# values: list[int] = [6, 6, 6, 7, 7, 11, 7, 222, 2521] 
# filtered: set[int] = {v*2 for v in values}
# print(filtered)  

# data: list[tuple[str, int]] = [("a", 1), ("b", 2), ("c", 3)]
# my_dict: dict[str, int] = {k: v*10 for k, v in data}
# print(my_dict)