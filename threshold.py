from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def threshold(image_array):
    """Returns a 0 if a pixel is [0,0,0] and 1 otherwise."""
    numrows = len(image_array)
    numcols = len(image_array[0])
    newar = [[0 for x in range(numrows)] for y in range(numcols)]

    i = 0
    for each_row in image_array:
        j = 0
        for each_pix in each_row:
            if each_pix[0] != 0 or each_pix[1] != 0 or each_pix[2] != 0:
                newar[i][j] = 1
            j = j + 1
        i = i + 1
    return newar

im = Image.open(
    "/Users/ravill2/birdPhotos/CUB_200_2011/CUB_200_2011/backInBlack/011.Rusty_Blackbird/Rusty_Blackbird_0016_6684.jpg")
im = im.resize((32,32),Image.NEAREST)
im = im.convert("RGB")
iar = np.array(im)
iar = threshold(iar)
print(iar)
plt.imshow(iar)
plt.show()
