# 🇪🇸 Español Interactivo · A1

> Cada aula é uma aplicação web completa — HTML, CSS e JavaScript puro — com um personagem, uma história e uma tarefa final de fala. Abre no projetor da sala e no celular do aluno, sem instalar nada.

---

## 📚 Aulas

| # | Personagem | Origem | Tema | Projeção | Celular |
|---|---|---|---|---|---|
| 08 | Martina García | 🇪🇸 Madrid | Lugares da cidade · transportes · rotina semanal | [abrir](https://juanidives.github.io/espanhol/aulas/aula-08/) | — |
| 09 | Sebastián Mora | 🇨🇴 Medellín | Alimentos e comidas típicas da América Latina | [abrir](https://juanidives.github.io/espanhol/aulas/aula-09/) | [abrir](https://juanidives.github.io/espanhol/aulas/aula-09/mobile.html) |
| 11 | Mateo González | 🇦🇷 Buenos Aires | Horas · esportes · a Copa do Mundo | [abrir](https://juanidives.github.io/espanhol/aulas/aula-11/) | [abrir](https://juanidives.github.io/espanhol/aulas/aula-11/mobile.html) |
| 12 | Valentina Ríos | 🇲🇽 Cidade do México | Gostos e opiniões · *gustar* e semelhantes | [abrir](https://juanidives.github.io/espanhol/aulas/aula-12/) | [abrir](https://juanidives.github.io/espanhol/aulas/aula-12/mobile.html) |
| 13 | Nicolás Quispe | 🇵🇪 Cusco | Possessivos e interrogativos · pronomes complemento | [abrir](https://juanidives.github.io/espanhol/aulas/aula-13/) | [abrir](https://juanidives.github.io/espanhol/aulas/aula-13/mobile.html) |
| 14 | Lucía Paredes | 🇨🇷 San José | Pretérito perfecto simple · pretérito imperfecto | [abrir](https://juanidives.github.io/espanhol/aulas/aula-14/) | [abrir](https://juanidives.github.io/espanhol/aulas/aula-14/mobile.html) |

As aulas 12, 13 e 14 têm ainda uma lacuna de informação em pares — `aluno-a.html` e `aluno-b.html`, um para cada metade da dupla.

---

## 🎭 Os personagens

<table>
  <tr>
    <td align="center"><img src="aulas/aula-08/images/Martina%20en%20la%20carniceria.png" width="150" alt="Martina García"/><br><sub><b>Martina</b> · Madrid</sub></td>
    <td align="center"><img src="aulas/aula-09/images/sebastian-mora.png" width="150" alt="Sebastián Mora"/><br><sub><b>Sebastián</b> · Medellín</sub></td>
    <td align="center"><img src="aulas/aula-11/images/mateo-gonzalez.png" width="150" alt="Mateo González"/><br><sub><b>Mateo</b> · Buenos Aires</sub></td>
  </tr>
  <tr>
    <td align="center"><img src="aulas/aula-12/images/valentina-rios.png" width="150" alt="Valentina Ríos"/><br><sub><b>Valentina</b> · CDMX</sub></td>
    <td align="center"><img src="aulas/aula-13/images/nicolas-quispe.png" width="150" alt="Nicolás Quispe"/><br><sub><b>Nicolás</b> · Cusco</sub></td>
    <td align="center"><img src="aulas/aula-14/images/lucia-retrato.png" width="150" alt="Lucía Paredes"/><br><sub><b>Lucía</b> · San José</sub></td>
  </tr>
</table>

Cada aula gira em torno de um personagem, com alternância de gênero entre aulas consecutivas e sotaque coerente com a origem — personagem argentino traz `vos` nas tabelas de conjugação, personagem peruana traz o vocabulário andino. As histórias se cruzam: o caderno que Nicolás guardava em Cusco é o que Lucía procura na aula seguinte.

---

## 🗂️ Estrutura

```
espanhol/
└── aulas/
    └── aula-NN/
        ├── index.html      # projeção em sala — 100vw/100vh, fontes grandes
        ├── mobile.html     # celular do aluno — scroll vertical, swipe
        ├── aluno-a.html    # lacuna de informação em pares
        ├── aluno-b.html
        ├── images/
        └── audio/
```

Cada aula é autocontida: um `.html` é a apresentação inteira e continua funcionando offline depois de carregada.

---

## 🚀 Como usar

**Na sala** — abra o link de projeção no navegador, tela cheia. Navegação por `→` / `←` ou pelos botões.

**No celular do aluno** — o link *mobile* é pensado para toque e scroll vertical; funciona em qualquer aparelho, sem app.

**Localmente**

```bash
git clone https://github.com/juanidives/espanhol
cd espanhol/aulas/aula-14
# abrir index.html no navegador — sem servidor, sem build
```

---

## 🛠️ Stack

```
HTML5 · CSS3 · JavaScript (vanilla) · GitHub Pages
```

Zero dependências, zero build step. A escolha é deliberada: qualquer professor consegue abrir o arquivo, entender e adaptar; a aula carrega rápido no 4G da sala e sobrevive a uma internet que cai no meio da explicação.

Layout pensado para o contexto real: fontes grandes e alto contraste para alunos com dificuldade visual, imagens em `object-fit: contain` para nunca cortar, e cada slide com a própria classe de layout.

---

## 🎯 A metodologia

Framework **Awareness → Appropriation → Autonomy**, com planejamento retroativo: define-se primeiro a tarefa final de produção oral e derivam-se os apoios a partir dela.

O teste que toda atividade oral precisa passar: *o aluno cumpre a tarefa só repetindo o modelo, ou precisa escolher e responder ao que o outro diz?* Se basta repetir, ainda é apoio — e o apoio existe para tornar o sucesso possível, mas precisa ser retirável.

A prioridade declarada pelos próprios alunos no fim do primeiro semestre: **falar**. É o critério que decide o desenho de cada aula.

---

## 👤 Sobre

Projeto voluntário de **Juan Antonio Morales** — profissional de dados, educador voluntário e entusiasta de tecnologia aplicada ao ensino. O objetivo de longo prazo é um livro didático A1 completo, aula por aula.

<p align="center">
  <sub>Español · Argentina e Brasil sempre no coração</sub>
</p>
