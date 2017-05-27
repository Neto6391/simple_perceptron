from random import random

def fatiarArquivo(file):
	f_split = file.split("\n")
	f_split = [f.replace(",",".") for f in f_split]
	return(f_split)


def listarTreinamento(file_split):
	lista_treinamento = []
	for row in file[1:len(file)-1]:
		split_list =  [float(r) for r in row.split(";")]
		split_list.pop(3)
		lista_treinamento.append(split_list)
	
	return(lista_treinamento)

def listarSaida(file_split):
	lista_saida = []
	for row in file[1:len(file)-1]:
		split_list =  [float(r) for r in row.split(";")]
		lista_saida.append(split_list[3])
	return(lista_saida)

def sinal(u):
	return 1.0 if u >= 0 else -1.0

def lerArquivo(file_dataset):
	f = open(file_dataset).read()
	file = fatiarArquivo(f)
	return(file)



file = lerArquivo(file_dataset="dataset_treinamento.csv")

conjunto_amostras = listarTreinamento(file)
num_amostra = len(conjunto_amostras[0])
conjunto_saida = listarSaida(file)

print(conjunto_amostras[0])

for amostra in conjunto_amostras:
	amostra.insert(0,-1)
	print(amostra)

peso = [random() for i in range(num_amostra)]
peso.insert(0, -1)


print("\nCarregando %d amostras de dados\nCom %d dados de saída\n" %(len(conjunto_amostras), len(conjunto_saida)))

num_epoca = 0
epoca = 1000
taxa_aprendizado = 0.1

while True:

	erro = False
	
	for i in range(len(conjunto_amostras)):
		
		u = 0
		
		for j in range(num_amostra + 1):
			u += peso[j] * conjunto_amostras[i][j]
			
		y = sinal(u)
		print("Função de ativação", y)
		if y != conjunto_saida[i]:
			erro_aux = conjunto_saida[i] - y

			for j in range(num_amostra + 1):
				peso[j] = peso[j] + taxa_aprendizado * erro_aux * conjunto_amostras[i][j]

			erro = True
	print(num_epoca)
	num_epoca += 1

	if num_epoca > epoca or not erro:
		break

print("\nSaida ", conjunto_saida)