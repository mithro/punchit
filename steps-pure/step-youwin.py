#! /usr/bin/python

import pyglet
win = pyglet.window.Window(800, 100)

chimp_happy = pyglet.resource.image('chimp-happy.png')
chimp_angry = pyglet.resource.image('chimp-angry.png')

todraw = []
chimp = pyglet.sprite.Sprite(chimp_happy)
todraw.append(chimp)

fist = pyglet.sprite.Sprite(pyglet.resource.image('fist.png'))
todraw.append(fist)

sound = pyglet.media.load('boom.wav')

@win.event
def on_draw():
    win.clear()
    for drawit in todraw:
        drawit.draw()

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
  if fist not in todraw:
      return
  if fist.x < chimp.x and chimp.x+chimp.width < fist.x+fist.width:
      sound = pyglet.media.load('boom.wav')
      sound.play()

      chimp.image = chimp_angry
      todraw.remove(fist)

      from pyglet import text
      label = pyglet.text.Label('You win!', font_size=36,
          x=win.width//2, y=win.height//2,
          anchor_x='center', anchor_y='center')
      todraw.append(label)

pyglet.app.run()
