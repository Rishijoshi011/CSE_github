def power(num, pow = 2):
    return num ** pow

num = int(input("Enter any number: "))
power_ = int(input("Enter power for number: "))

print(f"Square of {num} is: {power(num)}")
print(f"{num} rest to {power_} is: {power(num, power_)}")