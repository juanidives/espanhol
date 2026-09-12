# espanhol

Aulas de espanhol A1 interativas em HTML, CSS e JavaScript puro. Cada aula é uma aplicação web completa hospedada no GitHub Pages.

Projeto voluntário do Juani. Objetivo de longo prazo: montar um livro didático completo para os alunos.

## Contexto de sala — restringe todo o desenho

- **40 minutos por aula.** É pouco. Todo plano precisa somar 40 de verdade.
- **10 a 15 alunos**, trabalho em pares (turma ímpar → uma trinca; toda atividade precisa da variante).
- **Todos os alunos têm celular com internet na sala.** É isso que viabiliza vários HTMLs por aula.
- **Alunos com dificuldade visual.** Fontes grandes e alto contraste não são preferência estética, são requisito. Atividade cuja informação chegue só por imagem detalhada não funciona — a alternativa é texto grande ou áudio.
- **Prioridade número 1: fazer o aluno falar.** Feedback de fim de curso dos alunos. Aula bonita sem produção oral é aula que falhou.

## Estrutura

```
espanhol/
├── aulas/
│   └── aula-AAAA-MM-DD/
│       ├── index.html    ← projeção em sala (fontes grandes, 100vw/100vh)
│       ├── mobile.html   ← scroll vertical, touch, swipe
│       ├── aluno-a.html  ← lacuna de informação em pares (quando houver)
│       ├── aluno-b.html
│       ├── aula-AAAA-MM-DD.md  ← base de conhecimento (Obsidian)
│       ├── images/
│       └── audio/        ← gerado no ElevenLabs, voz compatível com o sotaque
├── tarefas/              ← tarefas de casa centralizadas, fora das pastas de aula
├── CLAUDE.md
└── README.md
```

Deploy: `https://juanidives.github.io/espanhol/aulas/aula-AAAA-MM-DD/`

**A pasta é a data em que a aula foi dada — não existe número de aula no caminho.** A numeração corrida antiga (`a1-aula08`…`a1-aula13`) foi abandonada em setembro/2026 porque competia com duas outras contagens que continuam em uso: as tarefas do 1º semestre (`tarefas/9.1`) e os PPTs do 2º (`ppt-aula2.2.pptx`). As aulas são identificadas por **data + personagem**. Os links antigos não foram preservados.

**Nomes de arquivo:** minúsculo, sem espaço, sem acento (`panaderia.png`, não `Panadería.png`). As aulas antigas violam isso em alguns arquivos — não renomear retroativamente, só seguir a convenção daqui para frente.

## Stack

HTML5 · CSS3 · JavaScript vanilla. Sem framework, sem build step, zero dependências. Um `.html` é a apresentação inteira e funciona offline depois de carregado.

## Regras de HTML que não podem ser quebradas

**A regra do `display`.** Nunca usar `.slide.active { display: grid !important; }` nem qualquer `display` global nos slides. Isso quebra todo slide que precisa de flex e o bug é difícil de rastrear depois. O padrão correto:

```css
.slide { display: none; }
.slide.active.layout-center    { display: flex; }
.slide.active.layout-two-col   { display: grid; }
.slide.active.layout-flex-col  { display: flex; }
```

Cada slide recebe a própria classe de layout e o `display` vem dela, nunca de uma regra global. **Isso precisa estar certo já no primeiro rascunho** — corrigir depois custa uma reescrita inteira.

**Imagens:** `object-fit: contain`, nunca `cover` — `cover` corta a imagem. No mobile, imagem em `65dvh` para caber inteira sem corte.

**QR codes.** Os QRs são PNG em base64 embutidos no `index.html` e codificam a **URL absoluta** do GitHub Pages (`https://juanidives.github.io/espanhol/aulas/aula-AAAA-MM-DD/mobile.html`). Não há como um `grep` encontrá-los: renomear a pasta quebra o QR silenciosamente e só se descobre na sala, com o aluno apontando o celular. Ao mover ou renomear qualquer aula, **regerar todos os QRs** e conferir decodificando a imagem gerada.

**Sem esfumados.** Nada de gradiente sobreposto em slide, salvo pedido explícito do Juani.

**Validação antes de entregar:** rodar o script estrutural em Python que confere que todo slide tem classe de layout e que nenhum `display` global escapou. Nenhum HTML é entregue sem passar.

## Cores — perguntar, nunca assumir

