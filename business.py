def get_data():
   file = open("data.txt","r") 
   content= file.read()
   print(content)
   namesList= content.splitlines()
   return namesList