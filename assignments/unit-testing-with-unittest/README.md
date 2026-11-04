# 📘 Atividade: Unit Testing with unittest

## 🎯 Objetivo

Aprenda a criar e executar testes automatizados com `unittest`, a biblioteca de testes incluída no Python. Você verificará resultados esperados e casos inválidos de uma função sem instalar dependências adicionais.

## 📝 Tarefas

### 🛠️ Executar e ampliar o primeiro teste

#### Descrição
Execute o código inicial e observe como uma classe baseada em `unittest.TestCase` verifica o cálculo de um desconto. Depois, crie um teste para o caso em que nenhum desconto é aplicado.

#### Requisitos
O programa concluído deve:

- Executar com `python starter-code.py`.
- Conter um método de teste que confirme o resultado de `calculate_discount(50, 0)` como `50`.
- Executar todos os testes e indicar que passaram.

### 🛠️ Testar diferentes valores e limites

#### Descrição
Adicione testes para verificar o cálculo com descontos diferentes, incluindo os limites de 0% e 100%.

#### Requisitos
O programa concluído deve:

- Confirmar que um desconto de 100% resulta em `0`.
- Testar pelo menos mais dois valores de preço e porcentagem.
- Usar `subTest` para agrupar casos de teste relacionados e identificar qual combinação falhou.

### 🛠️ Verificar entradas inválidas

#### Descrição
Use `assertRaises` para confirmar que a função rejeita preços negativos e porcentagens de desconto fora do intervalo permitido.

#### Requisitos
O programa concluído deve:

- Confirmar que um preço negativo gera `ValueError`.
- Confirmar que porcentagens menores que 0 ou maiores que 100 geram `ValueError`.
- Executar novamente todos os testes com `python starter-code.py` e confirmar que passam.