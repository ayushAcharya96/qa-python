for i in range(3, 30):
    flag = True
    for a in range(2, i):
        if i % a == 0:
            # flag = False
            break
    if flag:
        print(i)
    print(i)
