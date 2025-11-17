import time
import sys
a='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
z=print
l=input
def i(n, o):
    t=0
    for c in range(len(n)):
        t+=a.index(n[-(c+1)])*(int(o)**c)
    return t
def p(d, t):
    if d==0:
        return '0'
    c = ''
    while d > int(t):
        c=str(a[d%int(t)]) + c
        d=d//int(t)
    c=str(a[d]) + c
    return c
while True:
    z("Welcome to the abode of the hexorcist, I see not only did you not want to do the calculation yourself, or just google it, but went out of your way to get a python script to do it!\n")
    z("Well i guess lets do this then since you put so much work in to get here\n")
    o=l("Alright, well what base is it in?(2-36) ")
    n=l("Well get on with it, what's your number? ")
    t=l("What base would you like to convert to?(2-36) ")
    for c in '\nPython scripting your results\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
    z(f"\nYour original number {n} in base {o} is {p(i(n, o),t)} in base {t}")
    if l("\nWould you like to calculate a different number(yes/no) ") == 'no':
        break
    continue
z("\nThanks for connecting with the hexorcist, maybe just google it next time")