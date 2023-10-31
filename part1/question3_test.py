from question3 import alchemy_combine,make_oven 

def test_alchemy_combine():

  assert alchemy_combine(
    make_oven(),
    ["lead", "mercury"],
    5000
  ) == "gold"

  assert alchemy_combine(
    make_oven(),
    ["water", "air"],
    -100
  ) == "snow"

  assert alchemy_combine(
    make_oven(),
    ["cheese", "dough", "tomato"],
    150
  ) == "pizza"

  assert alchemy_combine(
    make_oven(),
    ["coco", "water"],
    70
  ) == "coconut water"


assert alchemy_combine(
    make_oven(),
    ["coco", "shoes"],
    70
  ) == "Receta no conocidad"

