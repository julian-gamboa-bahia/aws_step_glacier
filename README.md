# Armazenamento "Glacier" no AWS

Uma das formas mais econômicas de armazenar arquivos é usando o sistema GLACIER de armazenamento da AWS (https://aws.amazon.com/pt/glacier/), dado que os arquivos armazenados em dito sistema podem-se recuperar facilmente. 

Para este fim foi construído inicialmente um sistema caraterziado por:

+ Processamentos de fluxos de dados em JSON:
	- Lembremos que a consulta desde a CLI é feito com os comandos JSON:

+ 
<!---
+ Migrar o projeto anterior para consultar uma API (https://q2gp3i5m5c.execute-api.us-east-2.amazonaws.com/default/jogo_quina?numero_jogo=111) desenvolvida em AWS lambda (https://github.com/julian-gamboa-bahia/jogo_quina/blob/master/consulta_sequencia.js)
  - Para este fim será preciso apenas usar uma consulta "$.getJSON" consultando a API já mencionada.

+ Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    * Ac tristique libero volutpat at
    + Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit
+ Very easy!

-->