"""
aplikasi deteksi gempa
modularisasi dengan fungsi
modularisasi dengan package
"""


from gempaterkini import ekstraksi_data, tampilkan_data


if __name__ == '__main__':
    print ('\naplikasi utama')
    result = ekstraksi_data()
    tampilkan_data (result)


