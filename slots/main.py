def fruit(reels, spins):
    mult = 0
    score = 0
    hash = {
        'Wild' : 10,
        'Star' : 9,
        'Bell' : 8,
        'Shell' : 7,
        'Seven' : 6,
        'Cherry' : 5,
        'Bar' : 4,
        'King' : 3,
        'Queen' : 2,
        'Jack' : 1
    }
    ourArr = [reels[0][spins[0]],reels[1][spins[1]],reels[2][spins[2]]]
    ourArr.sort()
    if (ourArr[0] == ourArr[1] and ourArr[1] == ourArr[2]):
        mult = 10
    elif (ourArr[0] == ourArr[1] or ourArr[1] == ourArr[2]):
        mult = 1
        if (ourArr[1] != 'Wild' and (ourArr[0] == 'Wild' or ourArr[2] == 'Wild')):
            mult = 2
    return mult * hash[ourArr[1]]
        