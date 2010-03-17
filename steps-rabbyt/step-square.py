import rabbyt
import pyglet

# Step 1 - Create a window
win = pyglet.window.Window(800, 600)
rabbyt.set_default_attribs()

# Step 2 - Put some graphics on the window

# Load some media
chimp = rabbyt.Sprite('chimp-happy.png')
fist = rabbyt.Sprite('fist.png')
sound = pyglet.media.load('boom.wav', streaming=False)

chimp.y, fist.y = 50, 50

@win.event
def on_draw():
	rabbyt.clear()
	fist.render()
	chimp.render()

# Step 3 - Make the hand move 
from pyglet.window import mouse
@win.event
def on_mouse_motion(x, y, dx, dy):
	fist.xy = x, y

# Step 4 - Make the chip move
def boxchimp(*args):
	chimp.xy = rabbyt.chain(
		rabbyt.lerp((50, 50), (750, 50), dt=1.3),
		rabbyt.lerp(end=(750, 550), dt=1.3),
		rabbyt.lerp(end=( 50, 550), dt=1.3),
		rabbyt.lerp(end=( 50, 50), dt=1.3))

boxchimp()
pyglet.clock.schedule_interval(boxchimp, 1.3*4)

pyglet.clock.schedule(rabbyt.add_time)

# Step 5 - Add violance
@win.event
def on_mouse_press(x, y, b, m):
	# Check the chimp and hand positions
	if rabbyt.collisions.aabb_collide([chimp, fist]):
		# Play some sound
		sound.play()

		# Make the chimp angry
		chimp.texture = 'ca.png'

		# Stop the chimp
		chimp.xy = float(chimp.x), float(chimp.y)

pyglet.app.run()
