def prime_number(n):
    for i in range(2,n):

        for j in range(2,i):
            if i%j == 0 :
                break
        else:
            print(i,'is prime number')


if __name__ == '__main__':
    prime_number(100)
