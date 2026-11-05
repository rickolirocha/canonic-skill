# canonic

**Sua IA trabalha melhor quando sabe onde está, o que importa e qual é o próximo passo.**

A canonic organiza o contexto e as etapas do seu projeto em arquivos claros. Você consegue entender o fluxo, encontrar falhas e continuar o trabalho sem depender de uma estrutura complexa.

- Encontre informações perdidas e instruções duplicadas.
- Organize etapas, entregas e pontos de revisão.
- Investigue onde um fluxo parou e o que precisa mudar.

A skill atua em projetos baseados em ICM. Começa pelo que já funciona e ajuda a escolher a estrutura necessária para o trabalho.

## 5 mitos sobre otimizar o uso de IA

**“Preciso do modelo mais novo para ter bons resultados.”** O modelo importa. Mas, sem seu objetivo, suas informações e critérios, ele precisa adivinhar. Dê a ele o contexto do trabalho. [OpenAI](https://developers.openai.com/api/docs/guides/model-optimization)

**“Quanto mais contexto, melhor.”** Informação relevante ajuda; excesso e conteúdo repetido podem atrapalhar. Entregue o que a tarefa precisa, na hora certa. [Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

**“O segredo é um prompt gigante.”** Comece com objetivo, contexto e resultado esperado. Acrescente instruções e exemplos quando resolverem um problema observado. [OpenAI](https://developers.openai.com/api/docs/guides/optimizing-llm-accuracy)

**“Mais agentes sempre produzem resultados melhores.”** Eles podem ajudar em tarefas paralelas. Em tarefas sequenciais, a coordenação também pode piorar o resultado. [Google Research](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/)

**“Se parece certo, está pronto.”** Respostas convincentes ainda precisam de verificação. Defina critérios, teste com exemplos reais e revise o que importa. [OpenAI](https://developers.openai.com/cookbook/examples/agent_optimization/optimizing_agents_for_cost_and_quality)

## Instale no Codex

Copie e envie ao Codex:

> Use o `$skill-installer` para instalar a skill `skills/canonic` do repositório https://github.com/rickolirocha/canonic-skill.

A skill fica disponível na próxima interação. Se já estiver instalada, o instalador não sobrescreve a versão existente.

## Use

```text
Use $canonic para analisar meu workspace ICM e mostrar o que precisa melhorar.
```

Também funciona como ponto de partida para criar um fluxo ICM ou investigar uma etapa que falhou.

Para outros agentes compatíveis, instale a pasta inteira [`skills/canonic`](skills/canonic) conforme a documentação do agente. A compatibilidade varia.

## De onde vêm as ideias

Contexto claro e processos legíveis ajudam a IA a trabalhar com o que importa. Mais agentes podem ajudar em tarefas paralelas; em fluxos sequenciais, mais coordenação também pode atrapalhar.

- [OpenAI — Harness engineering](https://openai.com/index/harness-engineering/)
- [Anthropic — Engenharia de contexto](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Google Cloud — Open Knowledge Format (OKF)](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
- [Google Research — Escala de sistemas de agentes](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/)
- [Jake Van Clief e David McDermott — ICM](https://arxiv.org/html/2603.16021v2)

A canonic é independente. Suas ferramentas são centradas em ICM; a referência ao OKF não implica conformidade com o formato.

[Licença MIT](LICENSE).
