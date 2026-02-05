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
    def nueva_maquina(self):[
        ["COD 123 ", "MONOBRAZO2 ", "JK10" , "MINISTRO"]
    ]
    def agregar_nueva_maquina(self):
        self.Api_maquina.append(self.nueva_maquina)
        
    
    def buscar_info(self):
        return self.Api_maquina[2][2]        