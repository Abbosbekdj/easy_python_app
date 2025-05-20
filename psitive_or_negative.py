"""
2. Musbat, manfiy yoki nol
Foydalanuvchidan son qabul qilib, u musbat, manfiy yoki nol ekanligini aniqlash.
"""

print("Keling endi sonni musbat yoki manfiyligini topish o'ynaymiz! \n")

user = input("Istalgan son kiriting: ")

try:
    u1 = int(user)
    type_u1 = "Butun son"
    print(f"Siz kirtigan qiymat {type_u1} ekan endi uni tekshirishga o'tamiz")
    if (u1 > 0):
        print(f"Siz kiritgan qiymat ya'ni {u1} - soni musbat :)")
    elif (u1 == 0):
        print(f"Siz kiritgan qiymat ya'ni {u1} - qiymati u musbat ham emas manfiy ham emas :|")
    else:
        print(f"Siz kritgan qiymat ya'ni {u1} - soni manfiy :)")
except ValueError:
    try:
        u1 = float(user)
        type_u2 = "Haqiqiy son"
        print(f"Siz kirtigan qiymat {type_u2} ekan endi uni tekshirishga o'tamiz")
        if (u1 > 0):
            print(f"Siz kiritgan qiymat ya'ni {u1} - soni musbat :)")
        elif (u1 == 0):
            print(f"Siz kiritgan qiymat ya'ni {u1} - qiymati u musbat ham emas manfiy ham emas :|")
        else:
            print(f"Siz kritgan qiymat ya'ni {u1} - soni mafiy :)")
    except ValueError:
        u1 = user
        type_u1 = "String"
        print(f"Siz kiritgan qiymat ya'ni {u1} - string ya'ni matn yoki belgi uning ustida bunday mantiqlar noo'rin!!!")
        

    
# if (u1 > 0):
#     print(f"Siz kiritgan {user} soni musbat")
    
# elif (u1 == 0):
#     print(f"Siz kiritgan {user} soni buni musbat ham manfiy ham deya olmayman")
    
# else:
#     print(f"Siz kiritgan {user} soni manfiy")
