from itertools import count
import time
from random import randint

#Happy 2023 year

for i in range(1,45):
    print('')

    s = ''

    for i in range(1,1000):
        count = randint(1,100)
        while (count > 0):
            s += ''
            count -= 1

            if (i%10==0):
                print(s + 'Happy New Year 2023')
            else:
                print(s + '*')
            s = ''
            time.sleep
