
#here we are using default dict which is used to initialize the dict elements with default value
from collections import defaultdict 
  
#jug1 and jug2 have the max capacity of two jugs and target is the amount to be measured

jug1=int(input("Enter the capacity of Jug1"))
jug2=int(input("Enter the capacity of Jug2"))
target=int(input("Enter the capacity to be measured within the range of Max(Jug1,Jug2)"))

# Initialize dictionary with  
# default value as false. 
visited = defaultdict(lambda: False) 
print(visited)
  
# Recursive function which prints the intermediate steps to reach the final  
# solution and return boolean value  (True if solution is possible, otherwise False).

# amountt1 and amount2 are the amount of water present  in both jugs at a certain point of time. 
def waterjugProblem(amount1, amount2):  
  
    # returns true if out goal is achieved else return False
    if (amount1 == target and amount2 == 0) or (amount2 == target and amount1 == 0): 
        print(amount1,amount2) 
        return True
      
    # Checks if we have already visited the 
    # combination or not. If not, then it proceeds further. 
    if visited[(amount1, amount2)] == False: 
        print(amount1,amount2) 
      
        # Changes the boolean value to True indicating we already visited this combination
        visited[(amount1, amount2)] = True
      
        # here we are exploring 6 possible Solution
        #Empty the first jug completely
        #Empty the second jug completely
        #Fill the first jug
        #Fill the second jug
        #Fill the water from the second jug into the first jug until the first jug is full or the second jug has no water left
        #Fill the water from the first jug into the second jug until the second jug is full or the first jug has no water left1.
        
        return (waterjugProblem(0, amount2) or
                waterjugProblem(amount1, 0) or
                waterjugProblem(jug1, amount2) or
                waterjugProblem(amount1, jug2) or
                waterjugProblem(amount1 + min(amount2, (jug1-amount1)), 
                amount2 - min(amount2, (jug1-amount1))) or
                waterjugProblem(amount1 - min(amount1, (jug2-amount2)), 
                amount2 + min(amount1, (jug2-amount2)))) 
      
    #if the combination (amount1,amount2) is already visited return False as we do not perform same resursive call
    else: 
        return False
  
print("Steps: ") 
  
# Call the function and pass the 
# initial amount of water present in both jugs. 
waterjugProblem(0, 0)
