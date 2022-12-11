#Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
# Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.

kume=[[1, 2], [3, 4], [5, 6, 7]]

def ters(kume):
    for x in range(int(len(kume))):
     (kume[x])=(kume[x])[::-1]
     kume=kume[::-1]
    return kume 


print(ters(kume))   