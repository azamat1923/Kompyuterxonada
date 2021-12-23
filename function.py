# # -*- coding: utf-8 -*-
# """
# Created on Thu Aug 12 10:41:49 2021

# @author: Rafiqov Abulqosim
# """
# def test():
#     print("men funksiyaman")
    
# test()

# Python funktsiyalari
# Funktsiya - bu faqat chaqirilganda ishga tushadigan kod bloki.

# Siz parametr sifatida ma'lum bo'lgan ma'lumotlarni funktsiyaga o'tkazishingiz mumkin.

# Natijada funktsiya ma'lumotlarni qaytarishi mumkin.

# Funktsiyani yaratish
# Pythonda funktsiya def kalit so'z yordamida aniqlanadi :

# # Misol
# def my_function():
    
#   print("Hello from a function")
  
# def salom_ber():
#     '''Salom beruvchi funksiya'''
#     print("assalomu alaykum")
# def hello(f_name, l_name, age):
    
#     print("Hello " + f_name  + " " + l_name)
#     print('you are ' + str(age) + ' years old')
#     print('have a nice day!')
# hello('Abulqosim', 'rafiqov', 19)
    






# Funktsiyani chaqirish
# Funktsiyani chaqirish uchun funktsiya nomidan keyin qavsdan foydalaning:

# Misol
# def my_function():
#   print("Hello from a function")

# my_function()
# Argumentlar
# Ma'lumotni argument sifatida funktsiyaga o'tkazish mumkin.

# Argumentlar funktsiya nomidan keyin, qavs ichida ko'rsatiladi.
#  Siz xohlagancha argumentlarni qo'shishingiz mumkin, 
#  ularni vergul bilan ajratib qo'yish kifoya.

# Quyidagi misolda bitta argumentli funksiya mavjud (fname). 
# Funktsiya chaqirilganda, biz to'liq ismni chop etish uchun funktsiya ichida ishlatiladigan ismni beramiz:

# Misol
# def my_function(fname):
    
#   print(fname + " Rafiqov")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")
# Dalillar ko'pincha qisqartiriladi etiladi args Python hujjatlarni ham.


# Parametrlar yoki dalillar?
# Parametr va argument atamalari xuddi shu narsa uchun ishlatilishi mumkin: 
#     funktsiyaga uzatiladigan ma'lumotlar.

# Funktsiya nuqtai nazaridan:

# Parametr - bu funktsiya ta'rifidagi qavs ichida ko'rsatilgan o'zgaruvchi.

# Argument - bu funktsiya chaqirilganda yuboriladigan qiymat.

# Argumentlar soni
# Odatiy bo'lib, funktsiyani to'g'ri argumentlar soni bilan chaqirish kerak.
#  Bu shuni anglatadiki, agar sizning funktsiyangiz 2 ta argumentni kutsa,
#  siz funktsiyani 2 argument bilan chaqirishingiz kerak, ko'p emas, kam emas.

# Misol
# Bu funksiya 2 ta argumentni kutadi va 2 ta argumentni oladi:

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")
# Agar siz funktsiyani 1 yoki 3 argument bilan chaqirishga harakat qilsangiz, sizda xato bo'ladi:
# Misol
# Bu funksiya 2 ta argumentni kutadi, lekin faqat 1 oladi:

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil",'kagasg')
# Ixtiyoriy argumentlar, *args
# Agar siz funktsiyangizga qancha dalillar kiritilishini bilmasangiz *, 
# funksiya ta'rifiga parametr nomidan oldin qo'shing .

# Bu yo'l funksiya olasiz nizomning argumentlar, va shunga ko'ra ma'lumotlar kirishingiz mumkin:

# Misol
# Agar argumentlar soni noma'lum bo'lsa, *parametr nomidan oldin a qo'shing :

# def my_function(*kids):
#   print("The youngest child is " + kids[0])

# my_function("Emil", "Tobias", "Linus")
# Ixtiyoriy argumentlar ko'pincha Python hujjatlarida *argilarga qisqartiriladi .

# Kalit so'z argumentlari
# Siz argumentlarni key = value sintaksisi bilan yuborishingiz mumkin .

# Shunday qilib, argumentlarning tartibi muhim emas.

