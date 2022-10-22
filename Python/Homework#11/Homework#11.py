"""
Homework#11 - Homework#1
"""

Song = "Blanka"
Music_band = "PNL"
Artist1 = "Ademo"
Artist2 = "N.O.S"
Artist1_age = 34
Artist2_age = 31
Album = "Le monde Chico"
Record_Company = "QLF RECORDS"
Genre = "Rap"
DurationInSeconds = 304
YearReleased = 2015
Language = "French"

try:
    print(int(Song))
    print(int(Music_band))
    print(int(Artist1))
    print(int(Artist2))
    print(int(Album))
    print(int(Record_Company))
    print(int(Genre))
    print(int(Language))
except ValueError:
    print("Blanka")
    print("PNL")
    print("Ademo")
    print("N.O.S")
    print("Le monde Chico")
    print("QLF RECORDS")
    print("Rap")
    print("French")
finally:
    print("It is all done!")