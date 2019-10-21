from hashlib import sha256
import tkinter as tk
from datetime import datetime
import os
import time
import csv
import json
#temporal de clase
sel_root = None
class tmp_lst():
	def __init__(self):
		self.datos=[0,"", "", "", ""]

	def setx(self, index, tm_stamp, c_class, p_hash, a_hash):
		self.datos = [index, tm_stamp, c_class, p_hash, a_hash]
	def getx(self):
		return self.datos

#temporal de raiz arbol
class cab_avl():
	def __init__(self):
		self.raiz=None
	def setx(self, raiz_i):
		self.raiz=raiz_i
	def getx(self):
		return self.raiz


class lst():
	def __init__(self, index, tm_stamp, c_class,p_hash, a_hash, arbol_i):
		self.siguiente = None
		self.anterior = None
		self.index = index
		self.tm_stamp = tm_stamp
		self.c_class = c_class
		self.p_hash = p_hash
		self.a_hash = a_hash
		self.raiz=arbol_i



class m_lst():
	def __init__(self):
		self.primero = None
		self.ultimo = None
		self.tamanio = 0
	def pri(self):
		s=self.primero
		return s
	
	def ult(self):
		s = self.ultimo
		return s

	def agregar(self, tm_stamp, c_class, p_hash, a_hash, arbol_i):
		nuevo_b = lst(self.tamanio, tm_stamp, c_class, p_hash, a_hash, arbol_i)
		if self.primero is None:
			self.primero=nuevo_b
			self.ultimo=nuevo_b
			self.tamanio=1
		else:
			nuevo_b.anterior=self.ultimo
			self.ultimo.siguiente=nuevo_b
			self.ultimo=nuevo_b
			self.tamanio=self.tamanio+1
	
	def reporte(self):
		actual=self.primero
		f = open("lista_block.dot", "w")
		f.write("digraph { \n node[shape=component]; \n rankdir=TB; \n")
		while True:
			#muestra
			s="cxc"+str(actual.index)+"[label = \" Class: "+str(actual.c_class)+" \\n TimeStamp: "+str(actual.tm_stamp)+" \\n P_hash: "+str(actual.p_hash)+"\\n A_hash= "+str(actual.a_hash)+"  \" ]; \n"
			f.write(s)
			if(actual.siguiente != None):
				s = "cxc"+str(actual.index)+" -> cxc"+str(actual.siguiente.index)+"; \n"
				s += "cxc"+str(actual.siguiente.index)+" -> cxc"+str(actual.index)+"; \n"
				f.write(s)
			actual=actual.siguiente
			if(actual is None):
				break
		f.write("} ")
		f.close()
		os.system("dot -Tjpg lista_block.dot -o lst_blk.jpg")
		#time.sleep(1)
		os.system("xdg-open lst_blk.jpg")
		


class ar_avl(object):
	def __init__(self, carnet, nombre):
		self.left = None
		self.right = None
		self.carnet = carnet
		self.nombre = nombre
		self.hei = 1

