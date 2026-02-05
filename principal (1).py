from Empleado_modelo import Empleado_modelo 
from base_datos import Api_BD
from Api_BD_maquinas import Api_BD_maquinas

# codigo principal 
obj_Api = Api_BD()
obj_Api_maquina = Api_BD_maquinas()

obj_Empleado = Empleado_modelo("Dorian","cardenas","1090396992","350-3568391")
obj_Empleado2 = Empleado_modelo("Maria","perez","888909008","320-75834632")
obj_Empleado3 = Empleado_modelo ("pablo","maduro","1083729200","300-757493779")
obj_Empleado4 = Empleado_modelo("ana","zosa","888909008","320-75834632")

nueva_lista = [
            ["COD xxx ", "MONOBRAZO2 ", "JK1xxxx0" , "MINISTRO"], 
            ["cod345 "," camioneta", "kl2" , "en posesion"]
            
]
nuevo_elemento=[
    "cod 122 ", "metro" , "zk3" , "muerto"
]
insertar_elemento=(" xkx", "karretilla" , "zkl " , "dañao")

eleminar_elemento=["cod 1234", "cierra","x200","apagada"]

eliminar_posicion = (2)

devolver_posicion = ["cod 5648", "taladro","jk100","En reposo"]


obj_Api_maquina.eliminar_posicion(eliminar_posicion)
obj_Api_maquina.remover_elemento(eleminar_elemento)
obj_Api_maquina.insert_elemento(insertar_elemento)
obj_Api_maquina.agregar_elemento(nuevo_elemento)
obj_Api_maquina.agregar_nueva_lista(nueva_lista)
obj_Api_maquina.dar_posicion(devolver_posicion)
obj_Api_maquina.imprimir_info()
print(obj_Api_maquina.buscar_info())

obj_Api.guardar_empleado(obj_Empleado)
obj_Api.guardar_empleado(obj_Empleado2)
obj_Api.guardar_empleado(obj_Empleado3)
obj_Api.guardar_empleado(obj_Empleado4)

obj_Api.imprimir_Api()

