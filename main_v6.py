
import cv2  # openCV
import argparse
import numpy as np
import timeit
# from handythread import foreach # Thread
from handythread2 import foreach # Processo
# from handythread3 import foreach # Processo compartilhando memoria

'''
Paralelizando
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

def applyToAllPixels(img, action, threads=4):
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
						'fun' : programar
						}
					)
	'''

	height=len(img)
	width=len(img[0])

	fun=action.get('fun')

	# Usar paralelismo:
	# colocar a matriz em uma lista
	tempArray = np.asarray(img).reshape(height * width , 3)

	# rodar codigo paralelo em x processos
	tempArray2 = foreach(fun, tempArray, threads=threads, return_=True)

	# colocar lista em matriz de volta
	newImage = np.asarray(tempArray2).reshape(height ,  width , 3)

	return convertArrayToNumpy(newImage)

def applyChange(originalImage, color='gray', threads=4):
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
		imageResult = applyToAllPixels(originalImage, {'fun': calculateMeanAndAplly}, threads)

	# para cores primarias basta remover os outros valores
	elif (color == 'red'):
		imageResult = applyToAllPixels(originalImage, {'fun': toRed}, threads)
	elif (color == 'blue'):
		imageResult = applyToAllPixels(originalImage, {'fun': toBlue}, threads)
	elif (color == 'green'):
		imageResult = applyToAllPixels(originalImage, {'fun': toGreen}, threads)
	else:
		print("invalid Color")

	return imageResult

def calculateMeanAndAplly(bgr):
	'''
	Calcula a media de tres pixels e retorna um pixel com essa media
	'''
	average = np.mean(bgr)

	return [average,average,average]

def toGreen(bgr):
	'''
	converte todo o pixel para a banda verde
	'''
	b, g, r = bgr[0], bgr[1], bgr[2]
	return [0,g,0]

def toRed (bgr):
	'''
	converte todo o pixel para a banda vermelha
	'''
	b, g, r = bgr[0], bgr[1], bgr[2]
	return [0,0,r]

def toBlue (bgr):
	'''
	converte todo o pixel para a banda azul
	'''
	b, g, r = bgr[0], bgr[1], bgr[2]
	return [b,0,0]





if __name__ == "__main__":
	# construir o parse de argumentos
	ap = argparse.ArgumentParser()

	ap.add_argument("-i", "--image", required=False,
					help="Path to the image to be scanned")

	ap.add_argument("-c", "--scale", required=False,
					help="Color of the scale. Can be 'gray', 'red', 'blue' or 'green'")
	
	ap.add_argument("-t", "--threads", required=False,
					help="Number of threads to execute")

	ap.add_argument("-o", "--output", required=True,
					help="Path to the image to be saved")
	
	
	args = vars(ap.parse_args())

	# setar paramentos nao-obrigatorios
	if args["image"] == None:
		args["image"] = "image.jpeg"

	if args["scale"] == None:
		args["scale"] = "gray"

	if args["threads"] == None:
		args["threads"] = 4
	else:
		args["threads"] = int(args["threads"])



	# ler imagem.
	# A imagem lida eh um array[linha][coluna]
	img = cv2.imread(args["image"])
	
	# aplicar mudancas

	start = timeit.default_timer()

	result = applyChange(img, args["scale"], args["threads"])

	stop = timeit.default_timer()

	print('Execution Time: ', stop - start)  

	# salvar imagem
	cv2.imwrite(args['output'],result)