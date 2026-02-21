# Function to calculate the product of all elements in a tuple
def multiply_tuple(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Example tuple
my_tuple = (2, 3, 4, 5)

# Calculate and print the product
result = multiply_tuple(my_tuple)
print("The product of the tuple elements is:", result)