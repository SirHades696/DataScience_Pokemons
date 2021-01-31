import pandas
import requests
import matplotlib.pyplot as plt

url = r"https://pokemondb.net/pokedex/all"
table = requests.get(url).content
data = pandas.read_html(table)
data_pokemon = data[0]

#Total de Ataque y defensa de los pokemones
data_pokemon['Total Attack'] = data_pokemon['Attack'] + data_pokemon['Sp. Atk']
data_pokemon['Total Defense'] = data_pokemon['Defense'] + data_pokemon['Sp. Def']

#Pokemones con mas ataque
attack = data_pokemon.get(['Name', 'Total Attack']).sort_values(by = 'Total Attack', ascending = False).head()
print(attack)
attack.plot(kind = "barh", x='Name', y='Total Attack', title="More Attack")
plt.show()

#Pokemones con mas defensa
defense = data_pokemon.get(['Name', 'Total Defense']).sort_values(by = 'Total Defense', ascending = False).head()
print(defense)
defense.plot(kind = "barh", x='Name', y='Total Defense', title="More Defense")
plt.show()

#Pokemones mas rapidos
speed = data_pokemon.get(['Name', 'Speed']).sort_values(by = 'Speed', ascending = False).head()
print(speed)
speed.plot(kind = "barh", x='Name', y='Speed', title ="faster")
plt.show()

#pokemones con menor ataque 
minor_attack = data_pokemon.get(['Name', 'Total Attack']).sort_values(by = 'Total Attack').head()
print(minor_attack)
minor_attack.plot(kind = "barh", x='Name', y='Total Attack', title='Minor Attack')
plt.show()

#pokemones con menor defensa
minor_defense = data_pokemon.get(['Name', 'Total Defense']).sort_values(by = 'Total Defense').head()
print(minor_defense)
minor_defense.plot(kind = "barh", x='Name', y='Total Defense', title='Minor Defense')
plt.show()

