# password generator

'''
length manditory
numeric optional
strength optional
length, num = False strength (weak,strong,very)
'''

import random, string

def password(length,num = False,strength='weak'):
    """length of password, if you want a number,
    and strength(weak,strong,very)"""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    letters = lower + upper
    dig = string.digits
    punct = string.punctuation
    pwd = ''
    if strength == 'weak':
        if num:
            length -= 2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(lower)
    elif strength == 'strong':
        if num:
            length -= 2
            for i in range(2):
                pwd += random.choice(dig)
    elif strength == 'very':
        ran = random.randint(2,4)
        if num:
            length -= 2
            for i in range(ran):
                pwd += random.choice(dig)
        length -= ran
        for i in range(ran):
            pwd += random.choice(punct)
        for i in range(length):
            pwd += random.choice(letters)
    pwd = list(pwd)
    random.shuffle(pwd)
    print(''.join(pwd))


password(8,num=True,strength='very')
