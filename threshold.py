from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def threshold(imageArray):
    balanceAr = []
    newAr = imageArray
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = reduce(lambda x, y: x + y, eachPix[:2]) / len(eachPix[:2])
            balanceAr.append(avgNum)
    balance = reduce(lambda x, y: x + y, balanceAr) / len(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if reduce(lambda x, y: x + y, eachPix[:2]) / len(eachPix[:2]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                #eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                #eachPix[3] = 255
    return newAr

im = Image.open(
    "/Users/ravill2/birdPhotos/CUB_200_2011/CUB_200_2011/backInBlack/011.Rusty_Blackbird/Rusty_Blackbird_0016_6684.jpg")
im = im.resize((64,64),Image.NEAREST)
im = im.convert("RGB")
#im = im.convert("1")
iar = np.array(im)
iar = threshold(iar)
plt.imshow(iar)
print(iar)
plt.show()
