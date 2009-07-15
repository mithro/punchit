#! /usr/bin/python

from pyglet import *
w = window.Window(800, 100)

h = resource.image('chimp-happy.png')
a = resource.image('chimp-angry.png')

c = sprite.Sprite(h)
f = sprite.Sprite(resource.image('fist.png'))
s = media.load('boom.wav')

@w.event
def on_draw():
    w.clear()
    f.draw()
    c.draw()

from pyglet.window import mouse

@w.event
def on_mouse_motion(x, y, dx, dy):
    f.x = x - f.width/2
    f.y = y - f.height/2

c.dx = 300
def update(dt):
    if c.x+c.width >= w.width:
        c.dx = -300
    if c.x < 0:
        c.dx = 300

    c.x += c.dx*dt

clock.schedule_interval(update, 1/120.0)

@w.event
def on_mouse_press(x, y, button, modifiers):
  if button == mouse.LEFT:
    if f.x < c.x and c.x+c.width < f.x+f.width:
      s.play()
      c.image = a
      f.visible = 0

app.run()
