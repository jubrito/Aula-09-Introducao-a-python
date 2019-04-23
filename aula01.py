full_name = "Ana Beatriz"
age = 23
is_new = True
print(full_name)
birth_year = input('qual o ano quer vc nasceu? \n')
print(birth_year)
#colocar python aula01.py para rodar o arquivo

name = 'Juliana Witzke'
print(name[1:5])
print(len(name))
print(name.find('i'))
print(name.replace('Beatriz', 'Morita'))

course = 'Estação Hack do Facebook'
print('Hack' in course)

#LISTAS
numbers = [1,4,3,2,4,2,1]
numbers.append(20)
numbers.insert(0,99) #coloca 99 na posicao 0 
numbers.remove
numbers.pop()
numbers.index(345) #retorna a posicao do numero 345
#remove repetidos
nova_lista = []
for number in numbers:
    if number not in nova_lista:
        nova_lista.append(number)


#TUPLA (lista constante)
cursos = ('Matematica', 'Ingles', 'Frances')