
# 📘 Exercícios Integrados de Matemática e Python

## 1 – Operações Básicas e Variáveis

**Exemplos:**
```python
a = 5; b = 3; print(a + b)
x = 7; y = 2; print(x - y)
m = 4; n = 2; print(m * n)
dividendo = 10; divisor = 2; print(dividendo / divisor)
```

**Atividade:**  
Crie um programa em Python que recebe dois números inteiros e exibe:  
- a soma  
- a subtração  
- a multiplicação  
- a divisão entre eles

---

## 2 – Expressões Matemáticas e Precedência

**Exemplos:**
```python
resultado = 2 + 3 * 4
resultado = (2 + 3) * 4
resposta = 10 / 2 + 5
resposta = 10 / (2 + 5)
```

**Atividade:**  
Escreva um programa que peça três números ao usuário e calcule:  

$$
(a + b) \times c - a^2
$$

Mostre o resultado.

---

## 3 – Laços de Repetição e Tabuada

**Exemplos:**
```python
for i in range(1, 6): print(i)
for i in range(1, 11): print(f"2 x {i} = {2*i}")
n = 3
for i in range(1, 11): print(n * i)
for i in range(1, 6): print(f"Quadrado de {i} é {i**2}")
```

**Atividade:**  
Faça um programa que leia um número inteiro e exiba a **tabuada** dele do 1 ao 10.

---

## 4 – Condições e Cálculos

**Exemplos:**
```python
if x % 2 == 0: print("Par") else: print("Ímpar")
if nota >= 7: print("Aprovado") else: print("Reprovado")
if a > b: print(a) else: print(b)
if x < 0: print("Negativo") else: print("Positivo")
```

**Atividade:**  
Crie um programa que receba três números reais e informe:  
- o maior  
- o menor  
- a média aritmética

---

## 5 – Funções, Listas e Estatística

**Exemplos:**
```python
def soma(lista): return sum(lista)
numeros = [3, 5, 7]; media = sum(numeros)/len(numeros)
valores = [4, 2, 9]; print(min(valores), max(valores))
```

**Atividade:**  
Leia uma lista de números digitados pelo usuário e:  
- calcule a média  
- encontre o maior e o menor valor  
- conte quantos números são maiores que a média

---

# 📘 Exercícios de Funções Matemáticas e Python

## 1 – Funções Simples

**Exemplos:**
- $$f(x) = x + 2$$
- $$f(x) = 3x$$
- $$f(x) = x - 5$$
- $$f(x) = 2x + 1$$

**Atividade:**  
Crie um programa que calcule:

$$
f(x) = 3x + 2
$$

com entrada do usuário para a variável x.

---

## 2 – Funções Lineares em Python

**Exemplos:**
```python
def f(x): return 2*x + 3
def g(x): return -x + 5
def h(x): return 4*x - 7
print(f(2))  # saída: 7
```

**Atividade:**  
Implemente a função salário baseada em:

$$
S(h) = 20h + 200
$$

onde \( h \) é o número de horas trabalhadas. 

---

## 3 – Funções Quadráticas

**Exemplos:**
- $$f(x) = x^2$$  
- $$f(x) = x^2 - 4$$  
- $$f(x) = 2x^2 + 3x + 1$$
```python
def f(x): return x**2 - 2*x + 1
```

**Atividade:**  
Crie um programa que calcule:

$$
f(x) = x^2 - 3x + 2
$$

para valores de \( x \) de -5 a 5.

---

## 4 – Composição de Funções

**Exemplos:**
- $$f(x) = 2x + 1$$  
- $$g(x) = x - 3$$  
- $$f(g(x)) = 2(x - 3) + 1$$

```python
def f(x): return 2*x + 1
def g(x): return x - 3
print(f(g(5)))
```

**Atividade:**  
Implemente:

- $$f(x) = x^2 + 2$$  
- $$g(x) = x - 4$$  

e calcule:

$$
f(g(6))
$$

---

## 5 – Função de Lucro

**Exemplos:**
- $$C(t) = 5t + 100$$  
- $$V(t) = 10t$$  
- $$L(t) = V(t) - C(t) = 10t - (5t + 100)$$

```python
def lucro(t): return 10*t - (5*t + 100)
```

**Atividade:**  
Implemente a função:

$$
L(t) = 12t - (6t + 150)
$$

e mostre os resultados para \( t = 0 \) até \( 20 \).

---
