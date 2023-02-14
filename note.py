import sys
import os

if sys.argv[1] == 'note' and sys.argv[2] == 'yarat':
    a = input("faylın adını daxil edin: ")
    file = open(f'{a}.txt' , 'x')
    print('note yarandı')

if sys.argv[1] == 'noteları' and sys.argv[2] == 'göstər':
    b = input("faylın adını daxil edin: ")
    file = open(f'{b}.txt', 'r')
    content = file.read()
    print(content) 

if sys.argv[1] == 'faylı' and sys.argv[2] == 'sil':
    b = input("faylın adını daxil edin: ")
    os.remove(b)
    print('fayl silindi')

if sys.argv[1] == 'notu' and sys.argv[2] == 'dəyiş':
    c = input("faylın adını daxil edin: ")
    file = open(f'{c}.txt', 'w')
    content = file.write(input())