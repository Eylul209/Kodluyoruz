import math
from typing import Tuple

def oklid_mesafesi(nokta1: Tuple[float, float], nokta2: Tuple[float, float]) -> float:
    """
    İki nokta arasındaki Öklid mesafesini hesaplar.
    
    Args:
    nokta1 (Tuple[float, float]): Birinci noktanın (x1, y1) koordinatları.
    nokta2 (Tuple[float, float]): İkinci noktanın (x2, y2) koordinatları.
    
    Returns:
    float: İki nokta arasındaki Öklid mesafesi.
    """
    x1, y1 = nokta1
    x2, y2 = nokta2
    
    mesafe = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return mesafe

# Örnek kullanımlar
nokta_a = (1.0, 2.0)
nokta_b = (4.0, 6.0)

mesafe = oklid_mesafesi(nokta_a, nokta_b)
print(f"Öklid mesafesi: {mesafe:.2f}")



"""Açıklama
from typing import Tuple: Tuple türünü kullanabilmek için typing modülünden içe aktarırız.
Fonksiyon İmzası:
nokta1: Tuple[float, float]: nokta1'in iki float türünde elemandan oluşan bir tuple olacağını belirtir.
nokta2: Tuple[float, float]: nokta2'nin de aynı şekilde iki float türünde elemandan oluşan bir tuple olacağını belirtir.
-> float: Fonksiyonun dönüş değerinin float türünde olduğunu belirtir.
Bu tür ipuçları, kodun anlaşılmasını ve bakımını kolaylaştırır, ancak Python çalışma zamanında herhangi bir tür denetimi yapılmaz. Bu tür denetimleri gerçekleştirmek için ek araçlar veya kütüphaneler kullanmanız gerekebilir.

Çok Boyutlu Noktalar İçin Tür İpuçları
Çok boyutlu noktalarda da benzer bir yaklaşımı kullanabilirsiniz:
from typing import Tuple

def oklid_mesafesi_genel(nokta1: Tuple[float, ...], nokta2: Tuple[float, ...]) -> float:
     # İki nokta arasındaki Öklid mesafesini hesaplar, çok boyutlu uzayda da çalışır.
    
    # Args:
    # nokta1 (Tuple[float, ...]): Birinci noktanın koordinatları.
    #nokta2 (Tuple[float, ...]): İkinci noktanın koordinatları.
    
    # Returns:
    # float: İki nokta arasındaki Öklid mesafesi.

    if len(nokta1) != len(nokta2):
        raise ValueError("Noktaların boyutları uyuşmuyor")
    
    mesafe = math.sqrt(sum((x2 - x1) ** 2 for x1, x2 in zip(nokta1, nokta2)))
    return mesafe

# Örnek kullanımlar
nokta_a = (1.0, 2.0, 3.0)
nokta_b = (4.0, 6.0, 8.0)

mesafe = oklid_mesafesi_genel(nokta_a, nokta_b)
print(f"Öklid mesafesi: {mesafe:.2f}")  

Bu örnekte:  Tuple[float, ...] ifadesi, her türdeki tuple'ları kabul eder, bu da çok boyutlu noktaları kapsar.






"""







"""