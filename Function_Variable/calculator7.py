# Demonstrates formatting with commas

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

# Like 1,000
print(f"{z:,}")
