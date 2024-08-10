# enumerate ()
# enumerate() bize (index, element) çifti olarak verecek
adlar = ['Tyler', 'Blake', 'Cory', 'Cameron']
# for e in adlar: print(e)   : Tyler, Blake, Cory, Cameron


for i, e in enumerate (adlar): 
    print(i, e)                          # 0 Tyler yazdırdı
    print(i, "indexindeki eleman:", e)   # Ø indexindeki eleman: Tyler yazdırdı

# enumerate (adlar) yaptığımız için başına index iterasyonu yap 
# (i, e) olarak düşünürsek (0, Tyler ) olmuş oluyor ve birer birer arttırarak yap


# enumerate() 0'dan başlamak zorunda değil, özellikle kaçtan başlayacağını belirtebiliriz
for i, e in enumerate (adlar, start = 1): 
    print(i, e)                                   # artık 1 Tyler olacak
    print(i, "lokasyonunda bulunan eleman:", e)     


adlar = ('Tyler', 'Blake', 'Cory', 'Cameron')
for i, e in enumerate (adlar): 
    print(i, "indexindeki eleman:", e)



# zip()  : Farklı yapıların içinde paralel iterasyon yapmamızı sağlar 
# diyelimki elimizde iki tane liste var 
# bu listelerin sıralı elemanlarını birbirne yapıştırıyor ve 
# bize tuple olarak veriyor ve biz orada iterasyon yapıyoruz

ogrenciler = ["ogrenci_1", "ogrenci_2", "ogrenci_3"]
notlar = [90,80,72]

for s, g in zip(ogrenciler, notlar):   # variable unpacking
    print(s, g)                        # (oğrenci_1, 90)

for e in zip (ogrenciler, notlar):     # ('ogrenci_1', 90)
    print(e)

for i in range(len(ogrenciler)): 
    print(ogrenciler [i], notlar[i])



# Her ayki karı hesaplamak
satis = [3500.00, 76300.00, 67200.00] 
maliyet = [56700.00, 21900.00, 12100.00] 
for i in range(len(maliyet)): 
    s = satis[i]
    c = maliyet[i]
    kar = s - c 
    print(f'Total profit: {kar}')     # ?


satis = [3500.00, 76300.00, 67200.00] 
maliyet = [56700.00, 21900.00, 12100.00] 
for s, c in zip(satis, maliyet): 
    kar = s - c 
    print(f'Total profit: {kar}')


# zip() ile Dictionary Yaratmak:
keys = ['isim', 'soyad', 'ulke', 'is'] 
values = ['Denis', 'Walker', 'Turkey', 'data scientist']

d = {}
for k, v in zip(keys, values):      # (k,v) : ("isim","Denis")
    d[k] = v                        # dictionary'e yeni eleman eklemek
print(d)                            # {'isim': 'Denis', 'soyad': 'Walker', 'ulke': 'Turkey', 'is': 'data scientist'}
print(d["isim"])                    # Denis


for i in range(len(keys)): 
    k = keys[i]
    v = values[i]

    d[k] = v






