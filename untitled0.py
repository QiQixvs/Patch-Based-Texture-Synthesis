import cv2
import sys
import numpy as np
from random import randint

#Image Loading
InputName = str(sys.argv[1])
img_sample = cv2.imread(InputName)
sample_width = img_sample.shape[1]
sample_height = img_sample.shape[0]
img_height = 512
img_width  = 512
PatchSize = int(sys.argv[2])


#Picking random patch tp begin
randomPatchHeight = randint(0, sample_height - PatchSize)
randomPatchWidth = randint(0, sample_width - PatchSize)
crop_img = img_sample[randomPatchHeight:randomPatchHeight+PatchSize,randomPatchWidth:randomPatchWidth+PatchSize]

