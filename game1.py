import pgzrun
import random
WIDTH=400
HEIGHT=400
plane=Actor("plem")
yn=""
count=0
flag=1
hits=0
color="red"
def draw():
    screen.fill(color)
    plane.draw()
    screen.draw.text(yn,topright=(380,0),color=("white"))
    if flag==0:
        plane.x=500
        plane.y=500
        screen.draw.text("End of game, You got:\n|"+str(hits)+" Hits\n|"+str(20-hits)+" Misses",(0,0),color=("white"))
def on_mouse_down(pos):
    global yn,count,flag,hits,color
    if count!=20:
        count+=1
        if plane.collidepoint(pos):
            print("yarrrr")
            plane.x=random.randint(0,400)
            plane.y=random.randint(0,400)
            yn="yarrrr"
            color="green"
            hits+=1
        else:
            print("narrrr")
            yn="narrrr"
            color="black"
    else:
        flag=0
pgzrun.go()