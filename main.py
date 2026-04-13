import random
carateres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
senha = ''
tamanho_senha = int(input("tamanho da senha"))
for i in range(tamanho_senha):
    senha = senha + random.choice(carateres)

print(senha)