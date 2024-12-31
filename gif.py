import imageio.v3 as iio
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('Image1',help='Path of first image')
parser.add_argument('Image2',help='Path of second image')
args=parser.parse_args()
filenames=[args.Image1,args.Image2]
images=[]
for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('grp.gif',images,duration=500,loop=0)