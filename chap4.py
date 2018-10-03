try:
    """
    converts str to float.
    exception for invalid input.
    """
    age = "55.5"
    float_age = float(age)
    print(float_age)
except ValueError:
    print("Invalid input")
    
