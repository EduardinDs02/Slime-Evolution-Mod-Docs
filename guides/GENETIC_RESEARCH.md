# Pesquisa genética

A Slimepedia registra faixas de expressão observadas e genes
com alteração verificada no nascimento. A análise usa o genoma do indivíduo e
seu histórico; uma característica incomum, por si só, não comprova mutação.

## Descobrir variantes

Use o analisador em um slime ao alcance e com visão livre, ou conclua a análise
de uma cápsula válida na estação genética. Abra a aba **Genes** da Slimepedia:
ela acumula as faixas encontradas entre os indivíduos analisados da espécie.

| Faixa | Expressão calculada do gene |
|---|---|
| Baixa | 0 até 0,25, inclusive |
| Intermediária | acima de 0,25 e abaixo de 0,75 |
| Alta | 0,75 até 1, inclusive |

O cálculo respeita a expressão aditiva, dominante ou recessiva. As faixas
referem-se ao valor genético calculado; seus efeitos continuam sujeitos às
regras de cada espécie. Por exemplo, a luminosidade genética tem emissão
visual própria no Luminoso, conforme [GENETICS.md](../reference/GENETICS.md).

As variantes desta etapa são essas faixas, aplicadas aos 15 genes existentes.
O registro é cumulativo por espécie/jogador: encontrar outra faixa acrescenta
conhecimento sem substituir a anterior. Repetir a mesma análise não aumenta
uma contagem artificial. O livro guarda até três faixas por gene, sem uma
lista crescente de UUIDs ou genomas completos.

Observar com o livro, alimentar ou presenciar um nascimento continua liberando
seus próprios fatos. Os dados genéticos entram somente após análise. O livro
de outro jogador consulta o progresso desse jogador. Espectadores não avançam
pesquisa.

## Mutações verificadas no nascimento

A herança agora devolve o genoma e o conjunto de genes em que pelo menos um
alelo mudou **de fato** após aplicar a mutação e seus limites. Chance,
amplitude, seleção de alelos e consumo do RNG continuam iguais. Tentativas
com passo zero, delta zero ou resultado igual após o limite 0/1 não registram
uma alteração inexistente.

Novos descendentes produzidos pelo serviço de reprodução guardam esse
histórico. Após analisar um deles, o livro acrescenta os genes alterados à
pesquisa da espécie. Uma mudança pode existir mesmo quando a média dos dois
alelos, e portanto uma expressão aditiva, permanece igual.

O livro distingue:

- **Mutações verificadas:** genes alterados em nascimentos analisados com registro.
- **Nascimento sem novas alterações:** houve análise de um descendente com histórico conhecido e nenhum alelo novo nesse nascimento.
- **Histórico indisponível:** houve análise de descendente sem registro de origem verificável.

Fundadores têm variação genética e não fornecem, sozinhos, prova de mutação
num nascimento. Herdar um alelo já presente nos pais também não é uma nova
mutação nesse descendente. A observação é sobre o nascimento direto do
indivíduo; o livro não reconstrói todos os eventos dos seus ancestrais.

No analisador, passe o mouse sobre um gene para consultar o estado de seu
registro de nascimento, além do tipo de expressão e efeito existente.

## Persistência e compatibilidade

O NBT do indivíduo passa à **versão 6**, com `BirthMutationsKnown` e
`BirthMutationGenes`. Os genes usam nomes estáveis do enum; a lista é limitada
aos 15 genes. Campos ausentes ou histórico inválido carregam como indisponível.
Saves anteriores não recebem uma inferência retroativa baseada em valores raros.
Nascimentos conhecidos sem alteração são diferentes de histórico ausente.

O histórico acompanha cápsulas, leitura na estação e crescimento na incubadora.
Ele permanece fora do conjunto de campos que a incubadora pode modificar;
a troca condicional do registro rejeita mudanças no histórico/genoma/linhagem.
A inspeção fecha se seu histórico de nascimento mudar durante a leitura.

O diário pessoal passa ao **schema 2**. Diários da versão 1 preservam espécies,
estágios e rotas; uma nova análise preenche as faixas/histórico que faltavam.
Um trecho genético inválido é descartado durante a leitura sem apagar os
demais fatos válidos desse registro. O armazenamento continua compartilhado
entre dimensões pelo UUID do jogador.

O servidor transmite somente as descobertas do jogador e os detalhes da
espécie selecionada. Os novos dados usam 15 máscaras de faixas, uma máscara
de genes alterados e dois indicadores históricos. O pior caso do livro
continua abaixo dos 32.600 bytes do menu. Use a mesma versão do mod em cliente
e servidor, pois os snapshots de inspeção/livro receberam esses dados.
