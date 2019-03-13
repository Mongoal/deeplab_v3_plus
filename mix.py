from PIL import Image
import numpy as np
import os
#rgb_dir为原图所在文件夹，mask_dir为分割结果所在文件夹
rgb_dir= "./images"
mask_dir= "./segmentation_result"
output_dir = "./mix"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
filelist = os.listdir(mask_dir)
for file in filelist:
    filename,ext =os.path.splitext(file)
    mask_path = os.path.join(mask_dir,file)
    rgb_path = os.path.join(rgb_dir,filename+'.jpg')
    if os.path.isfile(mask_path):
        rgb = np.asarray(Image.open(rgb_path))
        mask = np.asarray(Image.open(mask_path))
        shape = rgb.shape
        m = np.uint8(np.reshape([1,0,0,0,0,0,0,0,0],(3,3)))
        e = np.eye(3,3,dtype='uint8')
        mix = (mask == 0) * rgb + (mask != 0) * (0.3 * rgb + 0.7 * mask)
        Image.fromarray(np.uint8(mix)).save(os.path.join(output_dir,filename+'.jpg'), format='jpeg')
