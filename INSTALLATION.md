# Instalar e atualizar

Requisitos testados: Minecraft Java **1.21.1**, NeoForge **21.1.264**, Java **21**.
Slime Evolution 0.14.2 requer **GeckoLib 4.9.3 para NeoForge/Minecraft 1.21.1**.
Instale os dois mods no cliente e no servidor, com as mesmas versões em todos
os participantes. O ZIP de entrega contém o JAR oficial do GeckoLib em `dependencies/`.

1. Instale Minecraft/NeoForge compatíveis em um perfil separado.
2. Com o jogo/servidor desligado, coloque os JARs de Slime Evolution e GeckoLib na pasta `mods/`.
3. Crie um mundo de teste. No primeiro início, confira itens, espécies e receitas.
4. Consulte [configurações](CONFIGURATION.md) e [balanceamento](BALANCE.md).

NeoForge, Minecraft, Java, caches, scripts de teste e mundos de validação não
fazem parte do pacote. Não coloque o ZIP de documentação em `mods/`.
O pacote contém SHA256SUMS; compare o SHA-256 antes de usar um arquivo transferido.
GeckoLib conserva sua licença MIT, incluída em `licenses/GECKOLIB_LICENSE` no ZIP.

## Atualização e backup

Pare o servidor e faça uma cópia **completa e consistente do mundo**, incluindo
playerdata, data, dimensões e serverconfig. Guarde também a versão anterior do
JAR e a lista de mods. Só depois substitua o JAR e teste a cópia do mundo.
Não faça downgrade de um save já usado pela versão nova.

As cápsulas dependem de `data/slimeevolution_captures.dat`, do inventário e das
entidades do mundo. A Slimepedia usa `data/slimeevolution_research.dat` no
Overworld. Restaurar apenas o inventário ou apenas o ledger pode invalidar
cápsulas ou reintroduzir um token antigo contra um estado de mundo incompatível.
Não há transação única entre todos os arquivos de um mundo.

Cada dimensão também salva as regiões protegidas em `slimeevolution_arenas.dat`
e os encontros reservados em `slimeevolution_rituals.dat`, na sua pasta `data/`.
Inclua esses arquivos no backup completo; remover apenas uma reserva pode
desalinhar o altar e o boss ainda existente.

O ensaio automatizado verifica gravação comprimida, leitura por um armazenamento
novo, invalidação persistida de token e restauração do par de SavedData. Isso
não equivale a recuperação após queda abrupta ou backup parcial. Ledger ausente
não autoriza liberar cápsulas; recuperar o conjunto completo é a opção suportada.
Nunca apague o ledger para tentar corrigir uma cápsula.

Indivíduos mantêm NBT 7 e diário schema 3. Genomas, identidades e registros de
versões anteriores são preservados pelos leitores existentes; dados antigos
sem prova de mutação continuam como histórico indisponível. Conteúdo novo de
geração aparece em chunks novos, sem reconstruir terreno explorado.

## Compatibilidade e diagnóstico

Dois clientes reais foram testados por TCP local, com desconexão/reconexão,
inventário salvo, configurações do servidor, pesquisa privada e replay de cápsula.
Os ensaios gráficos usam Xvfb/Mesa por software na nuvem. Login online, rede
pública, GPU física, shaders e modpacks específicos não foram certificados.
Testar uma combinação nova em cópia do mundo continua sendo necessário.

Ao relatar um problema, envie versões de Minecraft/NeoForge/Java/mod, lista de
mods, passos para reproduzir e o trecho relevante do log, removendo dados pessoais.
Para erro de datapack, confira o ID/arquivo apontado no log: o mod rejeita
definições inválidas em vez de publicar um catálogo parcialmente carregado.

## Licença

O proprietário escolheu **All Rights Reserved**. A presença do JAR neste pacote
não concede permissão geral de redistribuição, modpack ou cópia de código/assets.
Copiar ou redistribuir conteúdo deste mod por addons/modpacks exige autorização.
A licença não define uma política separada para addons independentes interoperáveis.
Consulte LICENSE e THIRD_PARTY_NOTICES.md no pacote. Esta entrega não publica
automaticamente uma release binária em serviços externos.
