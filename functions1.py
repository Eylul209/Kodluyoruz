""" functions
fonksiyonların ne yaptığını anlamak için olan sorgu komutumuz : "?"
comment line da istediğimiz kadar yazabilmek için 3 tane tırnak işareti  """
def square(x):
    """
    x'in karesini hesaplar
    """
    return x * x

# ?square  yazıldığında : "x'in karesini hesaplar" vermesi lazım

# birden çok outputu olan fonksiyonlar :
def f(x):
    return 2*x, 10*x

print(f(10))      # (20, 10)  : bana sonucu tuple olarak döndürdü

# variable unpacking'te gördüğümüz gibi bu iki değeri farklı değişkene eşitleyebilirim
a, b = f(10)
print(a)
print(b)

def f(x,y):
    return 2*x*y, (10*x)**y     # "**" işareti üzeri anlamında


# Predefined Methods
# sana özellikle şu değeri yerine al diye belirtmedikçe 
# benim sana önceden söylediğim değeri al
def hello(end, start = "Hello"):  
    #kullanıcı sana özellikle start yerine ("Hello") alma demedikçe sen Hello al
    print(start + " " + end)

print(hello("Denis"))                  # Hello Denis
print(hello("Denis", start = "Hey"))   # Hey Denis
print(hello("Denis", "Hey"))           # Hey Denis   start diye özellikle yazmamıza gerek yok


def power(x, y=1):
    return x ** y
print(power (3))       # 3
print(power (4, 2))    # 16

# Aksini belirtmezsek predefined değerleri kullanacak fonksiyon 
# # predefined olarak vereceğimiz değerleri en sona yazmalıyız yoksa hata alırız 

# HATALI : def hello(start = "Hello", end): print(start + end)


# Bir değişken ile fonksiyon çağırdığımda ;
a = 2

# def d(c): c = 4 return c
# print(fu(a))


# fonksiyonun içinde yaptığımız işlemler ile a'nın değeri değişir mi ?
# cevap : değişmez
# ama listeler için farklı değişir

l = [1, 2, 3]
l2 = l
l2 [0] = [10]    # yaptığımızda l'de değişir çünkü bu etiket tutuyor l ve l2

def c(l):
    l[0] = "a"
    return l

print(c(l))
print(l)     # ['a', 2, 3]   : l'de güncellenmiş oldu

# değişmesin istiyorsak copy() funciton : l2 = l.copy()

def d(x):
    l3 = x.copy()
    l3[0] = 2
    return l3

print(d(l))       # [2, 2, 3]
print(l)          # ['a', 2, 3]

# güncellenip güncellenmemesi verdiğimiz veri tipine bağlı 


""" first class function :
Bu programlama dilinde fonksiyona onu manipüle edip başka bir fonksiyona
bir argüman olarak veriliyorsa, gidip başka bir değişkene assign edebiliyorsak
* Phyton'da fonksiyonlar first class function
Python'da fonksiyonlar first class function. 
Bunun anlamı fonksiyonların diğer veri tipleri gibi manipüle edilebilir 
ve başka fonksiyonlara argüman olarak verilebilir.
Bir fonksiyonu bir değişkene atayabiliriz
"""

def kare(x):
    return x**2

a = kare          # burada a'yı kare fonksiyonuna eşitledi : a=kare
print(a(5))       # 25
print(kare(5))    # 25

# ***Bir fonksiyonu başka bir fonksiyona argüman olarak verebiliriz
def f2(x, f):           # fonksiyona fonksiyonu bir veri objesi olarak veriyor
    return f(x) + 4

print(f2(3, kare))
# return kare(3) + 4 olarak işlemi yapıcak : 13

# def f2(x, f):  burada f() açıp değer verseydik function call olup değerini alacaktı
# burada fonk bir veri objesi olarak verildi


""" Fonksiyonları Obje Olarak Kullanmak
Bir listem olsun bu listeyi fonksiyona eleman olarak veriyim
bu listenin bütün elemanlarına bu fonksiyon uygulansın ve günün sonunda böyle güncellesin
• Python'da fonksiyonların first class function olduklarını konuşmuştuk.
• Şimdi bu mantığı kullanarak belirli fonksiyonları 
listenin elemanlarına uygulayacağız """