class m_arbol(object):
	def __init__ (self):
		self.tmp_rep= ""

	def insertar(self, carnet, nombre, raiz):
		if not raiz:
			return ar_avl(carnet, nombre)
		elif carnet < raiz.carnet:
			raiz.left = self.insertar(carnet, nombre, raiz.left)
		else :
			raiz.right = self.insertar(carnet, nombre, raiz.right)

		#2
		raiz.hei = 1 + max(self.get_h(raiz.left), self.get_h(raiz.right))

		#3
		balance = self.get_bal(raiz)

		#4-balanceo
		if balance > 1 and carnet < raiz.left.carnet:
			return self.rot_der(raiz)

		if balance < -1	and carnet > raiz.right.carnet:
			return self.rot_izq(raiz)
		
		if balance > 1 and carnet > raiz.left.carnet:
			raiz.left = self.rot_izq(raiz.left)
			return self.rot_der(raiz)
		
		if balance < -1 and carnet < raiz.right.carnet:
			raiz.right = self.rot_der(raiz.right)
			return self.rot_izq(raiz)
		
		return raiz

	def get_h(self, t_raiz):
		if not t_raiz:
			return 0
		else:
			return t_raiz.hei
	
	def get_bal(self, t_raiz):
		if not t_raiz:
			return 0
		return self.get_h(t_raiz.left) - self.get_h(t_raiz.right)

	def rot_der(self, w):
		y = w.left
		t3 = y.right

		y.right = w
		w.left = t3

		w.hei = 1 + max(self.get_h(w.left), self.get_h(w.right))
		y.hei = 1 + max(self.get_h(y.left), self.get_h(y.right))

		return y

	def rot_izq(self, w):
		y=w.right
		t2=y.left

		y.left = w
		w.right=t2

		w.hei = 1 + max(self.get_h(w.left), self.get_h(w.right))
		y.hei = 1 + max(self.get_h(y.left), self.get_h(y.right))

		return y
	
	def pre_ord(self, raiz):
		if not raiz:
			return
		print ( str(raiz.carnet) +" ,"+ str(raiz.nombre))
		self.pre_ord(raiz.left)
		self.pre_ord(raiz.right)

	def arbol_dat(self, raiz):
		if not raiz:
			return
		ss="Carnet :"+str(raiz.carnet)+  "\\n Nombre: "+str(raiz.nombre) +" \\n Altura:"+str(self.get_h(raiz))+" \\n FE:"+str(self.get_bal(raiz))
		self.tmp_rep += "cc"+str(raiz.carnet) + \
			"[shape=record, label=\"<C0>|"+ss+" |<C1>  "+"\"]; \n"
		#print(str(raiz.carnet) + " ," + str(raiz.nombre))
		self.arbol_dat(raiz.left)
		self.arbol_dat(raiz.right)
	
	def arbol_rel(self, raiz):
		if not raiz:
			return
		if  raiz.left != None or raiz.right != None:
			if raiz.left != None:
				#aux = raiz.right
				self.tmp_rep += "cc"+str(raiz.carnet) + ":C1  -> cc" + str(raiz.left.carnet) + "; \n"
			if raiz.right != None:
				#aux1 = raiz.left
				self.tmp_rep += "cc"+str(raiz.carnet) + ":C0  -> cc" + str(raiz.right.carnet) + "; \n"
		#print(str(raiz.carnet) + " ," + str(raiz.nombre))
		self.arbol_rel(raiz.left)
		self.arbol_rel(raiz.right)


	def prt_avl_rep_nor(self, raiz):
		f=open("arb_avl.dot","w")
		f.write("digraph { \n")
		self.arbol_dat(raiz)
		f.write(self.tmp_rep)
		self.tmp_rep=""

		self.arbol_rel(raiz)
		f.write(self.tmp_rep)
		self.tmp_rep=""
		f.write("} ")
		f.close()
		os.system("dot -Tjpg arb_avl.dot -o imagen_avl.jpg")
		
		os.system("xdg-open imagen_avl.jpg")

	def reporte_preord(self, raiz):
		if not raiz:
			return
		l_tmp.agregar(raiz.carnet, raiz.nombre)
		self.reporte_preord(raiz.left)
		self.reporte_preord(raiz.right)

	def reporte_inord(self, raiz):
		if not raiz:
			return
		self.reporte_inord(raiz.left)
		l_tmp.agregar(raiz.carnet, raiz.nombre)
		self.reporte_inord(raiz.right)

	def reporte_postord(self, raiz):
		if not raiz:
			return
		self.reporte_postord(raiz.left)
		self.reporte_postord(raiz.right)
		l_tmp.agregar(raiz.carnet, raiz.nombre)
		
		

class l_temporal():
	def __init__(self, carnet, nombre):
		self.carnet = carnet
		self.nombre = nombre
		self.siguiente = None


class m_temporal():
	def __init__(self):
		self.primero = None
		self.ultimo = None
	
	def truncar(self):
		self.primero = None
		self.ultimo = None
	
	def agregar(self, carnet, nombre):
		nuevo = l_temporal(carnet, nombre)
		if(self.primero is None):
			self.primero = nuevo
			self.ultimo = nuevo
		else:
			self.ultimo.siguiente=nuevo
			self.ultimo=nuevo
	def genera_reporte_gnd(self, raiz, tipo):
		if tipo == 0:
			arbolito.reporte_preord(raiz)
		if tipo == 1:
			arbolito.reporte_postord(raiz)
		if tipo == 2:
			arbolito.reporte_inord(raiz)

		
		self.tmp_rep = ""
		f = open("arb_inord.dot", "w")
		f.write("digraph { \n node[shape=box]; \n rankdir=LR; \n")
		actual = self.primero
		while True:
			s="cc"+str(actual.carnet)+"[label=\" "+str(actual.carnet)+" \\n  "+str(actual.nombre)+" \" ]; \n"
			f.write(s)
			if not actual.siguiente is None:
				s="cc"+str(actual.carnet)+" -> cc"+str(actual.siguiente.carnet)+" ;\n"
				f.write(s)
			actual=actual.siguiente
			if actual is None:
				break

		f.write("} \n")
		f.close()
		os.system("dot -Tjpg arb_inord.dot -o imagen_avl1.jpg")

		os.system("xdg-open imagen_avl1.jpg")

