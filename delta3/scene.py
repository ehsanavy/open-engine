#scene
from tkinter import *
from OpenGL.GL import *
from OpenGL.Tk import *
from OpenGL.GLUT import *
import read_data

na = ''

class Main:
	def cube(px,py,pz,rx,ry,rz,sx,sy,sz):
		glTranslatef(float(px),float(py),float(pz))
		glRotatef(float(rx),float(ry),float(rz),1)
		glScalef(float(sx),float(sy),float(sz))
		glBegin(GL_QUADS)  # Start Drawing The Cube
		glColor(1,1,1)
		
		# Front Face (note that the texture's corners have to match the quad's corners)
		#glTexCoord2f(0.0, 0.0)
		glVertex3f(-1.0, -1.0, 1.0)  # Bottom Left Of The Texture and Quad
		#glTexCoord2f(1.0, 0.0)
		glVertex3f(1.0, -1.0, 1.0)  # Bottom Right Of The Texture and Quad
		#glTexCoord2f(1.0, 1.0)
		glVertex3f(1.0, 1.0, 1.0)  # Top Right Of The Texture and Quad
		#glTexCoord2f(0.0, 1.0)
		glVertex3f(-1.0, 1.0, 1.0)  # Top Left Of The Texture and Quad

		# Back Face
		#glTexCoord2f(1.0, 0.0)
		glVertex3f(-1.0, -1.0, -1.0)  # Bottom Right Of The Texture and Quad
		#glTexCoord2f(1.0, 1.0)
		glVertex3f(-1.0, 1.0, -1.0)  # Top Right Of The Texture and Quad
		#glTexCoord2f(0.0, 1.0)
		glVertex3f(1.0, 1.0, -1.0)  # Top Left Of The Texture and Quad
		#glTexCoord2f(0.0, 0.0)
		glVertex3f(1.0, -1.0, -1.0)  # Bottom Left Of The Texture and Quad

		# Top Face
		#glTexCoord2f(0.0, 1.0)
		glVertex3f(-1.0, 1.0, -1.0)  # Top Left Of The Texture and Quad
		#glTexCoord2f(0.0, 0.0)
		glVertex3f(-1.0, 1.0, 1.0)  # Bottom Left Of The Texture and Quad
		#glTexCoord2f(1.0, 0.0)
		glVertex3f(1.0, 1.0, 1.0)  # Bottom Right Of The Texture and Quad
		#glTexCoord2f(1.0, 1.0)
		glVertex3f(1.0, 1.0, -1.0)  # Top Right Of The Texture and Quad

		# Bottom Face
		#glTexCoord2f(1.0, 1.0)
		glVertex3f(-1.0, -1.0, -1.0)  # Top Right Of The Texture and Quad
		#glTexCoord2f(0.0, 1.0)
		glVertex3f(1.0, -1.0, -1.0)  # Top Left Of The Texture and Quad
		#glTexCoord2f(0.0, 0.0)
		glVertex3f(1.0, -1.0, 1.0)  # Bottom Left Of The Texture and Quad
		#glTexCoord2f(1.0, 0.0)
		glVertex3f(-1.0, -1.0, 1.0)  # Bottom Right Of The Texture and Quad

		# Right face
		#glTexCoord2f(1.0, 0.0)
		glVertex3f(1.0, -1.0, -1.0)  # Bottom Right Of The Texture and Quad
		#glTexCoord2f(1.0, 1.0)
		glVertex3f(1.0, 1.0, -1.0)  # Top Right Of The Texture and Quad
		#glTexCoord2f(0.0, 1.0)
		glVertex3f(1.0, 1.0, 1.0)  # Top Left Of The Texture and Quad
		#glTexCoord2f(0.0, 0.0)
		glVertex3f(1.0, -1.0, 1.0)  # Bottom Left Of The Texture and Quad

		# Left Face
		#glTexCoord2f(0.0, 0.0)
		glVertex3f(-1.0, -1.0, -1.0)  # Bottom Left Of The Texture and Quad
		#glTexCoord2f(1.0, 0.0)
		glVertex3f(-1.0, -1.0, 1.0)  # Bottom Right Of The Texture and Quad
		#glTexCoord2f(1.0, 1.0)
		glVertex3f(-1.0, 1.0, 1.0)  # Top Right Of The Texture and Quad
		#glTexCoord2f(0.0, 1.0)
		glVertex3f(-1.0, 1.0, -1.0)
		
		glEnd()

	def grid():
		glBegin(GL_LINES)		
		
		
		# x line
		glColor3f(1 , 0, 0)
		glVertex3fv((-100, 0, 0))
		glVertex3fv((100, 0, 0))
		glVertex3fv((-100, 0, 1))
		glVertex3fv((100, 0, 1))
		glVertex3fv((-100, 0, -1))
		glVertex3fv((100, 0, -1))
		glVertex3fv((-100, 0, -2))
		glVertex3fv((100, 0, -2))
		glVertex3fv((-100, 0, 2))
		glVertex3fv((100, 0, 2))
		glVertex3fv((-100, 0, -3))
		glVertex3fv((100, 0, -3))
		glVertex3fv((-100, 0, 3))
		glVertex3fv((100, 0, 3))
		glVertex3fv((-100, 0, -4))
		glVertex3fv((100, 0, -4))
		glVertex3fv((-100, 0, 4))
		glVertex3fv((100, 0, 4))
		glVertex3fv((-100, 0, -5))
		glVertex3fv((100, 0, -5))
		glVertex3fv((-100, 0, 5))
		glVertex3fv((100, 0, 5))
		
		# y line
		glColor3f(0 , 1, 0)
		glVertex3fv((0, -100, 0))
		glVertex3fv((0, 100, 0))
		# z line
		glColor3f(0 , 0, 1)
		glVertex3fv((0, 0, -100))
		glVertex3fv((0, 0, 100))
		glVertex3fv((1, 0, -100))
		glVertex3fv((1, 0, 100))
		glVertex3fv((-1, 0, -100))
		glVertex3fv((-1, 0, 100))
		glVertex3fv((-2, 0, -100))
		glVertex3fv((-2, 0, 100))
		glVertex3fv((2, 0, -100))
		glVertex3fv((2, 0, 100))
		glVertex3fv((-3, 0, -100))
		glVertex3fv((-3, 0, 100))
		glVertex3fv((3, 0, -100))
		glVertex3fv((3, 0, 100))
		glVertex3fv((-4, 0, -100))
		glVertex3fv((-4, 0, 100))
		glVertex3fv((4, 0, -100))
		glVertex3fv((4, 0, 100))
		glVertex3fv((-5, 0, -100))
		glVertex3fv((-5, 0, 100))
		glVertex3fv((5, 0, -100))
		glVertex3fv((5, 0, 100))
		
		glEnd()
	class Delta:
		na = ''
		def get_delta():
			c = read_data.Data.read_delta()
			return c
		def set_delta():
			global na
			a = Main.Delta.get_delta()
			#print(a)
			def draw():
				for i in a:
					#print(i)
					if i[0] == "c": 
						eocg = len(i)
						ocg = i[2:eocg]
						if i.find('pos') >= 0:
							ex = i.find('x')
							xc = i[5:ex]
							ey = i.find('y')
							yc = i[ex+1:ey]
							ez = i.find('z')
							zc = i[ey+1:ez]
							if i.find('rot') >= 0:
								erx = i.find('xr')
								xrc = i[ez+5:erx]
								ery = i.find('yr')
								yrc = i[erx+2:ery]
								erz = i.find('zr')
								zrc = i[ery+2:erz]
								if i.find('size') >= 0:
									esx = i.find('xs')
									xsc = i[erz+7:esx]
									esy = i.find('ys')
									ysc = i[esx+2:esy]
									esz = i.find('zs')
									zsc = i[esy+2:esz]
									mesh = Main.cube(xc,yc,zc,xrc,yrc,zrc,xsc,ysc,zsc)
									#print(i)
									Main.Redraw
								
							
						
					
				
			
			draw()
			a.clear()

	class Redraw:
		def __init__(self,o):
			glClearColor(0, 0.5, 1, 0)
			glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
			glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
			Main.grid()
			a = Main.Delta.set_delta()
			#o.redraw = Main.Redraw
			
	
