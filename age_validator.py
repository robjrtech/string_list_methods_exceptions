def validate_age(age):
    try: 
        age = int(age)
        if age < 0:
            raise ValueError("Age cannot be a negative number")
        elif age >= 120:
            raise ValueError("Age has to be between 0 and 120, due to government ordnance 'New Frontier'!")
        print("Welcome to my House!")

    except ValueError as error:
        print(f"Error: {error}")

age = input("Provide your age: ")
validate_age(age)

