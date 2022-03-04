'''
penggunaan tipe data list
'''

from traceback import print_tb
from turtle import clear


daftar_buku = ['seven habits', 'how to influence people', 'first things first']
print ('\ntampilkan variable daftar_buku')
print (daftar_buku)

print ('\nproses semua dgn for in')
for buku in daftar_buku :
    print (buku)

print ('\ntampilkan isi daftar_buku dgn indeks')
print (daftar_buku[0])
print (daftar_buku[2])

print ('\ntampilkan dengan for in range')
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

daftar_buku=[1, 'mangaku', -33, 3.14]
print ('\ntampilkan dgn for in range, dimana tipe data berbeda')
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

daftar_buku = ['seven habits', 'how to influence people', 'first things first']
print ('\nmenambahkan data dengan append')
print ('tambahkan 1 buku baru')
daftar_buku.append('4dx')
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nclear list')
daftar_buku.clear()
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nganti elemen pertama')
daftar_buku = ['seven habits', 'how to influence people', 'first things first']
daftar_buku[0] = 'one piece '
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nambil elemen ke dua')
buku = daftar_buku.pop(1)
print (buku)
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nPOP')
daftar_buku = ['seven habits', 'how to influence people', 'first things first']
daftar_buku.pop()
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nPOP -1/-dkk')
daftar_buku = ['seven habits', 'how to influence people', 'first things first']
daftar_buku.pop(-2)
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

