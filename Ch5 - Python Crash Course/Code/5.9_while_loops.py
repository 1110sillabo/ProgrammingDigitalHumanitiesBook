#while loops
"""
a = 1
b = 10
while a < b:
    print(a) #will go on forever 
"""

#docstringed loop above. Uncomment to see an infinite loop
#then kill it or wait for Python to reach an error

a = 1
b = 10
while a < b:
    print(a)
    a = a +1 #now it will stop
    #bonus: calculate the iterations before this stops
    
while True:
    #asks you things forever
    answer = input('Are you happy?')
    #unless you are forced into optimism
    if answer == 'yes':
        break
