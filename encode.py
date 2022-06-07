from math import floor
from random import randint
from PIL import Image
from Photo import Photo

# generate a random 8*8 block for testing purpose
def generae_block():
    block = []
    for i in range(8):
        block.append([randint(0, 255) for j in range(8)])
    return block

# convert a block of 0-255 values to 0-9 values
def convert_bloack(block: list):
    for i in range(len(block)):
        block[i] = (list(map(lambda x: floor(x/25.6), block[i])))
    return block

# encode a 8*8 block 
def encode(block: list, block_num: int):
    previous = None
    encoded = [str(block_num)]
    for row in block:
        if previous is not None and previous == row:  # signal = 10
            encoded.append('10')
        elif row.count(row[0]) == len(row):  # signal = 11
            encoded.append('11' + str(row[0]))
        else:  # signal = 0
            encoded.append('0' + ''.join(map(str, row)))
        previous = row.copy()
    return encoded

# read a image and convert it to a list of blocks
def read_blocks(file_path):
    img = Image.open(file_path)
    imgGray = img.convert('L')

    width, height = imgGray.size
    imgGray = imgGray.resize((width-width%8, height-height%8))
    width, height = imgGray.size

    photo_blocks = []    
    pixels = list(imgGray.getdata())

    for i_start in range(0, height, 8):
        i_end = min(i_start+8, height)
        for j_start in range(0, width, 8):
            block = []
            for i in range(i_start, i_end, 1):
                j_end = min(j_start+8, width)
                line = []
                for j in range(j_start, j_end, 1):
                    line.append(pixels[width*i+j])
                block.append(line)
            photo_blocks.append(block)
    img.close()
    return Photo(width, height, photo_blocks)

