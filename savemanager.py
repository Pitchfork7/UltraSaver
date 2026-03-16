
realsavefile = "save.txt"
content = ""

def loadreal():
  global realsavefile
  global content
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
  data_to_save = ""

  # 'w' stands for write mode
  with open(name, 'w') as file:
      file.write(data_to_save)
  
  print(f"Successfully created '{name}' and wrote data to it.")

def savetofake(name):
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
