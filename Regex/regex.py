# regex_guide.py

"""
Regular Expressions in Python - A Comprehensive Guide

This guide explains what regular expressions (regex) are, how they work, and provides examples and use cases.
"""

import re

# Introduction
### Introduction to Regular Expressions ###
"""
Regular expressions (regex) are powerful tools for matching patterns within text.
They allow you to define search criteria using a combination of characters, symbols, and special sequences.
Python provides built-in regex support through the 're' module.
"""

# Basic Regex Concepts
### Basic Concepts ###
"""
- Literal Characters: These match exactly as they are written. For example, 'hello' matches any occurrence of 'hello'.
- Metacharacters: Special characters with unique functions. Some common ones include:
  - . : Matches any character except newline.
  - ^ : Matches the start of a line.
  - $ : Matches the end of a line.
  - \\d : Matches any digit (0-9).
  - \\w : Matches any word character (alphanumeric + underscore).
  - \\s : Matches any whitespace character (space, tab, newline).
  - + : Matches one or more of the preceding pattern.
  - * : Matches zero or more of the preceding pattern.
  - ? : Matches zero or one of the preceding pattern.
  - {n,m} : Matches between n and m repetitions of the preceding pattern.
- Character Classes: Define a set of possible characters to match, e.g., '[abc]' matches 'a', 'b', or 'c'.
- Grouping and Capturing: Parentheses () group parts of a regex and capture the match.
- Escaping: Use \\ to match special characters literally, e.g., '\\.' matches a literal dot.
"""

# Example 1: Searching for a Pattern
print("### Example 1: Searching for a Pattern ###")
text = "My phone number is 555-123-4567. Call me!"
pattern = r"\d{3}-\d{3}-\d{4}"

print(f"\nSearching for pattern '{pattern}' in text: '{text}'")
match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found")

# Example 2: Replacing Text
print("\n### Example 2: Replacing Text ###")
replacement_text = re.sub(pattern, "[PHONE]", text)
print(f"Replacing phone numbers with '[PHONE]': '{replacement_text}'")

# Example 3: Finding All Matches
print("\n### Example 3: Finding All Matches ###")
text_multiple = "Contact 555-123-4567 or 123-456-7890 for help."
pattern_all = r"\d{3}-\d{3}-\d{4}"

print(f"\nFinding all phone numbers in text: '{text_multiple}'")
matches = re.findall(pattern_all, text_multiple)
print("All matches found:", matches)

# Example 4: Validating an Email
print("\n### Example 4: Validating an Email ###")
email = "user@example.com"
email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

def validate_email(email):
    if re.match(email_pattern, email):
        print(f"'{email}' is a valid email address.")
    else:
        print(f"'{email}' is NOT a valid email address.")

validate_email(email)

# Example 5: Splitting Text Based on a Pattern
print("\n### Example 5: Splitting Text Based on a Pattern ###")
text_to_split = "apple, banana; orange|grape"
split_pattern = r"[,;|]"

print(f"\nSplitting text '{text_to_split}' by commas, semicolons, or pipes.")
split_text = re.split(split_pattern, text_to_split)
print("Split result:", split_text)

# Example 6: Extracting Groups
print("\n### Example 6: Extracting Groups ###")
date_text = "Today's date is 2024-11-13."
date_pattern = r"(\d{4})-(\d{2})-(\d{2})"

print(f"\nExtracting year, month, and day from date text: '{date_text}'")
date_match = re.search(date_pattern, date_text)
if date_match:
    year, month, day = date_match.groups()
    print("Extracted Date - Year:", year, "Month:", month, "Day:", day)

# Summary of re Functions
### Summary of 're' Module Functions ###
"""
- re.search(pattern, string): Searches for the first match of the pattern in the string. Returns a Match object or None.
- re.match(pattern, string): Matches the pattern only at the start of the string.
- re.findall(pattern, string): Returns all occurrences of the pattern in the string as a list.
- re.sub(pattern, replacement, string): Replaces occurrences of the pattern in the string with the specified replacement.
- re.split(pattern, string): Splits the string by occurrences of the pattern.
"""

# Conclusion
### Conclusion ###
"""
Regular expressions are incredibly versatile for text processing, validation, and extraction.
With the 're' module, Python makes regex operations simple and efficient.
Experiment with different patterns to understand their behavior in various use cases.
"""
