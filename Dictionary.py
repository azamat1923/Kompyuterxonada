# # -*- coding: utf-8 -*-
# """
# Created on Mon Aug  9 07:46:22 2021

# @author: Rafiqov Abulqosim
# """
#print('hello world')
# Python lug'atlari
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# Lug'at
# Lug'atlar ma'lumotlar qiymatlarini kalit: qiymat juftlarida saqlash uchun ishlatiladi.

# Lug'at - buyurtma qilingan*, o'zgaruvchan va takroriy nusxalarga ruxsat bermaydigan to'plam.



# Lug'atlar jingalak qavslar bilan yozilgan va kalit va qiymatlarga ega:

# Misol
# Lug'atni yarating va chop eting:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# Lug'at elementlari
# Lug'at elementlari buyurtma qilingan, o'zgartirilishi mumkin va dublikatlarga ruxsat bermaydi.

# Lug'at elementlari kalit: qiymat juftligida taqdim etiladi va ularga kalit nomi yordamida murojaat qilish mumkin.

# Misol
# Lug'atning "brend" qiymatini chop eting:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])
# Buyurtma berilganmi yoki tartiblanmaganmi?
# Python 3.7 versiyasiga ko'ra, lug'atlar buyurtma qilinadi . Python 3.6 va undan oldingi versiyalarda lug'atlar tartiblanmagan .

# Lug'atlar buyurtma qilingan deb aytganimizda, bu ob'ektlar belgilangan tartibga ega ekanligini anglatadi va bu tartib o'zgarmaydi.

# Tartibga solinmagan, ob'ektlar belgilangan tartibga ega emas, siz indeks yordamida ob'ektga murojaat qila olmaysiz.

# O'zgaruvchan
# Lug'atlar o'zgaruvchan, ya'ni lug'at tuzilgandan so'ng biz elementlarni o'zgartirishimiz, qo'shishimiz yoki olib tashlashimiz mumkin.

# Takrorlashga ruxsat berilmagan
# Lug'atlarda bitta kalitli ikkita element bo'lishi mumkin emas:

# Misol
# Takroriy qiymatlar mavjud qiymatlarning ustiga yoziladi:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)

# Lug'at uzunligi
# Lug'atda nechta element borligini aniqlash uchun len()funksiyadan foydalaning :

# Misol
# Lug'atdagi elementlar sonini chop eting:

# print(len(thisdict))
# Lug'at elementlari - ma'lumotlar turlari
# Lug'at elementlari qiymatlari har qanday ma'lumot turiga ega bo'lishi mumkin:

# Misol
# String, int, boolean va ma'lumotlar turlarining ro'yxati:

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# turi ()
# Python nuqtai nazaridan, lug'atlar "dict" ma'lumotlar turiga ega ob'ektlar sifatida belgilanadi:

# <class 'dict'>
# Misol
# Lug'atning ma'lumot turini chop eting:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(type(thisdict))
# Python to'plamlari (massivlar)
# Python dasturlash tilida to'rtta ma'lumot yig'ish turi mavjud:

# Ro'yxat - bu buyurtma qilingan va o'zgaruvchan to'plam. A'zolarning takrorlanishiga ruxsat beradi.
# Tuple - bu buyurtma qilingan va o'zgartirilmaydigan to'plam. A'zolarning takrorlanishiga ruxsat beradi.
# Set og'riqqa va unindexed bir to'plam. Takroriy a'zolar yo'q.
# Lug'at - bu buyurtma qilingan va o'zgaruvchan to'plam. Takroriy a'zolar yo'q.
# To'plam turini tanlayotganda, uning turini bilish foydali bo'ladi. 
# Ma'lumotlar to'plami uchun to'g'ri turni tanlash ma'noni saqlab qolishni anglatishi mumkin,
#  va bu samaradorlik yoki xavfsizlikni oshiradi.
 
 
 
# # =============================================================================
# #  
# # =============================================================================
 
# Python - lug'at elementlariga kirish
# Ob'ektlarga kirish
# Kvadrat qavs ichida uning kalit nomiga murojaat qilib, lug'at elementlariga kirishingiz mumkin:

# Misol
# "Model" kalitining qiymatini oling:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
  
  

# }

# x = thisdict.keys()
# print(thisdict)
# x = thisdict["model"]
# print(x)
# get()Sizga bir xil natija beradigan usul ham mavjud :

# Misol
# # "Model" kalitining qiymatini oling:

# x = thisdict.get("model")
# print(x)
# Kalitlarni oling
# keys()Usuli lug'atda barcha kalitlari ro'yxatini qaytadi.

