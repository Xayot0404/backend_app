
# narx = int(input("Somsa narxi nech pul?"))
# def m(narxi):
#     if narxi > 3000:
#         print("Qimmat")
#     else:
#         print("Arzon")




# m(narx)


# lst = ["Abror","Somsa","Sevinch","Abbos","Anor","Banan", 2, 5, 14, 66, 85, 65, 55, True, False]

# def m(item):
#     for x in item:
#         if type(x) == str:
#             print(x)
# m(lst)        

# parol = input("Parolni kiriting")
# def a(item):
#     for x in item:
#         if item == "sarimsoqpiyoz":
#             print("Assalomu aleykum")
#         else:
#             print("Xato")
            

# a(parol)    



# lst = ["Anor","Banan","Muzqaymoq","Kiwi"]
# lst2 = []

# def k(item):
#     for x in item:
#          lst2.append (x)
#     print(lst2)        
    
# k(lst)


# colanarxi = int(input("Cola narxi"))
# def m(narxi):
    
#         if narxi == 15000:
#          print("2 litrli bervorin")
#         else:
#          print("1.5 liga pulim yetarkan")
# m(colanarxi)    


# def toliqism(ism, familiya):
#     print(f"Foydalanuvchini ismi: {ism.title()}\n" 
#           f"Foydalanuvchini familiyasi: {familiya.title()}")



# toliqism('abror', 'eshpolatov')
 

# def yosh_hisobla(ism, tugilgan_yil):
#     print(f"{ism.title()} {2022-tugilgan_yil} yoshda")

# yosh_hisobla('muslima',2020)

# import math
# import random

# lst = ["Fayzullo", "Amir", "Parviz", "Sulton", "Komil", "Said", "Sobif", "Osmon", "Umar", "Jovonir", "Hamza", "Rahim", "Najim"]
# rndm = random.choice(lst)

# print(rndm)

# parol = input ("Ismingizni kiriting")
# def m(item):
#     if m == "Ahmad":
#         print("Salom oga")
#     else:
#         print("Nima gap")   
# m(parol)
# import math
# import random
# rndm = random.random()*190
# print(math.trunc(rndm))

# sqrt = math.sqrt(100)
# print(sqrt)


# foyda = int(input("Qancha pulingiz bor?"))
# kiyim = 50000
# if foyda >= kiyim:
#     print("Sotib oldingiz")
# else:
    # print("pulingiz yetmadi")


# // list methods


# lst = ["anor", "banan", "nok", "Kiwi","uzum"]
# lst1 = [12,55,56,1,2,9,7,3,100,48,66]
# copy_list = lst.copy()


# lst.pop(2) index boyicha ochirib beradi
# lst.remove("olma") value boyicha ochiradi
# lst.reverse() qiymati boyicha ochiradi
# lst.sort() sortlab beradi alvafit boyicha number osuvchi tartibda
# index, element
# lst.insert(2, "Tarvuz") index boyicha qoshadi
# natija = lst.count("anor") valueni sanab beradi nechtaligini
# natija = lst.index("anor") valueni indexini chiqaradi
# lst.append("mandarin") lstni oxiridan qoshadi 
# lst.clear() butunlay ochirib tashlaydi
# lst1.extend(lst) copiya qiladi
# lst1.sort()
# print(lst1)
# lst1 = [12,55,56,1,2,9,7,3,100,48,66]

# # def kamayuvchi(newlist):
# #    newlist.sort()
# #    newlist.reverse()
# #    newlist.append(50000)
# #    print(newlist)

# # kamayuvchi(lst1)  
# m = []  
# def extends(item):
#     m.extend(item)
# extends(lst1)

# # toq = []
# juft = []


# # def remov(items):
# #     for x in items:
# #         if x % 2 != 0:
# #             toq.append(x)
# #         else:
# #             juft.append(x)
# # remov(m)    

# # print(toq.clear())
# # print(juft)

# # print(m)
# def Juft(jft):
#     jft.insert(0, 88)
#     for y in jft:
#         if y % 2 == 0:
#             juft.append(y)
# Juft(m)            
# print(juft)        
