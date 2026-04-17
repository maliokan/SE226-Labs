from data_package import remove_duplicates, strip_whitespaces, calculate_mean, find_maximum, find_minimum

raw = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): ")
tokens = strip_whitespaces(raw.split(","))
numbers = [float(t) for t in tokens]
cleaned = remove_duplicates(numbers)

print(f"\nCleaned and unique data: {cleaned}")
print("-" * 20)
print(f"Mean: {calculate_mean(cleaned)}")
print(f"Maximum: {find_maximum(cleaned)}")
print(f"Minimum: {find_minimum(cleaned)}")