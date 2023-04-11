from art import logo
import random
print(logo)

def tahmin_et(zorluk):
    if zorluk == "kolay":
        hak = 10
    elif zorluk == "zor":
        hak = 5
    else:
        print("Geçersiz zorluk seviyesi.")
        return

    sayi = random.randint(1, 100)
    while hak > 0:
        print(f"Kalan hakkınız: {hak}")
        tahmin = int(input("Tahmininiz: "))
        if tahmin == sayi:
            print("Tebrikler! Doğru tahmin!")
            return
        elif tahmin < sayi:
            print("Daha büyük bir sayı girin.")
        else:
            print("Daha küçük bir sayı girin.")
        hak -= 1

    print(f"Hakkınız bitti. Doğru cevap {sayi} idi.")

zorluk = input("Zorluk seviyesini seçin (kolay/zor): ")
tahmin_et(zorluk)

