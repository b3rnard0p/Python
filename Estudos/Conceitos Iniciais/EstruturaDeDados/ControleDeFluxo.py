
#IF and ELSE
senha = input("Digite a senha: ")

senha_secreta = "12345"

if senha == senha_secreta:
  print("Acesso permitido")
else:
  print("Acesso negado")
  
  
cargo = input("Digite seu cargo: ")

if cargo == "admin":
  print("Acesso total")
elif cargo == "user":
  print("Acesso limitado")
elif cargo == "guest":
  print("Acesso mínimo")
else:
  print("Acesso negado")
  
