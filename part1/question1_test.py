from question1 import get_city_weather

def test_get_city_weather():

  assert get_city_weather("Quito") == "22 degrees and sunny"

  assert get_city_weather("New York") == "14 degrees and rainy"

  assert get_city_weather("San Francisco") == "16 degrees and No weather"

  assert get_city_weather("Sao Paulo") == "17 degrees and cloudy"

  assert get_city_weather("Sin lugar") == "0 degrees and No weather"
  
  assert get_city_weather(1.128130123) == "Por favor ingrese el nombre de una cuidad"