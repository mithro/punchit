#! /usr/bin/python

# Step 1 - Create a win
from pyglet import *
w = window.Window(800, 100)

# Step 2 - Need some graphics!
happy = resource.image('chimp-happy.png')
angry = resource.image('chimp-angry.png')

c = sprite.Sprite(happy)
h = sprite.Sprite(resource.image('fist.png'))
media.load('boom.wav')

@w.event
def on_draw():
	w.clear()
	h.draw()
	c.draw()

# Step 3 - Make the hand move
from pyglet.window import mouse
@w.event
def on_mouse_motion(x, y, dx, dy):
	h.x = x - h.width/2
	h.y = y - h.height/2

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
		if h.x < c.x and c.x+c.width < h.x+h.width:
			# Play some sound
			s = media.load('boom.wav')
			s.play()

			# Make the chimp angry
			c.image = angry

			# Hide the hand
			h.visible = 0			

app.run()
