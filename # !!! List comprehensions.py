# !!! List comprehensions
squares = []
for i in range(1,11):
    squares.append(i*i)
print(squares)

# bu yazdığımız kodu list comprehension ile bir satırda yapabiliriz
squares2 = [i * i for i in range(1,11)]   
# "i * i" listin elemanlarını vericek
# for i .. burada da i'nin ne old belirtiyoruz her iterasyonda hangi değerleri alacağını
print(squares2)

# fonksiyonlarda da kullanabiliyoruz
def cube(x):
    return x*x*x

# bunu 
cubes2 = [cube(x) for x in range(1,11)]

squares3 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(squares3)

odd_squares = [ e for e in squares3 if e % 2 == 1]    #!!!
print(odd_squares)

def is_odd(x):
    if x % 2 == 1:
        return True
    else :
        return False

odd_squares1 = [e for e in squares3 if is_odd(e)]     #!!!
    
weird_squares = [ e if e % 2 == 0 else -1 for e in squares]
# ternal conditions
print(weird_squares)     # [-1, 4, -1, 16, -1, 36, -1, 64, -1, 100]

ultra_weird_squares = [ e if e % 2 == 0 else -1 for e in squares if is_odd(e)]
print(ultra_weird_squares)
# şurdaki kısım :  e if e % 2 == 0 else -1, 
# sadece şurası : if is_odd() doğru old (sadece tekleri döndürecek) bakılacak
# [-1, -1, -1, -1, -1]


# set comprehension : süslü parantez ile belirtiliyor
numbers = [1, 2, 3, 4, 5, 6, 7, 1, 2]
set_numbers = { s for s in numbers if s in [1, 2, 3, 4, 5, 6]}
print(set_numbers)             # {1, 2, 3, 4, 5, 6}

# dictionary comprehension : süslü parantez ile belirtiliyor
square_dict = { d : d * d for d in range(1,11) }
# key olarak : değerler, value olarak : karelerini veriyor
print(square_dict)     
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


# nested list comprehension :
m = [[ j for j in range(7)] for _ in range(5)]
print(m)
# kodu okurken şöyle okumalıyız : 2 list comprehension
# for i in range(5) : 5 defa "[ j for j in range(7)]"bunu yapıcak
# ne yapıcak - [ j for j in range(7)] : 0'dan 7'ye kadar bana bir list oluştur


# flatting : düzleştirme
# içerisindeki yapılara git onların elemanlarını düzleştir
# list'in içerisindeki elemanları sen al hepsini başka bir listede eleman ol yaz
n = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
new_m = []
for l in n:
    print(l)
    for e in l:
        new_m.append(e)
        print(e)
print(new_m)            # [10, 11, 12, 13, 14, 15, 16, 17, 18]

flatten_m = [ e for l in m for e in l]
# flatten_m'nin elemanları "e" olacak ve bu her zaman böyledir
# for l in m  : [10, 11, 12], [13, 14, 15], [16, 17, 18] böylece l :
# [10, 11, 12], 
# [13, 14, 15], 
# [16, 17, 18]
# oldu 
# for e in l :  böylece e'nin elemanları l : 
# [10, 11, 12, 13, 14, 15, 16, 17, 18]
print(flatten_m)


# variable unpacking 
# bir seferde birden çok değişkene değer vermek :
x, y = (4, 7)
x, y, z = (4, 7, 11)
print(x, y, z )

# diyelimki soldaki yapının sadece birinci elemanına bir değer eşitleyip
# kullanmak istiyoruz. Daha önce döngülerde yaptığımız gibi kullanmayacağımız 
# değişkene "_" diyebiliriz
x, _ = (4, 7)

# sağ ve soldaki değer sayısı farklıysa 
# Bunu gidermek için yapısını kullanacağız. 
# Aşağıdaki kod şu demek oluyor: ilk iki elemanı x ve y'ye eşitle, 
# sonuna kadar kalan diğer tüm elemanları z'ye eşitle. 
# Bunun sonunda z 11,2,21'den oluşacak, tipi list olacak
x, y, *z = (4, 7, 11, 4, 21)  # ( x = 4, y=7, z = 11,4,21)

print(type(z))   #list

# diyelimki ilk ikisini eşitleyip geriye kalanları kullanmıycaz :
x, y, *_ = (4, 7, 11)

x, y, *z, t = (4, 7, 11, 4, 21)
# ilk değeri x, ikinci değeri y, son değeri t, geriye kalan değerleri z ye eşitle
print(z)     # 11, 4


# Enumerate :
#  burada "*" olduğu için tipi list oluyor list döndürüyor
# ve bu yıldız sadece 1 kullanılır 
# for ile non-scalar yapılar içerisinde dolaşırken ya 
# elemanları ya da indexleri üzerinde dolanmıştık, 
# ama neden ikisi de aynı anda olmasın? : enumeration ile bu mümkün
# Variable unpacking konusunda bir tuple, 
# liste gibi yapıların değerlerini birden çok değişkene bir seferde eşitlemeyi görmüştük
# Bunun aynısını iterasyonda da yapabiliriz


# elemanları tuple'dan oluşan bir list :
p = [(1,2), (10,20)]

for e in p:
    print(e)

print(type(l[0]) )  # tuple

for e in p:
    a, b = p       
# 1. iterasyonda (a,b) = (1,2)   2. iterasyonda (a,b) = (10,20)   
    print(a)       # 1. iterasyonda  a=1,  2. iterasyonda  a=10
    print(b)       # 1. iterasyonda  b=2,  2. iterasyonda  b=20
    print("*********")

# for'un bodysi içerisinde unpack yapmak yerine en başta da unpacki burda sağlayabilirz

for a, b in p:
    print("tuple'ın ilk elemanı", a)
    print("tuple'ın ikinci elemanı", b)
    print("----------------------------")





















