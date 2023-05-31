from cliente import Cliente
from cliente_fidelidade import ClienteFidelidade
from controlador_pedidos import ControladorPedidos
from pedido import Pedido
from tipo_pedido import TipoPedido


c=ControladorPedidos()
# cliente1=Cliente('10600309932','isa','sc','988351707')
cliente2=ClienteFidelidade(1,0.1,'59714719968','isa','sc','988351707')
tipo1=TipoPedido('comida',2.5)
# p1=Pedido(1,cliente1,tipo1)
p2=Pedido(2,cliente2,tipo1)
p3=Pedido(1,cliente2,tipo1)
# p1.inclui_item_pedido(1,'x',10)
p2.inclui_item_pedido(2,'x',10)
# p2.inclui_item_pedido(4,'x',0)
p3.inclui_item_pedido(3,'x',20)
# print(p1.itens)
print(p2.itens)
print(p3.itens)
# p1.calcula_valor_pedido(1.5)
print(p2.calcula_valor_pedido(1.0))
print(p3.calcula_valor_pedido(1.0))
print('************************')
# c.incluir_pedido(p1)
c.incluir_pedido(p2)
c.incluir_pedido(p3)
print('faturamento cliente 2:')
print(c.calcular_faturamento_pedidos(1,'59714719968'))
# c.incluir_pedido(p1)
# c.incluir_pedido(p2)
# print(c.pedidos)
# c.excluir_pedido(1)
# c.excluir_pedido(3)
# print(c.pedidos)
# cliente2.mostra_cpf()