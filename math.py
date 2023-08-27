import math
def getsin(x):
    multiplier = 1
    result = 0
    
  for i in range(1,20,2):
		result += multiplier*pow(x,i)/math.factorial(i)
		multiplier *= -1
		
	return result
    
getsin(math.pi/2) # returns 1.0 
getsin(math.pi/4) # returns 0.7071067811865475
