#read data
#import main

prolist = []
data = []

		
class Data:
	def read_projects():
		f = open("projects/pro", 'r')
		for line in f:
			line = line.rstrip()
			if line.startswith("@"):
				e = len(line)
				p = line[1:e]
				prolist.append(p)
		return prolist
	def process():
		pass
	def write_delta(d):
		fw = open("projects/delta", 'a')
		fw.write("\n" + d)
		
	def write_delta_w(d):
		fww = open("projects/delta", 'w')
		fww.write(d)
	def read_delta():
		fd = open("projects/delta", 'r')
		#dd = fd.read()
		for line in fd:
			line = line.rstrip()
			if line.startswith("#"):
				e = len(line)
				p = line[1:e]
				data.append(p)
		return data

	def read_projects_data(n):
		fr = open("projects/"+str(n)+"/pro.oe", 'r')
		dd = fr.read()
		Data.write_delta_w(dd)
		
		return dd
	def write_new_project():
		pass
	def write_project_data(n,d):
		fw = open("projects/"+str(n)+"/pro.oe", 'a')
		
		fw.write("\n"+d)
	def write_project_data_l(n,d):
		fw = open("projects/"+str(n)+"/pro.oe", 'w')
		fw.write("\n"+d)
	def edit_data(pr,n,o,d):
		rd = open("projects/"+str(pr)+"/pro.oe", 'r')
		
		if o == "mesh":
			ld = []
			for line in rd:
				line = line.rstrip()
				if line.endswith(n):
					print(line)
					print("edit "+n)
					ld.append(d)
				else:
					ld.append(line)
			print(ld)
			s = ""
			e = len(ld)
			for i in range(e):
				s += ld[i]
				s += "\n"
			Data.write_project_data_l(pr,s)
	def select(pr,n):
		print("selected "+n)
		sl = open("projects/"+str(pr)+"/sl",'w')
		sl.write(n)
