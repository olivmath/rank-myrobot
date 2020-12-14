class ErroGrazy(Exception):
	pass
	# def __init__(self, mesagem, linha):
	# 	self.mesagem = mesagem
	# 	self.linha = linha
	
	# def __str__(self):
	# 	return f"Erro: {self.mesagem} na linha: {self.linha}"



try:
    prin("Grazy passou!")

except ErroGrazy as err:
	print(err)
finally:
    print("final do ano")
