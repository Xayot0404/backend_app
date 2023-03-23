
def summa(*sonlar):
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi

print(summa(1,2,3,4,5))
print(summa(2,4,5,6,7,8,9))
print(summa(100,2323,454))
    


def avto_info(kompaniya, model, **malumot):
    malumot['kompaniya']= kompaniya
    malumot['model']= model
    return malumot
avto1 = avto_info("GM","Cobolt",rangi = "Oq", yili = '2023')
avto2 = avto_info("Hyundai","Seltos",rangi ='mokriy', narxi=35000)
print(avto1)
print(avto2)

lst = ["Abror","Abbos","Bobur"]
if lst(type) == str:
    print("True")



