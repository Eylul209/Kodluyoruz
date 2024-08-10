##
# Bunların hepsi bir sınıftaki notları ifade ediyor. Bunları bir veri tipi olarak bir arada tutsak daha mantıklı olmaz mı?
# list veri tipi de tam burada devreye giriyor. Birden çok veriyi gruplayıp bir arada tutmak istediğimizde kullanabileceğimiz bir yapı
# list ler belirtirken köşeli parantezle belirtiyoruz: [element1, element2,...].
# list ler içsel yapı içerdikleri İçin non-scalar veri tipidir
# Elemanları arasına virgül koyarak farklı eleman belirtmeye başladığımı İfade ediyorum
notlar = [78, 80, 43, 65, 90]

# Listenin içinde arraylerdeki gibi belirli bir veri tipi tutma şartı yok 
# listin içinde listte olabilir
l = [1, 2, "a","b", True, 4.5,[1,2,3]]

#indexing : l[0] ve slicing : l[:]  yapılabilir

# listler stringlerden farklı olarakta immutable değil mutable !
notlar [1] = 85
notlar [1] += 5

# slicing ile de değiştirme yapabiliriz
l[0:3] = 30, 40, 60

# sağ  taraf ile sol taraf eşit olmak zorunda da değil 
l [0:3] = 50, 70

#slicing in sonucunda tek bir değer yazacaksak bile tek olarak veremeyiz iterable olması gerekir
# l[0:3] = 30 yanlış 
l [0:3] = [30]  # olmalı

# listenin sonuna eleman eklemek : append() fonksiyonu ile
l.append(200)
l.append("hey")

# listenin sonuna  birkaç eleman eklemek : append() fonksiyonu ile
l.extend(300,400)
l.extend(500,"by")

# spesifix bir indexe eleman eklemek : insert() fonksiyonu
l.insert(0, 100)  
# l[0] = 100 değil bu değiştirme bu 
# l.insert(0, 100) : burada 0. indexe 100 eklendi diğerleri bir sağa kaydı

# belirli bir elemanı listeden silmek : remove()
l.remove(5)

# diyelimki içerde iki tane 5 var remove fonksiyonu soldan başlayarak silme yapar 
# o yüzden ilk gördüğü 5i siler

# listenin belirli indexindeki elemanı silmeye ve o değeri döndürmeye yarar
# remove sadece siliyordu, pop aynı zamanda o değeri döndürüyor/alıyor
l.pop(1)

# count() : içine yazdığımız değerin listede kaç defa görümdüğünü döndürür
l.count(1) # 1 elemanı kaç defa görülüyor

# !! Aliasing : Listeler bilgisayarın hafızasında integer,float 
# gibi veri tiplerinin tutulduğundan biraz daha farklı tutuluyor

# şöyle :
a = 2
b = a 
a += 1
# !! yaptığımızda b değişmeyecek ama listelerde :
l = [1,2,3]
l2 = l
l[0]= [10]
# burada l2 değişecek çünkü burada aynı kutuya işaret eden bir etiket orası 
# bu davranışı copy() fonskiyonu ile değiştirebililrz.
l3  = l.copy()
# copy fonksiyonu ile yeni bir kutucuk oluşturuluyor

# listeleri birbirleri ile birleştirme : concatenation "+" operatörü ile
l2 + l3

# belirli bir elemanın indexi : index() istediğimiz elemanın kaçıncı indexte old
l.index(2)
# bu eleman ilk kaçıncı indexte gözüküyorsa bize onun index değerini veriyor

# listeleri tersine çevirmek : reverse()
# implace : yani l'yi günceller 
l.reverse()
# aynısını slicing ile de yapabiliriz ama liste güncellenmez : l[::-1]

# listin elemanlarını sıralamak : küçükten büyüğe sorted() fonksiyonu ile
sorted(l)
# implace değil orjinal liste güncellenmiyor
l.sort(l2)  # implace

# bir listenin içindeki integer ve stringleri aynı anda sort etmiyor 


