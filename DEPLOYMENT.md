# 🚀 Guia de Deployment - Sistema de Casamento Django

## Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)
- Git
- Conta no Asaas (para pagamentos)

## Deploy Local (Desenvolvimento)

### 1. Preparação do Ambiente

```bash
# Clone o repositório
git clone https://github.com/douglas-s29/casamento-django.git
cd casamento-django

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt
```

### 2. Configuração

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o .env com suas configurações
nano .env  # ou use seu editor preferido
```

Configurações mínimas necessárias:
```env
SECRET_KEY=sua-chave-secreta-muito-longa-e-aleatoria
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Asaas (opcional para testes iniciais)
ASAAS_API_KEY=
ASAAS_WEBHOOK_TOKEN=
ASAAS_ENVIRONMENT=sandbox
```

### 3. Inicialização do Banco de Dados

```bash
# Execute as migrações
python manage.py migrate

# Crie dados de exemplo (opcional)
python manage.py create_sample_data

# Crie um superusuário
python manage.py createsuperuser
```

### 4. Execute o Servidor

```bash
python manage.py runserver
```

Acesse:
- Site: http://localhost:8000
- Admin: http://localhost:8000/admin
- Dashboard: http://localhost:8000/dashboard

## Deploy em Produção

### Railway.app

1. **Conecte seu repositório GitHub ao Railway**

2. **Configure as variáveis de ambiente**:
   - `SECRET_KEY`: Gere uma chave secreta forte
   - `DEBUG`: False
   - `ALLOWED_HOSTS`: seu-app.railway.app
   - `ASAAS_API_KEY`: Sua chave da API Asaas
   - `ASAAS_WEBHOOK_TOKEN`: Token secreto único
   - `ASAAS_ENVIRONMENT`: production

3. **O Railway detectará automaticamente o Django**

4. **Configure o Procfile** (se necessário):
```
web: gunicorn config.wsgi:application
```

5. **Deploy automático** a cada push no GitHub

### Render.com

1. **Crie um novo Web Service**

2. **Conecte ao GitHub**

3. **Configure**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn config.wsgi:application`

4. **Adicione variáveis de ambiente**:
   - SECRET_KEY
   - DEBUG=False
   - ALLOWED_HOSTS=seu-app.onrender.com
   - ASAAS_API_KEY
   - ASAAS_WEBHOOK_TOKEN
   - ASAAS_ENVIRONMENT=production

5. **Deploy**

### VPS (Ubuntu/Debian)

#### 1. Preparar o Servidor

```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependências
sudo apt install python3-pip python3-venv nginx git -y
```

#### 2. Clonar e Configurar o Projeto

```bash
# Criar diretório
sudo mkdir -p /var/www/casamento
sudo chown $USER:$USER /var/www/casamento
cd /var/www/casamento

# Clonar repositório
git clone https://github.com/douglas-s29/casamento-django.git .

# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
pip install gunicorn
```

#### 3. Configurar Variáveis de Ambiente

```bash
# Criar arquivo .env
nano .env
```

```env
SECRET_KEY=sua-chave-secreta-muito-forte
DEBUG=False
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com

ASAAS_API_KEY=sua-api-key-producao
ASAAS_WEBHOOK_TOKEN=seu-token-secreto
ASAAS_ENVIRONMENT=production
```

#### 4. Preparar a Aplicação

```bash
# Migrar banco de dados
python manage.py migrate

# Coletar arquivos estáticos
python manage.py collectstatic --noinput

# Criar superusuário
python manage.py createsuperuser
```

#### 5. Configurar Gunicorn

Criar `/etc/systemd/system/casamento.service`:

```ini
[Unit]
Description=Casamento Django
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/casamento
Environment="PATH=/var/www/casamento/venv/bin"
ExecStart=/var/www/casamento/venv/bin/gunicorn --workers 3 --bind unix:/var/www/casamento/casamento.sock config.wsgi:application

[Install]
WantedBy=multi-user.target
```

```bash
# Iniciar serviço
sudo systemctl start casamento
sudo systemctl enable casamento
sudo systemctl status casamento
```

#### 6. Configurar Nginx

Criar `/etc/nginx/sites-available/casamento`:

```nginx
server {
    listen 80;
    server_name seu-dominio.com www.seu-dominio.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/casamento;
    }
    
    location /media/ {
        root /var/www/casamento;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/casamento/casamento.sock;
    }
}
```

```bash
# Ativar site
sudo ln -s /etc/nginx/sites-available/casamento /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

#### 7. Configurar SSL com Let's Encrypt

```bash
# Instalar Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obter certificado
sudo certbot --nginx -d seu-dominio.com -d www.seu-dominio.com

# Renovação automática já está configurada
```

## Configuração do Webhook Asaas

1. Acesse o painel do Asaas
2. Vá em Configurações > Webhooks
3. Adicione um novo webhook:
   - URL: `https://seu-dominio.com/pagamentos/webhook/asaas/`
   - Token: O mesmo que você configurou em `ASAAS_WEBHOOK_TOKEN`
   - Eventos: Selecione:
     - PAYMENT_CONFIRMED
     - PAYMENT_RECEIVED
     - PAYMENT_OVERDUE

## Manutenção

### Backup do Banco de Dados

```bash
# Backup
python manage.py dumpdata > backup_$(date +%Y%m%d).json

# Restaurar
python manage.py loaddata backup_20240122.json
```

### Atualização do Código

```bash
# No servidor
cd /var/www/casamento
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart casamento
```

### Logs

```bash
# Ver logs do Gunicorn
sudo journalctl -u casamento -f

# Ver logs do Nginx
sudo tail -f /var/log/nginx/error.log
sudo tail -f /var/log/nginx/access.log
```

## Checklist de Deploy

- [ ] Variáveis de ambiente configuradas
- [ ] DEBUG=False em produção
- [ ] SECRET_KEY forte e única
- [ ] ALLOWED_HOSTS configurado corretamente
- [ ] Banco de dados migrado
- [ ] Arquivos estáticos coletados
- [ ] Superusuário criado
- [ ] Webhook do Asaas configurado
- [ ] SSL/HTTPS configurado
- [ ] Backup configurado
- [ ] Monitoramento configurado (opcional)

## Troubleshooting

### Erro 502 Bad Gateway
- Verificar se o Gunicorn está rodando: `sudo systemctl status casamento`
- Verificar logs: `sudo journalctl -u casamento -f`

### Arquivos estáticos não carregam
- Executar: `python manage.py collectstatic`
- Verificar permissões da pasta static

### Webhook não funciona
- Verificar se a URL está acessível externamente
- Verificar se o token está correto
- Verificar logs do Django para erros

## Suporte

Para problemas específicos, abra uma issue no GitHub.
