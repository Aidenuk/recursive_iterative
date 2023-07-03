

# recursive vs iterative
# find out x sqaure number cube and so on by using iterative and recursive. 

# 1) iterative 

def iterative(x,n):
  res = 1
  for i in range(n):
    res *= x
  return res

print(iterative(2,3))

# 2) recursive

def recur(x,n):
  if n ==1:
    return x
  else:
    return x * recur(x,n-1) # in math we could use x^n = x * x^n-1

print(recur(2,3))

# what is benefitial using recursive then?
# -> reduce local variables which may cause some error as well as any side effect.Also, it would be easily visible and changable when it comes to working as team. However, it may occur stack overflow as it keeps piling up stack memories. 
# recursive problem may fail to terminate. Therefore, you must have code which terminate recursive in this example, we use if statement till it reaches the given number. 

# sum all from input int number to x 
def sum(x):
  if x == 10:
    return x
  else:
    return x + sum(x+1)
print(sum(0))
    


    