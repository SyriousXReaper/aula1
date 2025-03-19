
"""
EXERCICIO 1
numero1 = int(input("Digite o primeiro numero: "));

numero2 = int(input("Digite o segundo numero: "));

soma = numero1 + numero2;
print(f"A soma dos dois numeros e: {soma}");

"""
"""
EXERCICIO 2
entrada = input("Digite algo para ver o seu tipo: ");

print(type(entrada));

"""
"""
EXERCICO 3
numero = int(input("Digite um numero para ver seu antecessor e sucessor: "));

antecessor = numero - 1;
sucessor = numero + 1;

print(f"Sucessor:{sucessor}\nAntecessor:{antecessor}");

"""
"""
EXERCICIO 5
contador = 0;
notas = [];
while contador < 2:
    nota = input("Digite as notas do aluno: ");
    notas.append(float(nota));
    contador += 1;

media = (sum(notas)) / len(notas);
    

print(f"A media e: {media}");

"""

"""
EXERCICIO 6
multiplicador = 0;
def ImprimirTabuada(numero, multiplicador):
    if (multiplicador > 10):
        return
    print(f"{numero} X {multiplicador} = {numero * multiplicador}");
    ImprimirTabuada(numero, multiplicador + 1);

numero = int(input("Digite um numero para ver sua tabuada: "));
ImprimirTabuada(numero, 0);

"""
"""
EXERCICIO 7
produto = float(input("Digite o valor do produto: "))

desconto = float(produto * (5 / 100))
produto -= desconto

print(f"Produto com 5% de desconto: {produto}")

"""

    