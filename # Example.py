# Example
import math

""" Noktaların Tanımlanması:
‘points’ adında bir liste oluşturun. Bu liste, 2D uzaydaki noktaları temsil eden demetler (tuple) içermelidir. 
Örneğin, ‘(x, y)’ noktası bir demet ‘(x, y)’ olarak temsil edilecektir."""

point_a = (1, 2)
point_b = (4, 6)

point = [ (2,4), (3,6), (4,8), (5,10)]
# print(point[0][0])


"""Öklid Mesafesi İçin Bir Fonksiyon Yazma:
‘euclideanDistance’ adında bir fonksiyon tanımlayın. 
Bu fonksiyon, iki demet (her biri bir noktayı temsil eder) almalı ve bu iki nokta arasındaki Öklid mesafesini döndürmelidir."""

def euclideanDistance( point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

""" 
Böyle de kullanılabilirdi : 
 def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
"""

print(euclideanDistance (point[0], point[1]))

distance  = euclideanDistance( point_a, point_b)
print(f"Euclian Distance : {distance:.2f}")


"""Mesafelerin Hesaplanması:
Bir döngü kullanarak, ‘points’ listesindeki her nokta çifti arasındaki Öklid mesafesini hesaplayın. 
Bu mesafeleri ‘distances’ adında başka bir listede saklayın.  """

n = len(point)
distance = []

for i in range(n):
   for j in range(i + 1, n):
            mesafe = euclideanDistance(point[i], point[j])
            distance.append(mesafe)
   

print(distance[0])

# euclideanDistance( (point[n], point[n+1])) distance.append()




