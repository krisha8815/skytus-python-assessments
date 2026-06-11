import csv
from collections import Counter

# Create Sample Files
with open("sample.txt", "w") as f:
    f.write("""Python is easy to learn.
Python is powerful.
File handling is important.
Learning Python is fun.
""")

with open("file1.txt", "w") as f:
    f.write("This is File 1.\nWelcome to Python.\n")

with open("file2.txt", "w") as f:
    f.write("This is File 2.\nFile handling example.\n")

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Name", "Marks"])
    writer.writerow([1, "John", 85])
    writer.writerow([2, "Alice", 90])
    writer.writerow([3, "Bob", 78])

# 1. Read a file and display its contents
print("\n===== 1. READ FILE =====")
with open("sample.txt", "r") as f:
    print(f.read())

# 2. Count number of lines in a file
print("\n===== 2. LINE COUNT =====")
with open("sample.txt", "r") as f:
    lines = f.readlines()

print("Number of lines:", len(lines))

# 3. Count frequency of each word
print("\n===== 3. WORD FREQUENCY =====")
with open("sample.txt", "r") as f:
    words = f.read().lower().split()

word_count = Counter(words)

for word, count in word_count.items():
    print(word, ":", count)

# 4. Write 5 user-entered sentences to a file
print("\n===== 4. WRITE 5 SENTENCES =====")

with open("sentences.txt", "w") as f:
    for i in range(5):
        sentence = input(f"Enter sentence {i+1}: ")
        f.write(sentence + "\n")

print("Sentences saved successfully.")

# 5. Append a list of strings to existing file
print("\n===== 5. APPEND STRINGS =====")

new_lines = [
    "This is appended line 1.",
    "This is appended line 2.",
    "This is appended line 3."
]

with open("sample.txt", "a") as f:
    for line in new_lines:
        f.write(line + "\n")

print("Lines appended successfully.")

# 6. Print lines containing a specific word
print("\n===== 6. SEARCH WORD IN FILE =====")

search_word = input("Enter word to search: ")

with open("sample.txt", "r") as f:
    for line in f:
        if search_word.lower() in line.lower():
            print(line.strip())

# 7. Replace a specific word in a file
print("\n===== 7. REPLACE WORD =====")

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

with open("sample.txt", "r") as f:
    content = f.read()

content = content.replace(old_word, new_word)

with open("sample.txt", "w") as f:
    f.write(content)

print("Replacement completed.")

# 8. Merge two files into third file
print("\n===== 8. MERGE FILES =====")

with open("file1.txt", "r") as f1, \
     open("file2.txt", "r") as f2, \
     open("merged.txt", "w") as out:

    out.write(f1.read())
    out.write("\n")
    out.write(f2.read())

print("Merged file created: merged.txt")

# 9. Read CSV file and display formatted content
print("\n===== 9. CSV FILE CONTENT =====")

with open("students.csv", "r") as f:
    reader = csv.reader(f)

    for row in reader:
        print("{:<10} {:<15} {:<10}".format(*row))

# 10. Backup a file
print("\n===== 10. FILE BACKUP =====")

with open("sample.txt", "r") as source:
    content = source.read()

with open("sample_backup.txt", "w") as backup:
    backup.write(content)

print("Backup created: sample_backup.txt")

print("\nAll File Handling Programs Executed Successfully!")