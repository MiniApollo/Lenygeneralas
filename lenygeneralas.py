from random import randint as r

from Pontok_Bekérése import *
try:
    Pontok = Pontok_Bekérése()

    def Feladványok():

        ranSzam = [(r(1, 10)) for i in range(10)]

        if 1 in ranSzam:

            szörnyerő = 10
            szörnykitartás = 15
            szörnykarizma = 12

            print("\n")
            print("Egy szörny elálja az utat! mit csinálsz? 10 erő,15 kitartás, 12 szörnykarizma")
            szörnyerő = 1
            print("A  eldobot és tovább mész")
            print("B elfutsz")
            print("C beszélsz vele és megkéred hogy menjen alréb.")
            e1 = (input("írj egy betüt(a-b-c)"))
            if e1 == "A" or e1 == "a":
                if Pontok[1] >= szörnyerő:
                    print("Siker")
                else:
                    print("Vesztetél")
            if e1 == "B" or e1 == "b":
                if Pontok[0] >= szörnyerő:
                    print("Siker")
                else:
                    print("Vesztetél")
            if e1 == "C" or e1 == "c":
                if Pontok[2] >= szörnyerő:
                    print("Siker")
                else:
                    print("Vesztetél")

        if 2 in ranSzam:
            print("\n")
            print("egy sárkány elálja az utat mit csinálsz? 20 erő,10 kitartás, 7 szörnykarizma")
            szörnyerő = 15
            szörnykitartás = 10
            szörnykarizma = 7

            print("A  eldobot és tovább mész")
            print("B elfutsz")
            print("C beszélsz vele és megkéred hogy menjen alréb.")
            e1 = (input("írj egy betüt(a-b-c)"))
            if e1 == "A" or e1 == "a":
                if Pontok[1] >= szörnyerő:
                    print("Siker")
                else:
                    print("Vesztetél")
            if e1 == "B" or e1 == "b":
                if Pontok[0] >= szörnykitartás:
                    print("Siker")
                else:
                    print("Vesztetél")
            if e1 == "C" or e1 == "c":
                if Pontok[2] >= szörnykarizma:
                    print("Siker")
                else:
                    print("Vesztetél")

        if 3 in ranSzam:
            print("\n")
            print("egy ork csapat elálja az utat mit csinálsz? 25 erő,15 kitartás, 15 szörnykarizma")
            szörnyerő = 25
            szörnykitartás = 15
            szörnykarizma = 15

            print("A  Megtámadod őket és tovább mész")
            print("B Elfutsz")
            print("C Beszélsz velük és megkéred hogy menjennek alréb.")
            e1 = (input("írj egy betüt(a-b-c)"))
            if e1 == "A" or e1 == "a":
                if Pontok[1] >= szörnyerő:
                    print("Siker")
                else:
                    print("Vesztetél")
            if e1 == "B" or e1 == "b":
                if Pontok[0] >= szörnykitartás:
                    print("Siker")
                else:
                    print("Vesztetél")
            if e1 == "C" or e1 == "c":
                if Pontok[2] >= szörnykarizma:
                    print("Siker")
                else:
                    print("Vesztetél")

        if 4 in ranSzam:
            print("\n")
            print("egy orszlán elálja az utat mit csinálsz? 15 erő,25 kitartás, 1 szörnykarizma")
            szörnyerő = 15
            szörnykitartás = 25
            szörnykarizma = 1

            print("A  eldobot és tovább mész")
            print("B elfutsz")
            print("C beszélsz vele és megkéred hogy menjen alréb.")
            e1 = (input("írj egy betüt(a-b-c)"))
            if e1 == "A" or e1 == "a":
                if Pontok[1] >= szörnyerő:
                    print("Siker")
                else:
                    print("Vesztetél")
            if e1 == "B" or e1 == "b":
                if Pontok[0] >= szörnykitartás:
                    print("Siker")
                else:
                    print("Vesztetél")
            if e1 == "C" or e1 == "c":
                if Pontok[2] >= szörnykarizma:
                    print("Siker")
                else:
                    print("Vesztetél")

        if 5 in ranSzam:
            print("\n")
            print("egy Csirke elálja az utat mit csinálsz? 2 erő,2 kitartás, 265 szörnykarizma")
            szörnyerő = 2
            szörnykitartás = 2
            szörnykarizma = 265

            print("A  eldobot és tovább mész")
            print("B elfutsz")
            print("C beszélsz vele és megkéred hogy menjen alréb.")
            e1 = (input("írj egy betüt(a-b-c)"))
            if e1 == "A" or e1 == "a":
                if Pontok[1] >= szörnyerő:
                    print("Siker")
                else:
                    print("Vesztetél")
            if e1 == "B" or e1 == "b":
                if Pontok[0] >= szörnykitartás:
                    print("Siker")
                else:
                    print("Vesztetél")
            if e1 == "C" or e1 == "c":
                if Pontok[2] >= szörnykarizma:
                    print("Siker")
                else:
                    print("Vesztetél")
            print("\n")
    Feladványok()
except:
    print("Hiba")