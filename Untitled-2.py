# "-*-coding: utf-8 -*-"

# objectlerin tiplerine type() ile bakabiliriz
# type casting int (2.9) sonucu 2 olacak çünkü burda sadece tam kısmını alıyor.
# type (2.4 + 3) : float
# type (3/2) : float bölmede diğer işlemelere göre farklı oluyor
# type (3/1.5) : float verir sonuç = 2.0 dır
# int division : "//" : bölmenin tam kısmını verir ama bölme işlemine katılanlardan biri float ise cevapta float oluyor
# 5 // 2  sonuç : 2 ama 5 // 2.0 sonuç : 2.0
# % : mode operatörü
# ** : üs alma işlemi  2 ** 3 : 8 veya 5 ** -1 : 0.5 olarak döndürür

# string olarak yazmak istersek "" tırnak işareti içinde yazmak istiyorum
# ikili ve tekli tırnakla belirtmek sorun değil
# strinler immutable değiştirilemez
# " 5 + 10 " sonucu : '5 + 10'
# escape sequences *** BAK

# newline bitişik olmalı cümleciğe eğer olmaza boşluk bırakıyor ondan sonra ör : \nnasılsın
# "5" + "4"  sonuç : 54 oluyor çünkü + operatörü birleştirme
# "hey" + "nasılsın" : 'hey nasılsın'
# "*" operatörü ardışık birleştirmeye yarıyor
# örnek : 4 * "hey" : 'heyheyheyhey' oluyor
# "1" + "0"*10 : 10000000000
# len() metodu  len("hey") : 3, len("4") : 1
# isim = "Deniz"
# isim[1] in sonucu ile
# "Deniz"[1] in sonucu aynı değeri veriyor phytonda
# isim[-1] : sonkarakteri almak için [4] yazmak yerine [-1] yazmak
# string immutable isim[0] = "b" yanlış oluyor
# string ile arrayi karıştırmayalım
# slicing : istediğiniz kısmı getirme
# isim[0: 3] : o'dan 3'e kadar alma 'Den'
# isim[:3] : başlangıcı söylemeye gerek kalmıyor
# isim[1:]
# isim[: ...] bu kısım indexten daha büyük bir değerse hata almayız
# isim [başlangıç : bitiş : adım değeri]
# isim[: : 2] 2 2 atalayarak ilerleyerek değeri al
# tersten elemanları almak istersek ; isim [10:0:-1] ya da isim[::-1]

# casting string içerisinde sayısal ifade içeren stringi casting etme
# a = "5"  int(a) oluyor  ama a = "Hey 5" yapıp int(a) yaparsak hata alırdık
# int("5") : 5 (int)

x = input("Bir sayı girin")
# burda bunu output olarak karşımıza çıkarıyor ve ekstra inputu da girebiliyoruz.
# ** input sonucunda elimize gelen değer string oluyor inputtan dönen şey string
# type(x) : str

x = int(input("Bir sayı girin"))

# phytonda mantıksal operatörler ile direkt boolean
# stringlerde karşılaştırma
# "ab" < "b" : true  çünkü alfabetik sıralama ilk elemanlar üzerinden bakıyor

# "not" operatörü
not True
# cevabı false olur

# short circuit ilk başın true olması durumundan dolayı ikinci tarafa bakmıyor
( 5 < 3) and print("hey")   # false
( 5 < 3) or print("hey")    # hey
( 5 > 3) and print("hey")   # hey
( 5 < 3) or print("hey")    # hey

# short circuit old da ilk duruma bakmadığı için başka bir şey kullanıyoruz

( 5 < 3) & print("hey")    # type error alacak

# if else block

a = int(input("Bir sayı giriniz"))
if a == 10:
    print("sayı 10")
elif x < 10:
    print("sayı 10 dan küçük")

else :
    print("sayı 10 dan büyük")


# if ( x % 3 == 0) and ( x % 2 == 0 ):

# "ternary conditional if else olmadan kolayca yapabilmek"
# cevap = input("x in değeri 2 olsun mu ? y/n:")
# condition = cevap == "y"
# b = 2 if cevap == "y" else 0
# b = 2 if condition else 0
# print(x)



























