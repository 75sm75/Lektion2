## Repetition från kap 1 ##

## Strings

# str = "Hello"
# str[0] = "h"

# str = "Hello"
# new_str = 'h' + str[1:]
# print(new_str)

# str = "Python"
# new_str = str[:2] + 'T' + str[3:]
# print(new_str)

# age = 37
# result = "I am " + str(age) + " years old"
# print(result)

# print('3' + '5')
# print(3 + 5)

# words = ["Hello", "World", "Python"]
# result = ":".join(words)
# print(result)

# str = "Hello World"
# print(str.upper())
# print(str.lower())

# str = "hello world"
# print(str.capitalize())
# print(str.title())

# str = " Hello world "
# print(str)
# print(str.strip())
# print(str.lstrip())
# print(str.rstrip())

# str = "apple,banana,cherry"
# fruits = str.split(',')
# print(fruits)

# str = "one,two,three,four"
# str = str.split(',', 2)
# print(str)

# words = "I like apples apples"
# print(words.replace("apples", "melons"))

# words = "Hello world"
# print(words.find("world"))

# name = "Bobbo"
# age = 37
# print(f"My name is {name} and I am {age}")

# empty_list = []

# my_list = ["apple", 42, True, 3.14]

# print(my_list[1])

# my_list = ["apple", 42, True, 3.14]

# print(my_list[-2])

# my_list = ["apple", 42, True, 3.14]

# my_list[3] = "melon"
# print(my_list)

# numbers = [1,2,3,4,5]
# numbers[1:4] = [20,30,40]
# print(numbers)

# numbers = [1,2,3,4,5]
# numbers.append(6)
# print(numbers)

# numbers = [1,2,3,4,5]

# numbers.insert(122, "hej")
# print(numbers)

# fruits = ["apple", "banana", "melon", "cherry"]
# fruits.remove("melon")
# print(fruits)

# deleted = fruits.pop(2)
# print(f"We removed {deleted} in our list: {fruits}")

# fruits.pop()
# print(fruits)

# del fruits
# print(fruits)

# fruits.clear()
# print(fruits)

# fruits = ["apple", "banana", "melon", "cherry", "pear"]

# print(fruits[1:4])
# print(fruits[:3])
# print(fruits[2:])
# print(fruits[::2])
# print(fruits[::-1])
# print(fruits[-1:])

# fruits = ["apple", "pear", "melon", "cherry", "pear"]
# numbers = [2,7,4,5,1]
# print(fruits.count("apples"))

# fruits.sort()
# print(fruits)

# numbers.sort()
# print(numbers)

# fruits = ["apple", "pear", "melon", "cherry", "pear"]

# fruits.sort(key=len)
# print(fruits)

# print(len(fruits))

# numbers = [2,7,4,5,1]
# print(sum(numbers))

## Dictionaries ##

empty_dict = {}

# person = {"name": "Bobbo", "age": 37, "city": "Linköping"}

# print(person["names"])

# print(person.get("proffession", "Unknown"))

# person["age"] = 26
# print(person)

# person["profession"] = "Hacker"

# print(person)

# age = person.pop("age")
# print(age)
# print(person)

# person = {"name": "Bobbo", "age": 37, "city": "Linköping"}

# del person["name"]
# print(person)

# person["profession"] = "Hacker"
# print(person)

# key, value = person.popitem()
# print(key, value)
# print(person)

person = {"name": "Bobbo", "age": 37, "city": "Linköping"}

# person.clear()
# print(person)

# keys = person.keys()
# print(keys)

# values = person.values()
# print(values)

# tuples = person.items()
# print(tuples)

## Tuples ##

# empty_tuple = ()

# small_tuple = (5,)

# fruits = ("apple", "melon", "cherry")

# fruits = "apple", "melon", "cherry"
# print(fruits)
# print(type(fruits))

# fruits = ("apple", "melon", "cherry")
# print(fruits[0])
# print(fruits[-1])

# print(fruits[1:4])

# fruits[1] = "banana"

# fruits = ("apple", "melon", "cherry")
# fruits_list = list(fruits)
# fruits_list[1] = "banana"
# fruits = tuple(fruits_list)
# print(fruits)

# fruits = ("apple", "melon", "cherry")
# fruit1, fruit2, fruit3 = fruits
# print(fruit1)
# print(fruit2)
# print(fruit3)

# fruits = ("apple", "melon", "cherry", "banana", "grape")
# fruit1, fruit2, *rest = fruits
# print(fruit1)
# print(fruit2)
# print(rest)

# numbers = fruits.count("melon")
# print(numbers)

# index = fruits.index("banana")
# print(index)

## Sets ##

empty_set = set()

fruits = {"apple", "banana", "cherry", "apple"}
# print(fruits)
# print(fruits[0])

fruits.add("grape")
# print(fruits)

# fruits.update(["orange", "mango"])
# fruits.remove("banana")
# print(fruits)

# fruits.discard("cherrys")
# print(fruits)

# element = fruits.pop()
# print(element)
# print(fruits)

# fruits.clear()
# print(fruits)

# set1 = {1,2,3}
# set2 = {3,4,5}

# union_set = set1 | set2
# union_set = set1.union(set2)

# print(union_set)

# intersection_set = set1 & set2
# print(intersection_set)

# diffrence_set = set1 - set2
# print(diffrence_set)

# symmetric = set1 ^ set2
# print(symmetric)

# frozen_fruits = frozenset(["apple", "orange", "grape"])
# print(frozen_fruits)

# frozen_fruits.add("banana")
