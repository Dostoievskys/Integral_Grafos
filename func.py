class Parametros:
    def init(self, T, N, X, Y):
        self.T = T
        self.N = N
        self.X = X
        self.Y = Y
    def mostrar(self):
        print(self.T)
        print(self.N)
        print(self.X)
        print(self.Y)

class Conexion:
    def init(self, idCam, idCen, Punto, Cant):
        self.idCam = idCam
        self.idCen = idCen
        self.Punto = Punto
        self.Cant = Cant
    def mostrar(self):
        print('Camion: ', self.idCam)
        print('Centro:', self.idCen)
        print('Punto: ', self.Punto)
        print('Cantidad: ', self.Cant)

def lecturaArchivo(ar):
    archivo = open(ar)
    Rutas = []
    for linea in archivo:
        dato = linea.split(';') #Separo la linea por los ; y lo guardo en un arreglo
        R = Almacenar(dato)
        Rutas.append(R)
    archivo.close()
    return Rutas

def Almacenar(linea):
    Datos = Parametros()
    Datos.T = linea[0] #Guardo los datos del arreglo en la clase
    Datos.N = linea[1]
    C = linea[2].split(',') #Separo las coordenadas por la , 
    Datos.X=int(C[0]) #Guardo coordenada X 
    Datos.Y=int(C[1]) #Guardo coordenada Y
    return Datos

