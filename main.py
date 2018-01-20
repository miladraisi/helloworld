#!/usr/bin/python3

def main():
    print('--Hello World!--')
    for i in range(1, 10):
        for j in range(1, 10):
            print(format(i*j, '3d'), end = '')
        print()

if __name__ == "__main__": main()
