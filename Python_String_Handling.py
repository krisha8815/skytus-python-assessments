# 1. Take a string input and print its length
text = input("Enter a string: ")
print("1. Length:", len(text))

# 2. Convert a sentence to lowercase
sentence = input("\nEnter a sentence: ")
print("2. Lowercase:", sentence.lower())

# 3. Replace spaces with underscores in a string
text = input("\nEnter a string: ")
print("3. Modified String:", text.replace(" ", "_"))

# 4. Extract the first and last character of a string
text = input("\nEnter a string: ")
print("4. First Character:", text[0])
print("4. Last Character:", text[-1])

# 5. Reverse a string using slicing
text = input("\nEnter a string: ")
print("5. Reversed String:", text[::-1])

# 6. Count how many times a letter appears in a string
text = input("\nEnter a string: ")
letter = input("Enter a letter to count: ")
print("6. Count:", text.count(letter))

# 7. Check if a word is present in a sentence
sentence = input("\nEnter a sentence: ")
word = input("Enter a word to search: ")
print("7.", word in sentence)

# 8. Take name & age and print using f-string formatting
name = input("\nEnter your name: ")
age = int(input("Enter your age: "))
print(f"8. My name is {name} and I am {age} years old.")

# 9. Remove extra spaces from the start and end of a string
text = input("\nEnter a string with spaces: ")
print("9. Trimmed String:", text.strip())

# 10. Join a list of words into a single string with - between them
words = ["Python", "is", "easy", "to", "learn"]
print("10.", "-".join(words))

# 11. Create a list of your 5 favorite movies
movies = ["off campus", "devil wears prada", "dear zindagi", "five feets apart", "ZNMD"]
print("11. Movies:", movies)

# 12. Add a new movie to the list
movies.append("YJHD")
print("12. After Adding:", movies)

# 13. Remove the first movie from the list
movies.pop(0)
print("13. After Removing First Movie:", movies)

# 14. Sort a list of numbers in ascending order
numbers = [90, 67, 89, 36, 6]
numbers.sort()
print("14. Sorted List:", numbers)

# 15. Reverse a list
numbers.reverse()
print("15. Reversed List:", numbers)

# 16. Find the largest number in a list
numbers = [40, 62, 7, 30, 36]
print("16. Largest Number:", max(numbers))

# 17. Merge two lists into one
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = list1 + list2
print("17. Merged List:", merged)

# 18. Access the last element of a list without using index number
numbers = [10, 20, 30, 40, 50]
print("18. Last Element:", numbers[-1])

# 19. Create a nested list and access a specific inner element
nested_list = [[1, 2], [3, 4], [5, 6]]
print("19. Inner Element:", nested_list[1][1])

# 20. Count how many times an element appears in a list
numbers = [1, 2, 3, 2, 4, 2, 5]
print("20. Count of 2:", numbers.count(2))