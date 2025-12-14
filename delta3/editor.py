#editor
from tkinter import *
from OpenGL.GL import *
from OpenGL.Tk import *
import read_data
import scene
from tkinter import ttk
import load_ogui
import set_name


selct = "f"
nodelist = []

class Main:
	def set_theme():
		style = ttk.Style()
		style.theme_create('custom_theme', parent='alt', settings={
		    'TButton': {
		        'configure': {
		            'background': '#4CAF50',
		            'foreground': 'white',
		            'font': ('Helvetica', 12),
		            'padding': 10
		        }
		    },
		    'TLabel': {
		        'configure': {
		            'background': '#f0f0f0',
		            'foreground': '#333',
		            'font': ('Helvetica', 12)
		        }
		    }
		})
		style.theme_use('custom_theme')

	def main(n):
		o = Opengl(width = 1000, height = 600, double = 1, depth = 1)
		root = o.master
		root.title("openengine 1.0.4.3-0 "+str(n))
		Main.set_theme()
		#######################################################################
		#top frame
		tf = ttk.Frame(root)
		tf.pack(side = 'top')
		#exit button
		quit = ttk.Button(tf, text = 'Quit', command = sys.exit)
		quit.pack({'side':'top', 'side':'left'})
		#help button
		help = ttk.Button(tf, text = 'Help', command = o.help)
		help.pack({'side':'top', 'side':'left'})
		#reset button
		reset = ttk.Button(tf, text = 'Reset', command = o.reset)
		reset.pack({'side':'top', 'side':'left'})
		#######################################################################
		#node
		lf = ttk.Frame(root)
		lf.pack(side="left")
		#node settings	
		rf = ttk.Frame(root)
		rf.pack(side = 'right')
		#label title frame
		ltr = ttk.Label(rf,text="Node settings")
		ltr.pack(side="top")
		#label title nodes
		lnr = ttk.Label(rf,text="None")
		lnr.pack(side="top")
		
		#mode node
		
		def bms(event):
			global selct
			itemnumber = lst.curselection()
			itemname=lst.get(itemnumber)
			lnr.config(text=str(itemname))
			dd = read_data.Data.read_delta()
			e = len(dd)
			for line in range(e):
				p = dd[line] 
				if p.find(itemname) >= 0:
					px = p[p.find("pos")+3:p.find("x")]
					py = p[p.find("x")+1:p.find("y")]
					pz = p[p.find("y")+1:p.find("z")]
					rx = p[p.find("rot")+3:p.find("xr")]
					ry = p[p.find("xr")+2:p.find("yr")]
					rz = p[p.find("yr")+2:p.find("zr")]
					sx = p[p.find("size")+4:p.find("xs")]
					sy = p[p.find("xs")+2:p.find("ys")]
					sz = p[p.find("ys")+2:p.find("zs")]
					na = p[p.find("name")+5:]
					
					print(px,py,pz,rx,ry,rz,sx,sy,sz,na,n)
				
			
			print(selct)
			read_data.Data.select(n,na)
			if selct == "f":
					import nodes.mesh.ns as mesh
					mesh.mesh(rf,px,py,pz,rx,ry,rz,sx,sy,sz,na,n)
					selct = "t"
			if selct == "t":
				read_data.Data.select(n,na)
			
		######################################################################
		
		######################################################################
		#nodes
		
		#label title frame
		ltl = ttk.Label(lf,text="Nodes")
		ltl.pack(side='top')
		#add mesh node
		
		def addmesh(r):
			nodelist.append(str(r))
			nodelist_var = StringVar(value=nodelist)
			lst.insert(END, r)
			read_data.Data.write_project_data(n,"#c:pos0x0y0z;rot0xr0yr0zr;size1xs1ys1zsname:"+str(r))
			read_data.Data.write_delta("#c:pos0x0y0z;rot0xr0yr0zr;size1xs1ys1zsname:"+str(r))
			#nodeslist(r)
		def get_name_node():
			winn = Tk()
			winn.title("name")
			winn.resizable(False,False)
			
			def get_name():
				d = ewn.get()
				print(d)
				addmesh(d)
				lwn.configure(text = ""+d)
			lwn = Label(winn,text = "name node")
			lwn.pack()
			
			ewn = Entry(winn)
			ewn.pack()
			ewn.focus()
			bwn = Button(winn,text="OK",command=get_name)
			bwn.pack()
		
			winn.mainloop()
		#windows add new node
		def winan():
			wnn = Tk()
			wnn.title("Create a New Node")
			wnn.geometry("900x600")
			m3d = ttk.Button(wnn,text="Mesh3D",command=get_name_node)
			m3d.pack()
			wnn.mainloop()
		#add node
		ban = ttk.Button(lf,text="Add New Node",command=winan)
		ban.pack(side="top")
		 
		######################################################################
		
		
		a = read_data.Data.read_projects_data(n)
		de = read_data.Data.read_delta()
		print(de)
		for i in de:
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
							ena = i.find('name')
							nam = i[ena+5:len(i)]
							nodelist.append(nam)
							print(nodelist)
		nodelist_var = StringVar(value=nodelist)
		lst=Listbox(lf,listvariable=nodelist_var)
		lst.pack()
		lst.bind('<<ListboxSelect>>', bms)
		
		o.redraw = scene.Main.Redraw
		o.pack(expand = 1, fill = 'both',side = "top")
		o.mainloop()
