# Dictionaries operations

address_book = {
              "Alice": "123", # Number as string
              "Bob": 231, # This number is an int
              "Carl": "312"
              }

# Get the value for a certain key 
# (and return the default, if provided.)
address_book.get("Alice")
address_book.get("Ann") # Returns 0, no Ann in our dict

# Print all values in the dictionary, one by one:

for x in address_book: # x takes the key
    print(address_book[x]) # dict[key] returns you the value


# You can use  values() function to return values of a dictionary:

for x in address_book.values():
# Now x is whatever is founf in values() - i.e. values already
    print(x)
  
# Loop through both keys and values
# use the items() function that tell which items we have
# in a dictionary, i.e. keys values:

for x, y in address_book.items():
    print(x, y)
  
# You can replace x and y with what they stand for
# i.e. key, value

for key, value in address_book.items():
    print(key, value)