# Tuple
# tuple veri tipi listeler gibi birden çok veri tipini bir arada tutmamızı sağlar.
# !! listelerden farklı olarak tuple lar immutable dir
# Mesela bir deniz fenerinin konumunu belirtmek istiyoruz. bunun x ve y koordinat değerleri var (x,y). 
# Deniz fenerini söküp götüremiyoruz, ben bu iki değerin sabit, değiştirilemez olmasını istiyorum. 
# Burada bu iki değeri tutmak için tuple kullanmam mantıklı olabilir. Değişmiyeceğini bildiğim değerleri bir arada tutmak için
# tuple lar (elementi, element2...) şeklinde tanımlanır.
# tuple lar listeler gibi farklı veri yapılarında elemanlardan oluşabilir. Elemanları tuple bile olabilir

x = 10
y = 34
(x, y) = (y, x)   # x,y = y,x de yazabilirdik
# bu değiştirmeyi listlerde de yapabiliyoruz
konum = (10, 34)

#indexleme yapabiliyoruz
konum[0]

# tuple ın içinde her türlü veri tipi olabiliyor
# tuple ın içinde list var ve biz onun ilk elemanına erişmek istiyoruz :
t = ([1,2,3],2(1,2))
t[0][0]

# parantez koymasak bile phyon bunu tuple olarak algılıyor
a = 1,2,3
type(a)   # tuple

# tuple ve listlerde eleman kontrolü 
# belirli bir eleman listede veya tuplelarda var mı diye "in" keywordü kullanılır
1 in a
2 in t


# Dictionaries 
# Listeler bize bir arada tutulması anlamlı olacak verileri bir arada tutma gücü verir
# Mesela bir sınıftaki 3. öğrencinin aldığı notlar
grades = [80, 72, 95]

# Bu listedeki 1. eleman ilk öğrenciyi, 2. eleman 2. öğrenciyi, 3. eleman...
# Ben aynı zamanda bu öğrencilerin isimlerini de tutmak istiyorsam, 
# isimleri için ayrı bir liste oluşturmam lazım. Kuracağım mantık için 
# bu iki listenin eleman sayısı aynı olmalı. 
# her yeni bir özellik için yeni bir liste oluşturulabilir
# notlar[0] bana ilk öğrencinin notunu, isim[0] bana ilk öğrencinin notunu verecek

isim = ["Deniz", "Ege", "Gizem"]
isim[0]
notlar [0]
print(isim[0], "adlı öğrencinin notu", notlar[0])

#Öğrenci numaralarını tutmak istiyorsam bunu için de ayrı bir liste oluşturmam lazım

# Her farklı bilgi için yeni bir liste oluşturmam gerekiyor
# Aynı elemanı ifade eden mantıklar listeler arası aynı indexte tutuluyor (isim[0]'ın notu notlar[0])
# Bu yapılabilir ama optimal olmayan bir yaklaşım. Karışıklık çıkması çok muhtemel
# İstediğim kısmı almanın daha kolay bir yolu olabilir mi? Sadece bir veri yapısı kullansam... Ayrı ayrı listeler kullanmasam...
# Evet bunu yapabiliriz! Bunun için dictionary veri yapısını göreceğiz
# Dictionary yapısının elemanlarına erişmek için belirli key ler kullanacağız ve o da bize value lar verecek
# dictionaryleri süslü parantez {} ile belirteceğiz.
# Formumuz (key1:value2, key2:value2...} şeklinde olacak
# Elemanlarına ulaşmak için öbür non-scalar veri tiplerinde yaptığımız gibi [] kullanacağız. 
# Ama dictionary lerin elemanlarına ulaşmak için belirlediğimiz key leri kullanacağız, integer indexing değil
# ! dictionary lerin keyleri immutable herhangi bir yapıda olabilir. 
# ! value lar mutable da immutable da olabilir. int, float, bool, string, list, tuple, set, even dictionaries itself !

