# Configuração

As opções são SERVER do NeoForge, autoritativas e sincronizadas ao entrar. Edite
o arquivo do mundo <mundo>/serverconfig/slimeevolution-server.toml com o servidor
desligado; use defaultconfigs/ para padrões de mundos novos. Faça backup antes de
mudar versões. O botão Configuração no menu de mods usa a tela do NeoForge;
valores do servidor remoto são apenas leitura para o cliente.

20 ticks equivalem a um segundo carregado. Chunks descarregados não avançam
crescimento/recargas. Valores fora dos limites são corrigidos pelo NeoForge.
Na tabela, números aparecem como padrão, mínimo e máximo. O arquivo gerado
contém comentários e limites; não copie valores de outra versão
sem revisão. Alterações de geração só afetam terreno novo.

| Chave TOML | Padrão e limites | Efeito |
|---|---|---|
| `naturalSpawning` | `true` | Ativa a geração natural. Comandos e ovos continuam funcionando. |
| `localPopulationLimit` | `8, 1, 64` | Máximo de indivíduos em 32 blocos para aceitar geração natural; não remove os existentes. |
| `spawnChance` | `0.25, 0.0, 1.0` | Probabilidade adicional após as verificações normais de geração. |
| `damageMultiplier` | `1.0, 0.0, 4.0` | Afeta contato e projéteis de Cristal. Zero desativa esse dano; não controla chefes. |
| `abilityParticles` | `true` | Ativa partículas de habilidades no servidor. Avisos de chão dos chefes continuam disponíveis. |
| `combat.activeAbilities` | `true` | Ativa habilidades de contato e regeneração ambiental. Atributos e defesas passivas permanecem. |
| `combat.abilitySounds` | `true` | Som de ativação das habilidades; não controla os sons comuns das criaturas. |
| `combat.thermalReactions` | `true` | Fogo remove o frio do mod; contato gelado apaga um alvo em chamas em vez de resfriá-lo. |
| `combat.effectDurationMultiplier` | `1.0, 0.0, 4.0` | Afeta ignição, lama e frio. Zero desativa esses efeitos; limite de 200 ticks por aplicação. |
| `combat.healingMultiplier` | `1.0, 0.0, 4.0` | Cura combinada com o gene de regeneração; máximo de seis pontos por ativação. |
| `combat.mineralImpactReduction` | `0.25, 0.0, 0.5` | Proteção contra projéteis e explosões antes da armadura, ajustada pelo gene; máximo de 75%. |
| `combat.metalMeleeReduction` | `0.2, 0.0, 0.5` | Proteção do Ferro antes do ajuste genético; não afeta projéteis, explosões ou dano que ignora defesa. |
| `combat.obsidianBlastReduction` | `0.5, 0.0, 0.5` | Proteção contra explosões ajustada pelo gene; máximo de 75%. |
| `combat.iceFireMultiplier` | `1.5, 1.0, 4.0` | Multiplicador do dano de fogo recebido por slimes de Gelo. |
| `combat.wetFireDamage` | `1.0, 0.0, 4.0` | Dano por segundo carregado em água, chuva ou bolhas; zero desativa essa vulnerabilidade. |
| `combat.dischargeDamage` | `2.0, 0.0, 4.0` | Dano elétrico antes do ajuste genético. Alvos molhados recebem o dobro; máximo de seis pontos. |
| `combat.waterConduction` | `true` | Descargas em alvos molhados podem atingir até dois alvos molhados próximos com visão livre. |
| `breeding.enabled` | `true` | Ativa reprodução iniciada pelo cuidador. |
| `breeding.localPopulationLimit` | `12, 2, 64` | Máximo de indivíduos vivos e carregados em 32 blocos de um nascimento. |
| `breeding.recoveryTicks` | `6000, 200, 240000` | Recuperação dos pais em ticks, ajustada de 0,75 a 1,25 pela fertilidade. 20 ticks = um segundo. |
| `breeding.growthTicks` | `12000, 200, 240000` | Ticks carregados e em boas condições até a fase adulta. Filhotes existentes mantêm sua duração. |
| `breeding.mutationChance` | `0.02, 0.0, 0.25` | Chance por alelo, ajustada pela estabilidade e instabilidade dos pais; máximo de 25%. |
| `breeding.mutationStep` | `0.1, 0.0, 0.25` | Máxima alteração absoluta de um alelo por mutação; o resultado fica entre zero e um. |
| `evolution.metamorphosis` | `true` | Ativa exposição ambiental e metamorfose com catalisador; receitas definem condições e custos. |
| `ecology.foraging` | `true` | Permite procurar e comer itens da dieta; não aumenta confiança e respeita mobGriefing. |
| `ecology.grouping` | `true` | Permite agrupamento compatível por espécie e cuidador, respeitando sociabilidade genética. |
| `ecology.territories` | `true` | Permite defesa territorial das espécies configuradas; respeita limites e cuidador. |
| `ecology.surfaceNests` | `true` | Gera ninhos em terreno novo e ativa seus habitantes finitos. |
| `ecology.caveColonies` | `true` | Gera colônias no ar de cavernas de terreno novo e ativa seus habitantes finitos. |
| `ecology.nestRarity` | `24, 1, 1000` | Chance adicional de uma em N por tentativa de ninho; valores maiores reduzem a frequência. |
| `ecology.colonyRarity` | `12, 1, 1000` | Chance adicional de uma em N por tentativa de colônia; valores maiores reduzem a frequência. |
| `structures.enabled` | `true` | Gera os seis locais especiais em chunks novos. Locais e baús existentes permanecem. |
| `structures.crystalCaverns` | `true` | Ativa a geração de Cavernas Cristalinas em chunks novos. |
| `structures.gelatinousLakes` | `true` | Ativa a geração de Lagos Gelatinosos em chunks novos. |
| `structures.elementalSanctuaries` | `true` | Ativa a geração de Santuários Elementais em chunks novos. |
| `structures.researcherRuins` | `true` | Ativa a geração de Ruínas de Pesquisadores em chunks novos. |
| `structures.ancestralChambers` | `true` | Ativa a geração de Câmaras Ancestrais em chunks novos. |
| `structures.royalCourts` | `true` | Ativa Cortes Reais em chunks novos. |
| `structures.rarity` | `1,1,1000` | Filtro adicional determinístico de uma em N. Datapacks controlam espaçamento e biomas. |
| `bosses.enabled` | `true` | Permite iniciar os quatro rituais; encontros existentes continuam ativos. |
| `bosses.damageMultiplier` | `1.0,0.0,2.0` | Escala o dano de chefes e lacaios. Zero desativa esse dano; consulte os [valores atuais](BALANCE.md). |

