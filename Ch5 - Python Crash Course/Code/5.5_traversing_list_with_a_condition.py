#checking a condition on a lit


#initialize the list we want to test
test_list = ['no', 'yesss', 'tooshort', 'arg', 'nop', 'nope']
#initialize the result list
result_list = [] #[] empty list

#start iteration on the test_list
for item in test_list: #item is conventional. Use what you like.

#check the item
    if len(item) > 3:
        result_list.append(item)

print(result_list)    

#curved balls questions
#what is len(result_list)? and len(test_list)?
#what about len(test_list[2])?
