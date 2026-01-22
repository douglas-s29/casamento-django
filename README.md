# 💍 Site de Casamento - Django

Sistema completo para gerenciamento de casamento com site público elegante e área administrativa profissional. Design premium inspirado nos melhores sites do iCasei.

## ✨ Características

### Site Público
- ✅ **Hero Section**: Página inicial impactante com foto dos noivos e contador regressivo
- ✅ **Nossa História**: Timeline elegante com momentos importantes do casal
- ✅ **Lista de Presentes**: Grid responsivo com sistema de pagamento integrado
- ✅ **Confirmação de Presença**: Links únicos para cada convidado confirmar RSVP
- ✅ **Localização**: Mapa interativo com direções para Google Maps e Waze
- ✅ **Design Responsivo**: Perfeito em desktop, tablet e mobile

### Área Administrativa
- ✅ **Dashboard**: Estatísticas em tempo real e visão geral do evento
- ✅ **Gerenciamento de Convidados**: CRUD completo com links únicos de confirmação
- ✅ **Gerenciamento de Presentes**: Controle de estoque e categorização
- ✅ **Controle de Pagamentos**: Acompanhamento de todas as transações
- ✅ **Configurações**: Personalização de dados do evento e locais

### Design System
- 🎨 **Paleta Premium**: Dourado (#D4AF37), Rose (#B76E79), Grafite (#2C2C2C)
- 📝 **Tipografia Elegante**: Playfair Display, Great Vibes, Montserrat
- ✨ **Animações Suaves**: Fade-in ao scroll, parallax, transições CSS
- 🎭 **Efeitos Modernos**: Glassmorphism, gradientes, sombras elegantes

## 🚀 Tecnologias

- Django 4.2+
- Python 3.10+
- SQLite
- Asaas (Gateway de Pagamento) - *A implementar*
- HTML5 + CSS3 (Responsivo)
- JavaScript Vanilla (sem dependências)

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
# Edite o arquivo .env com suas configurações
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

8. Acesse:
   - **Site Público**: http://localhost:8000
   - **Painel Admin**: http://localhost:8000/painel/login/
   - **Django Admin**: http://localhost:8000/admin/

## 📁 Estrutura do Projeto

```
casamento-django/
├── manage.py
├── requirements.txt
├── README.md
├── .env.example
├── config/              # Configurações do Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── core/           # Site público (home, location)
│   ├── guests/         # Gerenciamento de convidados e RSVP
│   ├── gifts/          # Lista de presentes
│   ├── payments/       # Integração com Asaas
│   └── dashboard/      # Painel administrativo
├── static/             # CSS, JS, Imagens
│   ├── css/
│   │   ├── reset.css
│   │   ├── variables.css
│   │   ├── components.css
│   │   ├── public.css
│   │   └── admin.css
│   └── js/
│       ├── main.js
│       ├── countdown.js
│       ├── animations.js
│       └── admin.js
└── templates/          # Templates HTML
    ├── base.html
    ├── components/
    ├── public/
    └── dashboard/
```

## 🎨 Design System

### Cores
```css
--primary: #D4AF37 (Dourado)
--secondary: #C9A96E (Ouro Rose)
--accent: #B76E79 (Rose)
--dark: #2C2C2C (Grafite)
--light: #F8F6F3 (Off White)
```

### Tipografia
- **Títulos**: Playfair Display (serif elegante)
- **Script**: Great Vibes (nomes dos noivos)
- **Corpo**: Montserrat (texto geral)

## 🔧 Configurações

### Variáveis de Ambiente (.env)
```env
# Django
SECRET_KEY=sua-chave-secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Dados do Evento
GROOM_NAME=Noivo
BRIDE_NAME=Noiva
WEDDING_DATE=2026-12-31 18:00:00
WEDDING_LOCATION=Local da Cerimônia

# Asaas (Pagamentos)
ASAAS_API_KEY=sua-api-key
ASAAS_WEBHOOK_TOKEN=seu-token
ASAAS_ENVIRONMENT=sandbox
```

## 📱 Funcionalidades Principais

### 1. Confirmação de Presença (RSVP)
- Cada convidado recebe um link único
- Formulário simples: Confirmar / Não Pode Ir
- Campo para observações (restrições alimentares, etc)
- Confirmação salva automaticamente

### 2. Lista de Presentes
- Grid responsivo com filtros por categoria
- Imagem, descrição e valor de cada presente
- Barra de progresso mostrando disponibilidade
- Botão para presentear (integração com pagamento)

### 3. Painel Administrativo
- **Dashboard**: 4 cards de estatísticas + atividades recentes
- **Convidados**: Tabela com filtros, copiar link único, gerenciar status
- **Presentes**: Grid visual com edição inline
- **Pagamentos**: Histórico completo com filtros por status
- **Configurações**: Formulário para editar dados do evento

## 🌐 Páginas Públicas

### Home (`/`)
- Hero fullscreen com foto e countdown
- Seção "Salve a Data"
- Timeline "Nossa História"
- Cards de Cerimônia e Festa
- CTA para confirmar presença

### Lista de Presentes (`/presentes/`)
- Filtros por categoria
- Grid de 4 colunas (responsivo)
- Modal de compra com formulário

### Confirmação (`/confirmacao/<uuid>/`)
- Acesso via link único
- Formulário de confirmação
- Mensagem de sucesso

### Local (`/local/`)
- Informações de cerimônia e festa
- Mapa do Google Maps
- Botões para Waze e Google Maps
- Informações adicionais (estacionamento, dress code)

## 🔐 Segurança

- CSRF Protection habilitado
- Autenticação obrigatória para admin
- Links únicos (UUID) para convidados
- Validação de formulários
- Preparado para HTTPS em produção

## 📊 Modelos de Dados

### Guest (Convidado)
- Nome, email, telefone
- Link único (UUID)
- Status (pending, confirmed, declined)
- Observações

### Gift (Presente)
- Nome, descrição, imagem
- Preço, categoria
- Quantidade total/vendida
- Status ativo/inativo

### Payment (Pagamento)
- Presente relacionado
- Dados do comprador
- Valor, método (PIX/Cartão)
- Status (pending, confirmed, received)
- Integração Asaas

### EventSettings (Configuração)
- Dados dos noivos
- Data e horário
- Locais (cerimônia e festa)
- Imagens e mensagens

## 🚀 Próximos Passos

- [ ] Implementar integração completa com Asaas (PIX e Cartão)
- [ ] Adicionar CRUD completo via AJAX no admin
- [ ] Sistema de upload de imagens
- [ ] Exportação de relatórios (CSV/PDF)
- [ ] Email notifications
- [ ] Sistema de mensagens dos convidados
- [ ] Galeria de fotos
- [ ] Lista de músicas

## 📸 Screenshots

### Site Público
![Home Page](docs/screenshots/home.png)
*Página inicial com hero section e countdown*

### Admin Dashboard
![Dashboard](docs/screenshots/dashboard.png)
*Painel administrativo com estatísticas*

## 📝 Licença

MIT License

---

**Desenvolvido com ❤️ para celebrar momentos especiais**
