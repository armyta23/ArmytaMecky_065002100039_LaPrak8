# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 03:03:10 2021

@author: LENOVO
"""

def menghitung_range():
    print("PROGRAM MENGHITUNG JUMLAH RANGE")
    sarah = input("masukan angka pertama: ")
    sarah = int (sarah)
    input2=int(input('masukkan angka kedua: '))
    sum = 0
    for i in range(sarah, input2+1, 1):
        sum = sum+i
    print("Jumlah range adalah: ", sum )
menghitung_range()