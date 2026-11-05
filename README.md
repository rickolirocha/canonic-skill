# canonic

**Contexto. Processo. Inteligência.**

O que torna uma IA útil não começa apenas no modelo. Começa no que ela sabe sobre o trabalho, na clareza do caminho e na forma como cada decisão chega à próxima etapa.

A **canonic** é uma skill para projetar, auditar e evoluir espaços de trabalho baseados em ICM (*Interpretable Context Methodology*). Ela ajuda a transformar informações dispersas em contexto legível, etapas claras e entregas que pessoas e agentes conseguem acompanhar.

## Primeiro, a base

Agentes, ferramentas, prompts e modelos se multiplicam. Mas adicionar mais peças nem sempre resolve o que está desorganizado.

A canonic começa pelo que você já tem: o objetivo, os arquivos, o processo e as decisões que precisam continuar nas mãos de pessoas. A partir daí, ajuda a identificar o que falta, o que está duplicado e qual é a estrutura mais simples capaz de sustentar o trabalho.

- **Contexto:** informações, referências e decisões disponíveis no momento certo.
- **Processo:** etapas com entradas, saídas, critérios e pontos de revisão claros.
- **Inteligência:** o agente e as ferramentas adequados ao problema, com scripts para tarefas mecânicas quando fizer sentido.

Mais agentes podem ajudar em tarefas paralelas. Em fluxos sequenciais, a coordenação também pode acrescentar custo e perda de contexto. A escolha depende do trabalho — e deve ser verificada na prática.

## O que a canonic faz

- **Descobre e desenha:** mapeia objetivos, entradas, etapas, entregas e decisões humanas antes de propor uma estrutura ICM.
- **Audita:** encontra lacunas, duplicações, responsabilidades confusas e riscos em um workspace ICM existente.
- **Investiga:** ajuda a identificar falhas em etapas, contratos, contexto e passagens entre arquivos.
- **Evolui:** orienta mudanças estruturais preservando as fontes e usando validações adequadas.

A skill inclui referências, modelos e scripts locais. Seus validadores seguem algumas convenções de estrutura: passar em uma verificação não garante, por si só, a qualidade da entrega ou a fidelidade às fontes.

## Instalação no Codex

Envie esta mensagem ao Codex no computador onde deseja instalar:

> Use o `$skill-installer` para instalar a skill `skills/canonic` do repositório https://github.com/rickolirocha/canonic-skill. Depois, diga como ativá-la.

É necessário acesso à internet. A skill fica disponível na próxima interação. Se `canonic` já estiver instalada, o instalador avisa e não sobrescreve a cópia existente; peça ao agente para examiná-la antes de substituí-la.

## Como usar

Chame a skill pelo nome e apresente o problema que deseja resolver:

```text
Use $canonic para auditar este workspace ICM e apontar as melhorias prioritárias.
```

```text
Use $canonic para desenhar um fluxo ICM para meu processo de pesquisa.
```

```text
Use $canonic para investigar por que esta etapa do meu fluxo ICM falhou.
```

## Outros agentes

A pasta [`skills/canonic`](skills/canonic) contém as instruções e os arquivos de apoio. Em agentes que aceitam esse formato, consulte a documentação do próprio agente e instale a **pasta inteira**, incluindo `references`, `templates` e `scripts`. Os procedimentos e a compatibilidade variam. O arquivo `agents/openai.yaml` contém metadados específicos do Codex.

## Ideias que informam a canonic

Pesquisadores, equipes e métodos diferentes apontam para uma preocupação em comum: dar aos sistemas de IA o contexto e a estrutura necessários para trabalhar melhor. Estas referências ajudam a fundamentar a direção da canonic; não representam certificação, parceria ou promessa de resultado.

- **OpenAI — [Harness engineering](https://openai.com/index/harness-engineering/):** como ambiente, conhecimento do repositório e ciclos de feedback ajudam agentes a executar trabalho de engenharia.
- **Anthropic — [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents):** como selecionar e manter o contexto relevante para um agente.
- **Google Cloud — [Open Knowledge Format (OKF)](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing):** uma especificação aberta para organizar e compartilhar conhecimento em arquivos legíveis. A canonic se inspira nessa direção; não declara conformidade com o formato OKF.
- **Google Research — [Towards a science of scaling agent systems](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/):** por que a arquitetura e o tipo de tarefa importam ao decidir entre um agente e múltiplos agentes.
- **Jake Van Clief e David McDermott — [Interpretable Context Methodology](https://arxiv.org/html/2603.16021v2):** organização de fluxos sequenciais por arquivos, contratos de etapa e revisão humana.

A canonic é independente e não representa ou reivindica aprovação dos autores ou organizações citados. Suas instruções e ferramentas atuais são centradas em ICM; as demais referências ampliam os princípios que orientam sua apresentação.

## Estrutura

- `skills/canonic/SKILL.md`: instruções e critérios de uso.
- `skills/canonic/references/`: princípios, contratos e orientações de auditoria.
- `skills/canonic/templates/`: modelos para fluxos, planos e relatórios.
- `skills/canonic/scripts/`: utilitários locais em Python.
- `skills/canonic/tests/`: testes e exemplos para o validador.

Os scripts usam Python; consulte suas opções com `--help` quando aplicável.

## Licença

[MIT](LICENSE).
