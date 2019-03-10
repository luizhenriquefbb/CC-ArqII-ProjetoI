
import cv2  # openCV
import argparse
import numpy as np
import timeit

'''
Criando array de imagem em dois fors diferentes
'''

def convertArrayToNumpy(array):
	'''
	Coloca um array em forma de numpy_array pq eh o tipo de objeto que o openCV usa
	'''
	array_numPy=np.zeros((len(array), len(array[0]), 3))

	for row in range(len(array)):
		for colunm in range(len(array[row])):
			array_numPy[row][colunm]=array[row][colunm]

	return array_numPy

def applyToAllPixels(img, action):
	'''
	Aplica uma uma funcao para todos os pixels
	parametros:
		img: array.numpy ou simplesmente um array 3-dimensional que contem os pixels
		action: dicionario que contem duas chaves:
			'fun': nome da funcao a ser aplicada
			'parameters': parametros que a funcao usa alem do R,G,B
			Ex.: Se a funcao a ser passada tiver seus proprios parametros, como 'programar(computador,cafe)',
				os parametros computador e cafe estarao em outro dicionario separado (o dicionario seria o valor da
				chave 'parameters'). A chamada da funcao do exemplo acima ficaria:
					applyToAllPixels(img,{
						'fun' : programar,
						'parameters' : {
							'maquina' : computador,
							'liquido' : cafe
							}
						}
					)
	'''

	height=len(img)
	width=len(img[0])

	fun=action.get('fun')
	parameters=action.get('parameters')

	# construir matriz da nova imagem
	newImage=[]
	for _ in range(height):
		newImage.append( [None] * width )

	# Usar metodo pixel a pixel
	for w in range(width):
		for h in range(height):
			# Verifica se precisa de parametros fora o R,G,B
			if (parameters != None):
				newImage[h][w]=(fun(img[h][w][0], img[h][w][1],
									img[h][w][2],  parameters))
			else:
				newImage[h][w]=(fun(img[h][w][0], img[h][w][1],  img[h][w][2]))

	return convertArrayToNumpy(newImage)

def applyChange(originalImage, color='gray'):
	'''
	Coloca a imagem em modo monocromatico

	Parametros:
		originalImage: ----
		color: string que siginfica a banda escolhida:
			gray: --- (default)
			red: ---
			green:---
			blue: ---
	'''

	imageResult = None

	if (color == 'gray'):
		# media dos  valores de cada pixel
		imageResult = applyToAllPixels(originalImage, {'fun': calculateMeanAndAplly})

	# para cores primarias basta remover os outros valores
	elif (color == 'red'):
		imageResult = applyToAllPixels(originalImage, {'fun': toRed})
	elif (color == 'blue'):
		imageResult = applyToAllPixels(originalImage, {'fun': toBlue})
	elif (color == 'green'):
		imageResult = applyToAllPixels(originalImage, {'fun': toGreen})
	else:
		print("invalid Color")

	return imageResult

def calculateMeanAndAplly(b,g,r):
	'''
	Calcula a media de tres pixels e retorna um pixel com essa media
	'''
	
	average = np.mean([b,g,r])

	return [average,average,average]

def toGreen(b,g,r):
	'''
	converte todo o pixel para a banda verde
	'''
	return [0,g,0]

def toRed (b,g,r):
	'''
	converte todo o pixel para a banda vermelha
	'''
	return [0,0,r]

def toBlue (b,g,r):
	'''
	converte todo o pixel para a banda azul
	'''
	return [b,0,0]





if __name__ == "__main__":
	# construir o parse de argumentos
	ap = argparse.ArgumentParser()

	ap.add_argument("-i", "--image", required=False,
					help="Path to the image to be scanned")

	ap.add_argument("-c", "--scale", required=False,
					help="Color of the scale. Can be 'gray', 'red', 'blue' or 'green'")

	ap.add_argument("-o", "--output", required=True,
					help="Path to the image to be saved")
	
	
	args = vars(ap.parse_args())

	# setar paramentos nao-obrigatorios
	if args["image"] == None:
		args["image"] = "image.jpeg"

	if args["scale"] == None:
		args["scale"] = "gray"


	# ler imagem.
	# A imagem lida eh um array[linha][coluna]
	img = cv2.imread(args["image"])
	
	# aplicar mudancas

	start = timeit.default_timer()

	result = applyChange(img, args["scale"])

	stop = timeit.default_timer()

	print('Execution Time: ', stop - start)  

	# salvar imagem
	cv2.imwrite(args['output'],result)