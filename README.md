# Canonic

Uma skill para ajudar agentes de IA a projetar, auditar, depurar e evoluir espaços de trabalho baseados na **Interpretable Context Methodology (ICM)**. A Canonic favorece arquivos legíveis, etapas com contratos claros, entregas verificáveis e revisão humana quando necessária.

## Instalação no Codex

Envie esta mensagem ao Codex no computador em que deseja instalar a skill:

> Use o `$skill-installer` para instalar a skill `skills/canonic` do repositório https://github.com/rickolirocha/Canonic-Skill. Depois, diga como ativá-la.

A instalação exige acesso à internet. A skill fica disponível na próxima interação do Codex. Se já existir uma skill `canonic` no destino, o instalador avisa e não a sobrescreve; peça ao agente para inspecionar a instalação existente antes de substituí-la.

## Como usar

Invoque a skill pelo nome ou descreva uma tarefa sobre ICM. Exemplos:

- `Use $canonic para auditar este workspace ICM e apontar melhorias prioritárias.`
- `Use $canonic para desenhar um fluxo ICM para meu processo de pesquisa.`
- `Use $canonic para investigar por que uma etapa deste pipeline ICM falhou.`

A Canonic não substitui decisões humanas e não transforma a estrutura sugerida por seus modelos em uma exigência universal. Os scripts de auditoria e validação observam convenções específicas; uma verificação bem-sucedida não garante a qualidade dos resultados nem a fidelidade às fontes.

## Outros agentes

A pasta [`skills/canonic`](skills/canonic) contém o `SKILL.md` e todos os arquivos de apoio. Para agentes que suportam esse formato, peça que consultem a documentação de instalação do próprio agente e instalem a **pasta inteira**, incluindo `references`, `templates` e `scripts`. Os procedimentos e a compatibilidade variam por agente. `agents/openai.yaml` é metadado específico do Codex.

## Estrutura

- `skills/canonic/SKILL.md`: instruções e critérios de uso.
- `skills/canonic/references/`: princípios, contratos e orientações de auditoria.
- `skills/canonic/templates/`: modelos para fluxos, planos e relatórios.
- `skills/canonic/scripts/`: utilitários locais em Python.
- `skills/canonic/tests/`: testes e exemplos para o validador.

Os scripts usam Python; consulte suas opções com `--help` quando aplicável. A skill não requer serviços externos para executar seus scripts locais.

## Créditos e licença

A Canonic é uma skill independente baseada em ICM. Não representa Jake Van Clief ou David McDermott, nem afirma ter sua aprovação. Distribuída sob a [licença MIT](LICENSE).
