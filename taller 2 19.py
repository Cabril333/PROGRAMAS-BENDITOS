pokemons=[{'name','Bulbasaur','type','Planta','level',5},
          {'name','Charmander','type','Fuego','level',5},
          {'name','Squirtle','type','Agua','level',5}]

tipo= 'Fuego'
for p in pokemons:
    if p["type"] ==tipo:
        print(p["name"])
        


    