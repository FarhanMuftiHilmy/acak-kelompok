import random


Lnama = input("Masukkan nama orang (pisahkan dengan spasi) = ").split()
#versitanpainputan: Lnama = ['Farhan', 'Mufti', 'Hilmy'] 
n = len(Lnama)
Lkel = []
x = random.sample(range(n), n) #inisialisasi list nilai random berbeda rentang 0 sampai n sejumlah n 

#cek1: print(x)

nk = int(input("Masukkan jumlah  kelompok = "))
isi = True 
for i in range(nk):
    Lkel.append([])
i = -1
j = -1
sign = -1
#isi kelompok satu per satu, jika sudah penuh isi ulang dari awal
while isi == True:
    i += 1 #indeks kelompok
    j += 1 #indeks nama
    sign += 1
    #cek2: print("Indeks i ke", sign+1, "=", i)
    #cek3: print("Indeks j ke", sign+1, "=",j)
    Lkel[i].append(Lnama[x[j]]) #masukkan nama acak ke dalam list kelompok
    if i == nk-1:
        i = -1
    if sign == n-1:
        isi = False
#outputkan hanya nilai Lkel mulai dari indeks 0,1,...nk
sep = ','
for i in range(nk):
    print("KELOMPOK", i+1)
    for j in range(i+1):
        c = Lkel[j]
    print(sep.join(c)) #output dalam bentuk string dipiahkan koma

#cek4: print(Lkel)
        


# CODE HISTORY
#import numpy
# ==============================================TRY USING NUMPy = NOT WORKING===============================
# x = range(nk)
# l = numpy.array_split(numpy.array(x), nk)
# for i in range(n):
#     print("KELOMPOK", i+1)
#     print(Lnama[int(l[i])])
# 
# =============================================================================
# =============================================TRY USING ONLY FOR LOOP = NOT WORKING================================
# x = random.sample(range(n), 3)
# n2 = len(x)
# for i in range(1, nk+1):
#     print("KELOMPOK", i)
#     if i == 1:
#         for i in range(n2):
#             print("%i." % (i + 1), Lnama[x[i]], "no.urut =", x[i] + 1)
# =============================================================================

    

        
