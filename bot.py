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




