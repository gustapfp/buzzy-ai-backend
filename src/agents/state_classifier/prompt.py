STATE_CLASSIFIER_PROMPT = """

# Prompt — Classificador de Estado de Conversa**Objetivo**Classifique a mensagem {{ $json.chatInput }} **em exatamente um** dos estados a seguir, retornando **apenas** 3 valores em JSON
1. Estado da Mensagem 
2. Estado Anterior
3. A mensagem: {{ $json.chatInput }} 



## Estados (use exatamente estes rótulos)
* `cliente_curioso` — Cliente curioso sobre o produto/empresa (utilidade, funções, dúvidas gerais). 
* `cliente_interessado` — Pergunta preço, condições de pagamento, prazo/forma de entrega, detalhes comerciais. 
* `cliente_comprador` — Declara intenção clara de compra (ex.: “quero fechar”, “me manda o link”, “pode emitir o pedido”).
* `sem_resposta` — Cliente não respondeu dentro do tempo X definido nas regras de negócio. **Roteiro:** Nenhum; adicionar na planilha de follow up.
* `prospeccao_ativa` — Mensagem **proativa do agente** para clientes que não responderam ou pediram para esperar (follow-up).
* `em_espera` — Cliente disse que vai pensar/aguardar orçamento/verba/tempo. 
* `sem_interesse` — Cliente expressa desinteresse/quer parar de receber mensagens. **Roteiro:** Agente coletor de feedbacks. * `saudacao` — Saudação simples sem intenção (ex.: “oi”, “boa tarde”) 
* `sem_estado` — Ambíguo/indecidível/sem estado anterior ## Regras de decisão (prioridade)
1. **Opt-out/desinteresse** → `sem_interesse` (tem prioridade absoluta).
2. **Intenção explícita de compra** → `cliente_comprador`.
3. **Sinal comercial objetivo** (preço, condições, entrega) → `cliente_interessado`.
4. **Dúvida geral** (funcionamento/benefício/empresa) → `cliente_curioso`.
5. **Apenas saudação** → `saudacao`.
6. **Sem resposta no tempo X** (use metadados de tempo) → `sem_resposta`.
7. **Mensagem iniciada pelo agente para retomar contato** → `prospeccao_ativa`.
8. **Cliente pede tempo/“volte depois”** → `em_espera` (tente extrair data se houver).
9. **Persistindo ambiguidade/baixa confiança** → `sem_estado`.> **Empate / múltiplas intenções na mesma mensagem:** aplique a maior prioridade na ordem acima. 
## Exemplos
Siga a lógica dos exemplos a seguir. 
Mensagens recebida: Oi
Resposta esperada: Cliente esta intagindo com uma saudação, logo o estado que essa mensagem pertence é o de saudacao.Mensagens recebida: Sim
Resposta esperada: Cliente deu uma resposta positiva, logo deve proseguir para o proximo estado.

"""