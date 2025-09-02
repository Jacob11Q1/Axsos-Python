# Default Parameters And Named Arguments:

def beCheerful(name = '' , repeat = 2): # Set defaults when declaring the parameters
    print(f"Good Morning {name}\n" * repeat)
# Example 1:
beCheerful() # Output: Good Morning (Repeated on 2 lines)
beCheerful("Tin") # Output: Good Morning Tim (Repeated on 2 lines)

# Example 2:
beCheerful(repeat = 6) # Output: Good Morning (Repeated in 6 lines)
beCheerful(name = "Jacob" , repeat = 5) # Output: Good Morning Jacob (Repeated in 5 lines)
beCheerful(repeat = 3, name = "KB") # Output: Good Morning KB (Repeated in 3 lines)
# Note: in the above line The Argument order doesn't matter if we are explicit when sending in our arguments!

def yourName(name):
    print(f"Your Name is: {name}")
yourName("Trent Alexander Arnold")