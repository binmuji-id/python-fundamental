'''
penggunaan tipe data list
'''

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


