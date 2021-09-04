from PIL import Image
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', action='store', type=str, required=True)
parser.add_argument('--gridbuf', action='store', type=int, default=5)
parser.add_argument('--size', action='store', type=int, default=2000)
parser.add_argument('--grid', action='store', type=int, default=4)

args = parser.parse_args()
f = open(args.file)
data = json.load(f)
print(data)

#img.save("output.png", "PNG")

#img1 = Image.open("img1.png")
#img1.show()

osize = args.size
grid = args.grid
gridbuf = args.gridbuf
boxsize = int((osize - (grid-1)*5)/grid)
print(boxsize)
#img1x = img1.resize((boxsize,boxsize), Image.ANTIALIAS)
#img2x = img1.resize((2*boxsize,2*boxsize), Image.ANTIALIAS)
#img.paste(img1x)
#img.paste(img2x, (boxsize+gridbuf,0))
#img.show()
img = Image.new('RGB', (osize,osize), (255,255,255))

def csize(boxes, gridbuf, boxsize):
    return [b*boxsize + gridbuf*(b-1) for b in boxes]

def coords(gridloc, gridbuf, boxsize):
    print(gridloc)
    return [g*boxsize + gridbuf*g for g in gridloc]

for d in data:
    imgx = Image.open(d["fn"])
    reshape_size = csize(d["size"], gridbuf, boxsize)
    pxcoords = coords(d["coord"], gridbuf, boxsize)
    imgx = imgx.resize(tuple(reshape_size), Image.ANTIALIAS)
    img.paste(imgx, tuple(pxcoords))

#img.show()
img.save("output.png","PNG")
