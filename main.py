"""
Kullanicidan sayi adeti alinip o sayi adeti kadar
sayi istenerek bu sayilarin ortalamasini aliniz.

input:
Lutfen gireceginiz sayi adetini giriniz: n
lutfen 1. sayiyi girniz: 4
lutfen 2. sayiyi girniz: 5
            .
            .
lutfen n. sayiyi giriniz: 5

output:
girdiginiz n sayinin ortalamasi: 5

""" 
if __name__ == '__main__':
    adet = int(input("lutfen sayi adetini giriniz: "))

    toplam = 0
    for sayi in range(adet):
        girilen_sayi = int(input("sayi giriniz: "))
        toplam = toplam + girilen_sayi

    ortalama = toplam / adet
    print("girdiginiz" + str(adet) + "sayinin ortalamasi: " + str(ortalama))

    
