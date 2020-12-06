try:
    file= open("d:/dataMhs","a")
    print(file.write(a))
    int(input('masukkan bilangan bulat:'))
    while True:
        print('lagi (y/n)?:')
        x = int(input())
        if x == n:
            break
    file.close(n)
except NameError:
    while True:
        t =int(input('masukkan bilangan bulat:'))
        print('lagi (y/n)?:')
        jawab = input()
        if jawab =='n':
            break
