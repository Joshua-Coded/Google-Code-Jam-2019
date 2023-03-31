#!/usr/bin/env python3

def main():

    t = int(input())
    for i in range(1, t+1):
        input()
        p = input()

        res = p.replace('E', '0').replace('S', 'E').replace('0', 'S')
        print('Case #{0}: {1}'.format(i, res))



if __name__ == 'main':
    main()