# Misol
# =============================================================================
# # def my_function(child3, child2, child1):
# #   print("The youngest child is " + child1)
# 
# # my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# =============================================================================
# def add(num1, num2,num3):
#     sum = num1 + num2 + num3
#     return sum 
# print(add(1,2,3))

# Kalit so'zlar argumentlari iborasi ko'pincha Python hujjatlarida kvarglarga qisqartiriladi .

# O'zboshimchalik bilan kalit so'z argumentlari, ** kwargs
# Agar siz funktsiyangizga qancha kalit so'z argumentlari kirishini bilmasangiz, 
# ikkita yulduzcha qo'shing: **funktsiya ta'rifidagi parametr nomidan oldin.

# Shunday qilib, funktsiya argumentlar lug'atini oladi va mos ravishda elementlarga kira oladi:

# Misol
# Agar kalit so'z argumentlari soni noma'lum bo'lsa, **parametr nomidan oldin dubl qo'shing :

# def my_function(**kid):
#   print("His first name is " + kid["fname"])

# my_function(fname = "Tobias", lname = "Refsnes")
# O'zboshimchalik bilan Kword argumentlari Python hujjatlarida ** kvarglarga qisqartiriladi .

# Standart parametr qiymati
# Quyidagi misol standart parametr qiymatidan qanday foydalanishni ko'rsatadi.

# Agar biz funktsiyani argumentsiz chaqirsak, u standart qiymatdan foydalanadi:

# Misol
# def my_function(country = "Uzbekistan"):
#   print("I am from " + country)
  
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")
# Ro'yxatni argument sifatida o'tkazish
# Siz har qanday turdagi argumentlarni funktsiyaga yuborishingiz mumkin
#  (satr, raqam, ro'yxat, lug'at va boshqalar) 
#  va u funktsiya ichidagi bir xil ma'lumotlar turi sifatida ko'rib chiqiladi.

# Masalan, agar siz ro'yxatni argument sifatida yuborsangiz,
#  u funktsiyaga etib kelganida ham ro'yxat bo'lib qoladi:

# Misol
# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)
# Qaytish qiymatlari
# Funktsiya qiymatni qaytarishi uchun quyidagi return iborani ishlating:

# Misol
# def my_function(x):
#   return 5 ** x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))
# O'tish bayonoti
# functionta'riflar bo'sh bo'lishi mumkin emas, 
# lekin agar sizda biron sababga ko'ra functionmazmuni 
# bo'lmagan ta'rif bo'lsa pass, xatoga yo'l qo'ymaslik uchun bayonotga qo'ying .
# num = input("enter a whole positive number:")
# num = float(num)
# num = abs(num)
# num =round(num)
# print(num)
# Misol
# def myfunction():
#   pass
# Rekursiya
# Python shuningdek, funktsiyalarning rekursiyasini qabul qiladi, 
# ya'ni belgilangan funksiya o'zini o'zi chaqira oladi.

# Rekursiya - umumiy matematik va dasturlash tushunchasi. 
# Bu shuni anglatadiki, funktsiya o'zini o'zi chaqiradi. 
# Buning ma'nosi shundaki, siz natijaga erishish uchun ma'lumotlarni aylanib o'tishingiz mumkin.

# Ishlab chiquvchi rekursiya bilan juda ehtiyot bo'lishi 
# kerak, chunki hech qachon tugamaydigan yoki xotira yoki protsessor
#  quvvatidan ortiqcha foydalanadigan funktsiyani yozish juda oson. 
#  Biroq, to'g'ri yozilganda, rekursiya dasturlash uchun juda samarali
#  va matematik jihatdan oqlangan yondashuv bo'lishi mumkin.

# Bu misolda, tri_recursion () - bu biz o'zini chaqirish uchun 
# belgilagan funksiya ("qaytalanish"). Ma'lumot sifatida biz
#  k o'zgaruvchisidan foydalanamiz , u har safar
#  qaytganimizda ( -1 ) kamayadi. Rekursiya 0 dan katta bo'lmagan sharoitda tugaydi (ya'ni 0 bo'lganda).

# Yangi ishlab chiquvchi uchun bu qanday ishlashini 
# aniqlash uchun biroz vaqt ketishi mumkin, 
# buni aniqlashning eng yaxshi usuli - uni sinab ko'rish va o'zgartirish.

# Misol
# Rekursiya misoli

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)
# # =============================================================================
# # 
# # =============================================================================






