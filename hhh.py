from PIL import Image
import glob
import random

#
# LOAD defs
#

layer1options = []
def load_layer1():
    for filename in glob.glob('HHH/1-Background/*.png'): 
        im=Image.open(filename)
        layer1options.append(im)
    print("")
    print("#layer1options")
    print(layer1options)
load_layer1()

layer2options = []
def load_layer2():
    for filename in glob.glob('HHH/2-Body/*.png'): 
        im=Image.open(filename)
        layer2options.append(im)
    print("")
    print("#layer2")
    print(layer2options)
load_layer2()

layer3options = []
def load_layer3():
    for filename in glob.glob('HHH/3-Hand/*.png'): 
        im=Image.open(filename)
        layer3options.append(im)
    print("")
    print("#layer3")
    print(layer3options)
load_layer3()    

layer4options = []
def load_layer4():
    for filename in glob.glob('HHH/4-Decorating/*.png'): 
        im=Image.open(filename)
        layer4options.append(im)
    print("")
    print("#layer4")
    print(layer4options)
load_layer4()

layer5options = []
def load_layer5():
    for filename in glob.glob('HHH/5-Clothes/*.png'): 
        im=Image.open(filename)
        layer5options.append(im)
    print("")
    print("#layer5")
    print(layer5options)
load_layer5()

layer6options = []
def load_layer6():
    for filename in glob.glob('HHH/6-Face/*.png'): 
        im=Image.open(filename)
        layer6options.append(im)
    print("")
    print("#layer6")
    print(layer6options)
load_layer6()

#
# BUILD DEFS
#

def buildBEAST(current,death):
    avatar = Image.alpha_composite(random.choice(bg).convert('RGBA'),random.choice(b_char))
    avatar = Image.alpha_composite(avatar,random.choice(b_shirt))
    #dry death
    randomDeath = random.random();
    if death == 0:
        if random.random() < .5:
            avatar = Image.alpha_composite(avatar,survivor);
    elif death == 1:
        if randomDeath < .33:
            avatar = Image.alpha_composite(avatar,random.choice(weapon))
        elif randomDeath < .66:
            avatar = Image.alpha_composite(avatar,random.choice(enemy))
        else:
            avatar = Image.alpha_composite(avatar,random.choice(water))
    elif death == 2:
        if randomDeath < .33:
            avatar = Image.alpha_composite(avatar,random.choice(weapon))
            avatar = Image.alpha_composite(avatar,random.choice(enemy))
        elif randomDeath < .66:
            avatar = Image.alpha_composite(avatar,random.choice(weapon))
            avatar = Image.alpha_composite(avatar,random.choice(water))
        else:
            avatar = Image.alpha_composite(avatar,random.choice(water))
            avatar = Image.alpha_composite(avatar,random.choice(enemy))
    else:
        avatar = Image.alpha_composite(avatar,random.choice(weapon))
        avatar = Image.alpha_composite(avatar,random.choice(enemy))
        avatar = Image.alpha_composite(avatar,random.choice(water))
    #end dry death
    newName = "CauseOfDeath"+str(current)+".png"
    avatar.save(newName)
    print(newName)   

def buildMALE(current, death):
    avatar = Image.alpha_composite(random.choice(bg).convert('RGBA'),random.choice(m_char))
    avatar = Image.alpha_composite(avatar,random.choice(m_hair))
    avatar = Image.alpha_composite(avatar,random.choice(mf_shirt))
    #dry death
    randomDeath = random.random();
    if death == 0:
        if random.random() < .5:
            avatar = Image.alpha_composite(avatar,survivor);
    elif death == 1:
        if randomDeath < .33:
            avatar = Image.alpha_composite(avatar,random.choice(weapon))
        elif randomDeath < .66:
            avatar = Image.alpha_composite(avatar,random.choice(enemy))
        else:
            avatar = Image.alpha_composite(avatar,random.choice(water))
    elif death == 2:
        if randomDeath < .33:
            avatar = Image.alpha_composite(avatar,random.choice(weapon))
            avatar = Image.alpha_composite(avatar,random.choice(enemy))
        elif randomDeath < .66:
            avatar = Image.alpha_composite(avatar,random.choice(weapon))
            avatar = Image.alpha_composite(avatar,random.choice(water))
        else:
            avatar = Image.alpha_composite(avatar,random.choice(water))
            avatar = Image.alpha_composite(avatar,random.choice(enemy))
    else:
        avatar = Image.alpha_composite(avatar,random.choice(weapon))
        avatar = Image.alpha_composite(avatar,random.choice(enemy))
        avatar = Image.alpha_composite(avatar,random.choice(water))
    #end dry death    
    newName = "CauseOfDeath"+str(current)+".png"
    avatar.save(newName)
    print(newName)   

