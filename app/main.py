import utils
import read_csv #Llamar modulos
import charts 

""""
keys, values = utils.get_population()
print(keys, values)

print(utils.a)

data = [
  {
    'country' : 'colombia',
    'population' : 500  
  },
  {
    'country' : 'bolivia',
    'population' : 300
  }
]
"""

def run():
  data = read_csv.read_csv('data.csv') #modulo y función, se llaman igual en este caso
  data = list(filter(lambda item : item['Continent'] == 'South America', data)) #Filtro para solo SA

  countries = list(map(lambda x : x['Country/Territory'], data))
  percentages = list(map(lambda x : x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)


  country = input('Digite el pais => ')
  
  result = utils.population_by_country(data, country) #Envio y busco el pais  que quiero obtener
  
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values) #Toma el nombre de la columna de pais


if __name__ == '__main__':
  run()
