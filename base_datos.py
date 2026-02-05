class Api_BD:
    def __init__(self):
      self.Api_datos = []
      
    def guardar_empleado(self,obj_nuevo_empleado):
        self.Api_datos.append(obj_nuevo_empleado)
        
        
        
    def imprimir_Api(self):
        #usames el for para recorer la cantidad de datos que se presentan
        for i in range(len(self.Api_datos)):
            print(self.Api_datos[i].ver_infor())
    
    def eliminar_empleado(self,obj_empleado):
        self.Api_datos.pop(obj_empleado)
        
    def agregar_elemen_lista(self,obj_nuevo_elemento):
        self.Api_datos.extend(obj_nuevo_elemento)    
    
    
        