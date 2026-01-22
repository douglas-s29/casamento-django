"""
Comando para criar dados de exemplo para o sistema
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from apps.core.models import EventSettings
from apps.guests.models import Guest
from apps.gifts.models import Gift


class Command(BaseCommand):
    help = 'Cria dados de exemplo para demonstração do sistema'

    def handle(self, *args, **options):
        self.stdout.write('Criando dados de exemplo...\n')

        # Cria ou atualiza as configurações do evento
        event, created = EventSettings.objects.get_or_create(
            id=1,
            defaults={
                'nome_noivo': 'Douglas',
                'nome_noiva': 'Maria',
                'data_casamento': timezone.now() + timedelta(days=90),
                'local_nome': 'Igreja Nossa Senhora da Paz',
                'local_endereco': 'Rua das Flores, 123 - Centro - São Paulo/SP - CEP: 01234-567',
                'local_latitude': -23.550520,
                'local_longitude': -46.633308,
                'local_maps_url': 'https://maps.google.com/?q=-23.550520,-46.633308',
                'local_waze_url': 'https://waze.com/ul?ll=-23.550520,-46.633308',
                'mensagem_agradecimento': 'Muito obrigado pelo presente! Sua presença e carinho são muito especiais para nós. Mal podemos esperar para compartilhar este dia especial com você! ❤️',
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Configurações do evento criadas'))
        else:
            self.stdout.write(self.style.WARNING('⚠ Configurações do evento já existem'))

        # Cria convidados de exemplo
        guests_data = [
            {'nome': 'João Silva', 'email': 'joao@example.com', 'telefone': '(11) 98765-4321'},
            {'nome': 'Maria Santos', 'email': 'maria@example.com', 'telefone': '(11) 98765-4322'},
            {'nome': 'Pedro Oliveira', 'email': 'pedro@example.com', 'telefone': '(11) 98765-4323'},
            {'nome': 'Ana Costa', 'email': 'ana@example.com', 'telefone': '(11) 98765-4324'},
            {'nome': 'Carlos Ferreira', 'email': 'carlos@example.com', 'telefone': '(11) 98765-4325'},
        ]

        for guest_data in guests_data:
            guest, created = Guest.objects.get_or_create(
                email=guest_data['email'],
                defaults=guest_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Convidado criado: {guest.nome}'))

        # Cria presentes de exemplo
        gifts_data = [
            {
                'nome': 'Jogo de Panelas Tramontina',
                'descricao': 'Conjunto completo de panelas antiaderentes com tampas de vidro, 5 peças.',
                'valor': 299.90,
                'quantidade_total': 5,
            },
            {
                'nome': 'Jogo de Cama Casal Premium',
                'descricao': 'Jogo de cama 4 peças, 100% algodão, 300 fios, queen size.',
                'valor': 189.90,
                'quantidade_total': 8,
            },
            {
                'nome': 'Processador de Alimentos',
                'descricao': 'Processador multifuncional com 12 velocidades e múltiplos acessórios.',
                'valor': 349.90,
                'quantidade_total': 3,
            },
            {
                'nome': 'Aspirador de Pó Robô',
                'descricao': 'Aspirador robô inteligente com conexão WiFi e recarga automática.',
                'valor': 899.90,
                'quantidade_total': 2,
            },
            {
                'nome': 'Cafeteira Expresso Nespresso',
                'descricao': 'Cafeteira expresso com sistema de cápsulas, 19 bar de pressão.',
                'valor': 599.90,
                'quantidade_total': 4,
            },
            {
                'nome': 'Mixer Oster',
                'descricao': 'Mixer de mão com 5 velocidades, inclui copo medidor e batedor.',
                'valor': 129.90,
                'quantidade_total': 10,
            },
            {
                'nome': 'Sanduicheira Grill',
                'descricao': 'Sanduicheira e grill 2 em 1 com placas antiaderentes removíveis.',
                'valor': 159.90,
                'quantidade_total': 6,
            },
            {
                'nome': 'Conjunto de Taças de Vinho',
                'descricao': 'Kit com 6 taças de cristal para vinho tinto e branco.',
                'valor': 149.90,
                'quantidade_total': 8,
            },
            {
                'nome': 'Edredom Queen Size',
                'descricao': 'Edredom dupla face, hipoalergênico, queen size, várias cores.',
                'valor': 249.90,
                'quantidade_total': 5,
            },
            {
                'nome': 'Toalhas de Banho Premium',
                'descricao': 'Conjunto 4 toalhas de banho 100% algodão, extra macias.',
                'valor': 179.90,
                'quantidade_total': 10,
            },
        ]

        for gift_data in gifts_data:
            gift, created = Gift.objects.get_or_create(
                nome=gift_data['nome'],
                defaults=gift_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Presente criado: {gift.nome}'))

        self.stdout.write(self.style.SUCCESS('\n✅ Dados de exemplo criados com sucesso!'))
        self.stdout.write('\nPróximos passos:')
        self.stdout.write('1. Crie um superusuário: python manage.py createsuperuser')
        self.stdout.write('2. Execute o servidor: python manage.py runserver')
        self.stdout.write('3. Acesse o admin: http://localhost:8000/admin/')
        self.stdout.write('4. Acesse o site: http://localhost:8000/')
