def linearis_kereses_tetel():
    also = 42
    felso = 67
    i = also
    while i <= felso and not(i % 10 == 0):
        i += 1
    van = i <= felso
    if van:
        print(f"van 0-ra végződő szám: {i}")
        # return i
    else:
        print("nincs 0-ra végződő szám")
        # return "nincs"
