import encode
import decode

path = input('Enter the path of the image: ')

data = encode.read_blocks(path)
blocks = data.blocks
encoded_data = []
print('\nStart Encoding...\n')
for block_num, block in enumerate(blocks, 1):
    print(f'\nBlock #{block_num} Data:')
    for i in block:
        print(i)
    print()
    cb = encode.convert_bloack(block)

    encoded_block = encode.encode(cb, block_num)
    encoded_data.append(encoded_block)
    print('Compressed block:', encoded_block)
data.blocks = encoded_data

print('\nStart Decoding...\n')

decoded_data = []
for block in data.blocks:
    decoded_block = decode.decode(block)
    cb = decode.convert_bloack(decoded_block)
    decoded_data.append(cb)
data.blocks = decoded_data
decode.write_blocks(data, './decoded.png')





