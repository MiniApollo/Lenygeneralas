def Pontok_Bekérése():

    pontok = 25

    print(pontok, " pontod van")

    kitartas = int(input("A kitartásod értéke: "))
    pontok -= kitartas
    if pontok < 0:
        print("Elfogytak a pontjaid")
        e0 = input("előről kezded a játékot(Y/N): ")
        if e0 == "Y" or e0 == "y":
            pontok = 25
            Pontok_Bekérése()
        else:
            print("Köszönöm, hogy a játékkal játszottál")
            exit()

    print(pontok, " pontod van")

    ero = int(input("Az Erősséged értéke: "))

    pontok -= ero
    if pontok < 0:
        print("Elfogytak a pontjaid")
        e0 = input("előről kezded a játékot(Y/N): ")
        if e0 == "Y" or e0 == "y":
            pontok = 25
            Pontok_Bekérése()
        else:
            print("Köszönöm, hogy a játékkal játszottál")
            exit()
    print(pontok, " pontod van")

    karizma = int(input("A karizmatikuságod értéke: "))

    pontok -= karizma
    if pontok < 0:
        print("Elfogytak a pontjaid")
        e0 = input("előről kezded a játékot(Y/N): ")
        if e0 == "Y" or e0 == "y":
            pontok = 25
            Pontok_Bekérése()
        else:
            print("Köszönöm, hogy a játékkal játszottál")
            exit()

    print(pontok, " pontod van")

    turelem = int(input("A türelmed értéke: "))

    pontok -= turelem
    if pontok < 0:
        print("Elfogytak a pontjaid")
        e0 = input("előről kezded a játékot(Y/N): ")
        if e0 == "Y" or e0 == "y":
            pontok = 25
            Pontok_Bekérése()
        else:
            print("Köszönöm, hogy a játékkal játszottál")
            exit()

    print(pontok, " pontod van")

    erzelmek = int(input("Az érzelmed értéke: "))

    pontok -= erzelmek
    if pontok < 0:
        print("Elfogytak a pontjaid")
        e0 = input("előről kezded a játékot(Y/N): ")
        if e0 == "Y" or e0 == "y":
            pontok = 25
            Pontok_Bekérése()
        else:
            print("Köszönöm, hogy a játékkal játszottál")

            exit()

    print("A játék elkezdödött")
    return [kitartas, ero,karizma, turelem, erzelmek]