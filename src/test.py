# %% Aqui está um celular de código Python. Você pode executar o código dentro dele clicando no botão "Run Cell" ou pressionando Shift + Enter.
# Criar uma lista e exibir seus elementos
numeros = [1, 2, 3, 4, 5]
print("Lista de números:", numeros)

#%%
# Calcular o quadrado de cada número na lista
quadrados = [x ** 2 for x in numeros]
print("Quadrados dos números:", quadrados)

#%%
# Função para calcular a soma de uma lista
def soma_lista(lista):
    return sum(lista)

soma_total = soma_lista(numeros)
print("Soma dos números:", soma_total)

#%%
# Gerar uma mensagem formatada
mensagem = f"A soma dos números é {soma_total}, e os quadrados são {quadrados}."
print(mensagem)
