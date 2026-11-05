# canonic

**Sua IA trabalha melhor quando sabe onde está, o que importa e qual é o próximo passo.**

A **canonic** ajuda você a criar um **workspace canônico**: um espaço onde o contexto, as etapas e as decisões ficam claros para você e para sua IA.

Na prática, você entende o fluxo, encontra falhas e continua o trabalho sem depender de uma estrutura complexa.

- Encontre informações perdidas e instruções duplicadas.
- Organize etapas, entregas e pontos de revisão.
- Investigue onde um fluxo parou e o que precisa mudar.

Um workspace canônico começa pelo que já funciona e reúne apenas a estrutura necessária para o trabalho.

## 5 mitos sobre otimizar o uso de IA

**“Preciso do modelo mais novo para ter bons resultados.”** O modelo importa. Mas, sem seu objetivo, suas informações e critérios, ele precisa adivinhar. Dê a ele o contexto do trabalho. [OpenAI](https://developers.openai.com/api/docs/guides/model-optimization)

**“Quanto mais contexto, melhor.”** Informação relevante ajuda; excesso e conteúdo repetido podem atrapalhar. Entregue o que a tarefa precisa, na hora certa. [Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

**“O segredo é um prompt gigante.”** Comece com objetivo, contexto e resultado esperado. Acrescente instruções e exemplos quando resolverem um problema observado. [OpenAI](https://developers.openai.com/api/docs/guides/optimizing-llm-accuracy)

**“Mais agentes sempre produzem resultados melhores.”** Eles podem ajudar em tarefas paralelas. Em tarefas sequenciais, a coordenação também pode piorar o resultado. [Google Research](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/)

**“Se parece certo, está pronto.”** Respostas convincentes ainda precisam de verificação. Defina critérios, teste com exemplos reais e revise o que importa. [OpenAI](https://developers.openai.com/cookbook/examples/agent_optimization/optimizing_agents_for_cost_and_quality)

## Instale no Codex

Copie e envie ao Codex:

> Instale esta skill do repositório: https://github.com/rickolirocha/canonic-skill

A skill fica disponível na próxima interação. O Codex pode selecioná-la automaticamente ao organizar contexto e roteamento de um workspace de IA; a seleção depende da interpretação do pedido e não é garantida em toda conversa. Para chamá-la diretamente, use `$canonic`.

Se já estiver instalada, o instalador não sobrescreve nem atualiza a cópia existente. Para obter uma nova versão, peça ao Codex para conferir a instalação e orientar a atualização.

## Use

```text
Use $canonic para analisar meu projeto e propor um workspace canônico simples.
```

Você também pode pedir à canonic para auditar um workspace canônico ou investigar uma etapa que falhou.

Para outros agentes compatíveis, instale a pasta inteira [`skills/canonic`](skills/canonic) conforme a documentação do agente. A compatibilidade varia.

## De onde vêm as ideias

Contexto claro e processos legíveis ajudam a IA a trabalhar com o que importa. Mais agentes podem ajudar em tarefas paralelas; em fluxos sequenciais, mais coordenação também pode atrapalhar.

- [OpenAI — Harness engineering](https://openai.com/index/harness-engineering/)
- [Anthropic — Engenharia de contexto](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Google Cloud — Open Knowledge Format (OKF)](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
- [Google Research — Escala de sistemas de agentes](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/)
- [Jake Van Clief e David McDermott — ICM](https://arxiv.org/html/2603.16021v2)

A canonic é independente. O ICM é uma referência e seus modelos são opcionais; a referência ao OKF não implica conformidade com o formato.

[Licença MIT](LICENSE).