# Misol
# Kalitlar ro'yxatini oling:

# 
# Kalitlar ro'yxati - bu lug'atning ko'rinishi , 
# ya'ni lug'atga kiritilgan har qanday o'zgarishlar kalitlar ro'yxatida aks etadi.

# Misol
# Asl lug'atga yangi element qo'shing va kalitlar ro'yxati yangilanganligini ko'ring:

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# car["year"] = 2020
# # car["color"] = "white"
# print(car)

#x = car.values()

#print(x) #before the change



#) #after the change

# Qiymatlarni oling
# values()Usuli lug'atda barcha qadriyatlar ro'yxatini qaytadi.

# Misol
# Qiymatlar ro'yxatini oling:

# 
# Qiymatlar ro'yxati - bu lug'atning ko'rinishi ,
#  ya'ni lug'atga kiritilgan har qanday o'zgarishlar qiymatlar ro'yxatida aks etadi.

# Misol
# Asl lug'atga o'zgartirish kiriting va qiymatlar ro'yxati ham yangilanishini ko'ring:

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# 

# print(x) #after the change
# Misol
# Asl lug'atga yangi element qo'shing va qiymatlar ro'yxati ham yangilanganini ko'ring:

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["color"] = "red"

# print(x) #after the change
# Ob'ektlarni olish
# items()Usul ro'yxatda Umumiy bo'lim sifatida, bir lug'atda har bir ob'ektni qaytadi.

# Misol
# Kalitlar ro'yxatini oling: qiymat juftlari

# x = car.items()
# print(x)
# Qaytgan ro'yxat - bu lug'at elementlarining ko'rinishi , 
# ya'ni lug'atga kiritilgan har qanday o'zgarishlar ob'ektlar ro'yxatida aks etadi.

# Misol
# Asl lug'atga o'zgartirish kiriting va ma'lumotlar ro'yxati yangilanganligini ko'ring:

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change
# Misol
# Asl lug'atga yangi element qo'shing va elementlar ro'yxati yangilanganligini ko'ring:

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["color"] = "red"

# print(x) #after the change
# Kalit mavjudligini tekshiring
# Lug'atda ko'rsatilgan kalit mavjudligini aniqlash uchun inkalit so'zdan foydalaning :

# Misol
# Lug'atda "model" mavjudligini tekshiring:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "modell" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary") 
# else:
#     print('nope')
 
 
# # =============================================================================
# #  
# # =============================================================================
# Python - lug'at elementlarini o'zgartirish
# Qiymatlarni o'zgartirish
# Siz ma'lum bir elementning kalit nomiga murojaat qilib uning qiymatini o'zgartirishingiz mumkin:

# Misol
# "Yil" ni 2018 yilga o'zgartiring:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["model"] = 2022
# print(thisdict)
# Lug'atni yangilash
# update()Usul bu argument dan unsurlar bilan lug'ati yangilanadi.

# Argument lug'at yoki kalit: qiymat juftlari bo'lgan takrorlanadigan ob'ekt bo'lishi kerak.

# Misol
# Avtomobilning "yilini" quyidagi update() usul bilan yangilang:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})
# print(thisdict)
# # =============================================================================
# #  
# # =============================================================================
# Python - lug'at elementlarini qo'shish
# Ob'ektlarni qo'shish
# Lug'atga element qo'shish yangi indeks 
# kaliti yordamida va unga qiymat berish orqali amalga oshiriladi:


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)
# Lug'atni yangilash
# update()Usul berilgan argument dan unsurlar bilan lug'ati yangilanadi.
#  Agar element mavjud bo'lmasa, element qo'shiladi.

# Argument lug'at yoki kalit: qiymat juftlari bo'lgan takrorlanadigan ob'ekt bo'lishi kerak.

# Misol
# Rangli elementni lug'atga quyidagi update() usul bilan qo'shing :

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color": "red"}) 
 
# # =============================================================================
# #  
# # =============================================================================
#  Python - lug'at elementlarini o'chirish
# Elementlarni olib tashlash
# Lug'atdan elementlarni olib tashlashning bir necha usullari mavjud:

# Misol
# pop()Usuli belgilangan asosiy nomi bilan ob'ektni tozalaydi:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)
# Misol
# popitem()Usuli (3,7 oldin 
# versiyalarida tasodifiy item o'rniga olib tashlanadi)
# oxirgi kiritilgan elementni olib tashlanadi:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)
# Misol
# delKalit so'z belgilangan asosiy nomi bilan ob'ektni tozalaydi:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)
# Misol
# delKalit so'z ham butunlay lug'at o'chirishingiz mumkin:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict ['year']
# print(thisdict) #this will cause an error because "thisdict" no longer exists.
# Misol
# clear()Usul lug'at bo'shatmoqda:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.values():
#   print(x)
# thisdict.clear()
# print(thisdict)
 
