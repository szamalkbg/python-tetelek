def eldontes_tetel():
    print("\nszám: ", end="")
    n = int(input(""))
    prim = False
    if n < 2:
        prim = False
    else:
        i = 2
        while i <= n**0.5 and n % i != 0:
            i += 1
        prim = i > n**0.5
    print("Prím" if prim else "Nem prím")
