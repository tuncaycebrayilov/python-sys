from datetime import datetime
import sys
import os

# datetime
if sys.argv[1] == 'tarixi' and  sys.argv[2] == 'de':
    print(datetime.now())
elif sys.argv[1] == 'ili' and sys.argv[2] == 'de':
    print(datetime.today().year)
elif sys.argv[1] == 'ayı' and sys.argv[2] == 'de':
    print(datetime.today().month)
elif sys.argv[1] == 'saatı' and sys.argv[2] == 'de':
    print(datetime.now().strftime('%H-%M'))
elif sys.argv[1] == 'Heftenin' and sys.argv[2] == 'gününü'  and sys.argv[3] == 'de':
    print(datetime.now().strftime('%A'))


# folder yarat
if sys.argv[1] == 'folder' and sys.argv[2] == 'yarat':
    directory = input()
    parent_dir = "/Users/tuncaycebrayilov/Desktop/bot/"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print('folder yarandı')

if sys.argv[1] == 'folder' and sys.argv[2] == 'sil':
    directory = input()
    parent_dir = "/Users/tuncaycebrayilov/Desktop/bot/"
    path = os.path.join(parent_dir, directory)
    os.rmdir(path)
    print('folder silindi')





#calculator
op = sys.argv[1]

if op == 'topla':
    a = int(input())
    b = int(input())
    print(a + b)
if op == 'çıx':
    a = int(input())
    b = int(input())
    print(a - b)
if op == 'vur':
    a = int(input())
    b = int(input())
    print(a * b)
if op == 'böl':
    a = int(input())
    b = int(input())
    print(a / b)




# yaş
a = datetime.today().year

if sys.argv[1] == 'Yaşımı' and sys.argv[2] == 'de':
    b = int(input('doğum tarixinizi daxil edin: '))
    print(a - b)



#text fayl
if sys.argv[1] == 'text' and sys.argv[2] == 'fayl' and sys.argv[3] == 'yarat':
    c = input()
    file = open(f'{c}.txt' , 'x')
    print('text fayl yarandı')


if sys.argv[1] == 'text' and sys.argv[2] == 'yaz':
    d = input()
    file = open(f'{input("faylın adını daxil edin")}.txt', 'w')
    content = file.write(d)

if sys.argv[1] == 'text' and sys.argv[2] == 'elave' and sys.argv[3] == 'et':
    z = input()
    file = open(f'{input("faylın adını daxil edin")}.txt', 'a')
    content = file.write(z)

if sys.argv[1] == 'texti' and sys.argv[2] == 'sil':
    file = open(f'{input()}.txt', 'r+')
    content = file.truncate()