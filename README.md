# 💍 Sistema Completo de Gerenciamento de Casamento - Django

Sistema completo para gerenciamento de casamento com site público responsivo e área administrativa separada, desenvolvido com Django 4.2.

![Home Page](https://github.com/user-attachments/assets/9b5935cf-25c2-4f69-8e06-5dfb00b76c3c)

## 🚀 Tecnologias

- **Backend**: Django 4.2.9
- **Python**: 3.10+
- **Banco de Dados**: SQLite (embutido)
- **Gateway de Pagamento**: Asaas (PIX + Cartão de Crédito)
- **Frontend**: Django Templates + HTML5 + CSS3 (Responsivo, Mobile-First)
- **Deploy**: Simples (VPS, Railway, Render)

## ✨ Funcionalidades

### 🌐 Site Público

#### Página Inicial
- Nome dos noivos personalizável
- **Contador regressivo** em tempo real até a data do casamento
- Data, hora e local do evento
- Design moderno, elegante e responsivo

#### Sistema de Convites
- Cada convidado recebe um **link único** com UUID
- Confirmação de presença (Sim/Não)
- Campo para observações
- Controle de status (Confirmado/Não confirmado/Pendente)

![Guest Invite](https://github.com/user-attachments/assets/a016b722-cfa2-4a24-9109-e61e08d4d716)

#### Lista de Presentes
- Catálogo completo com imagens
- **Controle automático de estoque**
- Sistema de quantidade disponível
- Bloqueio automático quando esgotado
- Acesso público para compra

![Gift List](https://github.com/user-attachments/assets/e7707b03-c044-44c6-b267-807e6eb923b8)

#### Pagamentos Integrados
- **Integração completa com Asaas**
- Suporte a PIX (com QR Code)
- Suporte a Cartão de Crédito
- Webhook para atualização automática de status
- Mensagem de agradecimento personalizada após confirmação

#### Página do Local
- Nome e endereço completo
- Links diretos para Google Maps e Waze
- Mapa incorporado (iframe)
- Informações adicionais

### 🔐 Área Administrativa

#### Dashboard Personalizado
- Estatísticas em tempo real:
  - Total de convidados
  - Confirmados/Não confirmados/Pendentes
  - Total arrecadado
  - Presentes vendidos
- Tabela de pagamentos recentes
- Ranking de presentes mais vendidos

![Dashboard](https://github.com/user-attachments/assets/15071988-2301-4fe1-a85e-489e0ac9dae2)

#### Gerenciamento de Convidados
- CRUD completo
- Geração automática de link de convite único
- Visualização de status de confirmação
- Exportação de dados
- Link para compartilhar via WhatsApp/Email

#### Gerenciamento de Presentes
- CRUD completo com upload de imagens
- Controle automático de estoque
- Bloqueio de vendas ao atingir limite
- Preview de imagens
- Indicadores visuais de disponibilidade

#### Gerenciamento de Pagamentos
- Visualização de todos os pagamentos
- Filtros por status e método
- Detalhes completos de cada transação
- Integração com webhook do Asaas
- Atualização automática de status

## 📦 Instalação Rápida

### 1. Clone o repositório
```bash
git clone https://github.com/douglas-s29/casamento-django.git
cd casamento-django
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas configurações:
```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Asaas Payment Gateway
ASAAS_API_KEY=sua_api_key_aqui
ASAAS_WEBHOOK_TOKEN=seu_token_secreto
ASAAS_ENVIRONMENT=sandbox  # ou production
```

### 5. Execute as migrações
```bash
python manage.py migrate
```

### 6. Crie dados de exemplo (Opcional)
```bash
python manage.py create_sample_data
```

### 7. Crie um superusuário
```bash
python manage.py createsuperuser
```

### 8. Execute o servidor
```bash
python manage.py runserver
```

### 9. Acesse o sistema
- **Site Público**: http://localhost:8000/
- **Admin Django**: http://localhost:8000/admin/
- **Dashboard**: http://localhost:8000/dashboard/

## 📁 Estrutura do Projeto

```
casamento-django/
├── manage.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── db.sqlite3                    # Banco de dados SQLite
├── config/                       # Configurações do Django
│   ├── __init__.py
│   ├── settings.py              # Configurações principais
│   ├── urls.py                  # URLs principais
│   └── wsgi.py
├── apps/
│   ├── core/                    # Site público (Home, Local)
│   │   ├── models.py            # EventSettings
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── management/
│   │       └── commands/
│   │           └── create_sample_data.py
│   ├── guests/                  # Gerenciamento de convidados
│   │   ├── models.py            # Guest
│   │   ├── views.py             # Convites e confirmação
│   │   ├── urls.py
│   │   └── admin.py
│   ├── gifts/                   # Lista de presentes
│   │   ├── models.py            # Gift
│   │   ├── views.py             # Lista e detalhes
│   │   ├── urls.py
│   │   └── admin.py
│   ├── payments/                # Integração Asaas
│   │   ├── models.py            # Payment
│   │   ├── views.py             # Criação e webhook
│   │   ├── services.py          # AsaasService
│   │   ├── urls.py
│   │   └── admin.py
│   └── dashboard/               # Painel administrativo
│       ├── views.py             # Dashboard com estatísticas
│       └── urls.py
├── templates/
│   ├── base.html                # Template base
│   ├── public/                  # Templates públicos
│   │   ├── home.html
│   │   ├── venue.html
│   │   ├── convite.html
│   │   ├── gift_list.html
│   │   ├── gift_detail.html
│   │   ├── payment_form.html
│   │   └── payment_confirmation.html
│   └── admin/                   # Templates admin
│       └── dashboard.html
├── static/                      # CSS, JS, Imagens
│   ├── css/
│   ├── js/
│   └── images/
└── media/                       # Upload de imagens
    └── gifts/
```

## 🎯 Modelos de Dados

### EventSettings (Configuração do Evento)
```python
- nome_noivo: CharField
- nome_noiva: CharField
- data_casamento: DateTimeField
- local_nome: CharField
- local_endereco: TextField
- local_latitude: DecimalField (opcional)
- local_longitude: DecimalField (opcional)
- local_maps_url: URLField
- local_waze_url: URLField
- mensagem_agradecimento: TextField
```

### Guest (Convidado)
```python
- nome: CharField
- email: EmailField
- telefone: CharField (opcional)
- token_convite: UUIDField (único, gerado automaticamente)
- confirmou_presenca: BooleanField (null=True)
- observacoes: TextField (opcional)
- data_confirmacao: DateTimeField (opcional)
- data_criacao: DateTimeField (auto)
```

### Gift (Presente)
```python
- nome: CharField
- descricao: TextField (opcional)
- valor: DecimalField
- quantidade_total: PositiveIntegerField
- quantidade_vendida: PositiveIntegerField (default=0)
- imagem: ImageField (upload_to='gifts/')
- ativo: BooleanField (default=True)
- data_criacao: DateTimeField (auto)
- data_atualizacao: DateTimeField (auto)
```

### Payment (Pagamento)
```python
- presente: ForeignKey(Gift)
- nome_comprador: CharField
- email_comprador: EmailField
- telefone_comprador: CharField (opcional)
- valor: DecimalField
- quantidade: PositiveIntegerField
- asaas_payment_id: CharField (único)
- status: CharField (pending, confirmed, received, overdue)
- metodo_pagamento: CharField (PIX, CREDIT_CARD, BOLETO)
- qr_code: TextField (para PIX)
- qr_code_image: URLField (imagem do QR Code)
- link_pagamento: URLField
- data_criacao: DateTimeField (auto)
- data_confirmacao: DateTimeField (opcional)
- data_atualizacao: DateTimeField (auto)
```

## 🔗 Integração com Asaas

### Configuração

1. Crie uma conta em [Asaas](https://www.asaas.com)
2. Obtenha sua API Key no painel
3. Configure no arquivo `.env`:

```env
ASAAS_API_KEY=sua_api_key_aqui
ASAAS_WEBHOOK_TOKEN=seu_token_secreto_unico
ASAAS_ENVIRONMENT=sandbox  # sandbox para testes, production para produção
```

### Funcionalidades Implementadas

- ✅ Criação de clientes (busca ou cria automaticamente)
- ✅ Criação de cobranças (PIX e Cartão)
- ✅ Geração de QR Code PIX
- ✅ Webhook para receber notificações de pagamento
- ✅ Validação de webhook com token secreto
- ✅ Atualização automática de status
- ✅ Controle de estoque ao confirmar pagamento
- ✅ Proteção contra pagamentos duplicados

### Webhook

Configure no painel do Asaas:
- URL: `https://seu-dominio.com/pagamentos/webhook/asaas/`
- Token: O mesmo configurado em `ASAAS_WEBHOOK_TOKEN`
- Eventos: PAYMENT_CONFIRMED, PAYMENT_RECEIVED, PAYMENT_OVERDUE

## 🎨 Design e UX

- **Paleta de cores**: Tons pastéis com gradientes suaves (roxo/azul)
- **Tema**: Elegante e romântico, apropriado para casamento
- **Responsivo**: Mobile-first, funciona perfeitamente em todos os dispositivos
- **Animações**: Suaves e discretas
- **Feedback visual**: Claro e imediato para todas as ações
- **Loading states**: Durante processamento de pagamentos
- **Ícones**: Emojis para um toque amigável e moderno

## 🚀 Deploy

### Preparação
```bash
# Coletar arquivos estáticos
python manage.py collectstatic

# Configurar DEBUG=False no .env
DEBUG=False
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
```

### Opções de Deploy

#### Railway
1. Conecte seu repositório GitHub
2. Configure as variáveis de ambiente
3. Deploy automático

#### Render
1. Conecte seu repositório GitHub
2. Configure as variáveis de ambiente
3. Configure o comando de start: `gunicorn config.wsgi:application`

#### VPS (Ubuntu)
```bash
# Instalar dependências
sudo apt update
sudo apt install python3-pip python3-venv nginx

# Configurar aplicação com gunicorn e nginx
# Configurar supervisor ou systemd para gerenciar o processo
```

## 📝 Comandos Úteis

```bash
# Criar dados de exemplo
python manage.py create_sample_data

# Criar superusuário
python manage.py createsuperuser

# Fazer backup do banco de dados
python manage.py dumpdata > backup.json

# Restaurar backup
python manage.py loaddata backup.json

# Executar testes (se implementados)
python manage.py test

# Verificar problemas
python manage.py check
```

## 🔒 Segurança

- ✅ Webhook protegido por token secreto
- ✅ Validação de assinatura do webhook
- ✅ Proteção CSRF em todos os formulários
- ✅ Sanitização de inputs
- ✅ Validação de dados no backend
- ✅ Controle de acesso ao admin via autenticação
- ✅ Proteção contra SQL Injection (Django ORM)
- ✅ Proteção contra XSS (Django Templates)

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Enviar pull requests

## 📄 Licença

MIT License - Sinta-se livre para usar este projeto para seu casamento! ❤️

## 💡 Créditos

Desenvolvido com ❤️ para casais que querem um sistema moderno e funcional para gerenciar seu casamento.

## 📞 Suporte

Para dúvidas ou problemas, abra uma issue no GitHub.

---

**Feito com amor para tornar seu casamento ainda mais especial! 💍💕**
