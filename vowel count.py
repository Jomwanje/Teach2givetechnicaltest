# Question 6: Count Vowels
# Write a program that counts the number of vowels in a sentence.
# eg " Hello World " => returns 2

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    return sum(1 for char in sentence if char in vowels)

print(count_vowels(" Hello Woorld "))
