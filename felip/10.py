dd = int(input("Informe o DDD desejado:"))

dic_ddd = {"ddd":[11, 19, 21, 27, 31, 32, 61, 71],
           "cidades":["São Paulo","Campinas", "Rio de Janeiro", "Vitória", "Belo Horizonte", "Juiz de Fora", "Brasília", "Salvador"]}

if dd in dic_ddd["ddd"]:
    n = dic_ddd["ddd"].index(dd)
    print("Este DDD pertenca à", dic_ddd["cidades"][n])

else:
    print("DDD não cadastrado")