Desativar habilidades não desativa as defesas passivas; desativar rituais não
apaga chefes presentes. O dano de chefes usa bosses.damageMultiplier; o dano
de contato dos indivíduos usa damageMultiplier. Desativar estruturas não remove
blocos nem repõe baús. Raridades adicionais não são o espaçamento dos locais.

## Visual do cliente

O arquivo `config/slimeevolution-client.toml` é local e não muda regras do servidor.
A tela de configuração do NeoForge oferece rótulos e ajuda em português e inglês.

| Chave TOML | Padrão e limites | Efeito |
|---|---|---|
| `reducedMotion` | `false` | Reduz respiração, oscilação e pulsos; congela as deformações de chamas, raios e vapor. Saltos físicos continuam visíveis. |
| `visualParticleIntensity` | `0.75, 0.0, 1.0` | Intensidade das partículas extras de ação e dos acentos elementais em repouso; zero desativa essas partículas. |

Os efeitos extras respeitam a opção de partículas mínimas do Minecraft e
`abilityParticles` do servidor. Partes decorativas reduzem animação após 24 blocos
e param após 48. Isso não altera genética, dano, colisão ou iluminação do mundo.
Chamas, arcos elétricos e vapor geométricos continuam visíveis com partículas
mínimas ou intensidade zero; seu movimento usa `reducedMotion`. O orçamento
global das partículas extras é de quatro por cinco ticks, ou duas com partículas
reduzidas. Ações têm prioridade sobre acentos em repouso; movimento reduzido
também desativa esses acentos em repouso.

## Vínculo e simbiose

| Chave | Padrão | Efeito |
|---|---|---|
| `companions.training` | `true` | Permite lições e execução das ordens aprendidas |
| `companions.symbiosis` | `true` | Permite as duplas Água + Musgo e Elétrico + Ferro |

Desativar não apaga aprendizado, lar ou preferências. O cuidador ainda pode
selecionar Livre e desligar a cooperação. O cultivo também respeita `mobGriefing`
e a permissão de construção do cuidador. [Regras e custos](guides/COMPANIONS.md).

`companions.specializations` (padrão `true`) ativa as 19 funções individuais.
Ao desligar, processamento, auxílio e novos depósitos param; o cuidador
continua podendo retirar itens e cancelar uma função armazenada.

As quatro arenas de bosses têm proteção persistente contra alterações de blocos.
Desativar a geração não remove essa proteção nem libera um encontro ocupado.
