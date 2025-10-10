#todo - Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

#lista e dicionário:
galera = []
pessoas = {}
#validações:
soma_idade = 0 # a soma das idades das pessoas cadastradas.
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoas['sexo'] in "MF":
            break
        print("Digite apenas (M) para masculino ou (F) para feminino.")
    while True:
        try:
            pessoas['idade'] = int(input('Idade: '))
            break
        except ValueError as e:
            print(f"Por favor. Digite a idade correta.\n{e}")
    galera.append(pessoas.copy())
    soma_idade += pessoas['idade']

    while True:
        resp = str(input('Quer continuar [S/N]')).upper()[0]
        if resp in "SN":
            break
        print("Digite (S) para sim e (N) para não.")
    if resp == "N":
        break

print("--=="*20)
print(galera) #print do meu dicionário com uma lista dentro.
print(f'A) o total de {len(galera)} pessoas cadastradas.') #Total de pessoas cadastradas.
media_idade = soma_idade / len(galera) # len(galera) é o total de pessoas cadastradas
print(f'B) A média da idade foi: {media_idade:.1f} anos') #média da idade.
print(f'C) As mulheres cadastradas foram: ',end="")
for p in galera:
    if p['sexo'] == "F":
        print(f'{p["nome"]}', end=" ")
print()
print(f'D) Lista das pessoas que estão acima da média')
for p in galera:
    if p['idade'] > media_idade:
        print("           ")
        for k, v in p.items():
            print(f'{k} = {v}; ', end="")
        print()
print("««««ENCERRADO»»»»»»")