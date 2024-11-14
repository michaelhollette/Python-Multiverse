# file_handling_examples.py

# Opening a File in Read Mode
# "r" mode is for reading. The file must exist or an error will be raised.
file = open("example.txt", "r")
# Reading the entire file content at once
content = file.read()
print("File Content Read All at Once:")
print(content)
# Close the file after reading
file.close()

# Writing to a File
# "w" mode is for writing. If the file exists, it will be overwritten.
# If it doesn't exist, it will be created.
with open("example.txt", "w") as file:
    # Writing two lines to the file
    file.write("This is a line of text.\n")
    file.write("This is another line.\n")
print("Data written to 'example.txt' with 'w' mode.")

# Reading the File Line by Line
# Reopen the file in read mode to confirm what we wrote.
with open("example.txt", "r") as file:
    print("Reading file line by line:")
    # Reading each line one at a time
    for line in file:
        print(line.strip())  # strip() removes any extra newline characters

# Appending to a File
# "a" mode is for appending. It adds content at the end without overwriting existing content.
with open("example.txt", "a") as file:
    # Appending a new line to the file
    file.write("Appended text.\n")
print("Data appended to 'example.txt' with 'a' mode.")

# Reading All Lines as a List
# Reopen the file in read mode and read all lines into a list.
with open("example.txt", "r") as file:
    content = file.readlines()
    print("File content as a list of lines:")
    print(content)

# Using the 'with' statement
# The 'with' statement automatically closes the file after the block is executed.
with open("example.txt", "r") as file:
    print("Using 'with' to automatically handle file closing:")
    content = file.read()
    print(content)

# Handling Binary Files
# "rb" mode is for reading binary files, often used for non-text files like images.
# (This requires a binary file to work with; replace 'image.jpg' with your file's name)
try:
    with open("image.jpg", "rb") as file:
        data = file.read()
    print("Binary file read successfully.")
except FileNotFoundError:
    print("Binary file 'image.jpg' not found. Ensure a binary file is available.")

# Summary of File Modes and Actions
# Modes: "r" (read), "w" (write), "a" (append), "rb" (read binary)
# Action: Use with 'with' for automatic closing, .read() for whole file, .readline() for one line,
# .readlines() for list of lines, and .write() to write text.
