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

app.run()
