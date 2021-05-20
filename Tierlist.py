import random
import time

pool = []


def choice():
    inp = input("How many choices do you want? ")
    for i in range(int(inp)):
        i += 1
        inp2 = input("Choice #" + str(i) + ': ')
        inp2 += ' > '
        pool.append(inp2)
    gen(True)


def gen(doInput):
    if doInput == True:
        inp = input("Do you want to generate a tier list? (yes/no) ")
        if inp == 'yes':
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
        elif inp == 'no':
            print("Okay, terminating process..!")
            quit(-1)
        else:
            print("I couldn't parse that input! Try again")
            gen(True)
        choice()
    elif doInput == False:
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


choice()
