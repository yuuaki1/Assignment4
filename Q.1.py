while True:
    m=int(input('Enter the marks: '))
    if m in range(0,101):
        if m<25:
            print('F')
        elif m in range(25,46):
            print('E')
        elif m in range(46,51):
            print('D')
        elif m in range(51,61):
            print('C')
        elif m in range(61,81):
            print('B')
        else:
            print('A')
        
