#
# nonsacalar veri tiplerinde (listituple,dic) for 
# forda her iterasyonda bu yapının içerisindeki elemanları sırayla al
notlar = [90, 72, 81, 77]
for e in notlar :
    print(e)

# not ortalaması
t = 0
for e in notlar:           # e yerine penguen de yazılabilir çünkü özel bir anlamı yok
    t += e
ortalama = t / len(notlar)
print(ortalama)

# bu kodun aynısı range() fonksiyonu ile de yapılabilirdi
# for e in notlar diyince ilk iterasyonda e nin değeri 90, 
# ikincisinde 72... olarak devam etti
# * range() ile indexlerde iterasyon yapıp indexing ile değerlerine de ulaşabilirdim 
# (range belirli bir listenin indexlerinde iterasyon yapmamı sağlamıyor, 
# range(len(notlar)) diyince bize 0,1,2.. len (notlar)-1 sayılarını verecek, 
# bunlar da listenin indexleriyle örtüşüyor, 
# yoksa range() index verir diye bir şey yok)

for i in range(3):
    print("iteration :" , i)

# ya da 
for i in range(1,4):              # 1'den başlayıp 4'e kadar da gider
    print("iteration :" , i)

# ya da  slicingte eklenebillir
for i in range(1,4,2):              # 1'den başlayıp 4'e 2şer artarak kadar da gider
    print("iteration :" , i)

t = 0
for e in range(len(notlar)):           # aynısını indexleme ile de yapabiliriz
    t += notlar[e]
ortalama = t / len(notlar)
print(ortalama)

# range fonksiyonu sayı ile match ediyor o yüzden index no olarak kullanabilicez

# index ile iterasyon mantığı nerde önemli oluyor ?
# Diyelim ki öğretmen farketti ki herkese 5 puan az vermiş, 
# herkesin puanını 5 arttırmak istiyor, bunu direkt listenin elemanlarında iterasyon yaparak yapamam. 
# Listenin indexlerine erişip o değeri güncellemem lazım

# range fokksiyonu ile döngünün içinde güncellediğimiz değer 
# döngünün dışına çıkıncada güncellenmiş oluyor
# çünkü range fonksiyonunda lokasyona ulaşıyor ve değiştiriyor 
# o yüzden indexlerde iterasyon yapmak daha mantıklı

# Hadi biraz da continue mantığının alıştırmasını yapmış olalım. 
# Diyelim ki öğretmen 2. öğrencinin kağıdını doğru okumuş, 
# 2. öğrenci (index 1'deki) hariç hepsinin değerini 5 arttıracak
notlar = [90,72,81,77]
for i in range(len(notlar)):
    if i == 1:
      continue
    notlar[i] += 5
print(notlar)

# Şimdi de break egzersizi:
# Diyelim ki bir listenin içinde belirli bir eleman var mı diye kontrol etmek istiyoruz. 
# Bulunca aramaya devam etmeyeceğim. Devam etme mantığını break İle sağlayacağım
# İlk kullanıcıya hangi sayısı aradığını soracağız, sonra bu sayı var mı kontrol edeceğiz
x = int(input("Hangi sayıyı kontrol edeyim?:"))
l = [2,3,40,100,10,1]
for e in l:
    print(e) # iterasyon break ile çıkmış mı görelim mi diye
    if e == x:
        print("Buldum!!")
        break

# tuplelarda iterasyonda listelerde aynı sadece immutable old için değiştirme yapamıyoruz

# dictionarylerde sadece keylerde bastırıyor iteration ile
d = {"student_1": [90,89], "student_2": [80,83], "student_3": [72,71]}
for k in d:
    print(k)   # student_1

# Değerlerine ulaşmak istiyorsam şöyle yapabilirdim:
for kl in d:
    v = d[k]
    print(v)     # [90, 89]

# değere ulaşmak için zaten yazım şöyle : d["student_2"]

# eğer biz valueların üzerinde direkt iterasyon yapmak istiyorsak :
# Veya d.values() diyerek value'larında iterasyon yapabilirim. 
# Burada for <değişken> in <obje> yapısında değişken> int vs gibi şeyler değil 
# liste gibi yapılar da olabilir Iterasyon içerisinde, burada da öyle oldu
# bu.values() dan dolayı olan bir şey değil, dictionary'nin value'ları int olsa böyle olmazdı
d= {"student_1": 90, "student_2": 80, "student_3": 72}
for v in d.values():
    print(v)           # 90

# Burada v, her iterasyonda int
# 85'den fazla alan biri var mı diye bakmak istiyorum diyelim, 
# ve bunun kim olduğunu (olduklarını) bulmak istiyorum:
d = {"student_1": 90, "student_2": 80, "student_3": 72}
for k in d:
    value = d[k]       # values = 90
    if value > 85:
        print(k)       # student_1

# Aynı anda hem key hem de value 'larda iterasyon yapmak için:
# Variable unpacking konusunda bir tuple, 
# liste gibi yapıların değerlerini birden çok değişkene bir seferde eşitlemeyi görmüştük • 
# Bunun aynısını iterasyonda da yapabiliriz
# d.items() ban key ve value pairlarını veriyor
for k,v in d.items():
    print("key değeri:", k, "value değeri:", v)         # key değeri : student_1  value değeri : 90



# split ve join metodu
# stringten liste gitme
# split : belirli bir bölme kriterine göre stringin alt parçalarını listenin elemanları olarak dönüştürebilirz
s = "merhaba nasılsın ? "
print(s.split(" ")  )             # ['merhaba', 'nasılsın', '?']

# hiçbir şey yazmazsakta default olarak boşluk ekler 
s.split()


# join : listenin elemanları arasında belirtilen yapıyı koyup string'e dönüştürür
# listten stringe gitmek
# "paten".join(elemanları kullanacak liste)
l = ['limon','portakal','elma']
",".join(l)                        # 'limon,portakal,elma'
# listin elemanlarının arasına bu koyarak stringe dönüştür






