notlar = {"Deniz" : 80, "Ege":72, "Gizem": 95, 0 : 20}
notlar["Ege"]     # 72
ogrenciler = {"Deniz": {"not":89, "ogrenci_no":703} , "Ege": {"not":72, "ogrenci_no":408}, "Gizem": {"not":95, "ogrenci_no":690}}
notlar["Ege"]     # {'not':72, 'ogrenci_no':408}
ogrenciler ["Ege"]["not"]  #72
ogrenciler ["Ege"]["ogrenci_no"]  #408
notlar # {"Deniz" : 80, "Ege":72, "Gizem": 95}

# bana "key" değerini getir. indexle çağırmak yerine anahtar kelimeyi belirticez

# olmayan bir elemanı sorgularken hata alıyoruz. : notlar["mert"]
# dictionary de indexing yapmıyoruz

# value değerleri mutuable 
notlar["Ege "] +5 = notlar["Ege "]

len(notlar)   # kaç key değeri var : 4

# eleman eklemek 
notlar["Mert"] = 58
notlar   # {"Deniz" : 80, "Ege":72, "Gizem": 95, 0 : 20, "Mert" : 58}

# eleman silmek : del()
del notlar["Mert"]  # {"Deniz" : 80, "Ege":72, "Gizem": 95, 0 : 20}

# ! sadece immutable tipindeki veriler key olabilir örnek olarak listeyi veremezsiniz çünkü mutable
d = {1:2, 3 : "b"}
d1 = {(1,2) : "a", (4,5): [1,2,3]}
d2 = {[1,2]:4}  #hatalı

# boş bir dictionary yaratmak 
e = {}
e[1] = "a"    # {1:"a"} olur

# bir değer keyler arasında var mıs sorgusu yapmak : "in" sorgusu
"Mert" in notlar

#nonescalar veri tipi : list, tuple, dictionary, string, sets

# Sets
# Setleri kümeler olarak düşünebiliriz : bir elemandan sadece bir tane vardır
# Sadece özgün değerleri tutan, İçerisinde bir eleman var mı yok mu, 
# başka bir setle hangi elemanları farklı gibi işlemleri performanslı bir şekilde yapabileceğimiz bir veri yapısı.
# Dictionaryler gibi eleman sorgusu yapmak hızlıdır. 
# Dictionarylerde key-value çift olarak bulunduğu için aynı uzunluktaki bir set ten daha fazla yer kaplar
# Setler indexlenemez
# Setler mutable dir

s2 = {1,2,2,3,4,3,5}
s2   # {1,2,3,4,5}  bir kereden fazla yazılanları yazmıyor

# boş set yaratma 
s = set()

# listin elemanlarıyla set oluşturma
l = [1, 2,  3, 4]
s1 = set(l)

message = "Merhaba orada mısın ?"
s3 = set(message)
# " " boşluk karakterinide sayıyor
# setler sıralı değildir 
s3  # {' ', ',', 'M', .....}

# len(s)

# setler indexlenemez

# set'e eleman ekleme : add() fonksiyonu ile
s.add(6)   # sona ekliyor

# set'den eleman silme : remove() fonksiyonu ile silmek ist değeri 
s.remove(2)

# silmek istediğimiz eleman yoksa ve error almak istemiyorsak : discard()
s.discard(5)

# küme gibi düşünebileceğimiz için ona göre işlemde yapabiliriz.

# Difference : s4 ile s5 kümesinin farkına bakacağız (s4- s5) veya (s4\s5)
s4 = set([1, 5, 10])
s5 = set([2, 5, 3])
# s4 ün hangi elemanları s5 ten farklıdır : difference() komutu ile
s4.difference(s5)   # verdiği cevapta set : {1, 10}
s4 - s5 

# symetric difference (s4\s5) U (s5\s4) -> s4 U s5 - s4 ∩ s5
s4.symmetric_difference(s5)

# intersection s4 ∩ s5
s4.intersection(s5)
s4 & s5
s4 - (s4-s5)

# kesişim yapıp s4 ün değerini buna günceller 
s4.intersection_update(s5)  # s4 = s4.intersection(s5)

# union s4 U s5
s4.union(s5)

# Disjoint Set s4 ∩ s5 = boş küme olup olmadığı kontrol edilir
s4.isdisjoint(s5)

# subset 
s4.issubset(s5)

#superset 
s4.issuperset(s5)













































