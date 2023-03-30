#!/usr/bin/env python3

def main():
    # 't' : Number of test cases

    t = int(input())
    for i in range(1, t+1):
        # 'n' : the prime number
        n = input()
        a = n.replace('4', '3')
        print("CASE #{0}: {1} {2}".format(i, a, int(n) - int(a)))


if __name__ == 'main':
    main()
