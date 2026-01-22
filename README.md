# 💍 Site de Casamento - Django

Sistema completo para gerenciamento de casamento com site público e área administrativa.

## 🚀 Tecnologias

- Django 4.2+
- Python 3.10+
- SQLite
- Asaas (Gateway de Pagamento)
- HTML5 + CSS3 (Responsivo)

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/douglas-s29/casamento-django.git
cd casamento-django
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas credenciais
```

5. Execute as migrações:
```bash
python manage.py migrate
```

6. Crie um superusuário:
```bash
python manage.py createsuperuser
```

7. Execute o servidor:
```bash
python manage.py runserver
```

8. Acesse: http://localhost:8000

## 📁 Estrutura do Projeto

```
casamento-django/
├── manage.py
├── requirements.txt
├── README.md
├── .env.example
├── config/              # Configurações do Django
├── apps/
│   ├── core/           # Site público
│   ├── guests/         # Gerenciamento de convidados
│   ├── gifts/          # Lista de presentes
│   ├── payments/       # Integração Asaas
│   └── dashboard/      # Painel administrativo
├── static/             # CSS, JS, Imagens
└── templates/          # Templates HTML
```

## 🌐 Funcionalidades

### Site Público
- ✅ Página inicial com contador regressivo
- ✅ Confirmação de presença via link único
- ✅ Lista de casamento com pagamento (PIX/Cartão)
- ✅ Informações do local da cerimônia

### Área Administrativa
- ✅ Dashboard com estatísticas
- ✅ Gerenciamento de convidados
- ✅ Gerenciamento de presentes
- ✅ Controle de pagamentos
- ✅ Mensagens de agradecimento

## 🔐 Configuração do Asaas

1. Crie uma conta em: https://www.asaas.com
2. Obtenha sua API Key
3. Configure no arquivo `.env`:

```
ASAAS_API_KEY=sua_api_key_aqui
ASAAS_WEBHOOK_TOKEN=seu_token_secreto
ASAAS_ENVIRONMENT=sandbox
```

## 📝 Licença

MIT License
