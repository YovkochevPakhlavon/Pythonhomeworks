import os
import string
from collections import Counter

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def check_or_create_file(file_path):
    if not os.path.exists(file_path):
        print("File not found! Please enter a paragraph to create 'sample.txt':")
        user_text = input("Enter your paragraph: ")
        
        # Create and write the user's paragraph to the file
        file = open(file_path, 'wt+')
        file.write(user_text)
        print("File created successfully!")
        content=file.read()
        file.close()
        return content
    else:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
# File path
file_path = "sample.txt"

# Check or create the file
content = check_or_create_file(file_path)

#Ignore capitalization:
lower_content = content.lower()

#Ignore punctuation (like commas, periods, etc.):
cleaned_content=remove_punctuation(lower_content)

#Split it into individual words:
words=cleaned_content.split(" ")

# Count total words
total_words = len(words)

# Count word frequencies
word_counts = Counter(words)
    
# Get the top 5 most common words
top_words = word_counts.most_common(5)

# Display results
print(f"\nTotal number of words: {total_words}")
print("Top 5 most common words:")
for word, count in top_words:
    print(f"{word}: {count}")

# Save results to "word_count_report.txt"
report_path = "word_count_report.txt"
with open(report_path, 'w') as report:
    report.write(f"Total number of words: {total_words}\n")
    report.write("Top 5 most common words:\n")
    for word, count in top_words:
        report.write(f"{word}: {count}\n")

print(f"\nReport saved to '{report_path}'.")
