import os
import django
from django.conf import settings
from django.contrib.auth.models import User

# Definir o módulo de configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')  # Substitua 'mysite.settings' pelo caminho correto do seu arquivo de configurações

# Configurar o Django
django.setup()

# Detalhes do superusuário
username = 'scaetano'
email = 'sergioadrianomc@gmail.com'
password = 'WemyZul2014'

# Verificar se o superusuário já existe e criar se não existir
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print('Superusuário criado com sucesso!')
else:
    print('O superusuário já existe.')

