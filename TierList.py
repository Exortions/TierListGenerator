import random
import time

pool = ['Mental Health > ', 'School > ', 'Homework > ', 'Video Games > ']
def gen(doInput): # doInput checks if you want the prompt "Do you want to create a tier list? (yes/no)" 
    if doInput == True: # If doInput is true, show prompt
        inp = input("Do you want to generate a tier list? (yes/no) ") # The prompt
        if inp == 'yes': # If the input from the prompt is yes, continue
            key = '' # The tier list
            pools_called = [] # Pools called is used to see what choices have already been chosen from the pool.
            tmp = len(pool) # The total amount of items in the pool
            for i in range(tmp): # Repeat for each item in the pool
                temp2 = random.choice(pool) # A random choice in the pool
                if temp2 not in pools_called: # If the random choice hasn't been called yet, continue
                    key += temp2 # Add the random choice to the key
                    pools_called.append(temp2) # Add the random choice to the pools_called
                    time.sleep(0.01) # Wait a 0.01 of a second
                else: # If the random choice is already in the pool list, continue
                    print('Couldn\'t generate tier list... trying again! EC: DUPLICATE_POOL_CHOICE') # Say it couldn't generate the tier list with the error code DUPLICATE_POOL_CHOICE
                    gen(False) # Try to re-generate the key without the prompt
            final_key = key + "Nothing" # Add nothing to the end of the key.
            print('Tier list: ' + final_key) # Print the tier list
            gen(True) # Generate the key again with the prompt.
        elif inp == 'no': # If input is no, terminate process
            print("Okay, terminating process..!")
            quit(-1)
        else: # If input is anything else than yes or no, re-try prompt.
            print("I couldn't parse that input! Try again")
            gen(True)
    elif doInput == False: #If doInput is false, do the same thing as above but without the prompt.
        key = ''
        pools_called = []
        tmp = len(pool)
        for i in range(tmp):
            temp2 = random.choice(pool)
            if temp2 not in pools_called:
                key += temp2
                pools_called.append(temp2)
                time.sleep(0.01)
            else:
                print('Couldn\'t generate tier list... trying again! EC: DUPLICATE_POOL_CHOICE')
                gen(False)
        final_key = key + "nothing"
        print('Tier list: ' + final_key)
        gen(True)
gen(True) # Generate the key with the prompt. This is the code that runs at start of the program.
