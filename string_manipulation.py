# Takes a user input
user_input = input("Enter a sentence:")

# Stores the users input in uppercase
uppercase_user_input = user_input.upper()
print("Your input in uppercase", uppercase_user_input)

# Stores the users input in reverse
reverse_user_input = " ".join(user_input.split()[::-1])
print("Your input in reversed order", reverse_user_input)


# Checks if the user input contains vowels and counts them
vowels = "aeiouAEIOU"

if any(char in vowels for char in user_input):
    count = sum(1 for char in user_input if char in vowels)
    print("Your input contains vowels")
    print("Number of vowels:", count)

# Replaces spaces in the user input with hyphens
user_input_no_spaces = user_input.replace(" ", "-")
print("Your input with spaces replaced by hyphens:", user_input_no_spaces)