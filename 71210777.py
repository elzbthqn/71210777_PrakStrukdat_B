import time
def Deretajaib(y):
    if y<6 :
        return y
    else:
        return Deretajaib(y-2)+Deretajaib(y//2)

def Deretajaib(y):
    drt = [1,2,3,4,5]
    for i in range(5, y):
        hasil = Deretajaib(i-2)+Deretajaib(y//2)
        drt.append(hasil)

