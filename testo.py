print('diga valor de a')
valor_a = input()
print('diga valor de b')
valor_b = input()

try:
    a = float(valor_a)
    b = float(valor_b)
    resultado = a + b
    print( 'soma reulta em: {resultado}')
except ValueError:
    print('Erro: por favor, insira números válidos.')