class carga():
	def __init__(self):
		self.sxa=""
		self.clase=""
		self.data_js=""

	def carga_csv(self,ruta):
		self.sxa=""
		self.sxa += "bloques/"+str(ruta)
		with open(str(self.sxa),'r') as csvfile:
			readCSV = csv.reader(csvfile, delimiter=',')
			for row in readCSV:
				if(row[0]=="class"):
					self.clase=str(row[1])
				if row[0]=="data":
					self.data_js=str(row[1])
		self.blk_build()

	def blk_build(self):
		#print(self.clase)
		#print(self.data_js)
		now = datetime.now()
		dt_s = now.strftime("%d-%m-%Y::%H:%M:%S")
		idx=0
		p_ha=""
		hh=lista.pri()
		nn=lista.ult()
		if hh is None:
			idx=0
			p_ha="0000"
		else:
			idx=nn.index+1
			p_ha=nn.a_hash
		suma=str(idx)+str(dt_s)+str(self.clase)+str(self.data_js)+str(p_ha)
		super_hash = sha256(suma.encode('utf-8')).hexdigest()
		##ahora el bloque

		x={
			"INDEX":str(idx),
			"TIMESTAMP":dt_s,
			"CLASS":str(self.clase),
			"DATA":self.data_js,
			"PREVIOUSHASH":p_ha,
			"HASH":super_hash
		}
		y=json.dumps(x)
		
		
		





		


#inicializacion
tmp_a = cab_avl()
tmp_l = tmp_lst()
l_tmp = m_temporal()
arbolito = m_arbol()
lista = m_lst()
s_carga = carga()
#0 preord
#1 postord
#2 inord

def lim(texto):
	s=texto[:50]
	return s


def gtx(a):
	sm=a.get()
	s_carga.carga_csv(sm)

def lee_ruta():
	window = tk.Tk()
	window.geometry("650x150")
	e1 = tk.Label(window, text="Ingrese la ruta del archivo:")
	e1.grid(row=0, column=0)

	
	eln=tk.Entry(window)
	eln.grid(row=0, column=1)
	
	#print(sn)
	#sn = eln.get()
	r1 = tk.Button(window, text="Analizar", width=15, command=lambda:gtx(eln))
	
	r1.grid(row=2, column=1)

	window.mainloop()

def carrou():
	window = tk.Tk()
	window.geometry("600x100")
	l1 = tk.Label(window, text="Carrousell")
	l1.grid(row=0, column=0)
	window.mainloop()

def menu_reporte():
	window = tk.Tk()
	window.geometry("400x400")
	l1 = tk.Label(window, text="Reportes")
	l1.grid(row=0, column=0)

	r1 = tk.Button(window, text="R. bloque", width=15, command=lista.reporte)
	r1.grid(row=1, column=1)

	r2 = tk.Button(window, text="R. avl", width=15 )
	r2.grid(row=2, column=1)

	r3 = tk.Button(window, text="R. inorden", width=15)
	r3.grid(row=3, column=1)

	r4 = tk.Button(window, text="R. postorden", width=15 )
	r4.grid(row=4, column=1)

	r5 = tk.Button(window, text="R. preorden", width=15)
	r5.grid(row=5, column=1)
	window.mainloop()

def main():

	rr = None
	rr = arbolito.insertar(10, "michael 1", rr)
	rr = arbolito.insertar(20, "michael 2", rr)
	rr = arbolito.insertar(30, "michael 3", rr)
	rr = arbolito.insertar(40, "michael 4", rr)
	rr = arbolito.insertar(50, "michael 5", rr)
	rr = arbolito.insertar(25, "michael 25", rr)
	lista.agregar("tmps","arbolitos","sdfu3495-035n","vsdvrdf",None)
	lista.agregar("tmps1", "arbolitos1", "11sdfu3495-035n", "11vsdvrdf", None)
	lista.agregar("tmps2", "arbolitos2", "22sdfu3495-035n", "22vsdvrdf", None)
	#lista.reporte()
	#print(rr.carnet)
	#arbolito.pre_ord(rr)
	#arbolito.prt_avl_rep_nor(rr)
	#l_tmp.genera_reporte_gnd(rr,0)
	#sf=sha256("hola".encode('utf-8')).hexdigest()
	window = tk.Tk()
	window.geometry("250x200")
	l1 = tk.Label(window, text="Menu")
	l1.grid(row=0, column=0)
	b1 = tk.Button(window, text="Insertar Bloque", width=15, command=lee_ruta)
	b1.grid(row=1, column=1)

	b2 = tk.Button(window, text="Seleccionar bloque", width=15, command=carrou)
	b2.grid(row=2, column=1)

	b3 = tk.Button(window, text="Reportes", width=15, command=menu_reporte)
	b3.grid(row=3, column=1)

	window.mainloop()
	

main()


