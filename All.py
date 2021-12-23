# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 10:50:36 2021

@author: Rafiqov Abulqosim
"""

# Python ma'lumotlar turlari
# O'rnatilgan ma'lumotlar turlari
# Dasturlashda ma'lumotlar turi muhim tushuncha hisoblanadi.

# O'zgaruvchilar har xil turdagi ma'lumotlarni 
# saqlashi mumkin, va har xil turdagi har xil ishlarni bajarishi mumkin.

# Pythonda ushbu toifadagi sukut bo'yicha quyidagi ma'lumotlar turlari mavjud:

# Matn turi:	str
# Raqamli turlari:	int, float, complex
# Navbat turlari:	list, tuple, range
# Xaritalar turi:	dict
# Turlarni o'rnatish:	set, frozenset
# Boolean turi:	bool
# Ikkilik turlari:	bytes, bytearray, memoryview
# Ma'lumot turini olish
# Siz har qanday ob'ektning ma'lumot turini type()funktsiyadan foydalanib olishingiz mumkin :

# Misol
# X o'zgaruvchining ma'lumot turini chop eting:

   x = 5
    print(type(x))
# Ma'lumot turini sozlash
# Python -da ma'lumotlar turi o'zgaruvchiga qiymat tayinlanganda o'rnatiladi:

# Example	Data Type	Try it
# x = "Hello World"	str	
# x = 20	int	
# x = 20.5	float	
# x = 1j	complex	
# x = ["apple", "banana", "cherry"]	list	
# x = ("apple", "banana", "cherry")	tuple	
# x = range(6)	range	
# x = {"name" : "John", "age" : 36}	dict	
# x = {"apple", "banana", "cherry"}	set	
# x = frozenset({"apple", "banana", "cherry"})	frozenset	
# x = True	bool	
# x = b"Hello"	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview	
# Maxsus ma'lumotlar turini sozlash
# Agar siz ma'lumotlar turini ko'rsatmoqchi bo'lsangiz, 
# quyidagi konstruktor funktsiyalaridan foydalanishingiz mumkin:

# Example	Data Type	Try it
# x = str("Hello World")	str	
# x = int(20)	int	
# x = float(20.5)	float	
# x = complex(1j)	complex	
# x = list(("apple", "banana", "cherry"))	list	
# x = tuple(("apple", "banana", "cherry"))	tuple	
# x = range(6)	range	
# x = dict(name="John", age=36)	dict	
# x = set(("apple", "banana", "cherry"))	set	
# x = frozenset(("apple", "banana", "cherry"))	frozenset	
# x = bool(5)	bool	
# x = bytes(5)	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview

# # =============================================================================
# # 
# # =============================================================================
# Python raqamlari
# Python raqamlari
# Python -da uchta raqam turi mavjud:

# int
# float
# complex
# Raqamli turdagi o'zgaruvchilar siz ularga qiymat tayinlaganingizda yaratiladi:

# Misol
# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex
# Python -dagi har 
#qanday ob'ekt turini tekshirish uchun quyidagi type()funktsiyadan foydalaning :

# Misol
# print(type(x))
# print(type(y))
# print(type(z))
# Int
# Int yoki butun son - 
#bu butun son, musbat yoki manfiy, o'nliksiz, cheksiz uzunlik.

# Misol
# Butun sonlar:

# x = 1
# y = 35656222554887711
# z = -3255522

# print(type(x))
# print(type(y))
# print(type(z))
# Float
# Float yoki "suzuvchi nuqta raqami" - 
# bu bir yoki bir nechta o'nli kasrlarni o'z ichiga olgan, musbat yoki manfiy son.

# Misol
# Suzish:

# x = 1.10
# y = 1.0
# z = -35.59

# print(type(x))
# print(type(y))
# print(type(z))
# Float 10 ning kuchini ko'rsatish uchun "e" harfi bo'lgan ilmiy raqamlar ham bo'lishi mumkin.

# Misol
# Suzish:

# x = 35e3
# y = 12E4
# z = -87.7e100

# print(type(x))
# print(type(y))
# print(type(z))
# Kompleks
# Murakkab sonlar xayoliy qism sifatida "j" harfi bilan yozilgan:

# Misol
# Kompleks:

# x = 3+5j
# y = 5j
# z = -5j

# print(type(x))
# print(type(y))
# print(type(z))
# Konversiya turi
# Siz bilan bir turiga aylantirish mumkin int(), float()va complex()usullari:

# Misol
# Bir turdan boshqasiga o'tkazish:

# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# # #convert from int to float:
# a = float(x)

# # #convert from float to int:
# b = int(y)

# # #convert from int to complex:
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))
# Eslatma: Siz murakkab sonlarni boshqa raqam turiga o'zgartira olmaysiz.

# Tasodifiy raqam
# Python random()tasodifiy sonni tuzish funktsiyasiga ega emas , 
# lekin Pythonda randomtasodifiy sonlarni yaratish uchun ishlatilishi mumkin bo'lgan o'rnatilgan modul mavjud :

# Misol
# Tasodifiy modulni import qiling va 1 dan 9 gacha tasodifiy sonni ko'rsating:

# import random

# print(random.randrange(1, 10))

# # =============================================================================
# # 
# # =============================================================================

# Python satrlari
# String
# Pythondagi satrlar bitta tirnoq yoki ikkita tirnoq bilan o'ralgan.

# «Salom», deb bir xil bo'ladi "Salom" .

# Siz print()funktsiyali mag'lubiyatni ko'rsatishingiz mumkin :

# Misol
# print("Hello")
# print('Hello')
# O'zgaruvchiga satr tayinlang
# O'zgaruvchiga mag'lubiyatni belgilash o'zgaruvchining nomi, 
# so'ngra teng belgisi va satr bilan amalga oshiriladi:

# Misol
# a = "Hello"
# print(a)
# Ko'p qatorli satrlar
# Siz o'zgaruvchiga uchta tirnoq yordamida ko'p satrli qatorni belgilashingiz mumkin:

# Misol
# Siz uchta ikkita tirnoqdan foydalanishingiz mumkin:

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)
# Yoki uchta bitta tirnoq:

# Misol
# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(a)
# Eslatma: natijada satr uzilishlari kodda bo'lgani kabi joylashtiriladi.

# Stringlar - massivlar
# Boshqa ko'plab mashhur dasturlash tillari singari,
#  Python satrlari ham unicode belgilarini ifodalovchi baytlar massividir.

# Biroq, Pythonda ma'lumotlar turi yo'q, bitta belgi - uzunligi 1 ga teng.

# Ip elementlariga kirish uchun kvadrat qavslardan foydalanish mumkin.

# Misol
# Belgini 1 -pozitsiyada oling (birinchi belgining 0 pozitsiyasiga ega ekanligini unutmang):

# a = "Hello, World!"
# print(a[1])
# String orqali aylanish
# Stringlar massiv bo'lgani uchun, biz simlardagi simlarni pastadir bilan aylantira olamiz for.

# Misol
# "Banan" so'zidagi harflarni aylantiring:

# for x in "Abulqosim":
#   print(x)
# Python For Loops bo'limida Looplar haqida ko'proq bilib oling .

# Qator uzunligi
# Ip uzunligini olish uchun len()funksiyadan foydalaning .

# Misol
# len()Funktsiya bilan mag'lubiyatga uzunligini qaytaradi:

# a = "Hello, World!"
# print(len(a))
# Stringni tekshiring
# Qatorda ma'lum bir ibora yoki 
# belgi mavjudligini tekshirish uchun biz kalit so'zdan foydalanishimiz mumkin in.

# Misol
# Quyidagi matnda "bepul" mavjudligini tekshiring:

# txt = "The best things in life are free!"
# print("free" in txt)
# Buni ifbayonotda ishlating :

# Misol
# Faqat "bepul" mavjud bo'lganda chop eting:

# txt = "The best things in life are free!"
# if "freee" in txt:
#   print("Yes, 'free' is present.")
# Agar Python If ... Boshqacha bo'limida 
# If iboralari haqida ko'proq bilib oling .

# YO'Qligini tekshiring
# Ma'lum bir ibora yoki belgining satrda EMASligini 
# tekshirish uchun biz kalit so'zdan foydalanishimiz mumkin not in.

# Misol
# Quyidagi matnda "qimmat" yo'qligini tekshiring:

# txt = "The best things in life are free!"
# print("expensive" not in txt)
# Buni ifbayonotda ishlating :

# Misol
# faqat "qimmat" bo'lmasa, chop eting:

# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")

# # =============================================================================
# # 
# # =============================================================================
# Python - chiziqlarni kesish
# Kesish
# Siz til sintaksisidan foydalanib, bir qator belgilarni qaytarishingiz mumkin.

# Satrning bir qismini qaytarish uchun boshlang'ich va tugatish indekslarini belgilang.

# Misol
# Belgilarni 2 -pozitsiyadan 5 -pozitsiyagacha oling (shu jumladan emas):

# b = "Hello, World!"
# print(b[2:6])
# Eslatma: birinchi belgi 0 indeksiga ega.

# Boshidan kesish
# Boshlanish indeksini qoldirib, diapazon birinchi belgidan boshlanadi:

# Misol
# Belgilarni boshidan 5 -pozitsiyagacha oling (shu jumladan emas):

# b = "Hello, World!"
# print(b[:6])
# Oxirigacha bo'lak
# Yakuniy indeksni qoldirib , diapazon oxirigacha boradi:

# Misol
# Belgilarni 2 -pozitsiyadan oxirigacha oling:

# b = "Hello, World!"
# print(b[2:])
# Salbiy indekslash
# Kesimni satr oxiridan boshlash uchun manfiy indekslardan foydalaning:
# Misol
# Belgilarni oling:

# Kimdan: "Dunyo!" Da "o" (pozitsiya -5)

# Kimga, lekin kiritilmagan: "Dunyo!" Dagi "d". (pozitsiya -2):

# b = "Hello, World!"
# print(b[-5:-2])

# # =============================================================================
# # 
# # =============================================================================
# Python - Modify Strings
# Python has a set of built-in methods that you can use on strings.

# Upper Case
# Example
# The upper() method returns the string in upper case:

# a = "Hello, World!"
# print(a.upper())
# Lower Case
# Example
# The lower() method returns the string in lower case:

# a = "Hello, World!"
# print(a.lower())
# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

# Example
# The strip() method removes any whitespace from the beginning or the end:
# strip()Usuli boshida yoki oxirida har qanday bo'sh joy olib tashlanadi:
# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"
# Replace String
# Example
# The replace() method replaces a string with another string:
# replace()Usul boshqa kanop bilan, bir mag'lubiyatga o'rnini:
# a = "Hello, World!"
# print(a.replace("H", "l"))
# # Split String
# The split() method returns a list where the text between the specified separator becomes the list items.
# split()Usuli belgilangan satr bilan bo'linadi o'rtasidagi matn ro'yxati ma'lumotlar aylanadi ro'yxatini qaytaradi.
# Example
# The split() method splits the string 
#into substrings if it finds instances of the separator:

# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']

# # =============================================================================
# # 
# # =============================================================================
# Python - satrlarni birlashtirish
# String birikmasi
# Ikki qatorni birlashtirish yoki birlashtirish uchun siz + operatoridan foydalanishingiz mumkin.

# Misol
# O'zgaruvchini Birlashtirish ao'zgaruvchilar bilan bo'zgaruvchilar c:

# a = "Hello"
# b = "World"
# c = a +" " +  b
# print(c)
# Misol
# Ularning orasiga bo'sh joy qo'shish uchun " "quyidagilarni qo'shing :

# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)
# # =============================================================================
# # 
# # =============================================================================
# Python - Format - satrlar
# String formati
# Python o'zgaruvchilar bobida bilib olganimizdek, biz satr va raqamlarni birlashtira olmaymiz:

# Misol
# age = 36
# txt = "My name is John, I am " + age
# print(txt)
# Lekin biz format()usul yordamida simlar va raqamlarni birlashtira olamiz !

# format()Usuli, ularni biçimlendiren va yertutucuları
#  mag'lubiyatga joylar ularni, o'tgan dalillarini oladi {}bo'ladi:

# Misol
# format()Raqamlarni satrlarga kiritish uchun usuldan foydalaning :

# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))
# Format () usuli cheklanmagan miqdordagi argumentlarni oladi va tegishli joy egalariga joylashtiriladi:

# Misol
# quantity = 50
# itemno = 567
# price = 49.95
# myorder = "I want {}} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))
# {0}Argumentlar to'g'ri to'ldiruvchiga joylashtirilganligiga 
# ishonch hosil qilish uchun indeks raqamlaridan foydalanishingiz mumkin:

# Misol
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))

# # =============================================================================
# # 
# # =============================================================================
# Python - belgilar qochish
# Qochish xarakteri
# Qatorga noqonuniy belgilar kiritish uchun qochish belgisidan foydalaning.

# Qochish belgisi - bu teskari chiziq, \keyin siz kiritmoqchi bo'lgan belgi.

# Noqonuniy belgining namunasi, ikki tirnoq bilan o'ralgan satr ichidagi ikkita tirnoq:

# Misol
# Ikkita tirnoq bilan o'ralgan satr ichida ikkita tirnoq ishlatsangiz xato bo'ladi:

# txt = "We are the so-called "Vikings" from the north."
# Ushbu muammoni hal qilish uchun qochish belgisidan foydalaning \":

# Misol
# Qochish belgisi sizga ruxsat berilmagan hollarda ikki tirnoqdan foydalanishga imkon beradi:

# txt = "We are the so-called \"Vikings\" from the north."
# Qochish belgilar
# Python -da ishlatiladigan boshqa qochish belgilar:

# Code	Result	Try it
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value
# # =============================================================================
# # 
# # =============================================================================
# Python - String usullari
# String usullari
# Pythonda satrlarda ishlatishingiz mumkin bo'lgan o'rnatilgan usullar to'plami mavjud.

# Eslatma: Barcha satr usullari yangi qiymatlarni qaytaradi. Ular asl satrni o'zgartirmaydi.

# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning
# # =============================================================================
# # 
# # =============================================================================
# Python booleanlari
# Booleanlar ikkita qiymatdan birini ifodalaydi: Trueyoki False.

# Mantiqiy qadriyatlar
# Dasturlashda siz tez -tez ifoda Trueyoki False.

# Siz Python har qanday ifoda baholash va ikki javob olish, mumkin Trueyoki False.

# Ikki qiymatni solishtirganda, ifoda baholanadi va Python mantiqiy javobni qaytaradi:

# # Misol
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)
# Agar if iborasida shart bajarilsa, Python qaytaradi Trueyoki False:

# Misol
# Ahvoli yoki yo'qligini asoslangan xabar chop Trueyoki False:

# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")
# Qiymatlar va o'zgaruvchilarni baholang
# bool()Funktsiya har qanday qiymati baholash,
#  va sizga berishga imkon beradi Trueyoki False , evaziga

# Misol
# Ip va raqamni baholang:

# print(bool("Hello"))
# print(bool(15))
# Misol
# Ikkita o'zgaruvchini baholang:

# x = "Hello"
# y = 15

# print(bool(x))
# print(bool(y))


# Most Values are True
# Deyarli har qanday qiymat, Trueagar u qandaydir tarkibga ega bo'lsa , baholanadi .

# Har qanday satr Truebo'sh satrlardan tashqari.

# Har qanday raqam True, bundan mustasno 0.

# Har qanday ro'yxat, to'plam, to'plam va lug'at, Truebo'sh ro'yxatlardan tashqari.

# Misol
# Quyidagilar "True" ni qaytaradi:

# bool("abc")
# bool(123)
# bool(["apple", "cherry", "banana"])
# Ba'zi qiymatlar noto'g'ri
# Aslida, uchun baholash juda
#  ko'p qiymatlar mavjud emas Falsekabi bo'sh qadriyatlar 
#  tashqari, (), [], {}, "", qator 0va qiymati None. Va, albatta, qiymat Falsebaholanadi False.

# Misol
# Quyidagilar False qaytaradi:

# bool(False)
# bool(None)
# bool(0)
# bool(" ")
# bool(())
# bool([])
# bool({})
# Bu holda yana bir qiymat yoki ob'ekt baholanadi False,
#  va agar sizda ob'ektni __len__qaytaradigan 0yoki funktsiyali sinfdan yasalgan bo'lsa False:

# Misol
# class myclass():
#   def __len__(self):
#     return 0

# myobj = myclass()
# print(bool(myobj))
# Funktsiyalar mantiqiylikni qaytarishi mumkin
# Siz mantiqiy qiymatni qaytaradigan funktsiyalarni yaratishingiz mumkin:

# Misol
# Funktsiyaning javobini chop eting:

# def myFunction() :
#   return True

# print(myFunction())
# Siz funktsiyani mantiqiy javobiga asoslangan kodni bajarishingiz mumkin:

# Misol
# "Ha!" Chop etish agar funktsiya "True" ni qaytarsa, aks holda "YO'Q!"

# def myFunction() :
#   return True

# if myFunction():
#   print("YES!")
# else:
#   print("NO!")
# Python-da, funktsiya kabi, mantiqiy qiymatni 
# qaytaradigan ko'plab o'rnatilgan isinstance() funktsiyalar mavjud,
#  ular yordamida ob'ekt ma'lum bir ma'lumot turiga mansubligini aniqlash mumkin:

# Misol
# Ob'ekt butun son yoki yo'qligini tekshiring:

# x = 200
# print(isinstance(x, int))
# # =============================================================================
# # 
# # =============================================================================
# Python operatorlari
# Python operatorlari
# Operatorlar o'zgaruvchilar va qiymatlar bo'yicha operatsiyalarni bajarish uchun ishlatiladi.

# Quyidagi misolda biz +ikkita qiymatni qo'shish uchun operatordan foydalanamiz :

# Misol
# print(10 % 5)
# Python operatorlarni quyidagi guruhlarga ajratadi:

# Arifmetik operatorlar
# Topshiriq operatorlari
# Taqqoslash operatorlari
# Mantiqiy operatorlar
# Shaxsni aniqlash operatorlari
# A'zolik operatorlari
# Bitli operatorlar
# Python arifmetik operatorlari
# Arifmetik operatorlar umumiy matematik amallarni bajarish uchun sonli qiymatlar bilan ishlatiladi:

# Operator	Name	Example	Try it
# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y	
# Python tayinlash operatorlari
# Belgilash operatorlari o'zgaruvchilarga qiymatlarni belgilash uchun ishlatiladi:

# Operator	Example	Same As	Try it
# =	x = 5	x = 5	
# +=	x += 3	x = x + 3	
# -=	x -= 3	x = x - 3	
# *=	x *= 3	x = x * 3	
# /=	x /= 3	x = x / 3	
# %=	x %= 3	x = x % 3	
# //=	x //= 3	x = x // 3	
# **=	x **= 3	x = x ** 3	
# &=	x &= 3	x = x & 3	
# |=	x |= 3	x = x | 3	
# ^=	x ^= 3	x = x ^ 3	
# >>=	x >>= 3	x = x >> 3	
# <<=	x <<= 3	x = x << 3	

# Python solishtirish operatorlari
# Taqqoslash operatorlari ikkita qiymatni solishtirish uchun ishlatiladi:

# Operator	Name	Example	Try it
# ==	Equal	x == y	
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y	
# Python mantiqiy operatorlari
# Mantiqiy operatorlar shartli bayonotlarni birlashtirish uchun ishlatiladi:

# Operator	Description	Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)	
# Python identifikatorlari operatorlari
# Identifikator operatorlari ob'ektlarni solishtirish uchun ishlatiladi, 
# agar ular teng bo'lsa emas, lekin ular aslida bir xil ob'ekt bo'lsa, xotira joyi bir xil bo'lsa:

# Operator	Description	Example	Try it
# is 	Returns True if both variables are the same object	x is y	
# is not	Returns True if both variables are not the same object	x is not y	
# Python a'zolik operatorlari
# A'zolik operatorlari ob'ektda ketma -ketlik mavjudligini tekshirish uchun ishlatiladi:

# Operator	Description	Example	Try it
# in 	Returns True if a sequence with the specified value is present in the object	x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y	
# Python bitwise operatorlari
# Bitli operatorlar raqamlarni (ikkilik) solishtirish uchun ishlatiladi:

# Operator	Name	Description
# & 	AND	Sets each bit to 1 if both bits are 1
# |	OR	Sets each bit to 1 if one of two bits is 1
#  ^	XOR	Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the 
# right and let the leftmost bits fall off
# >>	Signed right shift	Shift right by pushing copies of the leftmost
#  bit in from the left, and let the rightmost bits fall off

# # =============================================================================
# # 
# # =============================================================================

# Python ro'yxatlari
# mylist = ["apple", "banana", "cherry"]
# print (mylist)
# Ro'yxat
# Ro'yxatlar bir nechta elementlarni 
#bitta o'zgaruvchiga saqlash uchun ishlatiladi.

# Ro'yxatlar-bu Python-da ma'lumotlar to'plamini 
# saqlash uchun ishlatiladigan 4 ta o'rnatilgan ma'lumotlar turlaridan biri, 
# qolgan 3 tuple , to'siq va lug'at bo'lib , ularning har biri har xil sifat va foydalanishga ega.

# Ro'yxatlar kvadrat qavslar yordamida tuziladi:

# Misol
# Ro'yxat yarating:

# thislist = ["apple", "banana", "cherry",'apple','banana']
# print(thislist)
# Elementlar ro'yxati
# Ro'yxat elementlari tartiblangan, o'zgartirilishi mumkin va takroriy 
# qiymatlarga ruxsat beradi.

# Ro'yxat elementlari indekslanadi, birinchi element indeksga ega [0],
#  ikkinchi element indeksga ega [1]va hokazo.

# Buyurtma qilingan
# Biz ro'yxatlar buyurtma qilingan deb aytganimizda, bu elementlar
#  belgilangan tartibga ega ekanligini anglatadi va bu tartib o'zgarmaydi.

# Agar siz ro'yxatga yangi elementlar qo'shsangiz, 
# yangi narsalar ro'yxatning oxiriga qo'yiladi.

# E'tibor bering: tartibni o'zgartiradigan ba'zi
#  ro'yxat usullari mavjud, lekin umuman: elementlarning tartibi o'zgarmaydi.

# O'zgaruvchan
# Ro'yxat o'zgarishi mumkin, ya'ni biz ro'yxatdagi
#  elementlarni yaratgandan so'ng o'zgartirishimiz, qo'shishimiz va o'chirishimiz mumkin.

# Takrorlashga ruxsat berish
# Ro'yxatlar indekslanganligi sababli, ro'yxatlar 
# bir xil qiymatga ega bo'lishi mumkin:

# Misol
# Ro'yxatlar takroriy qiymatlarga ruxsat beradi:

# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)
# Ro'yxat uzunligi
# Ro'yxatda nechta element borligini aniqlash uchun 
#len()funktsiyadan foydalaning :

# Misol
# Ro'yxatdagi elementlar sonini chop eting:

# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))
# Ro'yxat elementlari - ma'lumotlar turlari
# Ro'yxat elementlari har qanday turdagi bo'lishi mumkin:

# Misol
# String, int va boolean ma'lumotlar turlari:

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
# Ro'yxat har xil turdagi ma'lumotlarni o'z ichiga olishi mumkin:

# Misol
# Satrlar, butun sonlar va mantiqiy qiymatlar ro'yxati:

# list1 = ["abc", 34, True, 40, "male"]
# turi ()
# Python nuqtai nazaridan, ro'yxatlar ma'lumotlar turi 
# "ro'yxati" bo'lgan ob'ektlar sifatida belgilanadi:

# <class 'list'>
# Misol
# Ma'lumotlar ro'yxati qanday?

# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))
# Ro'yxat () Konstruktor
# Yangi ro'yxat tuzishda list () konstruktoridan foydalanish ham mumkin .

# Misol
# list()Ro'yxatni tuzish uchun konstruktordan foydalanish :

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)
# Python to'plamlari (massivlar)
# Python dasturlash tilida to'rtta ma'lumot yig'ish turi mavjud:

# Ro'yxat - bu buyurtma qilingan va o'zgaruvchan to'plam. A'zolarning takrorlanishiga ruxsat beradi.
# Tuple - buyurtma qilingan va o'zgartirilmaydigan to'plam. A'zolarning takrorlanishiga ruxsat beradi.
# Set og'riqqa va unindexed bir to'plam. Takroriy a'zolar yo'q.
# Lug'at - buyurtma qilingan va o'zgaruvchan to'plam. Takroriy a'zolar yo'q.

# # =============================================================================
# # 
# # =============================================================================
# Python - kirish elementlari ro'yxati
# Kirish elementlari
# Ro'yxat elementlari indekslanadi va siz indeks raqamiga murojaat qilib ularga kirishingiz mumkin:

# Misol
# Ro'yxatning ikkinchi bandini chop eting:

# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])
# Eslatma: birinchi element 0 indeksiga ega.

# Salbiy indekslash
# Salbiy indekslash oxiridan boshlanishini bildiradi

# -1oxirgi elementni, -2ikkinchi oxirgi elementni va boshqalarni bildiradi.

# Misol
# Ro'yxatning oxirgi bandini chop eting:

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])
# Indekslar diapazoni
# Siz indekslar diapazonini qaerdan boshlash va tugatish kerakligini belgilashingiz mumkin.

# Diapazonni ko'rsatganda, qaytariladigan qiymat ko'rsatilgan elementlar bilan yangi ro'yxat bo'ladi.

# Misol
# Uchinchi, to'rtinchi va beshinchi elementlarni qaytaring:

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# Eslatma: Qidiruv 2 -indeksdan boshlanadi (shu jumladan) va 5 -indeks bilan tugaydi (shu jumladan emas).

# Esda tutingki, birinchi element 0 indeksiga ega.

# Boshlanish qiymatini qoldirib, diapazon birinchi banddan boshlanadi:

# Misol
# Bu misol elementlarni boshidan qaytaradi, lekin "kivi" ni o'z ichiga olmaydi:

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])
# Yakuniy qiymatni qoldirib, diapazon ro'yxatning oxirigacha davom etadi:

# Misol
# Bu misol elementlarni "gilos" dan oxirigacha qaytaradi:

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])
# 	
# Salbiy indekslar diapazoni
# Qidiruvni ro'yxatning oxiridan boshlamoqchi bo'lsangiz, salbiy indekslarni ko'rsating:

# Misol
# Bu misol "apelsin" (-4) dan elementlarni qaytaradi, lekin "mango" (-1) ni o'z ichiga olmaydi:

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])
# Ob'ekt mavjudligini tekshiring
# Ro'yxatda ko'rsatilgan element mavjudligini aniqlash uchun inkalit so'zdan foydalaning :

# Misol
# Ro'yxatda "olma" mavjudligini tekshiring:

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")
# # =============================================================================
# # 
# # =============================================================================
# Python - ro'yxat elementlarini o'zgartirish
# Ob'ekt qiymatini o'zgartirish
# Muayyan elementning qiymatini o'zgartirish uchun indeks raqamiga murojaat qiling:

# Misol
# Ikkinchi elementni o'zgartiring:

# thislist = ["apple", "banana", "cherry"]
# thislist[0] = "blackcurrant"
# print(thislist)
# Element qiymatlari oralig'ini o'zgartiring
# Muayyan diapazondagi elementlarning qiymatini 
# o'zgartirish uchun yangi qiymatlar ro'yxatini aniqlang 
# va yangi qiymatlarni kiritmoqchi bo'lgan indeks raqamlari diapazoniga qarang:

# Misol
# "Banan" va "gilos" qiymatlarini "qora smorodina" va "tarvuz" qiymatlari bilan o'zgartiring:

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)
# Agar siz almashtirgandan ko'ra ko'proq element qo'shsangiz ,
#  yangi elementlar siz ko'rsatgan joyga kiritiladi va qolgan elementlar mos ravishda harakatlanadi:

# Misol
# Ikkinchi qiymatni ikkita yangi qiymat bilan almashtiring :

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)
# Eslatma: kiritilgan elementlar soni almashtirilgan 

# elementlar soniga to'g'ri kelmasa, ro'yxatning uzunligi o'zgaradi.

# Agar siz almashtirganingizdan kamroq element qo'shsangiz ,
#  yangi elementlar siz ko'rsatgan joyga kiritiladi va qolgan elementlar mos ravishda harakatlanadi:

# Misol
# Ikkinchi va uchinchi qiymatni bitta qiymatga o'zgartiring:

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)
# Elementlarni kiritish
# Yangi ro'yxat elementini kiritish uchun, mavjud qiymatlarni
#  almashtirmasdan, biz bu insert()usuldan foydalanishimiz mumkin .

# insert()Usuli belgilangan katalog bir narsani qo'shimchalar:

# Misol
# Uchinchi element sifatida "tarvuz" qo'shing:

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)
# Eslatma: Yuqoridagi misol natijasida endi ro'yxatda 4 ta element bo'ladi..

# # =============================================================================
# # 
# # =============================================================================
# Python - ro'yxat elementlarini qo'shish
# Ob'ektlarni qo'shish
# Ro'yxat oxiriga element qo'shish uchun append () usulidan foydalaning:

# Misol
# append()Ob'ektni qo'shish usulidan foydalanib :

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)
# Elementlarni kiritish
# Belgilangan indeksga ro'yxat elementini kiritish uchun insert()usuldan foydalaning .

# insert()Usuli belgilangan katalog bir narsani qo'shimchalar:

# Misol
# Elementni ikkinchi pozitsiya sifatida kiriting:

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)
# Eslatma: Yuqoridagi misollar natijasida endi ro'yxatlar 4 ta banddan iborat bo'ladi.

# Ro'yxatni kengaytirish
# Boshqa ro'yxatdagi elementlarni joriy ro'yxatga qo'shish uchun extend()usuldan foydalaning .

# Misol
# Elementlarini qo'shish tropicaluchun thislist:

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)
# Elementlar ro'yxatning oxiriga qo'shiladi .

# Iterable ni qo'shing
# extend()Usuli qo'shiladigan yo'q ro'yxatlar ,
#  siz (dizilerini silsilasini, lug'atlar va boshqalar) har qanday iterable ob'ektini qo'shishingiz mumkin.

# Misol
# Ro'yxatga qo'shma elementlarni qo'shing:

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# # =============================================================================
# # 
# # =============================================================================
# Python - ro'yxat elementlarini o'chirish
# Belgilangan elementni o'chirish
# remove()Usuli belgilangan ob'ektni tozalaydi.

# Misol
# "Banan" ni olib tashlang:

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)
# Belgilangan indeksni o'chirish
# pop()Usuli belgilangan katalog olib tashlanadi.

# Misol
# Ikkinchi elementni olib tashlang:

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)
# Agar siz indeksni ko'rsatmasangiz, pop()usul oxirgi elementni olib tashlaydi.

# Misol
# Oxirgi elementni olib tashlang:

# thislist = ["apple", "banana", "cherry",'asfgasf']
# thislist.pop()
# print(thislist)
# delKalit so'z ham belgilangan katalog olib tashlanadi:

# Misol
# Birinchi elementni olib tashlang:

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)
# delKalit so'z ham butunlay ro'yxatini o'chirish mumkin.

# Misol
# Butun ro'yxatni o'chirib tashlang:

# thislist = ["apple", "banana", "cherry"]
# del thislist
# Ro'yxatni tozalash
# clear()Usuli ro'yxatini bo'shatmoqda.

# Ro'yxat hali ham saqlanib qolmoqda, lekin uning mazmuni yo'q.

# Misol
# Ro'yxat tarkibini tozalang:

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)
# # =============================================================================
# # 
# # =============================================================================
# Python - Loop ro'yxatlari
# Ro'yxat orqali aylanish
# Ro'yxat elementlarini for pastadir yordamida aylantirishingiz mumkin:

# Misol
# Ro'yxatdagi barcha elementlarni birma -bir chop eting:

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)
# Python For Loops bobida forlooplar haqida ko'proq bilib oling .

# Indeks raqamlari orqali aylanish
# Siz indeks raqamiga murojaat qilib, ro'yxat elementlarini aylanib o'tishingiz mumkin.

# Tegishli takrorlanuvchi yaratish uchun range()va len()funktsiyalaridan foydalaning .

# Misol
# Barcha elementlarni indeks raqamiga qarab chop eting:

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])
# Yuqoridagi misolda yaratilgan iterable [0, 1, 2].


# Vaqt halqasidan foydalanish
# Loop yordamida ro'yxat elementlarini aylanib o'tishingiz mumkin while.

# len()Ro'yxat uzunligini aniqlash uchun funktsiyadan foydalaning , 
# so'ngra 0dan boshlang va indekslariga qarab, ro'yxat elementlari bo'ylab harakatlaning.

# Har bir takrorlashdan keyin indeksni 1 ga oshirishni unutmang.

# Misol
# Barcha whileindeks raqamlarini o'tish uchun pastadir yordamida barcha elementlarni chop eting

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1
# Python while Loops bobida whilelooplar haqida ko'proq bilib oling .

# Ro'yxatni tushunishdan foydalangan holda aylanmoq
# Ro'yxatni tushunish ro'yxatlarni aylantirish uchun eng qisqa sintaksisni taklif qiladi:

# Misol
# forRo'yxatdagi barcha elementlarni chop etadigan qisqa qo'l pastadir:

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# # =============================================================================
# # 
# # =============================================================================
# Python - List Comprehension
# Ro'yxatni tushunish
# Mavjud ro'yxat qiymatlari asosida yangi ro'yxat
#  tuzmoqchi bo'lganingizda ro'yxatni tushunish qisqa sintaksisni taklif qiladi.

# Misol:

# Meva ro'yxatiga asoslanib, siz faqat "a" harfi 
# bo'lgan mevalarni o'z ichiga olgan yangi ro'yxatni xohlaysiz.

# Ro'yxatni tushunmasdan, siz forshartli test bilan bayonot yozishingiz kerak bo'ladi:

# Misol
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "e" in x:
#     newlist.append(x)

# print(newlist)
# Ro'yxatni tushunish bilan siz buni faqat bitta kod satri bilan qilishingiz mumkin:

# Misol
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

# Sintaksis
# newlist = [expression for item in iterable if condition == True]
# Qaytish qiymati yangi ro'yxat bo'lib, eski ro'yxat o'zgarishsiz qoladi.

# Vaziyat
# Ahvoli faqat değerlemek deb mahsulot qabul, bir filtri o'xshaydi True.

# Misol
# Faqat "olma" bo'lmagan narsalarni qabul qiling:

# newlist = [x for x in fruits if x != "apple"]
# Shart if x != "apple" True"olma" dan boshqa barcha
#  elementlar uchun  qaytadi , yangi ro'yxatda "olma" dan boshqa barcha mevalar bor.

# Ahvoli ixtiyoriy va yozilmaydi mumkin:

# Misol
# Hech qanday ifbayonotsiz:

# newlist = [x for x in fruits]
# O'zgaruvchan
# Iterable ro'yxat kabi, har qanday iterable ob'ekt bo'lishi mumkin, nizomning, belgilangan boshqalar

# Misol
# range()Qayta ishlashni yaratish uchun siz funksiyadan foydalanishingiz mumkin :

# newlist = [x for x in range(10)]
# Xuddi shu misol, lekin shart bilan:

# Misol
# Faqat 5 dan past raqamlarni qabul qiling:

# newlist = [x for x in range(10) if x < 5]
# Ifoda
# Ifoda iterasyondaki joriy element hisoblanadi,
#  lekin u ham yangi ro'yxatda bir ro'yxat elementini 
#kabi tugaydi oldin qo'yishi mumkin natija hisoblanadi:

# Misol
# Yangi ro'yxatdagi qiymatlarni katta harf bilan o'rnating:

# newlist = [x.upper() for x in fruits]
# Siz natijani xohlaganingizcha belgilashingiz mumkin:

# Misol
# Yangi ro'yxatdagi barcha qiymatlarni "salom" ga o'rnating:

# newlist = ['hello' for x in fruits]
# Ifoda ham emas, bir filtri kabi, shart-sharoitlar o'z ichiga olishi mumkin, lekin bir yo'li sifatida natijalarini manipulyatsiya qilish:

# Misol
# "Banan" o'rniga "apelsin" ni qaytaring:

# newlist = [x if x != "banana" else "orange" for x in fruits]
# Ifoda misol yuqorida deydi:

# "Banan bo'lmasa, buyumni 
#qaytaring, agar banan bo'lsa, to'q sariq rangga qaytaring".

# # =============================================================================
# # 
# # =============================================================================
# Python - ro'yxatlarni saralash
# Ro'yxatni alfasayısal tartibda saralash
# Ro'yxat ob'ektlarida sort()ro'yxatni sukut bo'yicha alfasayısal, o'sish bo'yicha saralaydigan usul mavjud:

# Misol
# Ro'yxatni alifbo tartibida tartiblang:

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)
# Misol
# Ro'yxatni raqamli tartibda saralash:

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)
# Kamayish tartibida
# Kamayishni 
#tartiblash uchun argument kalit so'zidan foydalaning reverse = True:

# Misol
# Ro'yxatni pastga qarab saralash:

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)
# # Misol
# Ro'yxatni pastga qarab saralash:

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)
# # =============================================================================
# # 
# # =============================================================================
# Python - ro'yxatlarni nusxalash
# Ro'yxatni nusxalash
# Siz ro'yxatni shunchaki yozib nusxa ko'chira
#  olmaysiz list2 = list1, chunki: list2faqat havola 
#  bo'ladi list1va kiritilgan o'zgartirishlar 
#list1avtomatik ravishda kiritiladi list2.

# Nusxa ko'chirishning usullari bor, bir yo'li-o'rnatilgan List usulidan foydalanish copy().

# Misol
# copy()Usul yordamida ro'yxatning nusxasini yarating :

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)
# Nusxa ko'chirishning yana bir usuli-o'rnatilgan usuldan foydalanish list().

# Misol
# list()Usul yordamida ro'yxatning nusxasini yarating :

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)
# # =============================================================================
# # 
# # =============================================================================
# Python - ro'yxatga qo'shilish
# Ikki ro'yxatga qo'shilish
# Python -da ikki yoki undan ortiq ro'yxatga 
# qo'shilish yoki birlashtirishning bir necha yo'li mavjud.

# Eng oson usullardan biri + operatordan foydalanishdir .

# Misol
# Ikki ro'yxatga qo'shiling:

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)
# Ikki ro'yxatga qo'shilishning yana 
# bir usuli - list2 -dagi barcha elementlarni birma -bir ro'yxatga qo'shish:

# Misol
# List2 ro'yxatini1 ro'yxatiga qo'shing:

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list1:
#   list2.append(x)

# print(list2)
# Yoki siz extend() bitta ro'yxatdagi 
# elementlarni boshqa ro'yxatga qo'shish usulini ishlatishingiz mumkin :

# Misol
# extend()List1 oxiriga list2 qo'shish uchun usuldan foydalaning :

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)
# # =============================================================================
# # 
# # =============================================================================

# Python - ro'yxat usullari
# Ro'yxat usullari
# Python-da ro'yxatlarda foydalanishingiz mumkin bo'lgan o'rnatilgan usullar to'plami mavjud.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
# # =============================================================================
# # 
# # =============================================================================

