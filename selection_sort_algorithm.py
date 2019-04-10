#Selection Sort (Seçerek Sıralama) Algoritması
def selectionSort(dizi):
   for doldur in range(len(dizi)-1,0,-1):
       max_sayi = 0
       for konum in range(1,doldur+1):
           if dizi[konum]>dizi[max_sayi]:
               max_sayi = konum
       gecici = dizi[doldur]
       dizi[doldur] = dizi[max_sayi]
       dizi[max_sayi] = gecici
#kontrol
dizi = [54,26,93,17,77,31,44,55,20]
selectionSort(dizi)
print(dizi)
