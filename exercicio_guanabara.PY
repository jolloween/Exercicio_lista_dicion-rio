# TODO - Exercício Python 105: Faça um programa que tenha uma função notas() 
# que pode receber várias notas de alunos e vai retornar um dicionário com as 
# seguintes informações:
# - Quantidade de notas  
# – A maior nota  
# – A menor nota        
# – A média da turma
# – A situação (opcional)

def notas(*n, sit=False):

    r = {}
    
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] > 7:
            r['situacao'] = 'Boa'
        if 5 <= r['media'] < 7:
            r['situacao'] = 'razoavel'
        if r['media'] < 5:
            r['situacao'] = 'Ruim'         
    return r
 

#programa principal:
resp = notas(5.5, 8.0, 9, sit=True)
print(resp)