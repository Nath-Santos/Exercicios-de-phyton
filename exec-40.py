#40) Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário. Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que: 

#- Se quantidade <= 5 o desconto será de 2%
#- Se quantidade > 5 e quantidade <=10 o desconto será de 3%
#- Se quantidade > 10 o desconto será de 5%

def calculo_do_total (nome_produto, quant_produto, preco_produto)
print("Digite o nome do produto:")
nome_produto = input()

print("Digite a quantidade adquirida:")
quant_produto = input()

print("Digite o preço unitário:")
preco_produto = float(input())
