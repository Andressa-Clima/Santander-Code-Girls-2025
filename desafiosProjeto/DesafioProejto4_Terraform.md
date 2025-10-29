# 🚀 Desafio 4 DIO/CodeGirls - AWS CloudFormation - Terraform
## 📖 Visão Geral

Neste desafio, o objetivo é praticar a criação de infraestrutura automatizada utilizando o AWS CloudFormation, explorando o conceito de Stacks (pilhas) e o uso de templates prontos disponibilizados pela AWS no GitHub.

🔗 Repositório oficial:
https://github.com/aws-cloudformation/aws-cloudformation-templates

## 🛠️ Etapas Realizadas
1️⃣ Acesso ao Repositório
Entre no repositório da AWS no GitHub e explore os exemplos de templates disponíveis em YAML e JSON.

📁 Caminho sugerido:
/aws-cloudformation-templates/aws/services/

2️⃣ Escolha e Download do Template
Selecione o template desejado (por exemplo, um modelo de EC2 ou VPC), clique em Download e salve o arquivo .yaml ou .json no seu computador.

3️⃣ Criação da Stack no CloudFormation
No Console da AWS, acesse o serviço CloudFormation.
Clique em Criar pilha → Carregar um arquivo de modelo.
Envie o arquivo do template baixado.
Dê um nome à sua stack e, se necessário, preencha os parâmetros solicitados.
Finalize clicando em Criar pilha.

A AWS criará automaticamente todos os recursos definidos no template, como instâncias EC2, buckets S3, grupos de segurança ou bancos de dados, dependendo do modelo escolhido.

## ⚙️ Resultado Esperado

A infraestrutura será provisionada de forma automática conforme o código do template.
Será possível visualizar e gerenciar os recursos criados diretamente no console da AWS.
A stack poderá ser atualizada ou excluída a qualquer momento, mantendo o controle total via CloudFormation.

## 📘 Aprendizados e Comparações

Durante a prática, foi possível compreender as diferenças entre as duas principais ferramentas de Infraestrutura como Código (IaC):

Terraform    	     -- Multi-cloud, linguagem HCL, controle de estado local ou remoto

AWS CloudFormation --	Exclusivo da AWS, usa YAML/JSON, estado gerenciado automaticamente pela AWS

### 💡 Insight:
O CloudFormation é ideal para quem utiliza apenas a AWS e busca automação nativa, enquanto o Terraform é mais indicado para ambientes híbridos ou multi-cloud.
