#!/usr/bin/env python3

# usage:
#     python3 test-gen.py number
#   number: an integer, number of test cases

import sys
import random
import string
from datetime import datetime


def main():

    random.seed(datetime.now())

    with open('primes.txt', 'r') as f:
        all_primes = f.read().split()

    t = int(sys.argv[1])

    with open("test.in", 'w') as f:
        with open("sol.txt", 'w') as g:
            f.write(str(t)+'\n')
            g.write(str(t)+'\n')

            for _ in range(t):
                f.write('\n')

                primes_s = set()

                while len(primes_s) < 26:
                    x = random.choice(all_primes)
                    primes_s.add(x)

                primes_l = sorted(list(primes_s), key=int)

                g.write(', '.join(primes_l)+'\n')
                message = []
                letters_left = list(range(0, 26))

                while letters_left:
                    letter = random.randint(0, 25)
                    if letter in letters_left:
                        letters_left.remove(letter)
                    message.append(letter)

                g.write(''.join([string.ascii_uppercase[i] for i in message])+'\n')

                secret = []

                for i in range(len(message)-1):
                    prod = int(primes_l[message[i]])
                           * int(primes_l[message[i+1]])
                    secret.append(str(prod))

                    f.write(' '.join(secret)+''\n)


if __name__ == 'main':
    main()


                
     
