#! /usr/bin/env python
from __future__ import absolute_import
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.Tk import *
import sys
from six.moves import range
import numpy as np




def redraw(o):
	glClearColor(0, 0.5, 1, 0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glColor3f(0, 1, 0)
	#draw checkerboard
	
	glColor3f(1 , 0, 0)
	glPointSize(200.0)
	
	glBegin(GL_LINES)		
	
	# x line
	glColor3f(1 , 0, 0)
	glVertex3fv((-100, 0, 0))
	glVertex3fv((100, 0, 0))
	
	# y line
	glVertex3fv((0, -100, 0))
	glVertex3fv((0, 100, 0))
	
	# z line
	glVertex3fv((0, 0, -100))
	glVertex3fv((0, 0, 100))
	
			
	glEnd()
	
	
	
	
	N = 4
	glDisable(GL_LIGHTING)
	for x in range(-N, N):
		for y in range(-N, N):
			if (x + y) % 2 == 0:
				glColor3f(1, 1, 1)
			else:
				glColor3f(0, 0, 0)
			#glRectf(x, y, x + 1, y + 1)
			
			
	glEnable(GL_LIGHTING)
	
	
	
	

	glPushMatrix()
	glTranslatef(0., 0., 1.)
	
	glutSolidSphere(2.0,30,30)
	
	glPopMatrix()


def main():

	o = Opengl(width = 860, height = 480, double = 1, depth = 1)
	
	root = o.master
	root.title("Open Engine v 1.0.0-0(alpha)")
	
	
	f = Frame(root, bg = "black")
	f.pack(side = 'top')
	
	bl = Frame(root, bg = "black", width = 20)
	bl.pack(side = "left")
	
	node3ds = Frame(root, bg = "black")
	node3ds.pack(side = "right")		
	nntds = Label(node3ds, bg = "black", fg = "white",text = "node 3D", width = 20)
	nntds.pack({"side" : "top","side":"right"})
	
	
	o.set_background( 1.0, 0, 0)
	o.set_centerpoint(0, 0, 0)
	glutInit( [] )
	o.redraw = redraw
	
	quit = Button(f, text = 'Quit', command = sys.exit)
	quit.pack({'side':'top', 'side':'left'})
	
	help = Button(f, text = 'Help', command = o.help)
	help.pack({'side':'top', 'side':'left'})
	
	reset = Button(f, text = 'Reset', command = o.reset)
	reset.pack({'side':'top', 'side':'left'})
	
	a = Label(bl, text = "nodes", bg = "black", fg= "white", width = 20)
	a.pack({"side" : "left", "side":"top"})
	
	def nntdbr():
		nntds.config(text='node 3D')
	m = Button (bl,bg = "black",fg = "white",activebackground = "red",text= "node3D", width = 20, command = nntdbr)
	m.pack({"side" : "left", "side":"top"})
	
	
	
	def nsbr():
		nntds.config(text = "mesh 3D")
	scp = Button (bl,bg = "black",fg = "white",activebackground = "red",text= "mesh 3D", width = 20, command = nsbr)
	scp.pack({"side" : "left", "side":"top"})
	
	
	
	
	o.pack(expand = 1, fill = 'both',side = "top")
	o.set_eyepoint(20.)
	o.mainloop()

main()
