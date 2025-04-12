# 11/04/25

"""
1. Sonning juft yoki toq ekanligini aniqlash
Foydalanuvchidan bir son kiriting. Agar son juft bo‘lsa, "Juft son", aks holda "Toq son" deb chiqarish.
"""

print("Assalomu alaykum! \n")
print("Keling siz bilan bir o'yin o'ynaymiz 🤔 \n",'\n'"ya'ni sonnig juft yoki toqligini topamiz! \n")

user = input("Istalgan sonni kiritng: ")

try:
    u = int(user)
    type_u = "Butun son"
except ValueError:
    try:
        u = float(user)
        type_u = "Haqiqiy son"
    except ValueError:
        u = user
        type_u = "String !!!"
        
print(f"Siz kiritgan qiymat - {type_u}")



if (u == 0):
    print(f"Siz kiritgan {u} soni juft deb atash mumkin agar shunday atash to'g'ri bo'lsa")
elif (u == str(user)):
    print("BU string uni songa bo'lib bo'lmaydi !!!!!")
else:
    if (u % 2 == 0):
        print(f"Siz kiritgan qiymat {u} soni juft son")
    else:
        print(f"Siz kiritgan qiymat {u} soni toq son")

