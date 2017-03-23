#*********Now write a program to user input three and which number are big

a = int (input('Enter a number : '))

b = int (input('Enter b number : '))

c = int (input('Enter c number : '))

if a > b:

    if a > c:

        print('\nA >B > C')

    else:
        print('\nC is getter then A and B')

elif b > c:

    print('\nB is getter then A and C')

elif a ==b and b ==c:

    print('A = B = C')

else:

    print('\nC is getter then A and B')