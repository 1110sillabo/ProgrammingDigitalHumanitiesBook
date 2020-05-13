items = 1, 2, 3, 4
def yourfunction(x):
  print(x)
  print(x*x)
  
output = [yourfunction(item) for item in items]
