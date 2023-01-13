import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  print (conn.root.exposed_value())
  conn.root.exposed_append(5)       # Call an exposed operation,
  conn.root.exposed_append(6)       # and append two elements
  conn.root.exposed_append(10) 
  conn.root.exposed_append(77) 
  conn.root.exposed_append(18)
  conn.root.exposed_insert(99, 2)
  conn.root.exposed_append(101)
  print (conn.root.exposed_value()) 
  conn.root.exposed_delete(77)
  print("Posição do 17:", conn.root.exposed_find(17) if conn.root.exposed_find(17) != -1 else "NOT FOUND")
  print("Posição do 18:", conn.root.exposed_find(17) if conn.root.exposed_find(17) != -1 else "NOT FOUND")
  print (conn.root.exposed_value())   # Print the result
  conn.root.exposed_sort()
  print (conn.root.exposed_value())   # Print the result
