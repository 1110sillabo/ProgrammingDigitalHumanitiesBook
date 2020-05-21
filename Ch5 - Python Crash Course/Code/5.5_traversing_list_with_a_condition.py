# Checking a condition on a lit


# Initialize the list we want to test
test_list = ['no', 'yesss', 'tooshort', 'arg', 'nop', 'nope']
# Initialize the result list
result_list = [] #[] empty list

# Start iteration on the test_list
for item in test_list: # item is conventional. Use what you like.

# Check the item
    if len(item) > 3:
        result_list.append(item)

print(result_list)    

# Curved balls questions
# what is len(result_list)? and len(test_list)?
# what about len(test_list[2])?
