import googlemaps
import pandas as pd
from datetime import datetime


if __name__ == '__main__':
	
	gmaps = googlemaps.Client(key='AIzaSyBdmQARlwcAfIMrnhDPxsO8GZ_uKkyEQyg')

	df = pd.read_table("Dados/BASE_MUNICIPIOS.csv", sep = ',')

	cidades = df[['NOME_CIDADE', 'UF']].apply(lambda x: ', '.join(x), axis=1)

	with open('Aux/geolocalizacao_cidades.txt', 'w') as file:
		for cidade in cidades:
			geo_result = gmaps.geocode(cidade)
			if geo_result is not None and geo_result:
				file.write(cidade + '\t' + str(geo_result) + '\n')
			else:
				file.write(cidade + '\t' + "None" + '\n')
