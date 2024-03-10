# 并发编程
# 生成指定文件夹下图片的缩略图

import glob
import os.path
import threading
from PIL import Image

PREFIX = 'thumbnails'
def generate_thumbnail(img_file, thumbnail_size, img_format = 'JPEG'):
    img_name,end = os.path.splitext(os.path.split(img_file)[-1])
    thumbnail_save = f'{PREFIX}/{img_name}_{thumbnail_size[0]}_{thumbnail_size[1]}.{end}'
    img = Image.open(img_file)
    img.thumbnail(size=thumbnail_size)
    img.save(thumbnail_save, img_format)

def main():
    os.makedirs(PREFIX, exist_ok=True)
    for img_file in glob.glob('../images/*.jpg'):
        for size in [32,64,128]:
            threading.Thread(target=generate_thumbnail,args=(img_file,(size,size))).start()

if __name__ == '__main__':
    main()