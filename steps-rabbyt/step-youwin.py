import rabbyt
import pyglet

# Step 1 - Create a window
win = pyglet.window.Window(800, 100)
rabbyt.set_default_attribs()

# Step 2 - Put some graphics on the window

# Load some media
chimp = rabbyt.Sprite('chimp-happy.png')
fist = rabbyt.Sprite('fist.png')
sound = pyglet.media.load('boom.wav', streaming=False)

class SpriteText(rabbyt.BaseSprite):
    def __init__(self, ft, text="", *args, **kwargs):
        rabbyt.BaseSprite.__init__(self, *args, **kwargs)
        self._text = pyglet.font.Text(ft, text)

    def set_text(self, text):
        self._text.text = text

    def render_after_transform(self):
        self._text.color = self.rgba
        self._text.draw()

ft = pyglet.font.load('Arial', 24)
label = SpriteText(ft, "You win!", xy=(400,50))
label.rgba = (1, 0, 0, 0)

chimp.y, fist.y = 50, 50

@win.event
def on_draw():
	rabbyt.clear()
	fist.render()
	chimp.render()
	label.render()

	win.flip()


# Step 3 - Make the hand move 
from pyglet.window import mouse
@win.event
def on_mouse_motion(x, y, dx, dy):
	fist.xy = x, y

# Step 4 - Make the chip move
chimp.x = rabbyt.lerp(50, 750, dt=1.3, extend="reverse")

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

		# Hide the hand
		fist.alpha = 0

		# Show the text
		label.alpha = 1
		label.red = rabbyt.lerp(1, 0, dt=1, extend="reverse")
		label.green = rabbyt.lerp(1, 0, dt=2, extend="reverse")
		label.blue = rabbyt.lerp(1, 0, dt=3, extend="reverse")

pyglet.app.run()
