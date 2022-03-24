"""
aplikasi deteksi gempa
"""

def ekstraksi_data():
    """
    Tanggal : 24 Maret 2022
    Jam : 06:54:46 WIB
    Magnitudo : 4.8
    Kedalaman : 15 km
    Lokasi : LS=0.73, BT=133.60
    Titik Gempa : Pusat gempa berada di laut 53 Km baratlaut Manokwari
    Keterangan : Dirasakan (Skala MMI): II-III Manokwari
    """
    hasil = dict()
    hasil ['tanggal'] = '24 Maret 2022'
    hasil ['jam'] = '06:54:46 WIB'
    print (hasil)
    return hasil

def tampilkan_data (result):
    pass

if __name__ == '__main__':
    print ('aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data (result)


