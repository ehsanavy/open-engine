from OpenGL.Tk import *
import sys
from six.moves import range
import numpy as np
import nodes.camera.pct as camera3d


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
			
		
			
	glEnable(GL_LIGHTING)
