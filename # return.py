# return
# Bir fonksiyonu çalıştırdığımızda onun sonucuyla bir şeyler yapmak 
# isteyebilirim. Sonucu bana versin diye özellikle söylemem lazım, 
# bunu return keyword'ü ile sağlayacağız
# return yazmasaydık fonksiyon hiç bir şey döndürmezdi

# fonksiyon tanımladığımı python'a anlatmak için yapım:
# "def fonksiyonun_adı(input):"

# öbür yapılarda da olduğu gibi, bir kod bloğunun belirttiğimiz yapıya ait
#  olduğunu anlatmak için boşluk bırakarak içine yazmamız gerekiyor
# Verdiğimiz değerin karesini alan bir fonksiyon yazalım
def square(x):
    return x*x

# fonksiyonu tanımladıktan sonra tanımladığımız adla onu çağırabiliriz. 
# yapımız şöyle olacak: fonksiyonun_adı (inputlar), 
# bir fonksiyonu çağırmak için inputlarını () 'ın içine yazmalıyız. 
# Bazı durumlarda hiç input olmayabilir, 
# bazı durumlarda birden çok olabilir.

# print(square(3,4))    - HATA
print(square (3))
a = square (3)
print(a)                    # 
print(type(a))              #-- None Type  return yazmasaydık none type olacaktı
print(type(square(3)) )     ## 

# bize x*x i değer olarak vermedi. 
# Vermesi için bana o değeri döndür diye özellikle söylemem lazım. 
# Bunu return ile sağlıyoruz

square (2)
a = square(2)
print(a)
b = 4
b += 2

# Bu döndürülen değerin int 4 ten bir farkı yok, 
# nereden nasıl geldiği önemli değil, a = 4 dediğimdeki 4 ile aynı. 
# Bu değerle istediğimi yapabilirim
# 1 + square (2)

# Bilgisayar için o da sadece bir değerdi. 
# Aşağıdaki örenekte de square(3) bize 9 döndürüyor, 
# bilgisayar için aşağıdaki kod, square(9) ile aynı
print(square (square(3)))

# hiç bir inputu olmaya da bilirdi
def weird():
    return 5
print(weird())

# !! Fonksiyonlar return'e geldikten sonrasına bakmıyor, 
# return ün sağına yazılan değeri veriyor ve fonksiyondan çıkıyor
def square(x):
    res = x * x
    return res
    # print etmeyecek : print ("Square of" + str(x) + ":" + str(res))


# Bu yüzden burada bastırma kısmını yapmadı, 
# çünkü o kod return ün altında

print(square (4))      #16
print(square(4) + 2)   

def square(x):
    res = x * x 
    print("Square of" + str(x) + ":" + str(res)) 
    return res
print(square (4))  # Square of 4: 16


# Fonksiyona durumsallık da katabiliriz
def f(x):
    res = x * x
    if x % 2 == 0:
        return res
    else:
        return res + 10
    
    # print("Square of " + str(x) + ":" + str(res))
print(f(10))
print(f(13))


#Fonksiyonların içinde döngü mantığı da olabilir
def f(x):
    res = x * x

    for _ in range(10):
        res += 20
        return res
        # print("hey")

print(f(10))
print(f(10) + 23)

def f(x):
    res = x * x
    for _ in range(10): 
        res += 20 
        return res
print(f(10))


def f(x):
    l = [] 
    res = x * x
    for _ in range(10):
        res += 20
        l.append(res)
    return l
    
f(10)    # [120, 140, 160, 180, 200, 220, 240, 260, 280, 300]

# Void Fonksiyonlar (Değer Döndürmeyen Fonksiyonlar)
# bu fonksiyon çalışmaz : def f(x): x = 2

print(f(2))

print(f(10) + 4)
print(f(3))
print(type(f(3)))

# Bu kod x in karesini değer olarak bize vermiyor, sadece ekrana bastıracak 
def square(x):
    print(x, "in/ün/un karesi:", x*x)

print(square (3))

print(type(square (4)))   # None Type

# hem bir değer bastırıp aynı anda o değeri döndüre de bilirdi
def square(x):
    res = x * x
    print(x, "in/ün/un karesi:", x*x)
    return res
print(square (4))
print(square(4) + 2)




































