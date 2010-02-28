#! /usr/bin/python

# Step 1 - Create a win
from pyglet import *
w = window.Window(800, 100)

# Step 2 - Need some graphics!
happy = resource.image('ch.png')
angry = resource.image('ca.png')

c = sprite.Sprite(happy)
f = sprite.Sprite(resource.image('f.png'))
s = media.load('b.wav', streaming=False)

@w.event
def on_draw():
	w.clear()
	f.draw()
	c.draw()

# Step 3 - Make the hand move
from pyglet.window import mouse
@w.event
def on_mouse_motion(x, y, dx, dy):
	f.x = x - f.width/2
	f.y = y - f.height/2

# Step 4 - make the chimp move
c.dx = 300
def update(dt):
	if c.x+c.width >= w.width:
		c.dx = -300
	if c.x < 0:
		c.dx = 300

	c.x += c.dx*dt

clock.schedule_interval(update, 1/120.0)

# Step 5 - Make it punchable
@w.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
		# Check the chimp and hand positions
		if f.x < c.x and c.x+c.width < f.x+f.width:
			# Play some sound
			s.play()

			# Make the chimp angry
			c.image = angry

			# Hide the hand
			f.visible = 0			

app.run()
