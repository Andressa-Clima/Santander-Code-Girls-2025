# 🚀 Desafio 5 DIO/CodeGirls — Automação com AWS Lambda, S3 e DynamoDB

Projeto desenvolvido para praticar **tarefas automatizadas com Lambda Function e S3**, armazenando dados no **DynamoDB**.  
Foi executado **localmente** usando o **LocalStack** para simular os serviços da AWS.

---

## 🧩 Arquitetura

1. O usuário faz upload de um arquivo no **S3**.  
2. O **S3** aciona a **Lambda**, que processa o conteúdo.  
3. Os dados são gravados na tabela **DynamoDB**.  
4. A consulta e inserção de registros ocorrem via **API Gateway**.  

**Serviços usados:** S3, Lambda, DynamoDB, IAM e API Gateway.

---

## ⚙️ Etapas principais

- Instalação e inicialização do **LocalStack**  
- Criação do **bucket S3**, **tabela DynamoDB** e **função Lambda**  
- Configuração do **trigger S3 → Lambda**  
- Integração com **API Gateway**  
- Testes via **Postman** e **scripts Python**

---

## 📘 Aprendizados

- Simulação de recursos AWS com **LocalStack**  
- Integração entre **Lambda, S3 e DynamoDB**  
- Criação de **APIs locais** com o **API Gateway**  
- **Documentação técnica** e uso do **GitHub**
