# The next example is a simple Python-based algorithm for determining whether a number is prime

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
        return True

# The preceding code accepts a number as an argument and begins a for loop in
# which we divide the number by every integer from 2 up to that number and see
# if there’s a remainder. If there’s no remainder, we know that the number is
# not prime and we immediately return False. If we make it all the way up to the
# number and always find a remainder, then we know that the number is prime
# and we return True.

# In this case, the key question is slightly different than in the previous examples.
# In the previous examples, our key question asked how many steps the
# algorithm would take if there were N data elements in an array. Here, we’re
# not dealing with an array, but we are dealing with a number that we pass into
# this function. Depending on the number we pass in, this will affect how many 
# times the function’s loop runs.