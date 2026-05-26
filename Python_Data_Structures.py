# 1. Create a tuple with 5 numbers
numbers = (10, 20, 30, 40, 50)
print("1. Tuple:", numbers)

# 2. Access the third element in a tuple
print("2. Third Element:", numbers[2])

# 3. Unpack a tuple into separate variables
a, b, c, d, e = numbers
print("3. Unpacked Values:", a, b, c, d, e)

# 4. Create a set of 5 fruits
fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}
print("4. Fruits Set:", fruits)

# 5. Add a new fruit to the set
fruits.add("Pineapple")
print("5. After Adding:", fruits)

# 6. Remove an element from a set
fruits.remove("Banana")
print("6. After Removing:", fruits)

# 7. Find union of two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("7. Union:", set1.union(set2))

# 8. Find intersection of two sets
print("8. Intersection:", set1.intersection(set2))

# 9. Check if one set is subset of another
setA = {1, 2}
setB = {1, 2, 3, 4}
print("9. Is Subset:", setA.issubset(setB))

# 10. Convert a list with duplicate values into a set
duplicate_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(duplicate_list)
print("10. Unique Values:", unique_set)

# 11. Create a dictionary storing student names and marks
students = {"John": 85, "Alice": 90, "Bob": 78}
print("11. Students Dictionary:", students)

# 12. Add a new key-value pair to an existing dictionary
students["David"] = 88
print("12. After Adding:", students)

# 13. Delete a key-value pair from a dictionary
del students["Bob"]
print("13. After Deleting:", students)

# 14. Merge two dictionaries into one
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print("14. Merged Dictionary:", merged_dict)

# 15. Check if a key exists in a dictionary
print("15. Key Exists:", "John" in students)

# 16. Count word frequency in a given string using a dictionary
text = "apple banana apple orange banana apple"
words = text.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("16. Word Frequency:", frequency)

# 17. Find the key with the maximum value in a dictionary
marks = {"John": 85, "Alice": 92, "David": 88}
max_key = max(marks, key=marks.get)
print("17. Highest Marks:", max_key)

# 18. Reverse keys and values in a dictionary
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
print("18. Reversed Dictionary:", reversed_dict)

# 19. Update the value for a specific key
marks["John"] = 95
print("19. Updated Dictionary:", marks)

# 20. Convert a list of tuples into a dictionary
tuple_list = [("name", "Krisha"), ("age", 22), ("city", "Ahmedabad")]
result_dict = dict(tuple_list)
print("20. Dictionary:", result_dict)