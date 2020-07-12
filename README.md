# Armazenamento "Glacier" no AWS

Uma das formas mais econômicas de armazenar arquivos é usando o sistema GLACIER de armazenamento da AWS (https://aws.amazon.com/pt/glacier/), dado que os arquivos armazenados em dito sistema podem-se recuperar facilmente. 

Para este fim foi construído inicialmente um sistema caraterziado por:

+ Processamentos de fluxos de dados em JSON:
	- Lembremos que a consulta desde a CLI é feito com os comandos JSON:
	```bash
	aws glacier initiate-job --job-parameters '{"Type": "inventory-retrieval"}' --account-id YOUR_ACCOUNT_ID --region YOUR_REGION --vault-name YOUR_VAULT_NAME 
	```

+ Este procedimento de inventário demora aproximadamente 4 horas, e pode ser monitorado consultando a lista de trabalhos relacionada com dito VAULT:
	```bash
	aws glacier list-jobs --account-id - --vault-name 2020_abril_06
	```
+ Sendo possível esperar como resposta perante a consulta anterior:

	```json
			{
				"JobList": [
					{
						"InventoryRetrievalParameters": {
							"Format": "JSON"
						}, 
						"VaultARN": "arn:aws:glacier:us-east-2:937852338641:vaults/2020_abril_06", 
						"Completed": false, 
						"JobId": "O0bmSJWCWIJOTojdj_BhQjbdN6jrQ1O-q3A6v79d5MI-2mHbl-1iTnZUk0vhrrL-R44A70KO3767Azzz9STA9mMknVuD", 
						"Action": "InventoryRetrieval", 
						"CreationDate": "2020-07-12T14:55:22.300Z", 
						"StatusCode": "InProgress"
					}
				]
			}
	```

+ Se a resposta for do tipo:

	```json
	{
		"JobList": [
			{
				"CompletionDate": "2020-07-12T18:40:02.958Z", 
				"VaultARN": "arn:aws:glacier:us-east-2:937852338641:vaults/2020_abril_06", 
				"InventoryRetrievalParameters": {
					"Format": "JSON"
				}, 
				"Completed": true, 
				"InventorySizeInBytes": 34120, 
				"JobId": "O0bmSJWCWIJOTojdj_BhQjbdN6jrQ1O-q3A6v79d5MI-2mHbl-1iTnZUk0vhrrL-R44A70KO3767Azzz9STA9mMknVuD", 
				"Action": "InventoryRetrieval", 
				"CreationDate": "2020-07-12T14:55:22.300Z", 
				"StatusMessage": "Succeeded", 
				"StatusCode": "Succeeded"
			}
		]
	}

	```
Estariamos perando um cenário de "trabalho pronto" ("StatusCode": "Succeeded")
+ Já com este ("StatusCode": "Succeeded") pode-se coletar o inventário do VAULT usando:
	```bash
	aws glacier get-job-output --account-id - --vault-name 2020_abril_06 --job-id  O0bmSJWCWIJOTojdj_BhQjbdN6jrQ1O-q3A6v79d5MI-2mHbl-1iTnZUk0vhrrL-R44A70KO3767Azzz9STA9mMknVuD inventario_JSON.txt
	```
	Obte-se desta linha de comando o arquivo "inventario_JSON.txt" que pode ser estudado com ajuda dos arquivos:
	- ler_inventario_SAIDA_ArchiveId.py (Pare gerar uma lista de ArchiveID)
	- ler_inventario_SAIDA_DATA.py (Para ver a data de criação de cada elemento)
+ Já com este ("StatusCode": "Succeeded") pode-se coletar o inventário do VAULT usando:

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


Não se esqueça de usar o CACHE das credenciais para agilizar as operações

+ git config --global credential.helper cache

+ git config --global credential.helper 'cache --timeout=13600'
