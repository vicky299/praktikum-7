try:
    file= open("d:/dataMhs","a")
    print(file.write(a))
    int(input('data yang mau ditambahkan:'))
    while True:
        print('mau lagi (y/n):')
        x = str(input())
        if x == n:
            break
    file.close(n)
except NameError:
    while True:
        int(input('data yang mau ditambahkan:'))
        print('mau lagi (y/n):')
        jawab = input()
        if jawab =='n':
            break
        
        


          
