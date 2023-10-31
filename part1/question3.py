################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!
def make_oven():
  return Oven()

def alchemy_combine(oven, ingredients, temperature):
  
  for item in ingredients:
    oven.add(item)
  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()
  return oven.get_output()


class Oven:
  
   def __init__(self):
        # Declarar una lista como atributo de la clase
        self.mis_items = []
        self.cooking = ""

   def add(self,item):
      self.mis_items.append(item)

   def mostrar_lista(self):
      print(self.mis_items)
   
   def boil(self):
      self.cooking = "Hervir"
     
   def freeze(self):
    self.cooking = "Congelar"
   
   def wait(self):
      self.cooking = "Esperando"
   

   def get_output(self):
      if  {"lead", "mercury"}.issubset(set(self.mis_items)) and self.cooking == "Hervir":
         return "gold"
      elif {"water", "air"}.issubset(set(self.mis_items)) and self.cooking == "Congelar":
         return "snow"
      elif {"cheese", "dough", "tomato"}.issubset(set(self.mis_items)) and self.cooking == "Hervir":
         return "pizza"
      elif  {"coco", "water"}.issubset(set(self.mis_items)) and self.cooking == "Esperando":
         return "coconut water"
      else:
         return "Receta no conocidad"



   

