# demo-equidade-biometria

Demonstração didática de como medir **equidade demográfica** em verificação facial.

> Todos os dados são **sintéticos**, gerados por simulação. Este repositório não contém imagens, modelos nem código de nenhum projeto de terceiros.

## O que faz

O script `fairness_metrics.py`:

1. simula scores de similaridade para pares genuínos e impostores em três grupos (A, B, C), com o grupo C tendo scores genuínos sistematicamente piores;
2. escolhe **um único limiar global** que fixa a taxa de falsa aceitação (FMR) em 1%;
3. calcula FMR e FNMR (falsa rejeição) por grupo e as diferenças entre eles.

## Como executar

```bash
pip install numpy
python fairness_metrics.py
```

## Exemplo de saída

```text
grupo   FMR     FNMR
A      1.093%  5.121%
B      0.943%  9.922%
C      0.965% 18.911%

Razão FNMR max/min: 3.69
```

Com o mesmo limiar, o FMR fica estável entre os grupos, mas o FNMR do grupo C é cerca de 3,7 vezes o do grupo A. Um sistema que olha só a média global esconde essa disparidade.

## Limitações

- Os scores são gaussianos e o viés é injetado por construção; dados reais têm distribuições mais complexas.
- Não implementa mitigação (por exemplo, treinamento adversarial ou limiares por grupo). É só a etapa de medição.

## Autora

Fernanda Neiva Mesquita. [Lattes](https://lattes.cnpq.br/3639678638834402)
# demo-equidade-biometria
Demo: métricas de equidade demográfica (FMR/FNMR por grupo) em verificação facial, com dados sintéticos
