import requests
import json
import webbrowser
def getCocktails():
    v = r"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=Vodka"
    g = r"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=Gin"
    t = r"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=Tequila"

    data = requests.get(v)
    data2 = requests.get(g)
    data3 = requests.get(t)
    tt = json.loads(data.text)
    tt1 = json.loads(data2.text)
    tt2 = json.loads(data3.text)

    vodkaCocktails = [i['strDrink'] for i in (tt["drinks"])]
    ginCocktails = [i['strDrink'] for i in (tt1["drinks"])]
    teqCocktails = [i['strDrink'] for i in (tt2["drinks"])]

    #for x in vodkaCocktails:
    #    tempCLink = r"https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + 

    return vodkaCocktails + ginCocktails + teqCocktails
    
with open('cocktailOutput.txt', 'w') as f:
    for cock in getCocktails():
        f.write(cock)
        f.write('\n')

#print(getCocktails())
x = r"https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + "margarita"


def c():
    f = r"https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"
    data = requests.get(f)
    tt = json.loads(data.text)
    
    
    for i in (tt["drinks"]):
        print(i["strDrink"], "\n")
        print(i["strInstructions"], "\n")
        print(i["strInstructionsDE"], "\n")
        
        print(i["strIngredient1"])
        print(i["strIngredient2"])
        print(i["strIngredient3"])
        print(i["strIngredient4"])
       # url = i["strDrinkThumb"]
        #webbrowser.open(url)

