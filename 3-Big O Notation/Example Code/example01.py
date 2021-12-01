# Here's some typical Python code that prints all the itens from a list

things = ['apples', 'baboons', 'cribs', 'dulcimers']

for thing in things:
    print("Here's a thing: %s" % thing)

# The first thing to realize is that this is an example of an algorithm. 
# While it may not be fancy, any code that does anything at all is technically an algorithmit’s a particular process for solving a problem. 
# In this case, the problem is that we want to print all the items from a list. 
# The algorithm we use to solve this problem is a for loop containing a print statement.

# However, the number of steps isn’t constant. If the list contained 10 elements, the for loop would take 10 steps. 
# Since this for loop takes as many steps as there are elements, we’d say that this algorithm has an efficiency of O(N).