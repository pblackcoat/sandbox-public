import pyglet

window = pyglet.window.Window(resizable=True)

def drawLine(xstart, ystart, xend, yend):
		pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
			('v2i', (xstart, ystart, xend, yend))
			)

@window.event
def on_draw():
    i = 0
    window.clear()
    while i <= window.width:
       i = i + 10
       drawLine(i,0,i,window.height)
	drawLine(0,window.height//2,window.width,window.height//2)


		
pyglet.app.run()

#lets add this comment to check git
#new comment