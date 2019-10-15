import hashlib

#temporal de clase
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

	def agregar(self, index, tm_stamp, c_class, p_hash, a_hash, arbol_i):
		nuevo_b = lst(index, tm_stamp, c_class, p_hash, a_hash, arbol_i)
		if self.primero is None:
			self.primero=nuevo_b
			self.ultimo=nuevo_b
			self.tamanio=1
		else:
			nuevo_b.anterior=self.ultimo
			self.ultimo.siguiente=nuevo_b
			self.ultimo=nuevo_b


class ar_avl():
	def __init__(self, carnet, nombre):
		self.izquierda = None
		self.derecha = None
		self.carnet = carnet
		self.nombre = nombre

class m_arbol():
	def insertar(self,nombre, carnet)
#inicializacion
tmp_a = cab_avl()
tmp_l = tmp_lst()




def main():
	print("hello")


main()
