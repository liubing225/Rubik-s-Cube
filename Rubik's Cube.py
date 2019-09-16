from PIL import Image,ImageDraw
import random
#魔方阶数
n=50
#图片大小
m=n*100
im=Image.new('RGB',size=(m,m),color='white')
#im.save('魔方.png')
#白 蓝 录 黄 红 橙
colors=[(255,255,255),(255,0,0),(0,255,0),(255,255,0),(0,0,255),(240,133,25)]
def huakuai(startx,starty,endx,endy,color):
    for i in range(startx,endx):
        for j in range(starty,endy):
            im.putpixel(xy=(i,j),value=color)

#huakuai(0, 0, 100, 100,(255,0,0))

for j in range(0,m,100):
    ystart=j
    xstart=0
    while xstart<m:
        endx=xstart+100
        endy=j+100
        huakuai(xstart,ystart,endx,endy,random.choice(colors))
        xstart+=100
draw=ImageDraw.Draw(im)
for i in range(0,m+100,100):
    draw.line(xy=[(0,i),(m,i)],fill=(0,0,0),width=4)
for i in range(0,m+100,100):
    draw.line(xy=[(i,0),(i,m)],fill=(0,0,0),width=4)
im.show()
im.save("魔方.png")