# # =============================================================================
# #  
# # =============================================================================
# Python - Loop lug'atlari
# Lug'at orqali aylanish
# Siz loop yordamida lug'atni aylanib o'tishingiz mumkin for.

# Lug'at orqali Ko'chadan, qaytish qiymati bo'lgan kalitlari lug'at, 
# lekin qaytishga usullari bor qadriyatlarni shuningdek.

# Misol
# Lug'atdagi barcha kalit nomlarni birma -bir chop eting:

# for x in thisdict:
#   print(x)
# Misol
# Lug'atdagi barcha qiymatlarni birma -bir chop eting:

# for x in thisdict:
#   print(thisdict[x])
# Misol
# values()Lug'atning qiymatlarini qaytarish uchun siz ham ushbu usuldan foydalanishingiz mumkin :


# Misol
# keys()Lug'atning kalitlarini qaytarish uchun siz ushbu usuldan foydalanishingiz mumkin :

# for x in thisdict.keys():
#   print(x)
# Misol
# Usul yordamida kalitlarni ham , qiymatlarni ham aylantiring items():

# for x, y in thisdict.items():
#   print(x, y)
 
# # =============================================================================
# #  
# # =============================================================================
# Python - Lug'atlarni nusxalash
# Lug'atni nusxalash
# Siz lug'atni shunchaki yozib nusxa ko'chira olmaysiz dict2 = dict1, chunki: 
# dict2faqat havola bo'ladi dict1va kiritilgan o'zgartirishlar dict1avtomatik ravishda kiritiladi dict2.

# Nusxa ko'chirishning usullari bor, ulardan biri-o'rnatilgan Lug'at usulidan foydalanish copy().

# Misol
# Lug'atning nusxasini quyidagi copy()usul bilan yarating :

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)
# Nusxa olishning yana bir usuli-o'rnatilgan funksiyadan foydalanish dict().

# Misol
# Lug'atning nusxasini quyidagi dict() funktsiyaga ega qiling:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)

# # =============================================================================
# # 
# # =============================================================================
# Python - Nested Dictionaries

# Kiritilgan lug'atlar
# Lug'at lug'atlarni o'z ichiga olishi mumkin, bu ichki lug'atlar deb ataladi.

# Misol
# Uchta lug'atni o'z ichiga olgan lug'atni yarating:

# myfamily = {
#     "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
    
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
  
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
    
#         }
  
 
# }
# for x in myfamily:
#     print(x)
# print(myfamily)
# Yoki, agar siz uchta lug'atni yangi lug'atga qo'shmoqchi bo'lsangiz:

# Misol
# Uchta lug'atni yarating, so'ngra boshqa uchta lug'atni o'z ichiga olgan bitta lug'atni yarating:

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(myfamily)

# Python lug'at usullari
# Lug'at usullari
# Python-da lug'atlarda foydalanishingiz mumkin bo'lgan o'rnatilgan usullar to'plami mavjud.

# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary



# Mashq qilish:
# Lug'atning get"model" kalitining qiymatini chop etish uchun usuldan foydalaning car.

# mashina = {
#   "marka": "Ford",
#   "model": "Mustang",
#   "yil": 1964
# }
# print(mashina.get('model'))


# Mashq qilish:
# "Yil" qiymatini 1964 yildan 2020 yilgacha o'zgartiring.


# mashina = { 
#   "markasi": "Ford", 
#   "model": "Mustang", 
#   "yil": 1964 
# }
# mashina['yil']=2018
# print(mashina) 


# Mashq qilish:
# carLug'atga "rang": "qizil" kalit/qiymat juftligini qo'shing .


# mashina = { 
#   "markasi": "Ford", 
#   "model": "Mustang", 
#   "yil": 1964 
# }
 
# mashina['color']='black'
# print(mashina)


# Mashq qilish:
# Lug'atdan pop"model" ni olib tashlash uchun usuldan foydalaning car.


# mashina = { 
#   "markasi": "Ford", 
#   "model": "Mustang", 
#   "yil": 1964 
# }
# mashina.pop('model')
# print(mashina)




# Mashq qilish:
# Lug'atni clearbo'shatish uchun usuldan foydalaning car.


# mashina = {
#   "marka": "Ford",
#   "model": "Mustang",
#   "yil": 1964
# }
# mashina.clear()
# print(mashina)



