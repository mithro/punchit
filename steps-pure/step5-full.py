#! /usr/bin/python

import pyglet
win = pyglet.window.Window(800, 100)

chimp_happy = pyglet.resource.image('chimp-happy.png')
chimp_angry = pyglet.resource.image('chimp-angry.png')

chimp = pyglet.sprite.Sprite(chimp_happy)
fist = pyglet.sprite.Sprite(pyglet.resource.image('fist.png'))
sound = pyglet.media.load('boom.wav')

@win.event
def on_draw():
    win.clear()
    fist.draw()
    chimp.draw()

from pyglet.window import mouse

@win.event
def on_mouse_motion(x, y, dx, dy):
    fist.x = x - fist.width/2
    fist.y = y - fist.height/2

chimp.dx = 300
def update(dt):
    if chimp.x+chimp.width >= win.width:
        chimp.dx = -300
    if chimp.x < 0:
        chimp.dx = 300

    chimp.x += chimp.dx*dt

pyglet.clock.schedule_interval(update, 1/120.0)

@win.event
def on_mouse_press(x, y, b, _):
  if fist.x < chimp.x and chimp.x+chimp.width < fist.x+fist.width:
      sound = pyglet.media.load('boom.wav')
      sound.play()

      chimp.image = chimp_angry
      fist.visible = 0

pyglet.app.run()
