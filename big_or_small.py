"""
3. Ikki sondan kattasini topish
Ikkita son kiritiladi, qaysi biri katta ekanligini aniqlab ekranga chiqarish.
"""

print("\nKeling endi siz 2 ta son kriting men esa")
print("qaysi biri kattaligini topaman!\n")

user2 = input("Birinchi butun sonni kiriting: ")
user3 = input("Ikkinchi butun sonni kiriting: ")

try:
    u2 = int(user2)
    type_u2 = "Butun son"
except ValueError:
    try:
        u2 = float(user2)
        type_u2 = "Haqiqiy son"
    except ValueError:
        u2 = user2
        type_u2 = "String"
try:
    u3 = int(user3)
    type_u3 = "Butun son"
except ValueError:
    try:
        u3 = float(user3)
        type_u3 = "Haqiqiy son"
    except ValueError:
        u3 = user3
        type_u3 = "String"

print("\n1-kiritilgan qiymat", u2)
print("2-kiritilgan qiymat", u3)

if (type_u2 in ["Butun son", "Haqiqiy son"] and type_u3 in ["Butun son", "Haqiqiy son"]):
    if (u2 > u3):
        print(f"\nSiz kiritgan sonlardan birinchisi {u2} soni ikkinchi kiritgan {u3} soningizdan katta :)")
        
    elif (u2 < u3):
        print(f"\nSiz kiritgan sonlardan ikkinchi {u3} soni va birinchi kiritgan {u2} soningizdan katta!")
        
    else:
        print(f"Siz kiritgan sonlardan birinchi {u2} soni va ikkinchi kiritgan {u3} soni ikkalasi teng!")
else:
    print("qaysidir bittasi son emas")