# Scripts

**Scripts → Script window** (Ctrl+Shift+P) abre uma janela com vários scripts em abas, números de linha, realce de
sintaxe e um console. Os scripts são em Python e são salvos no projeto.

| Tecla | Ação |
|---|---|
| Ctrl+J | Executa a linha atual ou a seleção |
| Ctrl+Shift+J | Executa o script inteiro |
| Ctrl+Enter | Avalia e escreve o valor abaixo da linha (`#> valor`) |

O console embaixo executa um comando de cada vez e guarda o histórico. **Restart** limpa o interpretador.

![A janela de scripts]({{AROOT}}assets/manual/script-window.png)

## A API

O espaço de nomes já tem NumPy (`np`), pandas (`pd`), `math` e estas funções:

| Chamada | O que faz |
|---|---|
| `table("nome")` | Uma planilha; `t["col"]` lê uma coluna como array NumPy, `t["col"] = valores` grava uma (a tabela cresce se precisar). |
| `new_table("nome", x=…, y=…)` | Cria uma planilha a partir de colunas (ou de um DataFrame). |
| `matrix("nome")`, `new_matrix("nome", z=…, x=…, y=…)` | Lê ou cria uma matriz; `m.values("sin(x)*cos(y)")` define valores por fórmula. |
| `fit(data, x, y, model, …)` | Ajuste por mínimos quadrados (`model` é um nome pronto como `"gauss"` ou uma fórmula como `"a*exp(-x/t) + c"`); aceita `p0`, `sigma`, `fixed`, `xrange`, `bounds`, `method`, `tol`, `maxfev`, `scale_errors`, `n_curve`, `curve_x`. Devolve `values`, `errors`, `r2`, `report()`… |
| `plot(data, x, y, kind="line", new=False)` | Acrescenta uma curva ao gráfico ativo (ou a um novo). |
| `export("figura.pdf", dpi=300)` | Exporta o gráfico ativo. |
| `note("texto")` | Acrescenta às notas do projeto. |
| `recalculate()` | Refaz as análises que dependem de dados alterados. |
| `tables()`, `matrices()`, `datasets()` | Os nomes no projeto. |

```python
# Ajusta cada espectro de um projeto e reúne os centros dos picos numa tabela
centers, errors = [], []
names = [n for n in tables() if n.startswith("spectrum_")]
for name in names:
    r = fit(name, "x", "y", "gauss")
    k = list(r.names).index("xc")
    centers.append(r.values[k])
    errors.append(r.errors[k])
new_table("centers", sample=names, xc=centers, xc_err=errors)
plot("centers", "sample", "xc", kind="scatter", new=True)
```

## Sem a janela

A mesma API funciona na linha de comando, para lotes e clusters:

```bash
scivelyx script analise.py                                      # dados criados pelo próprio script
scivelyx script analise.py --project projeto.scivelyx.json        # sobre um projeto existente
scivelyx script analise.py --project p.scivelyx.json --save p2.scivelyx.json
```

Os scripts rodam com as suas próprias permissões, como qualquer programa Python; por isso, rode só scripts em que
você confia.
