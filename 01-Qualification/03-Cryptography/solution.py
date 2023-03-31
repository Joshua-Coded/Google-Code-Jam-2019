#!/usr/bin/env python3

from math import gcd


def main():

    t = int(input())

    for i in range(1, t+1):
        input()

        nums = [int(x) for x in input().split()]

        nums_copy = nums[1:]

        while nums[0] == nums[1]:
            nums = nums[1:]

        nums_removed = nums_copy[:len(nums_copy) - len(nums)][::-1]


        a, b = nums[:2]
        p = gcd(a, b)
        p a // p


        factored = [q, p, b // p]

        p = b // p

        for x in nums[:2]:
            p = x // p
            factored.append(p)

        factored.reverse()

        primes = sorted(list(set(factored)))


        if len(primes) != 26:
            while(True):
                print(1)

        dic = {primes[i]: chr(i+65) for i in range(26)}

        result = ''.join([dic[x] for x in factored])
        print("Case #{0}: {1}".format(i, result))



if __name__ == 'main':
    main()
    
