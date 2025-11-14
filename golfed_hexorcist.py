import time
import sys

a='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def to_decimal(n, o):
    t=0

    for c in range(len(n)):
        t+=a.index(n[-(c+1)])*(int(o)**c)
    
    return t


def from_decimal(d, t):
    if d==0:
        return '0'
    
    c = ''

    while d > int(t):
        c=str(a[d%int(t)]) + c
        d=d//int(t)
    
    c=str(a[d]) + c
    return c

while True:
    print("Welcome to the abode of the hexorcist, I see not only did you not want to do the calculation yourself, or just google it, but went out of your way to get a python script to do it!\n")
    print("Well i guess lets do this then since you put so much work in to get here\n")

    o=input("Alright, well what base is it in?(2-36) ")
    n=input("Well get on with it, what's your number? ")
    t=input("What base would you like to convert to?(2-36) ")
    for c in '\nPython scripting your results\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

    print(f"\nYour original number {n} in base {o} is {from_decimal(to_decimal(n, o),t)} in base {t}")
    if input("\nWould you like to calculate a different number(yes/no) ") == 'no':
        break
    continue

print("\nThanks for connecting with the hexorcist, maybe just google it next time")