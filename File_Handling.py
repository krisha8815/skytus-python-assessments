# 1. Read a file and display its contents
with open("sample.txt", "r") as file:
    print("1. File Contents:")
    print(file.read())


# 2. Count the number of lines in a file
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print("\n2. Number of Lines:", len(lines))


# 3. Count how many times each word appears in a file
word_count = {}

with open("sample.txt", "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            word = word.lower()
            word_count[word] = word_count.get(word, 0) + 1

print("\n3. Word Frequency:")
print(word_count)


# 4. Write 5 user-entered sentences to a file
with open("sentences.txt", "w") as file:
    print("\n4. Enter 5 sentences:")
    for i in range(5):
        sentence = input(f"Sentence {i+1}: ")
        file.write(sentence + "\n")

print("Sentences saved successfully.")


# 5. Append a list of strings to an existing file
lines = ["Python\n", "File Handling\n", "Append Example\n"]

with open("sample.txt", "a") as file:
    file.writelines(lines)

print("\n5. Strings appended successfully.")


# 6. Read a file and print only lines containing a specific word
search_word = input("\nEnter word to search: ")

with open("sample.txt", "r") as file:
    print("6. Matching Lines:")
    for line in file:
        if search_word.lower() in line.lower():
            print(line.strip())


# 7. Replace a specific word in a file and save changes
old_word = input("\nEnter word to replace: ")
new_word = input("Enter new word: ")

with open("sample.txt", "r") as file:
    content = file.read()

content = content.replace(old_word, new_word)

with open("sample.txt", "w") as file:
    file.write(content)

print("7. Word replaced successfully.")


# 8. Merge contents of two text files into a third file
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    data1 = f1.read()
    data2 = f2.read()

with open("merged.txt", "w") as merged:
    merged.write(data1)
    merged.write("\n")
    merged.write(data2)

print("8. Files merged successfully.")


# 9. Read a CSV file and display its content
import csv

print("\n9. CSV Contents:")
with open("data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(" | ".join(row))


# 10. Back up a file by copying its contents into another file
with open("sample.txt", "r") as source:
    content = source.read()

with open("backup_sample.txt", "w") as backup:
    backup.write(content)

print("\n10. Backup created successfully.")