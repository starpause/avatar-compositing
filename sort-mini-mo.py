#!/usr/bin/python
import glob
import os
import json

for filename in glob.glob('*.png'): 
    print("")
    data = {}
    splitted = filename.split("_", 1)
    edition = splitted[0]
    print(edition)
    os.mkdir(edition)
    #moved = edition + "/" + filename
    moved = edition + "/media.png"
    os.rename(filename, moved)

    #bg/planet
    background = ""
    if "bg0" in filename:
        background = "Sun"
    if "bg1" in filename:
        background = "Earth"
    if "bg2" in filename:
        background = "Europa"
    if "bg3" in filename:
        background = "Uranus"
    if "bg4" in filename:
        background = "Mercury"
    if "bg5" in filename:
        background = "Mars"
    if "bg6" in filename:
        background = "Pluto"
    print(background)

    #legs
    legs = ""
    if "legs0" in filename:
        legs = "Red Green"
    if "legs1" in filename:
        legs = "Black Yellow"
    if "legs2" in filename:
        legs = "Blue Yellow"
    if "legs3" in filename:
        legs = "Pink Red"
    if "legs4" in filename:
        legs = "Yellow Orange"
    print(legs)

    #head
    head = ""
    if "head0" in filename:
        head = "Pink Doge"
    if "head1" in filename:
        head = "Blue Poo"
    if "head2" in filename:
        head = "Blue Puff"
    if "head3" in filename:
        head = "Yellow Hatter"
    if "head4" in filename:
        head = "Orange Hatter"
    if "head5" in filename:
        head = "Blue Hatter"
    if "head6" in filename:
        head = "Blue Fruit"
    if "head7" in filename:
        head = "Orange Fruit"
    if "head8" in filename:
        head = "Pink Fruit"
    if "head9" in filename:
        head = "Purple Fruit"
    if "head10" in filename:
        head = "Green Poo"
    if "head11" in filename:
        head = "Yellow Poo"
    if "head13" in filename:
        head = "Pink Poo"
    if "head14" in filename:
        head = "Orange Appa"
    if "head15" in filename:
        head = "Green Appa"
    if "head16" in filename:
        head = "Blue Appa"
    if "head17" in filename:
        head = "Red Appa"
    if "head18" in filename:
        head = "Purple Puff"
    if "head19" in filename:
        head = "Yellow Puff"
    if "head20" in filename:
        head = "Pink Puff"
    print(head)

    #face
    face = ""
    if "face0" in filename:
        face = "😳"
    if "face1" in filename:
        face = "😈"
    if "face2" in filename:
        face = "👹"
    if "face3" in filename:
        face = "👺"
    if "face4" in filename:
        face = "🙂"
    if "face5" in filename:
        face = "🤪"
    if "face6" in filename:
        face = "😏"
    if "face7" in filename:
        face = "🤩"
    if "face8" in filename:
        face = "😙"
    if "face9" in filename:
        face = "🙄"
    if "face10" in filename:
        face = "😑"
    if "face11" in filename:
        face = "😥"
    if "face13" in filename:
        face = "🤨"
    if "face14" in filename:
        face = "😒"
    if "face15" in filename:
        face = "😕"
    if "face16" in filename:
        face = "😖"
    if "face17" in filename:
        face = "👁‍🗨"
    print(face)
    

    #symbol
    symbol = ""
    if "symbol0" in filename:
        symbol = "NEAR"
    if "symbol1" in filename:
        symbol = "OMEGA"
    if "symbol2" in filename:
        symbol = "PSI"
    if "symbol3" in filename:
        symbol = "CHI"
    if "symbol4" in filename:
        symbol = "PHI"
    if "symbol5" in filename:
        symbol = "UPSILON"
    if "symbol6" in filename:
        symbol = "TAU"
    if "symbol7" in filename:
        symbol = "SIGMA"
    if "symbol8" in filename:
        symbol = "RHO"
    if "symbol9" in filename:
        symbol = "PI"
    if "symbol10" in filename:
        symbol = "OMICRON"
    if "symbol11" in filename:
        symbol = "XI"
    if "symbol13" in filename:
        symbol = "NU"
    if "symbol14" in filename:
        symbol = "LAMBDA"
    if "symbol15" in filename:
        symbol = "KAPPA"
    if "symbol16" in filename:
        symbol = "IOTA"
    if "symbol17" in filename:
        symbol = "THETA"
    print(symbol)

    data['extra'] = []
    data['extra'].append({
        "trait_type":"Planet",
        "value": background
    })
    data['extra'].append({
        "trait_type":"Bod",
        "value": head
    })
    data['extra'].append({
        "trait_type":"Mood",
        "value": face
    })
    data['extra'].append({
        "trait_type":"Fit",
        "value": legs
    })
    data['extra'].append({
        "trait_type":"Team",
        "value": symbol
    })
    metadata = edition + "/info.json"
    with open(metadata, 'w') as outfile:
        json.dump(data, outfile)