# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.
# Examples:
# 8 => returns true
# 6 => returns false

def is_power_of_two(num):
    return num > 0 and (num & (num - 1)) == 0

print(is_power_of_two(8))
print(is_power_of_two(36))
