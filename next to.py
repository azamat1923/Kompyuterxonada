# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 08:51:39 2021

@author: Rafiqov Abulqosim
"""

# # Python Lambda
# # Lambda funktsiyasi - bu kichik anonim funksiya.

# # Lambda funktsiyasi har qanday argumentlarni 
# # qabul qilishi mumkin, lekin faqat bitta ifodaga ega bo'lishi mumkin.

# # Sintaksis
# # lambda arguments : expression
# # Ifoda bajariladi va natija qaytariladi:

# # Misol
# # Argumentga 10 qo'shing ava natijani qaytaring:

# x = lambda a :a + 10
# print(x(10))
# # Lambda funktsiyalari har qanday argumentlarni qabul qilishi mumkin:

# # Misol
# # Argumentni argument a bilan ko'paytiring b va natijani qaytaring:

# x = lambda a, b : a * b
# print(x(5, 6))
# # Misol
#Summarize argument a, b, and c and return the result:
# # Özetleme argument a, bva cva natija qaytadi:

# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))
# # Nima uchun Lambda funktsiyalaridan foydalanish kerak?
# # Lambdaning kuchi boshqa funktsiyadagi 
# # anonim funksiya sifatida ishlatilganda yaxshiroq namoyon bo'ladi.

# # Aytaylik, sizda bitta argumentga ega 
# # bo'lgan funktsiya ta'rifi bor va bu argument noma'lum raqamga ko'paytiriladi:

# def myfunc(n):
#   return lambda a : a * n
# # Siz yuborgan raqamni har doim ikki barobar
# #  ko'paytiradigan funktsiyani 
#yaratish uchun ushbu funktsiya ta'rifidan foydalaning:

# # Misol
# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))
# # Yoki siz yuborgan raqamni har doim uch baravar 
# # ko'paytiradigan funktsiyani yaratish
# uchun xuddi shu funktsiya ta'rifidan foydalaning :

# # Misol
# def myfunc(n):
#   return lambda a : a * n

# mytripler = myfunc(3)

# print(mytripler(11))
# # Yoki bitta dasturda ikkala
# funktsiyani bajarish uchun bir xil funktsiya ta'rifidan foydalaning:

# # Misol
# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(15))
# =============================================================================
# 
# =============================================================================
 #Python massivlari
# Eslatma: Pythonda massivlar uchun o'rnatilgan qo'llab-quvvatlash yo'q,
#  lekin uning o'rniga Python ro'yxatlari ishlatilishi mumkin.

# Massivlar
# Eslatma: Bu sahifada LISTS -ni ARRAYS sifatida qanday ishlatish kerakligi
#  ko'rsatilgan, lekin Python -da massivlar bilan 
#ishlash uchun NumPy kutubxonasi kabi kutubxonani import qilish kerak bo'ladi .

# Massivlar bitta o'zgaruvchida bir nechta qiymatlarni 
#saqlash uchun ishlatiladi:

# Misol
# Avtomobil nomlarini o'z ichiga olgan qator yarating:

# cars = ["Ford", "Volvo", "BMW"]
# Array nima?
# Massiv - bu bir vaqtning o'zida bir nechta qiymatni o'z ichiga 
#oladigan maxsus o'zgaruvchi.

# Agar sizda narsalar ro'yxati bo'lsa (masalan, avtomobil nomlari ro'yxati), 
# mashinalarni bitta o'zgaruvchiga saqlash quyidagicha ko'rinishi mumkin:

# car1 = "Ford"
# car2 = "Volvo"
# car3 = "BMW"
# Ammo, agar siz mashinalarni aylanib o'tib,
# o'ziga xosini topmoqchi bo'lsangiz? Va agar 
#sizda 3 ta emas, balki 300 ta mashina bo'lsa -chi?

# Yechim - bu massiv!

# Massiv bitta nom ostida ko'plab qiymatlarni 
# ushlab turishi mumkin va siz indeks raqamiga
# murojaat qilib, qiymatlarga kirishingiz mumkin.

# Massiv elementlariga kirish
# Siz indeks raqamiga murojaat qilib, massiv elementiga murojaat qilasiz .

# Misol
# Birinchi qator elementining qiymatini oling:

# x = cars[0]
# Misol
# Birinchi qator elementining qiymatini o'zgartiring:

# cars[0] = "Toyota"
# print(cars)
# Massivning uzunligi
# Massiv len()uzunligini qaytarish uchun usuldan
# foydalaning (massivdagi elementlar soni).

# Misol
# Jadvaldagi elementlar sonini qaytaring cars :

# x = len(cars)
# print(cars)
# Eslatma: qatorning uzunligi har doim eng yuqori indeksdan bir baravar ko'p.


# Array elementlarining aylanishi
# Siz for inmassivning barcha elementlarini aylanib o'tish uchun pastadirdan 
#foydalanishingiz mumkin .

# Misol
# Qatordagi har bir elementni chop carseting:

# for x in cars:
#   print(x)
# Array elementlarini qo'shish
# Siz append()massivga element qo'shish uchun usuldan foydalanishingiz mumkin .

# Misol
# Massivga yana bitta element qo'shing cars:

# cars.append("Honda")
# print(cars)
# Massiv elementlarini olib tashlash
# Siz pop()elementni massivdan olib tashlash uchun foydalanishingiz mumkin .

# Misol
# Massivning ikkinchi elementini o'chirib tashlang cars:

# cars.pop(1)
# print(cars)
# Siz remove()elementni massivdan olib tashlash uchun ham foydalanishingiz mumkin .

# Misol
# "Volvo" qiymatiga ega bo'lgan elementni o'chirib tashlang:

# cars.remove("Volvo")
# print(cars)
# Eslatma: ro'yxatning remove()usuli faqat 
# ko'rsatilgan qiymatning birinchi marta paydo bo'lishini olib tashlaydi.

# Array usullari
# Python-da ro'yxatlar/massivlarda foydalanishingiz mumkin bo'lgan o'rnatilgan usullar to'plami mavjud.

# Method  Description
# append()  Adds an element at the end of the list
# clear()  Removes all the elements from the list
# copy()  Returns a copy of the list
# count()  Returns the number of elements with the specified value
# extend()  Add the elements of a list (or any iterable), to the end of the current list
# index()  Returns the index of the first element with the specified value
# insert()  Adds an element at the specified position
# pop()  Removes the element at the specified position
# remove()  Removes the first item with the specified value
# reverse()  Reverses the order of the list
# sort()  Sorts the list
# Eslatma: Pythonda massivlar uchun o'rnatilgan qo'llab-quvvatlash yo'q, 
# lekin uning o'rniga Python ro'yxatlari ishlatilishi mumkin.

# =============================================================================
# # 
# =============================================================================
#Python sinflari va ob'ektlari
# Python sinflari/ob'ektlari
# Python - bu ob'ektga yo'naltirilgan dasturlash tili.

# Python -dagi deyarli hamma narsa ob'ekt va uning xususiyatlari va usullari bilan.

# Sinf ob'ektlar konstruktoriga yoki ob'ektlarni yaratish uchun "rejaga" o'xshaydi.

# Sinf yaratish
# Sinf yaratish uchun kalit so'zdan foydalaning class:

# Misol
# MyClass nomli, x nomli xususiyat yarating.

# class MyClass:
#   x = 5
# Ob'ekt yaratish
# Endi biz ob'ektlarni yaratish uchun MyClass nomli sinfdan foydalanishimiz mumkin:

# Misol
# P1 nomli ob'ekt yarating va x qiymatini chop eting:

# p1 = MyClass()
# print(p1.x)
# __Init __ () funktsiyasi
# Yuqoridagi misollar sinflar va ob'ektlar eng oddiy shaklda bo'lib,
#  haqiqiy hayotda qo'llanilmaydi.

# Sinflarning ma'nosini tushunish uchun biz o'rnatilgan __init __ () 
# funktsiyasini tushunishimiz kerak.

# Barcha sinflarda __init __ () deb nomlangan funksiya mavjud bo'lib,
#  u har doim sinf boshlanganda bajariladi.

# __Init __ () funktsiyasidan foydalanib, ob'ekt xususiyatlariga yoki
#  ob'ekt yaratilganda bajarilishi kerak bo'lgan boshqa operatsiyalarga qiymatlarni belgilang:

# Misol
# Shaxs nomli sinf yarating, __init __ () funktsiyasidan foydalanib ism va yoshga qiymat bering:

# class Person:
#   def __init__(self, name, age,year):
#     self.name = name          #''ism':'Abulqosim'
#     self.age = age
#     self.year=year

# p1 = Person("John", 36,2000)

# print(p1.name)
# print(p1.age)
# print(p1.year)
# Eslatma:__init__() funktsiyasi sinf 
#yangi ob'ekt yaratish uchun ishlatiladi avtomatik ravishda har safar deyiladi.


# Ob'ekt usullari
# Ob'ektlarda usullar ham bo'lishi mumkin.
# Ob'ektlardagi usullar - bu ob'ektga tegishli funktsiyalar.

# Keling, Person sinfida usul yarataylik:

# Misol
# Tabriknomani chop etadigan funktsiyani joylashtiring va uni p1 ob'ektida bajaring:

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)
#     print("Hello i am  " + str(self.age))

# p1 = Person("John", 36)
# p1.myfunc()
# Eslatma:self parametr sinf joriy misol uchun, bir Malumot bo'lib, 
# sinfga tegishli kirish o'zgaruvchilar uchun ishlatiladi.

# O'z -o'zidan parametr
# selfParametr sinf joriy misol uchun, bir Malumot bo'lib, 
# sinfga tegishli kirish o'zgaruvchilar uchun ishlatiladi.

# Uni selfnomlash shart emas, uni xohlaganingizcha chaqirishingiz mumkin,
#  lekin u sinfdagi har qanday funksiyaning birinchi parametri bo'lishi kerak:

# Misol
# O'z o'rniga mysillyobject va abc so'zlarini ishlating :

# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()
# Ob'ekt xususiyatlarini o'zgartirish
# Siz ob'ektlarning xususiyatlarini o'zgartirishingiz mumkin:

# Misol
# P1 yoshini 40 ga sozlang:

# p1.age = 40
# Ob'ekt xususiyatlarini o'chirish
# delKalit so'z yordamida ob'ektlarning xususiyatlarini o'chirib tashlashingiz mumkin :

# Misol
# P1 ob'ektidan yosh xususiyatini o'chirib tashlang:

# del p1.age
# Ob'ektlarni o'chirish
# delKalit so'z yordamida ob'ektlarni o'chirib tashlashingiz mumkin :

# Misol
# P1 ob'ektini o'chirib tashlang:

# del p1
# O'tish bayonoti
# classta'riflar bo'sh bo'lishi mumkin emas, lekin agar sizda biron sababga 
# ko'ra classmazmuni bo'lmagan ta'rif bo'lsa pass, xatoga yo'l qo'ymaslik uchun bayonotga qo'ying .

# Misol
# class Person:
#   pass

# =============================================================================
# 
# =============================================================================
# Python Inheritance
# Python merosi
# Python merosi
# Vorislik bizga boshqa sinfning barcha usullari va xususiyatlarini 
# meros qilib oladigan sinfni aniqlash imkonini beradi.

# Ota -ona sinfi - bu meros bo'lib o'tadigan sinf, uni asosiy sinf deb ham atashadi.

# Bola sinfi - bu boshqa sinfdan meros bo'lib o'tadigan sinf,
#  uni boshqa sinf deb ham atashadi.

# Ota -ona sinfini yarating
# Har qanday sinf ota -ona sinf bo'lishi mumkin, shuning uchun 
# sintaksis boshqa sinf yaratish bilan bir xil bo'ladi:

# Misol
# Xususiyatlari va nomi Personbilan sinf yarating va usuli:firstnamelastnameprintname

# class Student:
#   def init(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)
# x = Person("John", "Doe")
# x.printname()
# #Use the Person class to create an object, and then execute the printname method:


# Bolalar sinfini yarating
# Boshqa sinfdan funktsiyalarni meros qilib oladigan sinf yaratish 
# uchun, ota -ona sinfini bola sinfini yaratishda parametr sifatida yuboring:

# Misol
# StudentSinfdan xususiyatlar va usullarni meros qilib oladigan nomli sinf yarating Person:

# class Student(Person):
#   pass
# Eslatma:pass Agar sinfga boshqa xususiyatlar yoki usullarni
#  qo'shishni xohlamasangiz , kalit so'zdan foydalaning .

# Endi Talabalar sinfi Person klassi bilan bir xil xususiyat va usullarga ega.

# Misol
# StudentOb'ekt yaratish uchun sinfdan foydalaning va keyin 
# printnameusulni bajaring:

# x = Student("Mike", "Olsen")
# x.printname()
# Init  () funktsiyasini qo'shing
# Hozircha biz ota -onadan xususiyatlari va usullarini meros qilib 
# oladigan bolalar sinfini yaratdik.

# Biz init()funktsiyani bolalar sinfiga qo'shmoqchimiz ( passkalit so'z o'rniga ).

# Eslatma:init() funktsiyasi sinf yangi ob'ekt yaratish 
# uchun ishlatiladi avtomatik ravishda har safar deyiladi.

# Misol
# init()Funktsiyani Studentsinfga qo'shing :

# class Student(Person):
#   def init(self, fname, lname):
#     #add properties etc.
# Agar siz init()funktsiyani qo'shsangiz, bola sinfi endi
#  ota -onaning init()funktsiyasini meros qilib olmaydi.

# Eslatma: bolaning init() vazifasi bekor qiladi ota-ona merosi init()funktsiyasi.

# Ota -ona init() funktsiyasining merosxo'rligini saqlab qolish
#  uchun ota -ona funktsiyasiga qo'ng'iroq qo'shing init():

# Misol
# class Student(Person):
#   def init(self, fname, lname):
#     Person.init(self, fname, lname)
# Endi biz init  () funktsiyasini muvaffaqiyatli qo'shdik va 
# ota -ona sinfining merosxo'rligini saqlab qoldik va biz funksiyaga 
#funksionallikni qo'shishga tayyormiz init().

# Super () funktsiyasidan foydalaning
# Python shuningdek super(), bola sinfining barcha usullari va 
# xususiyatlarini ota -onasidan meros qilib oladigan funktsiyaga ega:

# Misol
# class Student(Person):
#   def init(self, fname, lname):
#     super().init(fname, lname)
# super()Funktsiyadan foydalanib , siz asosiy element nomini 
# ishlatishingiz shart emas, u avtomatik ravishda usul va xususiyatlarni ota -onasidan meros qilib oladi.

# Xususiyatlarni qo'shish
# Misol
# Deb nomlangan mulkni qo'shish graduationyearuchun Studentsinf:

# class Student(Person):
#   def init(self, fname, lname):
#     super().init(fname, lname)
#     self.graduationyear = 2019
# Quyidagi misolda, yil 2019o'zgaruvchan bo'lishi va 
# Studento'quvchilar ob'ektlarini yaratishda sinfga o'tkazilishi kerak .
#  Buning uchun init  () funktsiyasiga boshqa parametr qo'shing:

# Misol
# yearParametr qo'shing va ob'ektlarni yaratishda to'g'ri yilni o'tkazing:

# class Student(Person):
#   def init(self, fname, lname, year):
#     super().init(fname, lname)
#     self.graduationyear = year

# x = Student("Mike", "Olsen", 2019)
# Usullarni qo'shish
# Misol
# Deb nomlangan usul qo'shish welcomeuchun Studentsinf:

# class Student(Person):
#   def init(self, fname, lname, year):
#     super().init(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, 
#           "to the class of", self.graduationyear)
# Agar siz ota -ona sinfidagi funktsiya bilan 
# bir xil nomdagi sinfni qo'shsangiz, ota -ona usulining merosxo'rligi bekor qilinadi.

# =============================================================================
# 
# =============================================================================
# Python Iterators

# Python takrorlagichlari
# Python takrorlagichlari
# Iterator - bu hisoblanadigan qiymatlar sonini o'z ichiga olgan ob'ekt.

# Iterator - bu takrorlanishi mumkin bo'lgan ob'ekt, 
# ya'ni siz barcha qiymatlarni aylanib o'tishingiz mumkin.

# Texnik jihatdan, Pythonda iterator - bu usullar __iter__() 
# va usullardan tashkil topgan iterator protokolini amalga oshiruvchi ob'ekt __next__().

# Iterator va boshqalar
# Ro'yxatlar, katakchalar, lug'atlar va to'plamlar - bu takrorlanadigan
#  ob'ektlar. Bu takrorlanadigan konteynerlar , siz iteratorni olishingiz mumkin.

# Bu ob'ektlarning barchasida iter()iteratorni olish uchun ishlatiladigan usul mavjud:

# Misol
# Qatordan iteratorni qaytaring va har bir qiymatni chop eting:

# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# Hatto satrlar ham takrorlanadigan ob'ektlar bo'lib, iteratorni qaytarishi mumkin:

# Misol
# Stringlar, shuningdek, belgilar ketma -ketligini o'z 
# ichiga olgan takrorlanadigan ob'ektlardir:

# mystr = "bananan"
# myit = iter(mystr)#for x range('banana'):
#                            #print(x)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
#print(next(myit))
# Iterator orqali aylanish
# Biz fortakrorlanadigan ob'ekt orqali takrorlash uchun pastadirdan ham foydalanishimiz mumkin :

# Misol
# To'plam qiymatlarini takrorlang:

# mytuple = ("apple", "banana", "cherry")

# for x in mytuple:
#   print(x)
# Misol
# String belgilarini takrorlang:

# mystr = "banana"

# for x in mystr:
#   print(x)
# forHalqa aslida iterator obyektlari tashkil qiladi va har bir ko'chadan uchun keyingi () usuli amalga oshiradi.

# Iterator yaratish
# Ob'ektni/sinfni iterator sifatida yaratish uchun 
# siz usullarni __iter__()va __next__()ob'ektingizga amal qilishingiz kerak.

# Python sinflari/ob'ektlari bobida bilib olganingizdek ,
#  barcha sinflarda funktsiya mavjud bo'lib __init__(), bu sizga ob'ekt yaratilayotganda boshlang'ichni sozlash imkonini beradi.

# __iter__()Usuli shunga o'xshash bajaradi, siz (boshlash
#  va boshqalar) operatsiyalarni bajarish mumkin, lekin har doim iterator ob'ektini o'zi qaytib kerak.

# __next__()Usuli ham siz operatsiyalarini bajarish imkonini beradi,
#  va ketma-ketlikda keyingi elementni qaytarib kerak.

# Misol
# 1dan boshlab raqamlarni qaytaradigan iterator yarating va
#  har bir ketma -ketlik bittaga ko'payadi (1,2,3,4,5 va boshqalarni qaytarish):

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))# To'xtatish
# Agar keyingi () so'zlari etarli bo'lsa yoki u forpastadirda ishlatilsa, yuqoridagi misol abadiy davom etadi .

# Yinelemenin abadiy davom etmasligi uchun, biz StopIterationbayonotdan foydalanishimiz mumkin .

# Yilda __next__()qaytarish marta belgilangan qator amalga oshiriladi, 
# agar usuli, biz xato ko'tarish uchun bekor shartni kiritish mumkin:

# Misol
# 20 ta takrorlashdan keyin to'xtating:

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#       print(x)
# =============================================================================
# 
# =============================================================================
 #Python Scope

# O'zgaruvchi faqat yaratilgan mintaqaning o'zida mavjud. Bunga scope deyiladi .

# Mahalliy local qamrov
# Funktsiya ichida yaratilgan o'zgaruvchi ushbu 
# funktsiyaning mahalliy doirasiga tegishli va uni faqat shu funktsiya ichida ishlatish mumkin.

# Misol
# Funktsiya ichida yaratilgan o'zgaruvchi ushbu funktsiya ichida mavjud:

# def myfunc():
#   x = 300
#   print(x)

# myfunc()
# Ichki funktsiya
# Yuqoridagi misolda tushuntirilgandek, o'zgaruvchi xfunktsiyadan 
# tashqarida mavjud emas, lekin u funksiya ichidagi har qanday funksiya uchun mavjud:

# Misol
# Mahalliy o'zgaruvchiga funktsiyadagi funktsiyadan kirish mumkin:

# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()

# myfunc()
# Global qamrov
# Python kodining asosiy 
#qismida yaratilgan o'zgaruvchi global o'zgaruvchidir va global miqyosga kiradi.

# Global o'zgaruvchilar global va mahalliy har qanday doirada mavjud.

# Misol
# Funktsiyadan tashqarida yaratilgan o'zgaruvchi globaldir va hamma uni ishlatishi mumkin:

# x = 300

# def myfunc():
#   print(x)

# myfunc()

#print(x)
# O'zgaruvchilarni nomlash
# Agar siz funktsiya ichida va tashqarisida bir xil o'zgaruvchi nomi bilan ishlasangiz, 
# Python ularni ikkita alohida o'zgaruvchi sifatida ko'rib chiqadi,
#  ulardan biri global miqyosda (funktsiyadan tashqarida)
#va ikkinchisi mahalliy doirada (funktsiya ichida) mavjud:

# Misol
# Funktsiya mahalliyni x, so'ngra kod globalni chop etadi x:

# x = 300

# def myfunc():
#   x = 200
#   print(x)

# myfunc()

# print(x)
# Global kalit so'z
# Agar siz global o'zgaruvchini yaratishingiz kerak bo'lsa, lekin mahalliy
#  doirada qolsangiz, globalkalit so'zdan foydalanishingiz mumkin .

# globalKalit so'z o'zgaruvchan global qiladi.

# Misol
# Agar siz globalkalit so'zdan foydalansangiz, o'zgaruvchi global miqyosga tegishli:

# def myfunc():
#   global x
#   x = 300

# myfunc()

# print(x)
# globalAgar funktsiya ichida global o'zgaruvchiga o'zgartirish kiritmoqchi
#  bo'lsangiz , kalit so'zdan foydalaning .

# Misol
# Funktsiya ichida global o'zgaruvchining qiymatini o'zgartirish uchun 
# globalkalit so'z yordamida o'zgaruvchiga murojaat qiling :

# x = 300

# def myfunc():
#   global x
#   x = 200

# myfunc()

# print(x)

# =============================================================================
# 
# =============================================================================
# Python modullari
# Modul nima?
# Modulni kod kutubxonasi bilan bir xil deb hisoblang.

# Ilovangizga kiritmoqchi bo'lgan funktsiyalar to'plamini o'z ichiga olgan fayl.

# Modul yaratish
# Modulni yaratish uchun kerakli kodni fayl kengaytmasi bo'lgan faylga saqlang .py:

# Misol
# Nomli faylga ushbu kodni saqlang mymodule.py

# def greeting(name):
#   print("Hello, " + name)
# Moduldan foydalaning
# Endi biz yangi modulni quyidagi iboradan foydalanib ishlatishimiz mumkin import:

# Misol
# Mymodule nomli modulni import qiling va tabriklash funktsiyasini chaqiring:

# import mymodule


# Eslatma: Moduldan funktsiyani ishlatganda,
#sintaksisdan foydalaning: module_name.function_name .

# Moduldagi o'zgaruvchilar
# Modul yuqorida tavsiflangan funktsiyalarni o'z ichiga olishi mumkin,
#  lekin har xil turdagi o'zgaruvchilar (massivlar, lug'atlar, ob'ektlar va boshqalar):

# Misol
# Ushbu kodni faylga saqlang mymodule.py
# import mymodule
# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }
# a = mymodule.person1["age"]
# print(a)

# Misol
# Mymodule nomli modulni import qiling va person1 lug'atiga kiring:


# mymodule.greeting("Jonathan")


# Modulga nom berish
# Siz xohlagan modul faylini nomlashingiz mumkin, 
# lekin u fayl kengaytmasiga ega bo'lishi kerak .py

# Modulni qayta nomlash
# Modulni import qilganingizda askalit so'z yordamida taxallus yaratishingiz mumkin :

# Misol
# Uchun boshqa nom yaratish mymodulechaqirdi mx:

# import mymodule as mx

# a = mx.person1["age"]
# print(a)
# O'rnatilgan modullar
# Python-da bir nechta o'rnatilgan modullar mavjud,
# ularni xohlagan vaqtda import qilishingiz mumkin.

# Misol
# platformModulni import qilish va ishlatish :

# import platform

# x = platform.system()
# print(x)
# Dir () funktsiyasidan foydalanish
# Moduldagi barcha funktsiyalar nomlarini (yoki o'zgaruvchilar nomlarini) 
# ro'yxatga olish uchun o'rnatilgan funksiya mavjud. dir()funktsiyasi:

# Misol
# Platforma moduliga tegishli barcha aniqlangan nomlarni sanab bering:

# import platform

# x = dir(platform)
# print(x)
# Eslatma: dir () funktsiyasidan barcha modullarda, shuningdek 
# o'zingiz yaratgan modullarda ham foydalanish mumkin .


# Moduldan import
# fromKalit so'z yordamida moduldan faqat qismlarni import qilishni tanlashingiz mumkin .

# Misol
# Nomlangan modul mymodulebitta funktsiyaga va bitta lug'atga ega:

# def greeting(name):
#   print("Hello, " + name)

# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }
# Misol
# Moduldan faqat person1 lug'atini import qiling:

# from mymodule import person1

# print (person1["age"])
# Eslatma:from Kalit so'z yordamida import qilganda ,
#  moduldagi elementlarga murojaat qilganda modul nomidan foydalanmang.
#  Misol: person1["age"], balki mymodule.person1["age"]
# =============================================================================
# 
# =============================================================================


# =============================================================================
# 
# =============================================================================
#Python matematikasi python math
# Python-da matematik vazifalarni sonlar bo'yicha bajarishga imkon beradigan,
#  o'rnatilgan matematik modulni o'z ichiga olgan 
#o'rnatilgan matematik funktsiyalar to'plami mavjud.

# O'rnatilgan matematik funktsiyalar
# min()Va max()vazifalari bir iterable eng past yoki 
#eng yuqori qiymati topish uchun foydalanish mumkin:

# Misol
# x = min(5, 10, 25)
# y = max(5, 10, 25)

# print(x)
# print(y)
# abs()Funktsiya belgilangan qator mutlaq (ijobiy) qiymatini qaytaradi:

# Misol
# x = abs(-7.25)

# print(x)
# Funktsiya y (x kuchi uchun x qiymat qaytaradi y ).pow(x, y)

# Misol
# 4 qiymatini 3 kuchiga qaytaring (4 * 4 * 4 bilan bir xil):

# x = pow(4, 3)

# print(x)
# Matematika moduli
# Python-da mathmatematik funktsiyalar ro'yxatini kengaytiradigan o'rnatilgan modul ham mavjud .

# Uni ishlatish uchun siz mathmodulni import qilishingiz kerak :

# import math
# mathModulni import qilganingizda, siz modulning usullari
# va doimiylarini ishlatishni boshlashingiz mumkin.

# math.sqrt()Misol uchun usul, bir qator kvadrat ildiz qaytaradi:

# Misol
# import math

# x = math.sqrt(64)

# print(x)
# math.ceil()Usuli yuqoriga o'zining eng yaqin tamsayıya bir 
# qator va donachalari math.floor() o'z yaqin tamsayıya
# usul tur bir qator pastga va deklaratsiyalarini natija:

# Misol
# import math

# x = math.ceil(1.4)
# y = math.floor(1.4)

# print(x) # returns 2
# print(y) # returns 1
# math.piDoimiy, Piy (3.14 ...) qiymatini qaytaradi:

# Misol
# import math

# x = math.pi

# print(x)
# Matematik modulga to'liq ma'lumotnoma
# Bizning Matematik modullar ma'lumotnomasida siz Matematika moduliga 
# tegishli bo'lgan barcha usullar va konstantalarning to'liq ma'lumotnomasini topasiz.
# =============================================================================
# 
# =============================================================================
# Python JSON
# JSON - ma'lumotlarni saqlash va almashish uchun sintaksis.

# JSON - bu JavaScript obyekti belgisi bilan yozilgan matn.

# Pythonda JSON
# Python-da jsonJSON ma'lumotlari bilan ishlash uchun
# ishlatilishi mumkin bo'lgan o'rnatilgan paket mavjud .

# Misol
# Json modulini import qiling:

# import json
# JSONni tahlil qilish - JSON -dan Python -ga o'tkazish
# Agar sizda JSON satri bo'lsa, uni json.loads()usul yordamida tahlil qilishingiz mumkin .

# Natijada Python lug'ati bo'ladi .

# Misol
# JSON -dan Python -ga aylantirish:

# import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"])
# Python -dan JSON -ga aylantirish
# Agar sizda Python obyekti bo'lsa,
#  uni json.dumps()usul yordamida JSON qatoriga aylantirishingiz mumkin .

# Misol
# Python -dan JSON -ga aylantirish:

# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)

# Siz Python ob'ektlarini quyidagi turdagi JSON satrlariga o'zgartirishingiz mumkin:

# dikt
# ro'yxat
# yig'moq
# tor
# int
# suzmoq
# To'g'ri
# Yolg'on
# Hech kim
# Misol
# Python ob'ektlarini JSON satrlariga aylantiring va qiymatlarni chop eting:

# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))
# Python -dan JSON -ga o'zgartirganda, 
#Python ob'ektlari JSON (JavaScript) ekvivalentiga aylanadi:

# Python  JSON
# dict  Object
# list  Array
# tuple  Array
# str  String
# int  Number
# float  Number
# True  truese
# None  null
# Misol
# Barcha qo
# False  falnuniy ma'lumotlar turlarini o'z ichiga olgan Python ob'ektini aylantiring:

# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# # 
# # Natijani formatlash
# # Yuqoridagi misol JSON satrini bosib chiqaradi, 
# # lekin o'qish oson emas, chiziqlar va chiziqlar kesilmasligi kerak.

# # json.dumps()Usul osonroq natija o'qishni qilish parametrlarini ega:

# # Misol
# # indentChiziqlar sonini aniqlash uchun parametrdan foydalaning :

# # json.dumps(x, indent=4)

# # Siz shuningdek ajratuvchilarni belgilashingiz mumkin, 
# # odatiy qiymat (",", ":"), ya'ni har bir ob'ektni ajratish uchun vergul
# #  va bo'sh joy, kalitlardan qiymatlarni ajratish 
# ##uchun ikki nuqta va bo'sh joydan foydalaniladi:

# # Misol
# # separatorsStandart ajratgichni o'zgartirish uchun parametrdan foydalaning :

# json.dumps(x, indent=4, separators=(". ", " = "))
# print(json.dumps(x))
# Natijaga buyurtma bering
# json.dumps()Usuli natijasida kalitlari buyurtma parametrlarini ega:

# Misol
# sort_keysNatijani saralash kerakmi yoki yo'qligini aniqlash uchun parametrdan foydalaning :

# json.dumps(x, indent=4, sort_keys=True)
# =============================================================================
# 
# =============================================================================

# Python RegEx
# RegEx yoki Muntazam ifoda - bu qidiruv modelini tashkil etuvchi belgilar ketma -ketligi.

# RegEx -dan foydalanib, satrda ko'rsatilgan 
#qidiruv namunasi mavjudligini tekshirish mumkin.

# RegEx moduli
# Python-da reoddiy ifodalar bilan ishlash
# uchun ishlatilishi mumkin bo'lgan o'rnatilgan paket mavjud .

# reModulni import qilish :

# import re
# Python -da RegEx
# reModulni import qilganingizda, oddiy iboralarni ishlatishni boshlashingiz mumkin:

# Misol
# "The" bilan boshlanib, "Ispaniya" bilan tugashini bilish uchun satrni qidiring:

# import re

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)
# RegEx funktsiyalari
# reModuli bizga bir o'yinga, bir mag'lubiyatga 
#qo'ng'iroq qilish imkonini beradi vazifalar to'plamini taqdim etadi:

# Function  Description
# findall  Returns a list containing all matches
# search  Returns a Match object if there is a match anywhere in the string
# split  Returns a list where the string has been split at each match
# sub  Replaces one or many matches with a string
# Meta -belgilar
# Meta -belgilar - bu alohida ma'noga ega belgilar:

# Character  Description  Example  Try it
# []  A set of characters  "[a-m]"  
# \  Signals a special sequence (can also be used to escape special characters)  "\d"  
# .  Any character (except newline character)  "he..o"  
# ^  Starts with  "^hello"  
# $  Ends with  "world$"  
# *  Zero or more occurrences  "aix*"  
# +  One or more occurrences  "aix+"  
# {}  Exactly the specified number of occurrences  "al{2}"  
# |  Either or  "falls|stays"  
# ()  Capture and group      
# Maxsus ketma -ketliklar
# Maxsus ketma -ketlik \quyidagi belgilar ro'yxatidan keyin keladi va alohida ma'noga ega:

# Character  Description  Example  Try it
# \A  Returns a match if the specified characters are at the beginning of the string  "\AThe"  
# \b  Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")  r"\bain"
# r"ain\b"  
# \B  Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")  r"\Bain"
# r"ain\B"  
# \d  Returns a match where the string contains digits (numbers from 0-9)  "\d"  
# \D  Returns a match where the string DOES NOT contain digits  "\D"  
# \s  Returns a match where the string contains a white space character  "\s"  
# \S  Returns a match where the string DOES NOT contain a white space character  "\S"  
# \w  Returns a match where the string contains any word characters (characters from a to Z, 
#                                                                    digits from 0-9, and the underscore _ character)  "\w"  
# \W  Returns a match where the string DOES NOT contain any word characters  "\W"  
# \Z  Returns a match if the specified characters are at the end of the string  "Spain\Z"  
# To'plamlar
# To'plam - []bu alohida ma'noga ega bo'lgan qavsli qavs ichidagi belgilar to'plami :

# Set  Description  Try it
# [arn]  Returns a match where one of the specified characters (a, r, or n) are present  
# [a-n]  Returns a match for any lower case character, alphabetically between a and n  
# [^arn]  Returns a match for any character EXCEPT a, r, and n  
# [0123]  Returns a match where any of the specified digits (0, 1, 2, or 3) are present  
# [0-9]  Returns a match for any digit between 0 and 9  
# [0-5][0-9]  Returns a match for any two-digit numbers from 00 and 59  
# [a-zA-Z]  Returns a match for any character alphabetically between a and z, lower case OR upper case  
# [+]  In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string  
 
# Findall () funktsiyasi
# findall()Funktsiya Barcha kutilmaganda o'z ichiga olgan ro'yxatini qaytaradi.

# Misol
# Barcha o'yinlar ro'yxatini chop eting:

# import re

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)
# Ro'yxatda o'yinlar topilgan tartibda joylashgan.

# Agar moslik topilmasa, bo'sh ro'yxat qaytariladi:

# Misol
# Agar mos kelmasa, bo'sh ro'yxatni qaytaring:

# import re
# txt = "The rain in Spain"
# x = re.findall("Spain", txt)
# print(x)
 
# Qidiruv () funktsiyasi
# search()Funktsiya bir o'yinga mag'lubiyatga izlaydi va qaytib Match ob'ektini bir o'yin bor agar.

# Agar bir nechta o'yin bo'lsa, faqat birinchi uchrashuv qaytariladi:

# Misol
# Satrdagi birinchi bo'sh joy belgisini qidiring:

# import re

# txt = "The rain in Spain"
# x = re.search("\s", txt)

# print("The first white-space character is located in position:", x.start())
# Agar moslik topilmasa, qiymat Noneqaytariladi:

# Misol
# Hech qanday mos kelmaydigan qidiruvni amalga oshiring:

# import re

# txt = "The rain in Spain"
# x = re.search("Portugal", txt)
# print(x)
 
# Split () funktsiyasi
# split()Funktsiya string har o'yinda split bo'ldi ro'yxatini qaytaradi:

# Misol
# Har bir bo'sh joy belgisiga bo'ling:

# import re

# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)
# maxsplit Parametrni ko'rsatish orqali siz hodisalar sonini boshqarishingiz mumkin :

# Misol
# Ipni faqat birinchi marta bo'linadi:

# import re

# txt = "The rain in Spain"
# x = re.split("\s", txt, 1)
# print(x)
 
# Sub () funktsiyasi
# sub()Funktsiya siz tanlagan matni bilan uchrashuvlarini o'rnini:

# Misol
# Har bir bo'sh joy belgisini 9 raqami bilan almashtiring:

# import re

# txt = "The rain in Spain"
# x = re.sub("\s", "Abulqosim", txt)
# print(x)
# count Parametrni ko'rsatib, almashtirishlar sonini nazorat qilishingiz mumkin :

# Misol
# Birinchi 2 ta hodisani almashtiring:

# import re

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2)
# print(x)
 
# Ob'ektni moslashtirish
# Mos keladigan ob'ekt - bu qidiruv va natija haqidagi ma'lumotlarni o'z ichiga olgan ob'ekt.

# Eslatma: Agar mos kelmasa, mos keladigan Noneob'ekt o'rniga qiymat qaytariladi.

# Misol
# Match moslamasini qaytaradigan qidiruvni bajaring:

# import re

# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x) #this will print an object
# Match ob'ektida qidiruv va natija haqidagi ma'lumotlarni olish uchun 
# ishlatiladigan xususiyatlar va usullar mavjud:

# .span()o'yinning boshlang'ich va oxirgi pozitsiyalarini o'z ichiga olgan to'plamni qaytaradi.
# .stringfunktsiyaga o'tgan satrni
# .group()qaytaradi, mos keladigan satr qismini qaytaradi
# Misol
# Birinchi o'yin sodir bo'lgan joyni (boshlanish va tugatish pozitsiyasini) chop eting.

# Oddiy ibora "S" harfi bilan boshlanadigan har qanday so'zni qidiradi:

# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.span())
# Misol
# Funksiyaga berilgan qatorni chop eting:

# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.string)
# Misol
# Ipning mos keladigan joyini chop eting.

# Oddiy ibora "S" harfi bilan boshlanadigan har qanday so'zni qidiradi:

# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.group())
# Eslatma: Agar mos kelmasa, mos keladigan Noneob'ekt o'rniga qiymat qaytariladi.

# =============================================================================
# 
# =============================================================================





