# Usando SNS:

O SNS **( Simple Notification Service )** permite enviar notificações quando um evento no vault acontece-se, por exemplo:
 + Quando for finalizado o inventario, lembremos que o inventario se invoca com o comando:
 
 ```bash
 aws glacier initiate-job --job-parameters '{"Type": "inventory-retrieval"}' --account-id - --vault-name NOME
 ```
 
 + Quando for finalizada a recuperação de um arquivo, 

```bash
aws glacier get-job-output --account-id - --vault-name 2020_abril_06 --job-id  JOBID inventario_JSON.txt
```
 
A documentação deste serviço (https://aws.amazon.com/pt/sns/getting-started/) é bastante completa, mas vou sugerir uma sequência básica de passos para atingir uma configuração inicial:

 + Criando um tema no SNS:
 
 ![image.png](attachment:image.png)


