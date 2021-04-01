import requests
import sys
# Puntos Minimos
try:
    minPoints = int(input('Puntuación mínima (vacío para no mínimo)\n'));
except ValueError:
    minPoints = 0
    print('Valor se ajusta a 0')
    
# Puntos Máximos
try:
    maxPoints = int(input('Puntuación máxima (vacío para no máximo)\n'));
except ValueError:
    maxPoints = sys.maxsize
    print('Valor se ajusta a ' + str(sys.maxsize))
    


url = ''
response = requests.get(url)
json = response.json

