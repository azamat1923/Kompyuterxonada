mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:    
    print(mehmon)
mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:    
    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")    
    print("Hurmat bilan, Palonchiyevlar oilasi")
sonlar = list(range(1,11))
for son in sonlar:    
    print(f"{son} ning kvadrati {son**2} ga teng")
sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
for son in sonlar:  # sonlar dagi har bir son uchun    
    sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz
    print(sonlar)
    print(sonlar_kvadrati)
"""a=int(input('Son kiriting='))
yig=0
for son in range(0,a):
    yig+=son
print('0 dan ',a,' gacha sonlar yig\'indisi ',yig+a,' ga teng')
yig=1
for son in range(1,a):
    yig*=son
print('1 dan ',a,' gacha sonlar ko\'paytmasi ',yig*a,' ga teng')"""
n=int(input("n sonini kiriting: "))
m=[]
for i in range(1,n+1,1):
	if n%i==0:
        m.insert(-1, i)
        print(i)