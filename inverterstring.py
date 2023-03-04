# Solicita ao usuário a entrada da string
original = input("Digite uma string: ")

# Converte a string em um array de caracteres
caracteres = list(original)

# Inverte o array de caracteres
tamanho = len(caracteres)
for i in range(tamanho // 2):
    temp = caracteres[i]
    caracteres[i] = caracteres[tamanho - 1 - i]
    caracteres[tamanho - 1 - i] = temp

# Cria uma nova string a partir do array de caracteres invertido
invertido = ''.join(caracteres)

# Imprime a string original e a invertida
print("String original: " + original)
print("String invertida: " + invertido)
print("String invertida: " + invertido)





