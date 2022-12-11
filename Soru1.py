#Bir listeyi düzleştiren (flatten) fonksiyon yazın.
#Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir

boskume=[]
def flatten(k):

    for x in k:
        if isinstance(x,list):
            flatten(x)
        else:
            boskume.append(x)
            

k =[[1,'a',['cat'],2],[[[3]],'dog'],4,5]

flatten(k)

print(boskume)