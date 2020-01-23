"""
Created on Sun Sep 15 08:13:24 2019

@author: brahmasurya27
"""
import random 
from random import randint
fitnes = [] 
proporsisi =[] 

def individu(length,min,max):  
    krom = []
    for x in range(length):
        temp = randint(min,max)
        krom.append(temp)
    return krom

def populasi(jumlah,length,min,max):  
    pop = []
    for i in range(jumlah):
        tamp = individu(length,min,max)
        pop.append(tamp)
    return pop

def dekrom(populasi):
    krom = populasi
    dekod = []
    for i in krom:
        sum= 0
        tot= 0
        j=1
        panjang1 = len(krom[0])//2
        while j <= (panjang1):
            sum = sum + (9*10**-j)
            tot = tot + ((i[j-1])*10**-j)
            j+=1
        x1=-3+(((3-(-3))/sum)*(tot)) 
        sum =0
        tot =0
        k=(len(krom[0])//2)+1
        panjang2 = len(krom[0])
        while k <= (panjang2):
            sum = (sum + (9*10**-(k-(len(i)//2))))
            tot = (tot + ((i[k-1])*10**-(k-((len(i))//2))))
            k+=1
        x2=-2+(((2-(-2))/sum)*(tot))
        dekod.append([x1,x2])
    return dekod

def hitung_fitnes(x1,x2):
        return (((((4-2.1*x1**2+(x1**4/3))*x1**2)+(x1*x2))+((-4+4*x2**2)*x2**2)))
def minimasi_fitnes(x1,x2,fi):
    a = 10
    hasil = hitung_fitnes(x1,x2)
    fi = (1/(hasil+a))
    return fi
    
def fitnes_terbaik(fi):
    fit_temp = []
    max,indeks = 0,0
    feno = dekrom(pop)
    for j in feno:
        y1 = j[0]
        y2 = j[1]
        jum = minimasi_fitnes(y1,y2,fi)         
        fit_temp.append(jum)
    for i in range(len(feno)):
        if fit_temp[i] > max:
            max = fit_temp[i]
            indeks = pop[i]
    return max,indeks

def pemilihan_ortu(proporsisi):
    n =0
    hasil = proporsisi
    m=0
    x =  random.uniform(0,1)
    for i in (hasil):
        m =i+m
        if x < m:            
            break
        n = n+1
    return n

def crosover(x1,x2):
    n =0
    temp = 0
    y = randint(1,4)
    for i in (x2):
        if (n<y):
            temp = x1[n]
            x1[n]= x2[n]
            x2[n]= temp
        n +=1
    return x1,x2

def mutasi(x1,x2):
    x1,x2 = crosover(x1,x2)
    prob = 0.5
    n = 0
    x = random.uniform(0,1)
    y = randint(0,4) 
    for i in (x1):
        if ( x < prob):
            if (y==n):
                x1[n] = randint(0,9)
                break
        n += 1 
    n =0
    y = randint(0,5) 
    for i in (x2):
        if(x < prob):
            if (y==n):
                x2[n] = randint(0,9)
                break
        n +=1
    return x1,x2

#===================================MAIN===============================================


fi = 0
a=10
b =40
pop = populasi(b,6,0,9)            
fit_baik = fitnes_terbaik(fi)
for generasi in range(a):
    tampung =[]
    for i in range(int(b/2)):  
        print('Generasi ke-',i+1)
        jumlah =0
        feno = dekrom(pop)
        print('--Nilai decode kromosom--')
        print(feno)
        print('--nilai fitnes kromosom--')
        for i in feno:
            x1 = i[0]
            x2 = i[1]
            jum = minimasi_fitnes(x1,x2,fi)
            print((minimasi_fitnes(x1,x2,fi)))
            jumlah = jumlah + minimasi_fitnes(x1,x2,fi)
            fitnes.append(jum)
        for i in fitnes:
            prop = ((i/jumlah))
            proporsisi.append(prop)
        
        parent_1, parent_2 = pemilihan_ortu(proporsisi), pemilihan_ortu(proporsisi)
        print('parent yang terbentuk')
        parent1 = pop[parent_1]
        parent2 = pop[parent_2]
        print(parent1, parent2 )
        
        print('crosover yang terbentuk')
        print (crosover(parent1,parent2))
        
        print('mutasi yang di bentuk')
        cross1, cross2 = crosover(parent1,parent2)
        tem = mutasi(cross1,cross2)
        print(tem)
        print("="*50)
        tampung.append(tem[0])
        tampung.append(tem[1])
    pop = tampung
    
    temp_fit2 = fitnes_terbaik(fi)
    if temp_fit2[0] > fit_baik[0]:
        fit_baik = temp_fit2   
    generasi += 1

    
tot =0
jum =0
jum1 =0
tot1 =0
y =1
for i in fit_baik[1]:
    panjang1 = len(fit_baik[1])//2
    while y <= (panjang1):
        jum = jum + (9*10**-y)
        tot = tot + ((fit_baik[1][y-1])*10**-y)
        y+=1   
    x1=-3+(((3-(-3))/jum)*(tot))
    tot1 =0
    jum1 =0
    j=(len(fit_baik[1])//2)+1
    panjang2 = len(fit_baik[1])
    while j <= (panjang2):
        jum1 = jum1 + (9*10**-(j-(len(fit_baik[1])//2)))
        tot1 = tot1 + ((fit_baik[1][j-1])*10**-(j-((len(fit_baik[1]))//2)))
        if(j<=panjang2):
            x2=-2+(((2-(-2))/jum1)*(tot1))
        j+=1 
print('Kromosom Terbaik : '+str(fit_baik[1]))
print('Nilai Fitnes : '+str(fit_baik[0]))
print('Nilai dekode X1 : %r, dekode X2 : %r '%(x1,x2))
print('Nilai Minimum :'+str(hitung_fitnes(x1,x2)))



   