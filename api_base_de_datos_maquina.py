class Api_bd_maquina:
    def __init__(self):
        self.Api_maquina=[
            ["codigo "," nombre maquina" , " modelo maquina" , " estado maquina "],
            ["cod 1233443433"  , "tractomula" , "2024" , "prendida" ],
            ["cod 123343433"  , "tractoa" , "2024" , "prendida" ],
            ["cod 1233443433"  , "escavadora" , "2024" , "apagado" ],
            ["cod 1233443433"  , "camion" , "2024" , " en mantenimiento" ]
        
            ]
        
        
    def inprimir_info(self):
            for i in range (len(self.Api_maquina)):
                print(self.Api_maquina[i])

    def hacer_info(Self):
            return Self.Api_maquina[0],[1]