import ast

import pandas as pd

def leitura(arquivo):
	
	with open(arquivo, 'r') as file:
		info = file.read()
		info = list(map(lambda x: x.split('\t'),
						info.split('\n')))

	return info

def get_lat_lon(geo_data, df):

	for index, cidade in enumerate(geo_data):
		if len(cidade) > 1 and cidade[1] != "None":
			# convertendo a string para dicionário
			info_cidade = ast.literal_eval(cidade[1])[0]
			df.loc[index, 'Lat'] = info_cidade['geometry']['location']['lat']
			df.loc[index, 'Lng'] = info_cidade['geometry']['location']['lng']
		else:
			df.loc[index, 'Lat'] = None
			df.loc[index, 'Lng'] = None

	df.to_csv("Dados/geo_municipios.csv", sep=',', index=False)

if __name__ == '__main__':
	
	geo_data = leitura("Aux/geolocalizacao_cidades.txt")
	df = pd.read_table("Dados/BASE_MUNICIPIOS.csv", sep=',')
	df['Lat'] = 0
	df['Lng'] = 0
	lat_lon = get_lat_lon(geo_data, df)
