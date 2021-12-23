# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 12:13:37 2021

@author: Rafiqov Abulqosim

"""

# Python If ... Else

# Python shartlari va If bayonotlari
# Python matematikadan odatiy mantiqiy shartlarni qo'llab -quvvatlaydi:

# Teng: a == b
# Teng emas: a! = B a! = b
# Kamroq: a <b
# Kichik yoki teng: a <= b
# Katta: a> b
# Katta yoki teng: a> = b
# Bu shartlar bir necha usulda ishlatilishi mumkin,
# ko'pincha "if ifoda" va looplarda.

# "If ifoda" if kalit so'zidan foydalanib yoziladi .

# Misol
# Agar bayonot:

# a = 33
# b = 200
# if b > a:
    
#   print("b is greater than a")
# Bu misolda biz b ning a dan katta ekanligini tekshirish 
# uchun if ifodasining bir qismi sifatida ishlatiladigan 
# ikkita a va b o'zgaruvchilardan foydalanamiz . 
# As a bo'ladi 33 , va b bo'lgan 200 , biz 200 33 ortiq ekanligini bilaman,
#  va shuning uchun biz "b a kattaroqdir», deb ekranga chop.

# Chiziq
# Python koddagi ko'lamni aniqlash uchun indentatsiyaga 
# (satr boshidagi bo'sh joyga) tayanadi. Boshqa dasturlash 
#  tillari ko'pincha bu maqsadda jingalak qavslardan foydalanadilar.

# Misol
# Agar ifoda, indentatsiyasiz (xato keltirib chiqaradi):

# a = 33
# b = 200
# if b > a:
#  print("b is greater than a") # you will get an error
# ADVERTISEMENT	
# Elif
# Elif kalit so'z "avvalgi sharoiti to'g'ri 
#emas edi, agar, keyin bu shartni harakat", deb Pito'n yo'lidir.

# Misol
# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# Bu misolda a b ga teng , shuning uchun birinchi shart to'g'ri emas, 
# lekin elif sharti to'g'ri, shuning uchun ekranga "a va b teng" 
#deb chop etamiz.

# Boshqa
# Yana avvalgi sharoitlari qo'lga emas kalit so'z ushlaydi narsa.

# Misol
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")
# Bu misolda a b dan katta , shuning uchun birinchi shart to'g'ri emas,
#  elif sharti ham to'g'ri emas, shuning uchun biz boshqa shartga o'tamiz
# va "a b dan katta" ekranga chiqaramiz .

# Bundan tashqari, bir bo'lishi mumkin elseholda elif:

# Misol
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")
# Qisqa qo'l, agar
# Agar sizda bajarilishi kerak bo'lgan bitta bayonot bo'lsa, 
# uni if ​​iborasi bilan bir qatorga qo'yishingiz mumkin.

# Misol
# Agar bitta satr if bo'lsa:

# if a > b: 
#     print("a is greater than b")
# Qisqa yo'l, agar ... Boshqa
# Agar sizda bajarilishi kerak bo'lgan bitta bayonot bo'lsa, 
# bittasi if uchun va boshqasi uchun hamma narsani
# bir xil satrga qo'yishingiz mumkin:

# Misol
# Agar bitta satr if ifoda etsa:

# a = 20000
# b = 33000
# print("kichik") if a > b else print("katta")
# Bu usul uchlamchi operatorlar yoki shartli iboralar deb nomlanadi .

# Siz bir xil satrda yana bir nechta bayonotga ega bo'lishingiz mumkin:

# Misol
# Agar bitta satr if ifoda bo'lsa, 3 shart bilan:

# a = 300
# b = 300
# print("A") if a > b else print("==") if a == b else print("B")
# Va
# Va kalit so'z mantiqiy operator hisoblanadi 
#va shartli iboralar birlashtirish uchun ishlatiladi:

# Misol
# If adan katta bo'lsa b, AND c dan katta ekanligini tekshiring a:

# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")
# Yoki
# orKalit so'z mantiqiy operator hisoblanadi va shartli iboralar birlashtirish uchun ishlatiladi:

# Misol
# If adan katta byoki OR a dan katta ekanligini tekshiring c:

# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("ikkalasidan bittasi to'g'ri")
# Ichki if
# Siz ifbayonotlar ichida ifbayonotlarga ega 
#bo'lishingiz mumkin , buni ichki if bayonotlar deyiladi .


# x = 40

# if x > 10:
#   print("10 dan oshiqroq,")
#   if x > 50:
#     print("50dan ham katta!")
    
  
#   else:
#     print("lekinjddgg ham emas.")
# O'tish bayonoti
# ifbayonotlar bo'sh bo'lishi mumkin emas, lekin agar sizda 
# biron sababga ko'ra ifmazmuni bo'lmagan passbayonot
# bo'lsa, xato qilmaslik uchun bayonotni qo'ying .

# Misol
# a = 33
# b = 200
# c=545
# d=5
# g=5

# if b > a:
#   pass

#DAM OLISH KUNI HAQQIDA IF..ELSE GA M

# # =============================================================================
# # 
# # =============================================================================

# Python looplari
# Python looplari
# Pythonda ikkita boshlang'ich pastadir buyrug'i mavjud:

# ilmoqlar paytida
# uchun berk ko'chadan
# Vaqt davri
# Vaqt tsikli bilan shart to'g'ri bo'lsa, biz bir qator iboralarni bajarishimiz mumkin.

# Misol
# Men 6 -dan kichik bo'lganimga qadar chop eting:

# i = 1
# while i < 101:
#   print(i)
#   i += 1
# Eslatma: i ni oshirishni unutmang, aks holda WHILE abadiy davom etadi.

# Esa halqa Bu misolda biz katalog yaratish 
# o'zgarmaydigan aniqlash kerak, tayyor bo'lishi uchun tegishli 
# o'zgaruvchilari talab i , biz 1 o'rnatilgan.

# Tanaffus bayonoti
# Break iborasi bilan, agar vaqt sharti to'g'ri bo'lsa ham, biz loopni to'xtata olamiz:

# Misol
# Men 3 yoshda bo'lganimda, ko'chadan chiqing:

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1
# Davomiy bayonot
# Bilan davom bayonot biz hozirgi yineleme to'xtatish,
#  va keyingi bilan davom ettirishingiz mumkin:

# Misol
# Agar men 3 bo'lsa, keyingi iteratsiyani davom ettiring:

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)
# Boshqa bayonot
# Bilan yana bayonotda, biz Ahvoli endi haqiqiy bo'lsa bir marta,
#  bir kod bloklarini ishlatish mumkin:

# Misol
# Agar shart noto'g'ri bo'lsa, xabarni chop eting:

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

# # =============================================================================
# # 
# # =============================================================================
# Python For Loops


# A uchun Loop (yo ro'yxati, bir nizomning, lug'at,
#               bir to'siq yoki tor ekanligini) bir 
#               ketma-ketlikda ustida vasvasaga uchun ishlatiladi.

# Bu kam o'xshaydi uchun boshqa dasturlash tillarida kalit, 
# va yana boshqa ob'ekt yo'naltirilgan dasturlash tillari topilgan sifatida iterator usuli kabi ishlaydi.

# Bilan uchun biz, bir qator so'zlar amalga mumkin Ichak 
# bir marta ro'yxatda har bir element uchun, nizomning, belgilangan boshqalar

# Misol
# Har bir mevani meva ro'yxatiga chop eting:

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
# Uchun halqa oldin belgilash uchun bir katalog yaratish o'zgaruvchini talab qilmaydi.

# String orqali aylanish
# Hatto satrlar takrorlanuvchi ob'ektlar bo'lib, ular belgilar ketma -ketligini o'z ichiga oladi:

# Misol
# "Banan" so'zidagi harflarni aylantiring:

# for x in "GDKGMJSADOGIKDJGMODGMDSGK":
#   print(x)
# Tanaffus bayonoti
# Bilan tanaffus barcha ob'ektlar orqali topiladi oldin bayonotida, biz Loop to'xtatish mumkin:

# Misol
# x"Banan" bo'lganda, pastadirdan chiqing :

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break
# Misol
# x"Banan" bo'lgandan keyin ko'chadan chiqing , lekin bu safar tanaffus nashrdan oldin keladi:

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)
# print(fruits)

# Davomiy bayonot
# Bilan davom bayonot biz Ichak joriy yineleme to'xtatish, va keyingi bilan davom ettirishingiz mumkin:

# Misol
# Banan chop qilmang:

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)
# Diapazon () funktsiyasi
# Belgilangan miqdordagi kodlar to'plamini aylanib 
# o'tish uchun biz range () funktsiyasidan foydalanishimiz mumkin ,
# Oralig'i () funktsiyasi belgilangan qator (sukut) 
# 1 sukut 0 dan boshlab sonlar, va bosqichlarida bir ketma-ketlikni qaytaradi, va uchlari.

# Misol
# Range () funktsiyasidan foydalanib:

# for x in range(6):
#   print(x)
# E'tibor bering, (6) diapazon 0 dan 6 gacha emas, balki 0 dan 5 gacha bo'lgan qiymatlardir.

# Oralig'i () : a boshlang'ich qiymati 0 funktsiyasi standartni,
#  ammo u bir parametr qo'shib boshlab qiymatini belgilash 
#  mumkin qator (2, 6) 6, 2 dan vositalari qadriyatlar (lekin 6, shu jumladan emas):

# Misol
# Boshlash parametridan foydalanish:

# for x in range(6, 21):
#   print(x)
# Oralig'i () funktsiyasi Standartni Biroq u uchinchi parametr 
# qo'shib oshirish qiymatini belgilash mumkin, 
# 1 ketma-ketlikni oshirish uchun qator (2, 30, 3 ) :

# Misol
# Ketma -ketlikni 3 ga oshiring (standart 1):

# for x in range(0, 30, 2):
#   print(x)
# Boshqalar uchun Loop
# elseAgar kalit so'z forIchak kodi bir blok halqa tayyor bo'lganda ijro belgilaydi:

# Misol
# 0 dan 5 gacha bo'lgan barcha raqamlarni chop eting va tsikl tugagandan so'ng xabarni chop eting:

# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")
# Eslatma:else halqa bir tomonidan to'xtatildi bo'lsa blok ijro bo'lmaydi breakbayonotida.

# Misol
# x3 bo'lganingizda pastadirni uzing va elseblok bilan nima bo'lishini ko'ring :

# for x in range(6):
#   if x == 3: 
#       break
#   print(x)
# else:
#   print("Finally finished!")
# Ichki halqalar
# Ichki halqa - bu pastadir ichidagi pastadir.

# "Ichki pastadir" har bir takrorlash uchun bir marta bajariladi:

# Misol
# Har bir meva uchun har bir sifatni chop eting:

# abs = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in abs:
#   for y in fruits:
#     print(x, y)
# O'tish bayonoti
# forlooplar bo'sh bo'lishi mumkin emas,
#  lekin agar sizda biron bir sababsiz 
#  forkontent bo'lmasa, passxatoga yo'l qo'ymaslik uchun bayonotni qo'ying .

# # Misol
# for x in [0, 1, 2]:
#   pass


