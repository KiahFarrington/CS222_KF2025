"""
Python Collection Types: Lists, Tuples, Sets, and Dictionaries
--------------------------------------------------------------
This file explains each type, how to create it, how it behaves,
and demonstrates common operations.
Run this file to see all examples in action.
"""
# ==============================================================
# ✅ NESTED LISTS (2D)
# ==============================================================

print("\n--- NESTED LISTS ---")
afc = [
    ["Colts", "Jaguars", "Titans", "Texans"],
    ["Patriots", "Jets", "Dolphins", "Bills"],
    ["Browns", "Bengals", "Steelers", "Ravens"],
    ["Chargers", "Broncos", "Chiefs", "Raiders"]
]
print("Entire 3rd division:", afc[2])
print("2nd team in 3rd division:", afc[2][1])
print("First letter of that team:", afc[2][1][0])

# Shows how to index into nested structures:
# list[row][column][character]

# ==============================================================
# 1️⃣ LIST
# ==============================================================

print("\n--- LIST ---")
# Ordered, changeable (mutable), allows duplicates

fruits = ["apple", "banana", "cherry", "banana"]
print("Original list:", fruits) # preserves insertion order

# Access by index
print("First item:", fruits[0]) # 'apple'
print("Last item:", fruits[-1]) # 'banana'

# Modify
fruits[1] = "blueberry" # change value
fruits.append("date") # add to end
fruits.insert(1, "kiwi") # insert at position
print("After modifications:", fruits)

# Remove
fruits.remove("banana") # removes first occurrence
popped = fruits.pop() # removes last item
print("Popped:", popped)
print("After removals:", fruits)

# Iterate
for f in fruits:
    print("Fruit:", f)

# Slicing
print("First two:", fruits[:2])

# Check membership
print("Is 'cherry' in list?", "cherry" in fruits)

# ==============================================================
# 2️⃣ TUPLE
# ==============================================================

print("\n--- TUPLE ---")
# Ordered, **immutable**, allows duplicates

colors = ("red", "green", "blue", "red")
print("Tuple:", colors)

# Access by index
print("Second color:", colors[1])

# Count occurrences
print("'red' appears:", colors.count("red"))

# Index of value
print("Index of 'blue':", colors.index("blue"))

# Attempting to modify will cause an error:
# colors[0] = "orange"  # Uncomment to see TypeError

# Tuples are useful for fixed collections (e.g., coordinates)
point = (10, 20)
x, y = point  # tuple unpacking
print("x:", x, "y:", y) # x: 10 y: 20

# ==============================================================
# 3️⃣ SET
# ==============================================================

print("\n--- SET ---")
# Unordered, changeable (mutable), **no duplicates**

numbers = {1, 2, 3, 2, 1}
print("Set contents:", numbers)  # duplicates removed automatically

# Add / remove
numbers.add(4)
numbers.discard(2)
print("After add/discard:", numbers)

# Set operations
odds = {1, 3, 5}
evens = {2, 4, 6}
print("Union:", odds | evens)
print("Intersection:", numbers & odds)
print("Difference:", numbers - odds)

# Check membership
print("Is 3 in set?", 3 in numbers)

# Iterate
for n in numbers:
    print("Number:", n)

# Note: no indexing because sets are unordered
# numbers[0]  # would raise TypeError

# ==============================================================
# 4️⃣ DICTIONARY
# ==============================================================

print("\n--- DICTIONARY ---")
# Key → Value pairs, keys are unique, insertion order preserved (Python 3.7+)

person = {
    "name": "Alice",
    "age": 20,
    "hobbies": ["reading", "swimming"]
}
print("Dictionary:", person)

# Access
print("Name:", person["name"])
print("Age using get:", person.get("age"))

# Add or modify
person["age"] = 21                 # update
person["city"] = "Chicago"         # add new key
print("After update:", person)

# Remove
removed = person.pop("city")       # remove by key
print("Removed city:", removed)

# Keys / Values / Items
print("Keys:", person.keys())      # dict_keys object
print("Values:", person.values())  # dict_values object
print("Items:", person.items())    # dict_items object (key,value tuples)

# Looping
for key, value in person.items():
    print(key, "→", value)

# Nested access
print("First hobby:", person["hobbies"][0])

# ==============================================================
# Quick Comparison Summary
# ==============================================================

print("\n--- QUICK COMPARISON ---")
summary = """
LIST  : Ordered, mutable, allows duplicates, index-based access.
TUPLE : Ordered, immutable, allows duplicates, index-based access.
SET   : Unordered, mutable, no duplicates, no index access.
DICT  : Key–value mapping, keys unique, preserves insertion order.
STRING: Immutable sequence of characters (supports indexing & slicing like lists).
"""
print(summary)
