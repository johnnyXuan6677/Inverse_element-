# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:20:18 2020

@author: User
"""


p=27
y=21
g=8


for i in range(p):
 print("----------------------------------------\n")
 print("x=",i)
 print("                                         ")

 print((g**i)%p-y )
 print("                                       ")
    if(g**i)%p-y==0:
         print('找到密碼了，怎麼可能')
     
     break
     else: print('失敗繼續找，離散對數問題不是給人算的!!...')

       