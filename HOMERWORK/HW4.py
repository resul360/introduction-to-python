# Homework4 
# Global Ai HUB homework4 20/02/2021
import time
name = input("İsminizi Giriniz? :")
print ("Merhaba, " + name, "Adam Asmaca oynama Zamanı!")

time.sleep(1)
print ("Tahmin etme zamanı")
time.sleep(0.5)

#kelime beklirle
kelime = "Python"
# tahmin et
tahminler = ''
# Tahmin için kaç hak verelim?
tahminhakki = 10 

while tahminhakki > 0:         

    hata = 0             
    for karakter in kelime:
        if karakter in tahminler:    
           print (karakter)
        else:
            print ("_")     
            hata += 1    
        if hata == 0:        
            print ("doğru tahmin :)")
        break              
    tahmin = input("karakter tahmin et:") 
    tahminler += tahmin                    
    if tahmin not in kelime:  
        tahminhakki -= 1        
        print ("yanlış")    
 
        print ("Oyunda ", + tahminhakki, ' tahmin hakkın kaldı' )
        
        if tahminhakki == 0:           
            print ("Kaybettin ASILDIN!!!")  
# -*- coding: utf-8 -*-

