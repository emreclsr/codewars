def cakes(recipe, available):
    
    recipe_key = list(recipe.keys())
    available_key = list(available.keys())
    
    cake=0
    if all(x in available_key for x in recipe_key) is True:  
        while True:
            res = {key: available[key] - recipe.get(key, 0) for key in available.keys()}
            amount = list(res.values())
            print(amount)

            if any(n < 0 for n in amount) is True:
                break
                
            cake+=1
            available = res
        return cake
    else:       
        return cake










