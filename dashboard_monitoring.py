"""
aplikasi deteksi gempa
modularisasi dengan fungsi
modularisasi dengan package
"""


import gempaterkini


if __name__ == '__main__':
    print ('\naplikasi utama')
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data (result)


