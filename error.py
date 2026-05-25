def check_age(age):
    if age < 0:
        # Manually raising a ValueError with a custom message
        raise ValueError("Age cannot be negative.")
    return f"Age is {age}"

try:
    print(check_age(-5))
except ValueError as fault:
    print(f"Caught an error: {fault}")
