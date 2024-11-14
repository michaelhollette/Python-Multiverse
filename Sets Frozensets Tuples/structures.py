# Let's create a Python file with examples of manipulating lists, sets, tuples, and frozensets.

file_content = ""
# Python Examples of Manipulating Lists, Sets, Tuples, and Frozensets

# 1. List Manipulation
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# Adding an element
fruits.append("orange")
print("After appending:", fruits)

# Removing an element by value
fruits.remove("banana")
print("After removing 'banana':", fruits)

# Removing an element by index
del fruits[0]
print("After deleting index 0:", fruits)

# Sorting the list
fruits.sort()
print("Sorted list:", fruits)


# 2. Set Manipulation
unique_numbers = {1, 2, 3, 4}
print("\\nOriginal set:", unique_numbers)

# Adding an element
unique_numbers.add(5)
print("After adding 5:", unique_numbers)

# Removing an element
unique_numbers.discard(3)  # `discard` does not raise an error if the element is not found
print("After discarding 3:", unique_numbers)

# Set operations: union, intersection, difference
another_set = {3, 4, 5, 6}
print("Union with another set:", unique_numbers | another_set)
print("Intersection with another set:", unique_numbers & another_set)
print("Difference with another set:", unique_numbers - another_set)


# 3. Tuple Manipulation (Tuples are immutable, so we cannot change elements directly)
coordinates = (10, 20, 30)
print("\\nOriginal tuple:", coordinates)

# Accessing elements
x = coordinates[0]
print("First element:", x)

# Concatenating tuples
new_coordinates = coordinates + (40, 50)
print("After concatenation:", new_coordinates)

# Counting occurrences and finding index
tuple_with_duplicates = (1, 2, 3, 1, 2, 1)
print("Count of 1 in tuple:", tuple_with_duplicates.count(1))
print("Index of first occurrence of 3:", tuple_with_duplicates.index(3))


# 4. Frozenset Manipulation (Frozensets are immutable, but we can perform set operations)
immutable_set = frozenset([1, 2, 3, 4])
print("\\nOriginal frozenset:", immutable_set)

# Set operations with frozenset
another_frozenset = frozenset([3, 4, 5, 6])
print("Union with another frozenset:", immutable_set | another_frozenset)
print("Intersection with another frozenset:", immutable_set & another_frozenset)
print("Difference with another frozenset:", immutable_set - another_frozenset)

# Attempting to modify a frozenset will raise an error
# immutable_set.add(7)  # Uncommenting this line would raise an AttributeError

# Summary:
# - Lists allow indexing, adding, removing, and sorting.
# - Sets support adding, removing, and set operations but are unordered.
# - Tuples support indexing, concatenation, and are immutable. 


# - Frozensets are immutable and allow set operations but do not support adding/removing elements.


# Write this content to a .py file
with open("/mnt/data/data_structure_manipulation_examples.py", "w") as file:
    file.write(file_content)
"/mnt/data/data_structure_manipulation_examples.py"
