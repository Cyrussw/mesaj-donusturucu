# Os Kütüphanesini isteğe bağlı dahil ederseniz program her başladığında temiz bir sayfa açar.

#import os
#os.system("cls")

mesaj = input("mesajınız: ")
mesaj_ters = mesaj[::-1]
mesaj_yuksek = mesaj.upper()
mesaj_alcak = mesaj.lower()

print(f"""
# ------------------- Mesaj Dönüştürücü ------------------- #

Normal Mesaj: {mesaj}
Ters Çevirilmiş: {mesaj_ters}
Caps Açık: {mesaj_yuksek}
Caps Kapalı: {mesaj_alcak}

# ------------------- Mesaj Dönüştürücü ------------------- #
""")
