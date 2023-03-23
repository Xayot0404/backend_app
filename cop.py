#string methods

# lst = ["anor", "banan", "nok", "uzum",]

# def boshxarf(item):
#     for items in item:
#         print(items.upper())


# boshxarf(lst)    


# text = "B\tu\tg\tu\tn"
# x = text.expandtabs(10)

# print(x)



# x = text.center(100)
# print(x)

# print(text.replace("yomon","zor").replace("hohlamayman", "hohlayman"))
# lst = ['b','a','t','s','d','e','f','g']
# def harf(item):
#    item.sort()
#    print(item)
# # harf(lst)    
# m = "Salom"
# toliqism = ("eshpolatov abror kamoliddin ogli")
# print(len(toliqism))

# toliqism = ("eshpolatov abror kamoliddin ogli")
# print(toliqism.replace(' ', '_'))

# print(text.center(10, "*")) bu kiritilgan qiymatni ortaga qoyib beradi yani markazga 
# print(text.count('u')) textni ichidagi harflarni qiymatini sanaydi 
# print(m.expandtabs(10)) textga tab tashab beradu
# print(text.endswith("yomon")) textni qiymatini oxiridaligini chiqarib beradi 
# print(text.format()) qiymatni textga qoyib beradi 
# print(text.find("juda")) qiymatni indexini qayerdan boshlanishini beradi
# print(text.rfind("Bugun")) #qiymatni o'ng tarafdan indexini beradi
# print(text.join()) qiymatga joylaydi
# print(text.index()) indexini sanab beradi 
# print(text.rindex()) ong tarafdan sanab beradi 
# print(text.islower()) qiymatni hamma harflari kichkinaligini tekshiradi # eslatma is bn boshlangan kodlar textni tekshirib chiqadi
# print(text.upper()) hamma harflar katta qilib beradi 
# print(text.isupper()) hamma harflar kattaligini tekshirib chiqadi 
# # x = "'\\ backslash'" joy tashlab beradi yana \n, \b , \t lari bor 
# print(text[1::2])  bu ham muhim lekn chunmadim organvolaman
# print(text.isalnum()) qiymatda numberlarini tekshiradi 
# print(text.isnumeric()) bu ham qiymatda numberlar borini tekshiradi
# print(text.isspace()) bu tab borligini tekshiradi 
# m = "Salom"
# # x = m.strip() 
# # print('\\', x,)
# # print(text.rstrip()) bu ong tarafga qoyib beradi
# # print(text.rjust())
# x = m.rjust(10) ong tarafga kiritilgan qiymatga tab tawab beradi 
# print(x, 'yaxwimisan')

# dict methods
#keys, valuesi

# dct = {"ism": "Abror", "yoshi": 24, "talabami": False }
# print(dct["yoshi"])
# key = "Salom"
# value = 45
# m = dict.fromkeys(key, value)
# print(m)
# dct["fam"] = "Eshpolatov"
# dct["yoshi"] = 24
# print(dct.keys())  bu keylarini topadi
# print(dct.values()) bu valuesini topado
# dct.pop("ismi") berilgan qiymatni ochiradi 
# dct.clear()  butunlay ochiradi 
# print(dct.get("ismi")) tekshirib chiqdi 
# dct1 = dct.copy() kopiya qiladi
# for x in dct.values():
#     if type(x) == str:
#         print(x)
# print(dct)        
# lst = [
#     {"name": "apple", "narxi": "1200", "color": "gold" "ary": ["oq", "qora"]},
#     {"name": "samsung", "narxi": "500", "color": "oq"},
#     {"name": "Redmi", "narxi": "300", "color": "qora"}

# ]
# lst[0]["narxi"]+=0
# lst[1]["narxi"]+=0
# lst[2]["narxi"]+=0
# print(lst)
# newary = lst[0]["ary"]
# newary.append("Purple")
# for x in lst:
#     x["narxi"] += 2045
#     x.pop("color")
#     print(x)
# args, kwargs
# a = 24
# b = 45
# c = 54
# d = 343
# def x (*args):
#     print(args)
# x(a,b,c,d)
# lst = ["olma", "banan", "nok"]
# newlist = [*lst]
# for n in lst:
#     print(n)
# print(*lst) # Abstrakt
# for i in range(1,10):
#     for j in range(i):
#          print(1, end=' ')


#   nech kun yashagan
# person = int(input("yoshingizni kiriting "))
# def yoshi(personage):
#     tugulganyil = 2023 - personage
#     tugulganoy = personage * 12
#     tugulganhafta = (personage *365) // 7
#     yashagankun = personage * 365
#     yashagansoat = (personage * 365) * 24
#     print(f"Salom siz {tugulganyil} yilda tugulgansiz va {tugulganoy} oy , {tugulganhafta} hafta, {yashagankun} kun , {yashagansoat} da yashadiz")

# yoshi(person




# import random
# # number = [3,4,7,8,9,10,23,34,25,76,87,55,99,65,54,32,12,21,98,89,76,77,80]
# # son = [3,4,7,8,9,10,23,34,25,76,87,55,99,65,54,32,12,21,98,89,76,77,80]

# for m in range(20):
#     x = random.randint(1,20)
#     y = random.randint(1,30)
#     son = int(input(f"{x} x {y} = "))
#     if son == x*y:

#      print("Togri")
#     else:
#      print("Xatobosh")    



# for x in range(2,50):
#     son = int(input(f"{x} x {7} = "))
#     if son == x*7:
#         print("togri")
#     else:
#         print("xato")    



# mevalar = ["banan","ananas","blueberry","tarvuz", "qovun", "pamidor",
#            "qulupnay","olma","kiwi","mandarin","apelsin","orik","shaftoli","mango","uzum"]


# holmeva = []
# polizmeva = []

# for meva in mevalar:
#     if meva == "tarvuz":
#         polizmeva.append(meva)
#     elif meva == "qovun":
#         polizmeva.append(meva)
#     elif meva == "pamidor": 
#         polizmeva.append(meva)   
#     else:
#         holmeva.append(meva)

# print(holmeva)
# print(polizmeva)            


        
# dct = [{"meva": "olma","polizmeva": "Tarvuz"},
#        {"meva": "banan","polizmeva": "Qovun"},
#        {"meva": "ananas","polizmeva": "kartoshka"},
#        {"meva": "kiwi","polizmeva": "Karam"},
#     ]

# for m in dct:
#     holmeva.append(m["meva"].title())
#     polizmeva.append(m["polizmeva"].title())
# print(holmeva)
# print(polizmeva)    

# def narsa(*item):
#     sum = 0
#     for sum in item:
#         print("true")

# narsa([0,4,5,6,7,8])    


# def summa(*sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi

# print(summa(1,2,3,4,5))
# print(summa(2,4,5,6,7,8,9))
# print(summa(100,2323,454))
    

# #
# def avto_info(kompaniya, model, **malumot):
#     malumot['kompaniya']= kompaniya
#     malumot['model']= model
#     return malumot
# avto1 = avto_info("GM","Cobolt",rangi = "Oq", yili = '2023')
# avto2 = avto_info("Hyundai","Seltos",rangi ='mokriy', narxi=35000)
# print(avto1)
# print(avto2)



# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()} ning bahosini kiriting ")
#         baholar[ism]=baho
#     return baho
# talabalar = ['Mohira','Sevinch','Muslina','Abbos']
# baholar = bahola(talabalar)
# print(baholar)









