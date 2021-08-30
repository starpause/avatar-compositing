from PIL import Image
import glob
import random

#
# LOAD defs
#

survivor = Image.open('8_survivor/SurvivorBand_01.png')
print("")
print("#SURVIVOR")
print(survivor)

bg = []
def loadBG():
    for filename in glob.glob('0_bg/*.png'): 
        im=Image.open(filename)
        bg.append(im)
    print("")
    print("#BG")
    print(bg)

b_char = []
f_char = []
m_char = []
def loadCHAR():
    # char beast
    for filename in glob.glob('1_b_char/*.png'): 
        im=Image.open(filename)
        b_char.append(im)
    print("")
    print("#B_CHAR")
    print(b_char)

    # char female
    for filename in glob.glob('1_f_char/*.png'): 
        im=Image.open(filename)
        f_char.append(im)
    print("")
    print("#F_CHAR")
    print(f_char)

    # char male
    for filename in glob.glob('1_m_char/*.png'): 
        im=Image.open(filename)
        m_char.append(im)
    print("")
    print("#M_CHAR")
    print(m_char)

f_hair = []
m_hair = []
def loadHAIR():
    # hair female
    for filename in glob.glob('2_f_hair/*.png'): 
        im=Image.open(filename)
        f_hair.append(im)
    print("")
    print("#F_HAIR")
    print(f_hair) 

    # hair male
    for filename in glob.glob('2_m_hair/*.png'): 
        im=Image.open(filename)
        m_hair.append(im)
    print("")
    print("#M_HAIR")
    print(m_hair) 

b_shirt = []
mf_shirt = []
def loadSHIRT():
    # shirt beast
    for filename in glob.glob('3_b_shirt/*.png'): 
        im=Image.open(filename)
        b_shirt.append(im)
    print("")
    print("#B_SHIRT")
    print(b_shirt) 

    # shirt male/female
    for filename in glob.glob('3_mf_shirt/*.png'): 
        im=Image.open(filename)
        mf_shirt.append(im)
    print("")
    print("#MF_SHIRT")
    print(mf_shirt) 

weapon = []
enemy = []
water = []
def loadDEATH():
    # death weapon
    for filename in glob.glob('5_weapon/*.png'): 
        im=Image.open(filename)
        weapon.append(im)
    print("")
    print("#WEAPON")
    print(weapon) 

    # death enemy
    for filename in glob.glob('6_enemy/*.png'): 
        im=Image.open(filename)
        enemy.append(im)
    print("")
    print("#ENEMY")
    print(enemy)

    # death environment
    for filename in glob.glob('7_water/*.png'): 
        im=Image.open(filename)
        water.append(im)
    print("")
    print("#WATER")
    print(water)

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

loadBG()
loadCHAR()
loadHAIR()
loadSHIRT()
loadDEATH()
print("")

race = ['beast','beast','beast','male','male','female','female']
current = 0
while current < 111: 
    template = random.choice(race)
    death = random.random();
    if death < .02:
        death = 0
    elif death < .5:
        death = 1
    elif death < .9:
        death = 2
    else:
        death = 3
    if template == 'beast':
        buildBEAST(current, death)
    elif template == 'male':
        buildMALE(current, death)
    else:
        buildFEM(current, death)
    current += 1
