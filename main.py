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
	f = Frame(root)
	f.pack(side = 'top')
	
	
	
	
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
	o.pack(side = 'top', expand = 1, fill = 'both')
	o.set_eyepoint(20.)
	o.mainloop()

main()
