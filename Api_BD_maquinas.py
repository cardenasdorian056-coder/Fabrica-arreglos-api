class Api_BD_maquinas:
    def __init__(self):
        self.Api_maquina = [
            [ "codigo","nombre maquina","Modelo Maquina","Estado maquina"],
            ["cod 1234", "cierra","x200","apagada"],
            ["cod 2352","optimous","zx400","requiere mantenimiento"],
            ["cod 5648", "taladro","jk100","En reposo"]
        ]
        
    def imprimir_info(self):
        for i in range(len(self.Api_maquina)):
            print(self.Api_maquina[i])
            
    def agregar_elemento(self, nuevo_elemento):
        self.Api_maquina.append(nuevo_elemento)
        
    def insert_elemento(self, insertar_elemento):
        self.Api_maquina.insert( 4 , insertar_elemento)
            
    def remover_elemento(self , eleminar_elemento):
        self.Api_maquina.remove(eleminar_elemento)
    
    def eliminar_posicion(self , eliminar_posicion):
        self.Api_maquina.pop(eliminar_posicion)
        
    def agregar_nueva_lista(self, nueva_lista):
         self.Api_maquina.extend(nueva_lista)
   
    def revertir_orden(self):
        self.Api_maquina.reverse() 
        
    def ordenar_lista(self):
        self.Api_maquina.sort()
        
    def dar_posicion(self, devolver_posicion):
        self.Api_maquina.index(devolver_posicion)
    
    def contar_elementos(self):
        return len(self.Api_maquina)       
    
    def eleminar_maquina(self):
        self.Api_maquina.pop(1)
        
    def buscar_info(self):
        return self.Api_maquina[2][2]        