'''Write a Python program that takes a sentence as input and counts the occurrences of each word. Ignore case differences (e.g., "Hello" and "hello" should be considered the same word).Delete the most occured word'''

from collections import Counter

sentence = input("Enter your sentence: ")
sentence = sentence.lower()
sentence = sentence.split()

counter = Counter(sentence)
print(counter)

common_word = counter.most_common(1)[0][0]

print(common_word)

del counter[common_word]

print(counter)