def buildFEM(current, death):
    avatar = Image.alpha_composite(random.choice(bg).convert('RGBA'),random.choice(f_char))
    avatar = Image.alpha_composite(avatar,random.choice(f_hair))
    avatar = Image.alpha_composite(avatar,random.choice(mf_shirt))
    #dry death
    randomDeath = random.random();
    if death == 0:
        if random.random() < .5:
            avatar = Image.alpha_composite(avatar,survivor);
    elif death == 1:
        if randomDeath < .33:
            avatar = Image.alpha_composite(avatar,random.choice(weapon))
        elif randomDeath < .66:
            avatar = Image.alpha_composite(avatar,random.choice(enemy))
        else:
            avatar = Image.alpha_composite(avatar,random.choice(water))
    elif death == 2:
        if randomDeath < .33:
            avatar = Image.alpha_composite(avatar,random.choice(weapon))
            avatar = Image.alpha_composite(avatar,random.choice(enemy))
        elif randomDeath < .66:
            avatar = Image.alpha_composite(avatar,random.choice(weapon))
            avatar = Image.alpha_composite(avatar,random.choice(water))
        else:
            avatar = Image.alpha_composite(avatar,random.choice(water))
            avatar = Image.alpha_composite(avatar,random.choice(enemy))
    else:
        avatar = Image.alpha_composite(avatar,random.choice(weapon))
        avatar = Image.alpha_composite(avatar,random.choice(enemy))
        avatar = Image.alpha_composite(avatar,random.choice(water))
    #end dry death
    newName = "CauseOfDeath"+str(current)+".png"
    avatar.save(newName)
    print(newName)

#
# COMPOSITE
#
print("")

def buildGeneric():
    # BG
    bgCount = len(bg)
    b = 0
    while b < bgCount:
        # LEGS
        legCount = len(legs)
        l = 0
        while l < legCount:
            bgLeg = Image.alpha_composite(bg[b],legs[l])
            # HEAD
            headCount = len(head)
            c = 0
            while c < headCount:
                legBody = Image.alpha_composite(bgLeg,head[c])
                # CHEEK
                cheekCount = len(cheek)
                k = 0
                while k < cheekCount:
                    pileLBM = Image.alpha_composite(legBody,cheek[k])
                    # FACE
                    faceCount = len(face)
                    e = 0
                    while e < faceCount:
                        pileLBME = Image.alpha_composite(pileLBM,face[e])
                        # SYMBOL
                        pileLBMEK = Image.alpha_composite(pileLBME,random.choice(symbol))

                        newName = "good-one/"+"bg"+str(b)+"-legs"+str(l)+"-head"+str(c)+"-face"+str(e)+".png"
                        pileLBMEK.save(newName)
                        print(newName)

                        e += 1
                    k += 1
                c += 1
            l += 1
        b += 1


#
# RUN
#

current = 0
while current < 111: 
    # load random images for the current PFP
    layer1image = random.choice(layer1options)
    layer2image = random.choice(layer2options)
    layer3image = random.choice(layer3options)
    layer4image = random.choice(layer4options)
    layer5image = random.choice(layer5options)
    layer6image = random.choice(layer6options)
    # composite all the random choices together 
    composite_image = Image.alpha_composite(layer1image.convert('RGBA'),layer2image.convert('RGBA'))
    composite_image = Image.alpha_composite(composite_image.convert('RGBA'),layer3image.convert('RGBA'))
    composite_image = Image.alpha_composite(composite_image.convert('RGBA'),layer4image.convert('RGBA'))
    composite_image = Image.alpha_composite(composite_image.convert('RGBA'),layer5image.convert('RGBA'))
    composite_image = Image.alpha_composite(composite_image.convert('RGBA'),layer6image.convert('RGBA'))
    # save 
    new_name = "HHH/0-Results/"+"HHH"+str(current)+".png"
    composite_image.save(new_name)
    print(new_name)
    # loop
    current += 1
