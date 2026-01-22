"""
Serviço para integração com a API do Asaas
"""
import requests
from django.conf import settings
from decimal import Decimal


class AsaasService:
    """Classe para integração com a API do Asaas"""
    
    def __init__(self):
        self.api_key = settings.ASAAS_API_KEY
        self.api_url = settings.ASAAS_API_URL
        self.headers = {
            'access_token': self.api_key,
            'Content-Type': 'application/json'
        }
    
    def create_payment(self, customer_data, payment_data):
        """
        Cria um pagamento no Asaas
        
        Args:
            customer_data: Dados do cliente (nome, email, cpfCnpj, etc)
            payment_data: Dados do pagamento (valor, billingType, dueDate, etc)
        
        Returns:
            dict: Resposta da API do Asaas
        """
        # Primeiro, cria ou recupera o cliente
        customer = self._get_or_create_customer(customer_data)
        
        if not customer:
            return {'error': 'Erro ao criar/recuperar cliente'}
        
        # Cria o pagamento
        payment_data['customer'] = customer['id']
        
        try:
            response = requests.post(
                f'{self.api_url}/payments',
                headers=self.headers,
                json=payment_data,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}
    
    def _get_or_create_customer(self, customer_data):
        """
        Busca ou cria um cliente no Asaas
        
        Args:
            customer_data: Dados do cliente
        
        Returns:
            dict: Dados do cliente
        """
        # Busca cliente por email
        try:
            response = requests.get(
                f'{self.api_url}/customers',
                headers=self.headers,
                params={'email': customer_data.get('email')},
                timeout=30
            )
            response.raise_for_status()
            data = response.json()
            
            if data.get('data') and len(data['data']) > 0:
                return data['data'][0]
            
            # Se não encontrou, cria um novo
            return self._create_customer(customer_data)
        except requests.exceptions.RequestException:
            return self._create_customer(customer_data)
    
    def _create_customer(self, customer_data):
        """
        Cria um novo cliente no Asaas
        
        Args:
            customer_data: Dados do cliente
        
        Returns:
            dict: Dados do cliente criado
        """
        try:
            response = requests.post(
                f'{self.api_url}/customers',
                headers=self.headers,
                json=customer_data,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return None
    
    def get_payment(self, payment_id):
        """
        Recupera informações de um pagamento
        
        Args:
            payment_id: ID do pagamento no Asaas
        
        Returns:
            dict: Dados do pagamento
        """
        try:
            response = requests.get(
                f'{self.api_url}/payments/{payment_id}',
                headers=self.headers,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}
    
    def get_pix_qrcode(self, payment_id):
        """
        Recupera o QR Code PIX de um pagamento
        
        Args:
            payment_id: ID do pagamento no Asaas
        
        Returns:
            dict: Dados do QR Code PIX
        """
        try:
            response = requests.get(
                f'{self.api_url}/payments/{payment_id}/pixQrCode',
                headers=self.headers,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}
