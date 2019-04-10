#Bubble Sort (Kabarcık Sıralaması) Algoritması
def bubbleSort(dizi):
    for i in range(len(dizi)-1,0,-1):
        for j in range(i):
            if (dizi[j] > dizi[j+1]):
                gecici = dizi[j]
                dizi[j] = dizi[j+1]
                dizi[j+1] = gecici
#kontrol
dizi = [54,26,93,17,77,31,4,55,20]
bubbleSort(dizi)
print(dizi)
