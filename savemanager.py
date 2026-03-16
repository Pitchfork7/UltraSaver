import sys


realsavefile = "save.txt"
content = ""
fakecontent = "None Loaded"

def loadreal():
  global realsavefile
  global content
  global fakecontent
  try:
      # 'r' stands for read mode
      with open(realsavefile, "r") as file:
          content = file.read()
      
      # Now you can use the 'content' variable
      print("File content successfully loaded:")
      #print(content)
  
  except FileNotFoundError:
      print("Error: no save file was not found.")
  except Exception as e:
      print(f"An unexpected error occurred: {e}")

def makefile(name):
  name = f"{name}.txt"
  data_to_save = ""

  # 'w' stands for write mode
  with open(name, 'w') as file:
      file.write(data_to_save)
  
  print(f"Successfully created '{name}' and wrote data to it.")

def savetofake(name):
  name = f"{name}.txt"
  global content
  data_to_save = content

  # 'w' stands for write mode
  with open(name, 'w') as file:
      file.write(data_to_save)

def savetoreal():
  global content
  data_to_save = content

  # 'w' stands for write mode
  with open(realsavefile, 'w') as file:
      file.write(data_to_save)

def loadfake(name):
  name = f"{name}.txt"
  global content
  global fakecontent
  try:
      # 'r' stands for read mode
      with open(name, "r") as file:
          content = file.read()
      
      # Now you can use the 'content' variable
      print("File content successfully loaded:")
      #print(content)
  
  except FileNotFoundError:
      print("Error: no save file was not found.")
  except Exception as e:
      print(f"An unexpected error occurred: {e}")




def menu():
  global realsavefile
  global content
  global fakecontent
  print("Welcome to UltraSave")
  print("")
  print("")
  print(f"Content = {fakecontent}")
  print("")
  print("")
  print("1. load fake file")
  print("2. load real file")
  print("3. save to fake")
  print("4. save to real")
  print("5. Make file")
  print("5. exit")
  op = input("Select Option> ")
  if op == "1":
    loadfake(input("Name of file> "))
    fakecontent = "fake"
  elif op == "2":
    loadreal()
    fakecontent = "real"
  elif op == "3":
    savetofake(input("Name of file> "))
  elif op == "4":
    savetoreal()
  elif op == "5":
    makefile(input("Name of file> "))
  elif op == "6":
    sys.exit()
  else:
    print("not an option")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  menu()

menu()
  
  

