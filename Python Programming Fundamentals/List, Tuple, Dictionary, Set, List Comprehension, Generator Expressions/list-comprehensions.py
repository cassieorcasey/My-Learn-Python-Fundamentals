# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_list = []
# for n in nums:
#     if n % 2 == 0:
#         my_list.append(n)
# print(my_list)

# my_list = [n for n in nums if n%2 == 0]
# print(my_list)

# my_list = [n for n in nums]
# print(my_list)

# my_list = map(lambda n: n*n, nums)
# print(my_list)

# memakai filter + lambda
# my_list = filter(lambda n: n%2 == 0, nums)
# print(my_list)

# letter, num
# my_list = []
# for letter in "abcd":
#     my_list.append(letter)
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)

# my_list = [(letter, num) for letter in "abcd" for num in range(4)]
# print(my_list)

# Dictionary comprehension
# names = ["Cassandra", "Cassie", "Cassey"]
# keys = ["nama", "panggilan", "nama_panggilan"]

# dict {"name" : "key"}
# my_dict = {name: key for name, key in zip(names, keys)}
# print(my_dict)

# Set comprehension
# nums = [1, 1, 2, 3, 4, 5, 6, 7, 9, 8, 10]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

# my_set = {n for n in nums}
# print(my_set)

# Generator expression
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def gen_func(nums):
#     for n in nums:
#         yield n*n

# my_gen = gen_func(nums)

# for i in my_gen:
#     print(i)

# my_gen = (n*n for n in nums)

# for i in my_gen:
#     print(i)