
import tuna
import random

#tutoiral # 10
'''
for n in range(101):
    if n is magicNumber:
        print(n, "is the magic number!")
        break
    else:
        print(n)
'''
# magicNumber = 26
'''
numbersTaken = [2, 5, 12, 13, 17]

print("Here are the numbers that are still available")

for n in range(1,20):
    if n in numbersTaken:
        continue
    print(n)
'''

# function

''' def beef():
    print("daym, function are cool!")

beef()
'''
'''
def bitcoin_to_usd(btc):
    amount = btc * 527
    print(amount)

bitcoin_to_usd(1)

'''

# Dating Advice for guys ** next Gen ...lol
'''
def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age

guys_limit = allowed_dating_age(25)
print(guys_limit
'''

#Default values for Arguments
'''
def get_geneder(sex = 'Unknown'):
    if sex is 'm':
       sex  = "Male"
    elif sex is 'f':
        sex = "Female"
    print(sex)

get_geneder('m')
get_geneder('f')
get_geneder()
'''

#variable scope
'''
a = 7834

def corn():
    print(a)


def fudge():
    print(a)


corn()
fudge()

'''
# video # 16 -- keyword arguments --****
'''
def dumb_snce(name='Bucky', action='ate', item='tuna'):
    print(name, action, item)

dumb_snce("sally", "farts", "gently")



dumb_snce(name='surafel', action='is', item='smart boy')
'''

#flexible  number of arguments -- Video 17

'''
def add_numbers(*args):
    total = 0

    for a in args:
        total += a
    print(total)

add_numbers(3, 9, 10)

'''


#video 18 -- unpacking arguments
'''
def health_calculator(age, apple_ate, cigs_smoked):
    answer = (100-age) + (apple_ate * 3.5) - (cigs_smoked * 2)
    print(answer)


bucky_date =[27, 20, 0]

'health_calculator(bucky_date[0], bucky_date[1], bucky_date[2])'


health_calculator(*bucky_date)

'''
#sets --ignores duplicates
'''
groceries = {'creal', 'milk', 'starcrunch', 'beer', 'duck', 'beer'}

print(groceries)

if 'milk' in groceries:
    print("you already bought it")
else:
    print("you don't have it")
'''


#dictionary in paython
'''
classmates = {'Tony': 'person number 1', 'Mark': 'person number 2 ', 'Borch': 'this is my name'}


print(classmates)

print(classmates['Mark'])


for k, v in classmates.items():
    print(k + v)

'''

#modules


tuna.calling()


x = random.randrange(1, 1000)

print(x)








