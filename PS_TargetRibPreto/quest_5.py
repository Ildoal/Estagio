# string a ser invertida
string_original = "Exemplo de string a ser invertida"

# Criar uma nova string vazia
string_invertida = ""

# Loop para percorrer a string original ao contrário e adicionar cada caractere na nova string
for i in range(len(string_original)-1, -1, -1):
    string_invertida += string_original[i]

# string original e a string invertida
print("String original: ", string_original)
print("String invertida: ", string_invertida)
