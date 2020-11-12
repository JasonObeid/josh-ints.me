import os
from PIL import Image
import glob
path = 'src/public/images/item_old'
newPath = 'src/public/images/item'
for file in os.listdir(path):
    image = Image.open(f'{path}/{file}')
    new_image = image.resize((40, 40))
    new_image.save(f'{newPath}/{file[:-4]}.jpg')

    print(image.size)
    print(new_image.size)

"""root_dir = 'spellOld'
for filename in glob.iglob(root_dir + '**/**', recursive=True):
    if filename[-4:] == '.png':
        image = Image.open(filename)
        new_image = image.resize((40, 40))
        new_image.save(f'spell/{filename}')

        print(image.size)
        print(new_image.size)"""

"""
    if filename[-4:] == '.png':
        image = Image.open(filename)
        new_image = image.resize((40, 40))
        print('filename[:-4]')
        new_image.save(f'{filename[:-4]}.jpg')

        print(image.size)
        print(new_image.size)

path = 'images/runes_old'
newPath = 'images/runes'
for file in os.listdir(path):
    image = Image.open(f'{path}/{file}')
    new_image = image.resize((40, 40))
    new_image.save(f'{newPath}/{file[:-4]}.jpg')

    print(image.size)
    print(new_image.size)"""