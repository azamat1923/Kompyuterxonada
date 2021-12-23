# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 19:27:33 2021

@author: Rafiqov Abulqosim
"""

#student = ("Abulqosim",19 ,'male')
# print(student)
# print(student.index("male"))

# Python Tuples
# mytuple = ("apple", "banana", "cherry")
# print(mytuple)
# # Tuple
# Tuplar bir nechta elementlarni bitta o'zgaruvchiga saqlash uchun ishlatiladi.

# Tuple-bu ma'lumotlar to'plamini saqlash uchun ishlatiladigan Python-dagi 4 ta 
# o'rnatilgan ma'lumotlar turlaridan biri, qolgan 3 tasi har xil sifat 
# va foydalanishga ega bo'lgan List , Set va Lug'at .

# Tuple - bu buyurtma qilingan va o'zgartirilmaydigan to'plam .

# Tuplar dumaloq qavslar bilan yozilgan.

# Misol
# Tuple yaratish:

# thistuple = ("apple", "banana", "cherry")
# print(type(thistuple))
# Tuple elementlari
# To'plamli elementlar buyurtma qilingan, o'zgartirilmaydi va takroriy qiymatlarga ruxsat beradi.

# Tuple elementlari indekslanadi, birinchi element 
#indeksga ega [0], ikkinchi element indeksga ega [1]va hokazo.

# Buyurtma qilingan
# Tuplar buyurtma qilingan deb aytganimizda, b
#u buyumlar belgilangan tartibga ega va bu tartib o'zgarmaydi.

# O'zgarmas
# Tuplar o'zgarmas, ya'ni biz yaratganimizdan keyin elementlarni o'zgartira olmaymiz, 
# qo'sha olmaymiz yoki o'chira olmaymiz.

# Takrorlashga ruxsat berish
# Tuplar indekslanganligi sababli, ular bir xil qiymatga ega bo'lishi mumkin:

# Misol
# Tuplar qiymatlarni takrorlashga ruxsat beradi:

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

# Tup uzunligi
# To'plamda nechta element borligini aniqlash uchun quyidagi len()funktsiyadan foydalaning :

# Misol
# To'plamdagi elementlar sonini chop eting:

# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))
# Bitta element bilan birikma yaratish
# Faqat bitta elementdan iborat korpus yaratish uchun elementdan keyin vergul qo'shish kerak, 
# aks holda Python uni katak sifatida tan olmaydi.

# Misol
# Bitta element yig'ilganda, vergulni eslang:

# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))
# To'plam elementlari - ma'lumotlar turlari
# To'plam elementlari har qanday turdagi bo'lishi mumkin:

# Misol
# String, int va boolean ma'lumotlar turlari:

# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)
# To'plam har xil turdagi ma'lumotlarni o'z ichiga olishi mumkin:

# Misol
# Stringlar, tamsayılar va mantiqiy qiymatlarga ega bo'lak:

# tuple1 = ("abc", 34, True, 40, "male")
# turi ()
# Python nuqtai nazaridan, tuplar "tuple" ma'lumotlar turiga ega ob'ektlar sifatida belgilanadi:

# <class 'tuple'>
# Misol
# To'plamning ma'lumotlar turi qanday?

# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))
# Tuple () konstruktor
# Tuple yaratish uchun tuple () konstruktoridan foydalanish ham mumkin .

# Misol
# Tuple qilish uchun tuple () usuli yordamida:

# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)
# Python to'plamlari (massivlar)
# Python dasturlash tilida to'rtta ma'lumot yig'ish turi mavjud:

# Ro'yxat - bu buyurtma qilingan va o'zgaruvchan to'plam. A'zolarning takrorlanishiga ruxsat beradi.
# Tuple - bu buyurtma qilingan va o'zgartirilmaydigan to'plam. A'zolarning takrorlanishiga ruxsat beradi.
# Set og'riqqa va unindexed bir to'plam. Takroriy a'zolar yo'q.
# Lug'at - buyurtma qilingan va o'zgaruvchan to'plam. Takroriy a'zolar yo'q.


# # =============================================================================
# # 
# # =============================================================================
# Python to'plamlari
# utensils = {'fork','spoon','knife','spoon','knife'}
# # print(utensils)
# dishes = {'bowl', 'plate', 'cup', }
# utensils.update(dishes)
# print(utensils)
# utensils.clear()
# print(utensils)
# utensils.add('napkin')

# utensils.remove('fork')
# print(utensils)
# for x in utensils:
#     print(x)
#print(utensils)


# myset = {"apple", "banana", "cherry"}
# print(myset)
#O'rnatish
# To'plamlar bir nechta elementlarni bitta o'zgaruvchiga saqlash uchun ishlatiladi.

# To'plam-bu Python-da ma'lumotlar to'plamini saqlash uchun ishlatiladigan 4 ta 
# o'rnatilgan ma'lumotlar turlaridan biri, qolgan 3 tasi List , Tuple va Dictionary bo'lib , 
# ularning har biri har xil sifat va foydalanishga ega.

# To'plam - bu tartiblanmagan va indekslanmagan to'plam .

# To'plamlar jingalak qavslar bilan yozilgan.

# Misol
# To'plam yaratish:

# thisset = {"apple", "banana", "cherry"}
# print(thisset)
# Eslatma: To'plamlar tartibsiz, 
#shuning uchun buyumlar qaysi tartibda paydo bo'lishini aniq bila olmaysiz.

# Elementlarni sozlash
# O'rnatilgan elementlar tartibsiz, o'zgarmas va takroriy qiymatlarga ruxsat bermaydi.

# Tartibsiz
# Tartibga solinmagan, to'plamdagi elementlarning belgilangan tartibga ega emasligini bildiradi.

# O'rnatish elementlari har safar ishlatilganda boshqacha tartibda paydo bo'lishi mumkin va ularni indeks yoki kalit bilan bog'lab bo'lmaydi.

# O'zgarmas
# To'plamlar o'zgarmasdir, ya'ni to'plam yaratilgandan so'ng biz elementlarni o'zgartira olmaymiz.

# To'plam yaratilgach, siz uning elementlarini o'zgartira olmaysiz, lekin siz yangi elementlarni qo'shishingiz mumkin.

# Takrorlashga ruxsat berilmagan
# To'plamlarda bir xil qiymatga ega ikkita element bo'lishi mumkin emas.

# Misol
# Takroriy qiymatlar e'tiborga olinmaydi:

# thisset = {"apple", "banana", "cherry", "apple"}

# print(thisset)
# To'plam uzunligini oling
# To'plamda nechta element borligini aniqlash uchun len()usuldan foydalaning .

# Misol
# To'plamdagi elementlar sonini oling:

# thisset = {"apple", "banana", "cherry"}

# print(len(thisset))
# Elementlarni sozlash - ma'lumotlar turlari
# To'plam elementlari har qanday turdagi bo'lishi mumkin:

# Misol
# String, int va boolean ma'lumotlar turlari:

# set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False}
# To'plam har xil turdagi ma'lumotlarni o'z ichiga olishi mumkin:

# Misol
# Stringlar, butun sonlar va mantiqiy qiymatlar to'plami:

# set1 = {"abc", 34, True, 40, "male"}
# turi ()
# Python nuqtai nazaridan, to'plamlar "set" ma'lumotlar turiga ega ob'ektlar sifatida belgilanadi:

# <class 'set'>
# Misol
# To'plamning ma'lumotlar turi qanday?

# myset = {"apple", "banana", "cherry"}
# print(type(myset))
# Set () konstruktori
# To'plam yaratish uchun set () konstruktoridan foydalanish ham mumkin .

# Misol
# To'plam yaratish uchun set () konstruktoridan foydalanib:

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)
# Python to'plamlari (massivlar)
# Python dasturlash tilida to'rtta ma'lumot yig'ish turi mavjud:

# Ro'yxat - bu buyurtma qilingan va o'zgaruvchan to'plam. A'zolarning takrorlanishiga ruxsat beradi.
# Tuple - bu buyurtma qilingan va o'zgartirilmaydigan to'plam. A'zolarning takrorlanishiga ruxsat beradi.
# Set og'riqqa va unindexed bir to'plam. Takroriy a'zolar yo'q.
# Lug'at - buyurtma qilingan va o'zgaruvchan to'plam. Takroriy a'zolar yo'q.


# # =============================================================================
# # 
# # =============================================================================
# Python lug'atlari




# thisdict = {
     
#    "brand": "Ford",
#    "model": "Mustang",
#    "year": 1964,
#    'sfsasf':'fasfas'
   
  
# }
# print(thisdict)
# Lug'at
# Lug'atlar ma'lumotlar qiymatlarini kalit: qiymat juftlarida saqlash uchun ishlatiladi.

# Lug'at - bu buyurtma qilingan*, o'zgaruvchan va takrorlanishga ruxsat bermaydigan to'plam.

# Python 3.7 versiyasiga ko'ra, lug'atlar buyurtma qilinadi . 
#Python 3.6 va undan oldingi versiyalarda lug'atlar tartiblanmagan .

# Lug'atlar jingalak qavslar bilan yozilgan, kalitlari va qiymatlari bor:

# Misol
# Lug'atni yarating va chop eting:
# capitals = {
#     'USA':'Washington',
#     'India':'NewDlphi',
#     'Russia':'Moscoiw',
#     'UZB':"Samarqand"
#     }

# # print(capitals.get('Russia'))
# # print(capitals['USA'])
# # capitals.clear()
# # capitals.pop('USA')
# # capitals.update({'Germany':'Berlin'})
# print(capitals)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# Lug'at elementlari
# Lug'at elementlari buyurtma qilingan, o'zgaruvchan va dublikatlarga ruxsat bermaydi.

# Lug'at elementlari kalit: qiymat juftligida taqdim etiladi 
#va ularga kalit nomi yordamida murojaat qilish mumkin.

# Misol
# Lug'atning "brend" qiymatini chop eting:
# car_0={
#         'model':'cobalt',
#         'rang':'oq',
#         'yili':'2022'  
       
#         }
# print(car_0.get('rang'))

# talaba ={}
# car_0 ['ism'] = 'cobalt'
# car_0 ['ism'] = 'cobalt'
# car_0 ['ism'] = 'cobalt'
# car_0 ['ism'] = 'cobalt'
# car_0 ['ism'] = 'c
# print(talaba)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["year"])
# Buyurtma berilganmi yoki tartiblanmaganmi?
# Python 3.7 versiyasiga ko'ra, lug'atlar buyurtma qilinadi . Python 3.6 va undan oldingi versiyalarda lug'atlar tartiblanmagan .

# Lug'atlar buyurtma qilingan deb aytganimizda,
# bu ob'ektlar belgilangan tartibga ega ekanligini anglatadi va bu tartib o'zgarmaydi.

# Tartibga solinmagan, bu elementlarning belgilangan tartibiga ega emas,
#siz indeks yordamida ob'ektga murojaat qila olmaysiz.

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

# =============================================================================
# =============================================================================
# # Python - Tuple elementlariga kirish
# Tuple elementlariga kirish
# Kvadrat qavs ichidagi indeks raqamiga murojaat qilib, 
#qo'shma elementlarga kirishingiz mumkin:

# Misol
# To'plamdagi ikkinchi elementni chop eting:

# =============================================================================
# # thistuple = ("apple", "banana", "cherry")
# # print(thistuple[1])
# =============================================================================
# Eslatma: birinchi element 0 indeksiga ega.

# Salbiy indekslash
# Salbiy indekslash oxiridan boshlanishini bildiradi.

# -1oxirgi elementni, -2ikkinchi oxirgi elementni va boshqalarni bildiradi.

# Misol
# To'plamning oxirgi elementini chop eting:

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])
# Indekslar diapazoni
# Siz indekslar diapazonini qaerdan boshlash va tugatish kerakligini ko'rsatib belgilashingiz mumkin.

# Diapazonni belgilashda, qaytish qiymati ko'rsatilgan elementlar bilan yangi to'plam bo'ladi.

# Misol
# Uchinchi, to'rtinchi va beshinchi elementlarni qaytaring:

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])
# Eslatma: Qidiruv 2 -indeksdan boshlanadi (shu jumladan) 
#va 5 -indeks bilan tugaydi (shu jumladan emas).

# Esda tutingki, birinchi element 0 indeksiga ega.

# Boshlanish qiymatini qoldirib, diapazon birinchi banddan boshlanadi:

# Misol
# Bu misol elementlarni "kivi" dan boshidan qaytaradi, lekin o'z ichiga olmaydi:

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])
# Yakuniy qiymatni qoldirib, diapazon ro'yxatning oxirigacha davom etadi:

# Misol
# Bu misol elementlarni "gilos" dan oxirigacha qaytaradi:

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:])
# Salbiy indekslar diapazoni
# Qidiruvni oxiridan boshlab boshlamoqchi bo'lsangiz, salbiy indekslarni ko'rsating:

# Misol
# Bu misol -4 indeksidagi elementlarni -1 indeksiga qaytaradi.

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])
# Ob'ekt mavjudligini tekshiring
# To'plamda ko'rsatilgan element mavjudligini aniqlash uchun inkalit so'zdan foydalaning :

# Misol
# To'plamda "olma" mavjudligini tekshiring:

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")
# # =============================================================================
# #   
# # =============================================================================
# Python - Tuples -ni yangilang
# Tuplar o'zgarmasdir, demak, katakchani yaratgandan 
#so'ng uni o'zgartirish, qo'shish yoki o'chirish mumkin emas.

# Ammo ba'zi echimlar mavjud.

# Tuple qiymatlarini o'zgartirish
# Tuple yaratilgach, siz uning qiymatlarini o'zgartira olmaysiz. 
# Tuplar o'zgarmas yoki o'zgarmasdir .

# Ammo vaqtinchalik echim bor. Siz qo'shimchani ro'yxatga o'zgartirishingiz,
#  ro'yxatni o'zgartirishingiz va ro'yxatni qaytadan qo'shishingiz mumkin.

# Misol
# O'zgartirish uchun to'plamni ro'yxatga aylantiring:

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)
# Ob'ektlarni qo'shish
# Tuplar o'zgarmas bo'lgani uchun ularni o'rnatish append()usuli yo'q, 
# lekin elementlarni qo'shish uchun boshqa usullar mavjud.

# 1. Ro'yxatga aylantirish : To'plamni o'zgartirishning vaqtinchalik echimi singari, 
# siz ham uni ro'yxatga aylantira olasiz, elementlaringizni qo'shib, uni yana qo'shishingiz mumkin.

# Misol
# To'plamni ro'yxatga aylantiring, "apelsin" qo'shing va uni yana to'plamga aylantiring:

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)
# 2. To'plamga qo'shimchani qo'shing . Siz qo'shimchalarga qo'shimchalarni qo'shishingiz mumkin, 
# shuning uchun agar siz bitta elementni (yoki ko'pini) qo'shmoqchi bo'lsangiz, elementlar 
#                                         bilan yangi qo'shma yarating va mavjud to'plamga qo'shing:

# Misol
# "To'q sariq" qiymatiga ega yangi to'plamni yarating va unga qo'shiling:

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)
# E'tibor bering: faqat bitta elementdan iborat katakchani yaratishda, elementdan keyin vergul 
# qo'yishni unutmang, aks holda u birikma sifatida aniqlanmaydi.

# Elementlarni o'chirish
# E'tibor bering: siz qo'shimchadagi elementlarni o'chira olmaysiz.

# Tuplar o'zgarmas , shuning uchun siz undan elementlarni olib tashlay olmaysiz, lekin biz elementlarni
#  o'zgartirish va qo'shish uchun ishlatilgan vaqtinchalik echimdan foydalanishingiz mumkin:

# Misol
# To'plamni ro'yxatga aylantiring, "olma" ni olib tashlang va uni yana to'plamga aylantiring:

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)
# Yoki qo'shiqni butunlay o'chirib tashlashingiz mumkin:

# Misol
# delKalit so'z to'liq shamlardan o'chirishingiz mumkin:

# thistuple = ("apple", "banana", "cherry")
# del thistuple[1]
# print(thistuple) #this will raise an error because the tuple no longer exists


# # =============================================================================
# # 
# # =============================================================================
# Python - Tupllarni ochish
# Tuplni ochish
# Tuple yaratganimizda, biz odatda unga qiymatlar belgilaymiz. 
#Bunga "o'rash" to'plami deyiladi:

# Misol
# To'plamni qadoqlash:

# fruits = ("apple", "banana", "cherry")
# Ammo, Python -da, biz qiymatlarni o'zgaruvchiga qaytarishga ruxsat beramiz. 
#Bu "ochish" deb nomlanadi:

# Misol
# To'plamni ochish:

# fruits = ("apple", "banana", "cherry")

# (green, yellow, red,) = fruits

# print(green)
# print(yellow)
# print(red)
#print(brown)
# Eslatma: O'zgaruvchilar soni to'plamdagi qiymatlar 
#soniga mos kelishi kerak, 
# agar bo'lmasa, qolgan qiymatlarni ro'yxat 
#sifatida yig'ish uchun yulduzchadan foydalanish kerak.


# Misol
# Qolgan qiymatlarni "qizil" deb nomlangan ro'yxat sifatida belgilang:

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)
# Agar yulduzcha boshqa o'zgarmaydigan nomga qo'shilsa, 
#Python o'zgarmaydiganga 
# qolgan qiymatlar soni qolgan 
#o'zgaruvchilar soniga mos kelmaguncha qiymatlar beradi.

# Misol
# "Tropik" o'zgaruvchiga qiymatlar ro'yxatini qo'shing:

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)



# # =============================================================================
# # 
# # =============================================================================
# Python - Loop Tuples
# Tuple orqali aylanish
# Loop yordamida elementlarni birlashtira olasiz for.

# Misol
# Ob'ektlarni takrorlang va qiymatlarni chop eting:

# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)
# Python For Loops bobida forlooplar haqida ko'proq bilib oling .

# Indeks raqamlari orqali aylanish
# Siz shuningdek indeks raqamiga murojaat qilib, qo'shma 
#elementlarni aylanib o'tishingiz mumkin.

# Tegishli takrorlanuvchi yaratish uchun 
#range()va len()funktsiyalaridan foydalaning .

# Misol
# Barcha elementlarni indeks raqamiga qarab chop eting:

# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])
# Vaqt halqasidan foydalanish
# Ro'yxat elementlarini whilepastadir yordamida aylantirishingiz mumkin.

# len()To'plamning uzunligini aniqlash uchun funktsiyadan foydalaning ,
# so'ngra 0dan boshlang va indekslariga murojaat qilib, 
#elementlar bo'ylab harakatlaning.

# Har bir takrorlashdan keyin indeksni 1 ga oshirishni unutmang.

# Misol
# Barcha whileindeks raqamlaridan o'tish uchun pastadir 
#yordamida barcha elementlarni chop eting:

# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1
# Python while Loops bobida whilelooplar haqida ko'proq bilib oling .


# # =============================================================================
# # 
# # =============================================================================
# Python - Tupllarga qo'shiling
# Ikki guruhga qo'shiling
# Ikki yoki undan ko'p guruhlarga qo'shilish uchun 
#siz + operatordan foydalanishingiz mumkin :

# Misol
# Ikki guruhga qo'shiling:

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)
# Tuplarni ko'paytirish
# Agar siz tupl tarkibini bir necha marta ko'paytirmoqchi bo'lsangiz,
#  * operatordan foydalanishingiz mumkin :

# Misol
# Mevalarni 2 ga ko'paytiring:

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 50

# print(mytuple)


# # =============================================================================
# # 7
# # =============================================================================

# Python - ulash usullari
# Birlashtirish usullari
# Python-da ikkita ichki o'rnatilgan usul mavjud, siz ularni katakchalarda ishlatishingiz mumkin.

# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found














# # =============================================================================
# # =============================================================================

# Python - sozlash elementlariga kirish
# Kirish elementlari
# Indeks yoki kalitga murojaat qilib, to'plamdagi elementlarga kira olmaysiz.

# Lekin siz kalit elementni ishlatib, to'plam elementlarini pastadir 
# yordamida aylantira olasiz for yoki to'plamda ko'rsatilgan qiymat mavjudligini so'rashingiz mumkin in.

# Misol
# To'plamni aylantiring va qiymatlarni chop eting:

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)
# Misol
# To'plamda "banan" mavjudligini tekshiring:

# thisset = {"apple", "banana", "cherry"}

# print("banana" in thisset)

# Ob'ektlarni o'zgartirish
# To'plam yaratilgach, siz uning elementlarini o'zgartira olmaysiz, 
# lekin siz yangi elementlarni qo'shishingiz mumkin.


# # =============================================================================
# # 
# # =============================================================================
# Python - O'rnatish elementlarini qo'shing
# Ob'ektlarni qo'shish
# To'plam yaratilgach, siz uning elementlarini o'zgartira olmaysiz, lekin siz yangi elementlarni qo'shishingiz mumkin.

# To'plamga bitta element qo'shish uchun add() usuldan foydalaning .

# Misol
# add() Usul yordamida to'plamga element qo'shing :

# thisset = {"apple", "banana", "cherry"}

# thisset.add("orange")

# print(thisset)
# To'plamlarni qo'shish
# Boshqa to'plamdagi elementlarni 
#joriy to'plamga qo'shish uchun update() usuldan foydalaning .

# Misol
# Dan elementlarni qo'shish tropicalichiga thisset:

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)
# Iterable ni qo'shing
# Ob'ekt update()usuli majmuini bo'lishi shart emas,
#  u (dizilerini ro'yxati, lug'atlar va boshqalar)
# har qanday iterable ob'ekt bo'lishi mumkin.

# Misol
# To'plamga ro'yxat elementlarini qo'shing:

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]

# thisset.update(mylist)

# print(thisset)

# # =============================================================================
# # 
# # =============================================================================
# Python - O'rnatilgan elementlarni o'chirish
# Elementni o'chirish
# To'plamdagi elementni olib tashlash uchun remove(), yoki discard()usulini ishlating .

# Misol
# "Banana" ni quyidagi remove() usul bilan olib tashlang :

# thisset = {"apple", "banana", "cherry"}

# thisset.remove("banana")

# print(thisset)
# Eslatma: Agar o'chiriladigan element bo'lmasa,
# remove()xato paydo bo'ladi.

# Misol
# "Banana" ni quyidagi discard() usul bilan olib tashlang :

# thisset = {"apple", "banana", "cherry"}

# thisset.discard("banana")

# print(thisset)
# Eslatma: remove element mavjud bo'lmasa, 
#discard()bo'ladi EMAS xato oshirish.

# Siz pop()elementni o'chirish uchun ham usuldan foydalanishingiz mumkin ,
# lekin bu usul oxirgi elementni olib tashlaydi . Shuni esda tutingki, 
# to'plamlar tartibsiz, shuning uchun siz qaysi element o'chirilishini bilmay qolasiz.

# pop()Usulning qaytish qiymati o'chirilgan element hisoblanadi.

# Misol
# pop() Usul yordamida oxirgi elementni olib tashlang :

# thisset = {"apple", "banana", "cherry"}

# x = thisset.pop()

# print(x)

# print(thisset)
# Eslatma: silsilasini og'riqqa , shuning uchun foydalanish paytida pop()usuli, 
# siz olib oladi, deb qaysi element bilmayman.

# Misol
# clear() Usuli majmuini bo'shatmoqda:

# thisset = {"apple", "banana", "cherry"}

# thisset.clear()

# print(thisset)
# Misol
# delKalit so'z butunlay majmuini o'chiradi:

# thisset = {"apple", "banana", "cherry"}
# print(thisset)
# del thisset




# # =============================================================================
# # 
# # =============================================================================

# Python - Loop to'plamlari
# Loop elementlari
# Belgilangan elementlarni for pastadir 
#yordamida aylantirishingiz mumkin:

# Misol
# To'plamni aylantiring va qiymatlarni chop eting:

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)
  
# # =============================================================================
# # 
# # =============================================================================
# Python - to'plamlarga qo'shilish
# Ikki to'plamga qo'shilish
# Python -da ikki yoki undan ortiq to'plamga qo'shilishning bir necha yo'li mavjud.

# Siz foydalanishingiz mumkin union()ikkala fotoalbomlarda barcha narsalarni 
# o'z ichiga olgan yangi bir qator yoki qaytib usuli update()usuli deb yana bir to'plamining uchlari barcha mahsulot:

# Misol
# union()Usuli, ham fotoalbomlarda 
#barcha unsurlar bilan yangi bir qator qaytaradi:

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set3 = set2.union(set1)
# print(set3)
# Misol
# update()Usuli set1 ichiga set2 yilda mahsulot qo'shimchalar:

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set1.update(set2)
# print(set1)
# Eslatma: ikkalasi ham union()va update() 
#takrorlanadigan elementlarni istisno qiladi.

# FAQAT dublikatlarni saqlang
# intersection_update()Usuli, ham 
#fotoalbomlarda mavjud faqat mahsulot davom etadi.

# Misol
# Ikkala to'plamda ham mavjud elementlarni saqlang xva o'rnating y:

# x = {"apple", "banana", "cherry"}
# y = {"google",'google', "microsoft", "apple"}

# x.intersection_update(y)

# print(x)
# intersection()Usul qaytadi yangi faqat 
#har ikki setda mavjud ma'lumotlar o'z ichiga oladi, majmuini.

# Misol
# Ikkala to'plamda ham mavjud bo'lgan 
#elementlarni o'z ichiga olgan to'plamni qaytaring xva o'rnating y:

# x = {"google", "banana", "cherry"}
# y = {"google", "microsoft", "google"}

# z = x.intersection(y)

# print(z)
# Hammasini saqlang, lekin nusxalarini emas
# symmetric_difference_update()Usuli, ham fotoalbomlarda mavjud emas faqat elementlarni davom etadi.

# Misol
# Ikkala to'plamda ham bo'lmagan narsalarni saqlang:

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.symmetric_difference_update(y)

# print(x)
# symmetric_difference()Usuli, ham fotoalbomlarda mavjud emas faqat elementlarni o'z ichiga olgan yangi bir qator, qaytadi.

# Misol
# Ikkala to'plamdagi barcha elementlarni o'z ichiga olgan to'plamni qaytaring, faqat ikkalasida ham mavjud:

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.symmetric_difference(y)

# print(z)

# # =============================================================================
# # 
# # =============================================================================
# Python - usullarni sozlash
# Usullarni o'rnatish
# Python-da siz ishlatishingiz mumkin bo'lgan o'rnatilgan usullar to'plami mavjud.

# Method	Description
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others




