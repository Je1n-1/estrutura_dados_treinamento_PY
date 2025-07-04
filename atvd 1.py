
print("*'*" * 20)  #Linha decorativa 1
print('Boas Vindas a minha loja de vendas, by Jean RIcardo Land Miranda') #apresentação
print("*'*" * 20) #Linha decorativa 2
valor_pedido = float(input('DIgite o valor do pedido: '))
quantidade_parcelas = int(input('Digite a quantidade de parcelas: ')) 

if quantidade_parcelas < 4: # menos de 4 parcelas recebe 0% de juros
    juros = 0
elif 4 <= quantidade_parcelas < 6: # de 4 a 5,99... parcelas recebe 4% de juros
    juros = 4 / 100
elif 6 <= quantidade_parcelas < 9: # de 6 a 8,99... parcelas recebe 8% de juros
    juros = 8 / 100
elif 9 <= quantidade_parcelas < 13: # de 9 a 12,99... parcelas recebe 16% de juros
    juros = 16 / 100
else:
    juros = 32 / 100  #se maior que 13 parcelas o juros será 32%

# Cálculo do valor da parcela e do total
valor_parcela = (valor_pedido * (1 + juros)) / quantidade_parcelas
# Cálculo do valor total do pedido
valor_total = valor_parcela * quantidade_parcelas

# Exibição dos resultados
print(f'O valor do pedido total parcelado é: {valor_total:.2f}')
print(f'O valor da parcela é: {valor_parcela:.2f}')