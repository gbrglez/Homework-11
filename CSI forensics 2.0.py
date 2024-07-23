humanChar = {
    "HairColor": {
        "Black": "CCAGCAATCGC",
        "Brown": "GCCAGTGCCG",
        "Blonde": "TTAGCTATCGC"
    },
    "FaceShape": {
        "Square": "GCCACGG",
        "Round": "ACCACAA",
        "Oval": "AGGCCTCA",
    },
    "EyeColor": {
        "Blue": "TTGTGGTGGC",
        "Green": "GGGAGGTGGC",
        "Brown": "AAGTAGTGAC",
    },
    "Gender": {
        "Female": "TGAAGGACCTTC",
        "Male": "TGCAGGAACTTC",
    },
    "Race": {
        "White": "AAAACCTCA",
        "Black": "CGACTACAG",
        "Asian": "CGCGGGCCG",
    },
}

people = {
    "Eva": {
        "Gender": "Female",
        "Race": "White",
        "HairColor": "Blonde",
        "EyeColor": "Blue",
        "FaceShape": "Oval"
    },
    "Larisa": {
        "Gender": "Female",
        "Race": "White",
        "HairColor": "Brown",
        "EyeColor": "Brown",
        "FaceShape": "Oval"
    },
    "Matej": {
        "Gender": "Male",
        "Race": "White",
        "HairColor": "Black",
        "EyeColor": "Blue",
        "FaceShape": "Oval"
    },
    "Miha": {
        "Gender": "Male",
        "Race": "White",
        "HairColor": "Brown",
        "EyeColor": "Green",
        "FaceShape": "Square"
    },
}

with open("dna.txt", "r") as exibitFile:
    exibitTxt = exibitFile.read()
    translation = ""
    for x in humanChar:
        for y in humanChar[x]:
            if humanChar[x][y] in exibitTxt:
                translation = translation + y
    #print(translation)

    for x in people:
        test = True
        for y in people[x]:
            test = test and people[x][y] in translation
        if test:
            print("Person you are looking for is " + x)






