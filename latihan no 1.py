try:
    file = open("d:\anyfiles.txt","r")
    print('Isi file d:\ anyfile.txt adalah:')
    print(file.read())
except OSError:
    print('Isi file d:\anyfiles.txt adalah:')
    print('XXXXXX')
    print('XXXXXX')
    print('XXXXXX')


