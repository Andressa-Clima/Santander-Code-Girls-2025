# 🚀 Desafio 2 DIO/CodeGirls - Workflows Automatizados com AWS Step Functions
Este projeto foi desenvolvido como desafio da DIO para o aprendizado sobre **workflows automatizados utilizando AWS Step Functions**.  
O objetivo é entender como orquestrar diferentes serviços da AWS, como Lambda e S3 no Step Functions.

---

## 🧩 O que é o AWS Step Functions?
O **AWS Step Functions** é um serviço que permite criar um tipo de fluxo automático (é como montar uam receita com passo a passo), conectando diversos serviços da AWS (como Lambda, S3, DynamoDB, etc.) de forma **visual, arrastando caixinhas, sem precisar de código complexo**.  

**Exemplo simples prático:**
1. Um arquivo é enviado para o **Amazon S3**;  
2. O **AWS Step Functions** inicia automaticamente um fluxo;  
3. Uma **função Lambda** é executada para processar o arquivo;  
4. O fluxo termina após a execução com sucesso.

<img width="250" height="552" alt="image" src="https://github.com/user-attachments/assets/7fb53fdf-a24a-4fcf-9b86-3b849a81c940" />

---

## ⚙️ Passo a Passo no Console da AWS

### 1. Criar a Máquina de Estados
- Acesse o **AWS Step Functions** no console da AWS;  
- Clicar em **Create state machine**;  
- Escolher **“Design visually”**.

### 2. Escolher o Tipo de Fluxo
- **Standard** (ideal para execuções mais longas).  

### 3. Adicionar as Etapas do Workflow
1. **Start** → ponto inicial do fluxo;  
2. **Lambda - ProcessarArquivo** → executa uma função Lambda que processa um arquivo vindo do S3;  
3. **Success (Finalizado)** → marca o fim da execução bem-sucedida.
