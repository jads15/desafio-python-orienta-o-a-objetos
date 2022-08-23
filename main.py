from datetime import datetime
class Pessoa:
  def __init__(self,nome,idade):
   self.nome = nome
   self.idade = idade
  def __str__(self):
    return f'o nome do cliente é {self.nome} e idade é {self.idade}'
  def é_adulto(self):
    if self.idade <18:
      print('não é adulto')
    else:
      print('é adulo')
class Vendedor(Pessoa):
 def __init__(self,nome,idade,salario):
  super().__init__(nome,idade)
  self.salario = salario
class Cliente(Pessoa):
 def __init__(self,nome,idade):
   super().__init__(nome,idade)
   self.compras =[] 
   self.registro = []
 def registrar_compra(self,compra):
   self.compras.append(compra)
   self.registro.append(datetime.now())
 def get_ultima_compra(self):
   print(self.registro[-1])
 def total_compras(self):
  print(f'o total das compras é R${sum(self.compras)}')  
class Compra:
  def __init__(self,vendedor,data,valor):
   self.vendedor = vendedor
   self.data = data
   self.valor = valor
c1 = Cliente('João',17)
compra1 =Compra('Ps4',datetime.now(),2000)
compra2 = Compra('Tv',datetime.now(),1500)
c1.registrar_compra(compra1.valor)
c1.registrar_compra(compra2.valor)
c1.total_compras()
