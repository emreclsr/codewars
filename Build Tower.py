def tower_builder(n_floors):
    a = []
    for i in range(n_floors):
        a.append(((2*i+1)*"*").center(2*n_floors-1))
    return a