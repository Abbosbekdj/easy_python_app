# 09/05/2025

"""
4. Bahoni harf bilan ifodalash
Foydalanuvchi 0 dan 100 gacha baho kiritadi:
"""

print("Baholashni chet el standarti asosida qilamiz \nyani o'quvchi olgan ballga qarab uni harflar orqali ifodalaymiz!")

user = input("O'quvchining yoki talabaning to'plagan ballini kiriting - ")

try:
    u = float(user)
    print(f"Siz kiritgan ball - {u} 'Ball'")
    if (not 0<= u <= 100):
        print("Son 0 va 100 oralig'ida bo'lishi kerak esdan chiqarmang")
    elif (u >= 90):
        print("Siz kiritgan talabaning bali 90 va 100 ball orasida shunday ekan\nuning darajasi eng yuqori 'A' :)")
    elif (u >= 80):
        print("Siz kiritgan talaba bali 80 va 89 orasida uning darajasi 'B' :)")
    elif (u >= 70):
        print("Siz kiritgan talaba bali 70 va 79 orasida uning darajasi 'C' :|")
    elif (u >= 60):
        print("Siz kiritgan talaba bali 60 va 69 orasida uning darajasi 'D' :|")
    elif (u >= 50):
        print("Siz kiritgan talaba bali 50 va 59 orasida uning darajasi 'E' :(")
    else:
        print("Siz kiritgan talaba bali 0 va 49 orasida uning darajasi 'F' :(")
except ValueError:
    u = user
    print(f"Siz kiritgan talaba bali {u} bu string uni men sonlar orasida tekshira olmayman!")