p = [1,2,3,4]
def apply(l, f):     # listenin elemanlarına fonksiyonun uygulanacağı liste f'te input olarak vereceğim fonksiyon (obje olarak)
    """ 
    bir liste, f listenin tüm elemanlarına uygulanacak fonksiyon
    sonunda listenin orijinali elemanlarına 
    fonksiyonun uygulanmış haliyle güncellenir 
    """
    n = len(l)

    for i in range(n): 
        l[i] = f(l[i])


def kare(x):
    return x**2

print(apply(p, kare))

def kup(x):
    return x**3

# Tüm elemanlara fonksiyon uygulandı ve güncelledik

# Fonksiyonlar Listesini Belirli Bir Değere Uygulamak
# fonksiyon listem olsun (tek bir değerim olsun, collection olmasın)
# ama vereceğim fonksiyon list halinde olsun 
# bir liste olsun içerisnde ve farklı farklı fonksiyonlar olsun

# önemli bir örnek

def apply_funcs(f_list, x): 
    l = []
    for f in f_list:
        l.append(f(x))
    return l

# hem kareyi hem küpü uyguluycam
print(apply_funcs([kare, kup], 5))      
# fonksiyonlar burada veri objesi old için elemanları arasında iterasyon yapabiliyorum



# Underscore Placeholders

num_1 = 90000000000

"""Kaç tane 0 var burada ? 1,2,3,4... bir tanesini atladım mı? 
Nerede kalmıştım, başa dönüp bir daha sayayım... 
Pff yok mu bunun daha okunabilir bir yolu?
Cevap tabii ki de evet. Sayıları arka planda algılanmasını değiştirmeden, 
ama bize daha kolay okunabilir yapan bir yöntem var. """

num_2 = 90_000_000_000      # bilgisayar "_"yi görmezden geliyor

""" Sayıların arasına alttan çizgi koymak !
Bu bilgisayarın sayıları algılamasını değiştirmiyor, 
o onları görmezden geliyor, ama bizim için daha okunabilir oluyor."""

print(num_1)   
print(num_2)

# Bilgisayar için 90_000_000_000 ile 90000000000 sayısının hiç bir farkı yok

print(type(90_000_000_000))   #int

# bu mantığı float içinde kullanabiliyoruz.
num_3 = 0.12_11_12
print(num_3)



# F-Strings
# Strinler'in içerisine belli bir yapı gömmemizi sağlayan bir mantık
"""
Değişkenlerimizin değerlerini direkt olarak string 'lerin içine koymak isteyebiliriz.
f-string de yaptığımız tek şey aslında değişkenlerin değerlerini veya 
hesaplamaların sonucunu string in içine gömmek.
f"..." diye göreceğimiz yapının adını String Interpolation diye görebilirsiniz.
"""
x = 2

# Diyelim ki ekrana x'in değerini bastırmak istiyorum. 
# Bu durumda istediğim şey "x in değeri 2" diye bastırmak. 
# Bunu şöyle yapabilirim:

print("x in değeri" + " e" + str(x))   # bu zahmetli bir iş 

# Ama ayrı ayrı yazmaya ihtiyaç olmadan direkt x'in değerini 
# x'i alıp direkt string 'in içine gömebilseydim daha iyi olmaz mıydı?

print(f"x in değeri {x}")      # {} ve içine gömmek istediğimiz yapı

""" İçine değer gömeceğimiz string'i tanımlarken başına f yazarak başlıyoruz
 f"....". Gömmek istediğimiz değeri/değişkeni süslü parantez içine yazıyoruz 
 f"........". Birden çok değer de gömmek isteyebiliriz, 
 o zaman kaç tane yapacaksak o kadar süslü parantez koymamız gerekirdi
• Python'ın yaptığı şey süslü parantezin içini hesaplayıp 
stringin içine gömmek """

print(f"x in değerinin iki fazlası {x+2}")

# {x+2) kısmında python x+2 'yi hesapladı ve string'in içine cevabın değerini gömdü

isim = input("İsim:")
print(f"verilen isim {isim}")

q = [1, 2, 3, 4]
print(f" verilen liste {q}")    # 'verilen liste [1, 2, 3, 4]

y = {1:1, 2:2, 3:3, 4:4}
print(f" verilen disctionary {y}")      # 'verilen disctionary  '{1:1, 2:2, 3:3, 4:4}'

# {} İçerisine değeri hesaplanacak herhangi bir şey yazılabilir
print(f"verilen isim {isim.capitalize()}")


# Süslü parantezin içine fonksiyon da yazabiliriz
def kare(x):
    return x**2

x = 10 
print(f"{x} sayısının karesi {kare(x)}")


































       