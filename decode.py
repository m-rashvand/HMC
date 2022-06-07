from math import floor
from PIL import Image
from Photo import Photo



# decode a 1*9 encoded block into a 8*8 block 
def decode(encoded_block):
    decoded = []
    encoded_block.pop(0)
    for row in encoded_block:

        if row == '10':
            decoded.append(decoded[-1])
        elif row[0] == '0':
            decoded.append([int(char) for char in row[1:]])
        elif row[0:2] == '11':
            decoded.append([int(row[2])]*8)

    return decoded


# convert a block of 0-9 values into 0-255 values
def convert_bloack(block: list):
    for i in range(len(block)):    
        # 12 is the midlle of each section    
        block[i] = (list(map(lambda x: floor(x*25.6)+12, block[i])))
        
    return block


# put pixel data of decoded image into a new image and save it
def write_blocks(photo: Photo, path: str):
    img = Image.new('L', (photo.width,photo.height))
    data = []
    num = int(photo.width / 8) # number of 8*8 blocks in a row

    # create a flattened pixel data using 8*8 blocks
    for bl_num in range(0, len(photo.blocks), num):
        for i in range(8):

            for row in photo.blocks[bl_num: bl_num+num]:
                for pix in row[i]:
                    data.append(pix)
    
    img.putdata(data)
    img.save(path)
    img.close()
 

