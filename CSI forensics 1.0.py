hairColor = {
            "black": "CCAGCAATCGC",
            "brown": "GCCAGTGCCG",
            "blonde": "TTAGCTATCGC"
        }

facialShape = {
            "square": "GCCACGG",
            "round": "ACCACAA",
            "oval": "AGGCCTCA"
        }

eyeColor = {
            "blue": "TTGTGGTGGC",
            "green": "GGGAGGTGGC",
            "brown": "AAGTAGTGAC"
        }

gender = {
            "female": "TGAAGGACCTTC",
            "male": "TGCAGGAACTTC"
        }

race = {
            "white": "AAAACCTCA",
            "black": "CGACTACAG",
            "asian": "CGCGGGCCG"
        }


with open("dna.txt", "r") as exibitFile:
    exibitTxt = exibitFile.read()
    for x in hairColor:
        if hairColor[x] in exibitTxt:
            print("Suspect hair color is " + x)
            break

    for x in facialShape:
        if facialShape[x] in exibitTxt:
            print("Suspect facial shape is " + x)
            break

    for x in eyeColor:
        if eyeColor[x] in exibitTxt:
            print("Suspect eye color is " + x)
            break

    for x in gender:
        if gender[x] in exibitTxt:
            print("Suspect gender is " + x)
            break

    for x in race:
        if race[x] in exibitTxt:
            print("Suspect race is " + x)
            break

    #print(brown in exibitTxt)
    #print(exibitTxt)
