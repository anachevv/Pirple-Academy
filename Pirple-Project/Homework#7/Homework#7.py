Song = {"Blanka": 0, "Le monde chico": 0, "Mexico": 1, "Kratos": 0}
while True:
    favouriteSong = str(input("Which song do you think I prefer the most?\n"))
    if Song[favouriteSong] > 0:
        print("True")
        break
    else:
        print("False")
        break

Music_band = {"PNL": 1, "idk1": 0, "idk2": 0, "idk3": 0}
while True:
    favouriteMusicBand = str(input("Which band do you think I prefer the most?\n"))
    if Music_band[favouriteMusicBand] > 0:
        print("True")
        break
    else:
        print("False")
        break
