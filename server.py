import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  # Retorna o índice da primeira ocorrência de value
  # Caso nenhuma ocorrência seja encontrada, o valor -1 é retornado
  def exposed_find(self, value):
    try:
      value_index = self.value.index(value)
    except:
      value_index = -1

    return value_index

  # Remove a primeira ocorrência de value na lista
  def exposed_delete(self, value):
    value_index = self.value.index(value)
    self.value = self.value[0:value_index] + self.value[value_index+1:]
    return self.value

  # Insere data no índice `position` da lista
  def exposed_insert(self, data, position):
    self.value = self.value[0:position] + [data] + self.value[position:]
    return self.value

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  # Ordena a lista ascendente ou descendentemente
  def exposed_sort(self, reverse = False):
    self.value.sort(reverse=reverse)
    return self.value

  def exposed_value(self):
    return self.value

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

