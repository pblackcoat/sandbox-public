import pyglet

window = pyglet.window.Window(resizable=True)

def drawLine(xstart, ystart, xend, yend):
    

@window.event
def on_draw():
    i = 0
    window.clear()
    while i <= window.width:
                i = i + 10
                pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                        ('v2i', (i, 0, i, window.height))
                        )


		
pyglet.app.run()
