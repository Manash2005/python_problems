'''Write a Python program that takes a sentence as input and counts the occurrences of each word. Ignore case differences (e.g., "Hello" and "hello" should be considered the same word).'''

from collections import Counter

sentence = input("Enter your sentence: ")
sentence = sentence.lower()
sentence = sentence.split()

counter = Counter(sentence)
print(counter) 