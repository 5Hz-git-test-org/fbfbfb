for i in range(1, 16+1):
    if i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print('fizz')
    else:
        print(f'{i}')