def get_salas_por_reunioes(reunioes):
    salas = 0
    quantidade_reunioes = get_quantidade_reunioes(reunioes)

    if quantidade_reunioes > 0:
        reunioes.sort(key=lambda x: x[1])
        salas += 1

        fim = reunioes[0][1]

        for i in range(1, quantidade_reunioes):
            if reunioes[i][0] < fim:
                fim = reunioes[i][1]
                salas += 1

    return salas

def get_quantidade_reunioes(reunioes):
    quantidade = 0
    for item in reunioes:
        if item != []:
            quantidade += 1
    return quantidade

print(get_salas_por_reunioes([[0, 30], [5, 10], [15, 20]]))
print(get_salas_por_reunioes([[]]))
print(get_salas_por_reunioes([[15, 20], [15, 20], [15, 20]]))
print(get_salas_por_reunioes([[10, 20], [20, 30]]))