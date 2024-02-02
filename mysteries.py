# Tehtava 2a 
#
# Funktio saa parametrina nopeuden kilometreina tunnissa (kokonaisluku).
# Funktion  pitaisi tulostaa luetun arvon mukaan, saako silla (vanhan tieliikennelain mukaisen) rikesakon.
# Rikesakon saa, jos 60 km/h nopeusrajoitusalueella ajaa 7 km/h yli nopeusrajoituksen,
# eli jos tulos on vahintaan 67, se ylittaa rikesakon rajan.
# Funktio ei kuitenkaan toimi oikein. Korjaa funktio.

def mystery1(speed):
    print("Your speed was", speed, "km/h.")
    if speed >= 67:
        print("Oh no, better prepare yourself for a fine.")
    if speed < 0:
        print("Negative speed is not possible.")
    elif speed < 66:
        print("You should be all good.")


# Tehtava 2b
#
# Funktio saa ensimmaisena parametrina positiivisia kokonaislukuja sisaltavan listan.
# Funktion tarkoitus on tutkia, ovatko kaikki listan luvut jaollisia toisena parametrina
# annetulla positiivisella kokonaisluvulla. Funktio ei kuitenkaan toimi tarkoitetulla tavalla.
# Korjaa funktio.

def mystery2(list1, number):
    i = 0
    while i < len(list1):
        if list1[i] % number != 0:
            return False
        else:
            i = i + 1
    return True


# Tehtava 2c 
#
# Seuraava funktio saa parametrina kaksi samanmittaista merkkijonoa.
# Sen tarkoitus on tulostaa uusi merkkijono, jossa on vuoron peraan merkki kummastakin merkkijonosta,
# eli ensin ensimmainen merkki ensimmaisesta merkkijonosta,
# sitten ensimmainen merkki toisesta merkkijonosta,
# sitten toinen merkki ensimmaisesta merkkijonosta, jne. merkkijonon loppuun asti.
# Funktio ei kuitenkaan toimi tarkoitetulla tavalla. Korjaa funktio.

def mystery3(string1, string2):
    result = ""
    for i in range(len(string1)):
        result += string1[i] + string2[i]
    return result


# Tehtava 2d
#
# Seuraava funktio saa parametrina kaksi samanmittaista listaa, joissa molemmissa on kokonaislukuja.
# Sen tarkoitus on laskea yhteen ne ensimmaisen listan alkiot, jotka ovat suurempia kuin toisessa
# listassa samassa kohtaa (eli samalla indeksilla) olevat alkiot, mutta nain se ei tee.
# Korjaa funktio

def mystery4(list1, list2):
    i = 0
    result = 0
    while i < len(list1):
        if list1[i] > list2[i]:
            result += list1[i]
        i += 1

    return result


# Omaa testaamistasi varten paaohjelma.
# Voit kirjoittaa lisaa testeja paaohjelmaan,
# mutta niita ei kayteta tehtavaa tarkistettaessa.

def main():
    print("2a)")
    mystery1(68)
    print()

    print("2b)")
    print("This should work:", mystery2([2,4,6,8], 2))
    print("This should fail:", mystery2([2,3,4,5], 2))
    print()

    print("2c)")
    print("Results should be 'abcdefgh'. Your result is following:", mystery3("aceg", "bdfh"))
    print()

    print("Tehtava 2d)")
    print("Result should be 10. Your result is following:", mystery4([1,4,9],[0,5,8]))
    print()


main()