**A paleta muda a cada aula e é decisão do Juani.** Não existe paleta padrão do projeto. A associação histórica (personagem masculino → cores vibrantes, feminino → tons pastel) é ponto de partida descartável, e ele descarta com frequência.

No brainstorming, propor 2 ou 3 paletas ligadas ao tema e esperar a escolha. Só fixar no código depois de confirmada.

## Metodologia

Framework **Awareness → Appropriation → Autonomy**, com **planejamento retroativo**: define-se primeiro a tarefa final de produção oral e derivam-se os apoios a partir dela. Planejar na ordem direta (vocabulário → gramática → "e no fim uma atividade oral") produz sempre uma atividade oral decorativa que não acontece.

Teste aplicado a toda atividade oral: *o aluno cumpre a tarefa só repetindo o modelo, ou precisa escolher e responder ao que o outro diz?* Se basta repetir, ainda é Appropriation.

Na Appropriation o erro **não** é minimizado pelo controle — isso seria drilling. O apoio existe para tornar o sucesso possível, mas precisa ser retirável.

Cada aula gira em torno de um personagem fictício, com **alternância de gênero** entre aulas consecutivas e sotaque coerente com a origem. Precisão regional importa: personagem argentino exige `vos` nas tabelas de conjugação (7 pronomes, não 5).

O plano pedagógico não se inventa aqui — vem pronto da etapa de desenho (skill `aula-espanhol-desenho`). Este repositório é a etapa de produção.

## Pipeline por aula

0. Brainstorming e ficha de aula → aprovação do Juani
1. `index.html` (projeção)
2. Aprovação
3. `.pptx` → PDF (texto em tamanho normal, para distribuir aos alunos)
4. `mobile.html`
5. `.md` do Obsidian (base de conhecimento), nomeado `aula-AAAA-MM-DD.md` dentro da própria pasta da aula

Arquivos `aluno-a.html` / `aluno-b.html` entram no passo 1, junto com o `index.html`, quando a aula tiver lacuna de informação.

**PPTX:** gerado com pptxgenjs. As imagens do GitHub Pages não são acessíveis durante a geração — usar placeholders rotulados com o nome exato do arquivo para o Juani inserir manualmente no PowerPoint.

**Antes de gerar qualquer derivado** (PPTX, mobile, `.md`), ler o HTML final inteiro. Ele é a fonte da verdade — tabelas de conjugação e conteúdo precisam bater exatamente.

## Aulas

Aulas aos sábados.

| Data | Personagem | Tema | Duração |
|---|---|---|---|
| 2026-05-16 | Martina García (Madrid) | Lugares · transportes · rotina semanal | 40 min |
| 2026-05-23 | Sebastián Mora (Medellín) | Alimentos e comidas típicas | 40 min |
| 2026-06-13 | Mateo González (Buenos Aires) | Horas e esportes | 40 min |
| 2026-08-15 | Valentina Ríos (Cidade do México) | Gustar e semelhantes · gostos e opiniões | 40 min |
| 2026-08-22 | Nicolás Quispe (Cusco) | Possessivos e interrogativos · repasso dos pronomes | 60 min |
| 2026-09-12 | Lucía Paredes (San José) | Pretérito perfecto simple · pretérito imperfecto | 90 min |

Uma aula sobre família e gerúndio foi desenhada mas nunca ministrada — não tem pasta.

## Conteúdo já ensinado (1º semestre)

Consultar antes de propor qualquer coisa, para não reintroduzir o que já foi dado nem exigir o que ainda não foi.

**Gramática:** pronomes e formas de tratamento · ser e estar · querer · voseo · presente do indicativo regular e irregular · pronomes complemento (átonos e tônicos, OD e OI) · pronomes reflexivos · gustar e semelhantes (encantar, interesar, fascinar, molestar, importar, parecer, preocupar) · gerúndio

**Vocabulário:** saudações e apresentações · descrever-se · rotina · dias, meses e estações · expressões de frequência · lugares e transportes · números cardinais e ordinais · comidas e alimentos · família · horas · esportes

**Ainda não visto:** futuro e `ir a + infinitivo` · comparativos · imperativo. O passado entrou em 12/09/2026 (pretérito perfecto simple e pretérito imperfecto); até ali o curso inteiro vivia no presente.

## Git

`git pull origin main` antes de qualquer push quando houver conflito no remoto.
