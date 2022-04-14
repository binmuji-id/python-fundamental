from urllib import request
from bs4 import BeautifulSoup


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
    hasil ['tanggal'] = "24 Maret 2022"
    hasil ['jam'] = '06:54:46 WIB'
    hasil ['magnitudo'] = 4.8
    hasil ['kedalaman'] = '15 km'
    hasil ['lokasi'] = {'ls': 0.73, 'bt': 133.60}
    hasil ['titik gempa'] = 'Pusat gempa berada di laut 53 Km baratlaut Manokwari'
    hasil ['keterangan'] = 'Dirasakan (Skala MMI): II-III Manokwari'
    
    return hasil
    

def tampilkan_data (result):
    print ('\nGempa berdasarkan info BMKG')
    print (f"Tanggal {result['tanggal']}")
    print (f"Jam {result['jam']}")
    print (f"Magnitudo {result['magnitudo']}")
    print (f"Kedalaman {result['kedalaman']}")
    print (f"Lokasi : LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print (f"Titik Gempa {result['titik gempa']}")
    print (f"Keterangan {result['keterangan']}")

print('ini tes package')