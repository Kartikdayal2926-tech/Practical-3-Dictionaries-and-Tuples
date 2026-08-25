# Practical 3 - Dictionaries & Tuples
# Name: Kartik Dayal
# University: Shoolini University

# =========================
# PART-A: DICTIONARIES
# =========================

# Q1. Create an empty Dictionary
inventory = {}
print(inventory)


# Q2. Store the first product details in variables
ProductNo1_name = "Mobile Phone"
ProductNo1_quantity = 5
ProductNo1_price = 20000
ProductNo1_releaseYear = 2020

print(ProductNo1_name)
print(ProductNo1_quantity)
print(ProductNo1_price)
print(ProductNo1_releaseYear)


# Q3. Add details in inventory
inventory["ProductNo1"] = {
    "Name": ProductNo1_name,
    "Quantity": ProductNo1_quantity,
    "Price": ProductNo1_price,
    "ReleaseYear": ProductNo1_releaseYear
}

print(inventory)


# Q4. Store the second product details in variables
ProductNo2_name = "Laptop"
ProductNo2_quantity = 3
ProductNo2_price = 50000
ProductNo2_releaseYear = 2022

print(ProductNo2_name)
print(ProductNo2_quantity)
print(ProductNo2_price)
print(ProductNo2_releaseYear)


# Q5. Add the second product details in inventory
inventory["ProductNo2"] = {
    "Name": ProductNo2_name,
    "Quantity": ProductNo2_quantity,
    "Price": ProductNo2_price,
    "ReleaseYear": ProductNo2_releaseYear
}

print(inventory)


# Q6. Display the products present in inventory
print("Products present in inventory:")
print(inventory)


# Q7. Check if release years are in inventory
print(ProductNo1_releaseYear in inventory["ProductNo1"].values())
print(ProductNo2_releaseYear in inventory["ProductNo2"].values())


# Q8. Delete release year of both products
del inventory["ProductNo1"]["ReleaseYear"]
del inventory["ProductNo2"]["ReleaseYear"]

print(inventory)


# =========================
# PART-B: TUPLES
# =========================

# Q1. Create a tuple called prices
prices = (250, 300, 150, 400, 100, 350, 200)
print(prices)


# Q2. Find and print the highest price
print("Highest price:", max(prices))


# Q3. Find and print the lowest price
print("Lowest price:", min(prices))


# Q4. Calculate and print the total sum
print("Total sum:", sum(prices))


# Q5. Convert the tuple into a sorted list
sorted_prices = sorted(prices)
print("Sorted list:", sorted_prices)


# Q6. Try to modify an element in the tuple
# This raises TypeError because tuples are immutable.
prices[0] = 500
