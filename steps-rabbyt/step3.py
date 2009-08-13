import rabbyt as r
from pyglet import *

# Step 1 - Create a window
w = window.Window(800, 100)
r.set_default_attribs()

# Step 2 - Put some graphics on the window

# Load some media
c = r.Sprite('ch.png')
f = r.Sprite('f.png')
s = media.load('b.wav')

c.y, f.y = 50, 50

@w.event
def on_draw():
	r.clear()
	f.render()
	c.render()
	w.flip()

# Step 3 - Make the hand move 
from pyglet.window import mouse
@w.event
def on_mouse_motion(x, y, dx, dy):
	f.xy = x, y
app.run()
