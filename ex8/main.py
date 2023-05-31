from elevador import Elevador
from controladorElevador import ControladorElevador

# e=Elevador(5,1,10,1)
controlador=ControladorElevador()
controlador.inicializar_elevador(0,10,5,1)
print(f'Quantidade de pessoas : {controlador.elevador.total_pessoas}')
print(f'Andar atual: {controlador.elevador.andar_atual}')
print(controlador.subir())
print(controlador.subir())
print(f'Andar atual: {controlador.elevador.andar_atual}')
print(controlador.descer())
print(f'Andar atual: {controlador.elevador.andar_atual}')
print(controlador.entra_pessoa())
print(f'Quantidade de pessoas : {controlador.elevador.total_pessoas}')



