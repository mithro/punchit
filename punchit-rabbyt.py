import rabbyt as r
from pyglet import *

# Step 1 - Create a window
w = window.Window(width=800, height=100)
r.set_default_attribs()

# Step 2 - Put some graphics on the window

# Load some media
c = r.Sprite('ch.png')
f = r.Sprite('f.png')
media.load('b.wav')

c.y, f.y = 50, 50

@w.event
def on_draw():
	r.clear((0,0,0))
	f.render()
	c.render()
	w.flip()

# Step 3 - Make the hand move 
from pyglet.window import mouse
@w.event
def on_mouse_motion(x, y, dx, dy):
	f.xy = x, y

# Step 4 - Make the chip move
c.x = r.lerp(50, 750, dt=1.3, extend="reverse")

clock.schedule(r.add_time)

# Step 5 - Add violance
@w.event
def on_mouse_press(x, y, b, m):
    if b == mouse.LEFT:
		# Check the chimp and hand positions
		if r.collisions.aabb_collide([c, f]):
			# Play some sound
			s = media.load('b.wav')
			s.play()

			# Make the chimp angry
			c.texture = 'ca.png'

			# Hide the hand
			f.texture.visible = 0

app.run()
