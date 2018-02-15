# Muhammed Can TASASIZ

import os
clear = lambda: os.system('cls')

def toplama(x, y):
   return x + y

def çıkarma(x, y):
   return x - y

def çarpma(x, y):
   return x * y

def bölme(x, y):
   return x / y

def islemler():

    print("İşlemi seçiniz")
    print("1.Toplama")
    print("2.Çıkarma")
    print("3.Çarpma")
    print("4.Bölme")

    seçim = input("Seçiminiz(1/2/3/4):")

    num1 = int(input("Birinci sayı: "))
    num2 = int(input("İkinci sayı: "))

    if seçim == '1':
       print(num1,"+",num2,"=", toplama(num1,num2))

    elif seçim == '2':
       print(num1,"-",num2,"=", çıkarma(num1,num2))

    elif seçim == '3':
       print(num1,"*",num2,"=", çarpma(num1,num2))

    elif seçim == '4':
       print(num1,"/",num2,"=", bölme(num1,num2))
    else:
        while 1:
            clear()
            print("Geçersiz ifade kullandınız tekrar deneyiniz!")
            islemler()

islemler()