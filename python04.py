'''
perulangan dengan while sampai paham
'''

jumlah_buku = 10
print (f'bacalah {jumlah_buku} bukumu')
total_jumlah_baca = 0

jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
print (f'jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca += 1
    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == 9:
        print (f'buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1} belum paham')
    else:
        jumlah_buku_yang_sudah_dibaca_dan_dipahami +=1
        print (f'buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca & dipahami')

print (f'jumlah buku yang sudah dibaca & dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')
if jumlah_buku_yang_sudah_dibaca_dan_dipahami == jumlah_buku:
    print ('semua buku sudah dibaca & dipahami')
else:
    print (f'tidak semua buku dibaca & dipahami, hanya {jumlah_buku_yang_sudah_dibaca_dan_dipahami} saja')


