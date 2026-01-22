# 🚀 Guia Rápido de Instalação

## Começando em 5 Minutos

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Configurar Ambiente
```bash
# Copiar arquivo de exemplo
cp .env.example .env

# Editar com seus dados (opcional, já tem valores padrão)
nano .env  # ou vim, ou seu editor preferido
```

### 3. Preparar Banco de Dados
```bash
# Criar banco de dados
python manage.py migrate

# Criar usuário admin
python manage.py createsuperuser
# Usuário: admin
# Email: admin@example.com
# Senha: (escolha uma senha)
```

### 4. Rodar o Servidor
```bash
python manage.py runserver
```

### 5. Acessar o Site
- **Site Público**: http://localhost:8000
- **Painel Admin**: http://localhost:8000/painel/login/
- **Django Admin**: http://localhost:8000/admin/

## 📝 Próximos Passos

### Adicionar Dados Iniciais

1. **Configurar o Evento** (via Django Admin ou Painel)
   - Acesse `/admin/` ou `/painel/configuracoes/`
   - Preencha: nomes dos noivos, data, local
   - Faça upload da foto do casal (hero)

2. **Adicionar Convidados**
   - Acesse `/painel/convidados/`
   - Clique em "Novo Convidado"
   - Preencha nome e email
   - Copie o link único para enviar ao convidado

3. **Adicionar Presentes**
   - Acesse `/painel/presentes/`
   - Clique em "Novo Presente"
   - Faça upload de foto, adicione descrição e preço
   - Defina categoria e quantidade

## 🎨 Personalização Rápida

### Alterar Cores
Edite `static/css/variables.css`:
```css
:root {
  --primary: #D4AF37;    /* Sua cor principal */
  --secondary: #C9A96E;  /* Cor secundária */
  --accent: #B76E79;     /* Cor de destaque */
}
```

### Alterar Textos
Edite os templates em `templates/public/`:
- `home.html` - Página inicial
- `rsvp.html` - Confirmação
- `gifts.html` - Presentes
- `location.html` - Local

### Adicionar Fotos
1. **Foto Hero**: Upload via configurações (`/painel/configuracoes/`)
2. **Fotos Presentes**: Upload ao criar/editar presente
3. **Placeholder**: Por padrão usa Unsplash para demonstração

## 🔧 Comandos Úteis

```bash
# Ver rotas disponíveis
python manage.py show_urls  # (se instalado django-extensions)

# Criar backup do banco
cp db.sqlite3 db.backup.sqlite3

# Resetar banco (CUIDADO!)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser

# Coletar arquivos estáticos (produção)
python manage.py collectstatic
```

## 🐛 Solução de Problemas

### Erro: "No module named 'decouple'"
```bash
pip install python-decouple
```

### Erro: "Static files not found"
```bash
# Verificar se existe o diretório
mkdir -p static
python manage.py collectstatic --noinput
```

### Erro: "Template does not exist"
```bash
# Verificar estrutura de templates
ls templates/
ls templates/public/
ls templates/dashboard/
```

### Porta 8000 já em uso
```bash
# Usar outra porta
python manage.py runserver 8080
```

## 📊 Dados de Teste

Quer popular com dados de exemplo? Crie alguns convidados e presentes manualmente ou use o shell do Django:

```python
python manage.py shell

# Criar convidados de teste
from apps.guests.models import Guest
Guest.objects.create(name="João Silva", email="joao@example.com", phone="11999999999")
Guest.objects.create(name="Maria Santos", email="maria@example.com")

# Criar presentes de teste  
from apps.gifts.models import Gift
Gift.objects.create(
    name="Jogo de Panelas",
    description="Conjunto completo de panelas antiaderentes",
    price=299.90,
    category="cozinha",
    total_quantity=2
)
```

## 🚀 Deploy (Produção)

### Preparar para Produção
1. Altere `DEBUG=False` no `.env`
2. Configure `ALLOWED_HOSTS` com seu domínio
3. Gere nova `SECRET_KEY` (use generator online)
4. Configure banco PostgreSQL (opcional)
5. Configure servidor web (Nginx + Gunicorn)

### Deploy Rápido (Heroku)
```bash
# Instalar Heroku CLI e fazer login
heroku create seu-casamento

# Adicionar PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# Deploy
git push heroku main

# Migrar banco
heroku run python manage.py migrate

# Criar superuser
heroku run python manage.py createsuperuser
```

## 💡 Dicas

- **Teste Mobile**: Use DevTools do Chrome (F12 > Toggle Device)
- **Backup Regular**: Copie `db.sqlite3` antes de mudanças grandes
- **Git**: Faça commits frequentes das suas alterações
- **Logs**: Verifique o terminal para erros durante desenvolvimento

## 📞 Suporte

Problemas? Verifique:
1. README.md - Documentação completa
2. Código de exemplo nos templates
3. Comentários no código
4. Issues do GitHub

Boa sorte com seu site de casamento! 💍✨
