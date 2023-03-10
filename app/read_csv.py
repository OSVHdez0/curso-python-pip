import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',') # puede ser tambien ;
    header = next(reader)
    #print(header)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      #print(country_dict)
      data.append(country_dict) #Diccionario 
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])