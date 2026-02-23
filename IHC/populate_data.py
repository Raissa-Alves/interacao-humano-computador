import os
import django
from datetime import time, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from noponto.models import Onibus, Linha, Rota, Horario

def populate():
    print("Populating database...")
    
    # Create Bus
    b1, _ = Onibus.objects.get_or_create(
        modelo="Mercedes-Benz O500",
        placa="ABC-1234",
        numero_veiculo=101,
        capacidade_total=44,
        ano=2023,
        acessibilidade=True
    )
    
    # Create Line
    l1, _ = Linha.objects.get_or_create(
        codigo="EXP01",
        nome="Expresso Litoral",
        origem="Santos",
        destino="São Paulo",
        tarifa=45.50
    )
    
    l2, _ = Linha.objects.get_or_create(
        codigo="EXP02",
        nome="Linha Serrana",
        origem="Curitiba",
        destino="Florianópolis",
        tarifa=89.90
    )
    
    # Create Route
    r1, _ = Rota.objects.get_or_create(
        sentido="Ida",
        distancia=80.0,
        tempo=timedelta(hours=1, minutes=30),
        linha=l1
    )
    
    # Create Schedule
    Horario.objects.get_or_create(
        horario_saida=time(8, 0),
        horario_chegada=time(9, 30),
        dia_semana="Segunda",
        linha=l1,
        rota=r1,
        onibus=b1
    )
    
    Horario.objects.get_or_create(
        horario_saida=time(14, 0),
        horario_chegada=time(15, 30),
        dia_semana="Segunda",
        linha=l1,
        rota=r1,
        onibus=b1
    )

    print("Database populated successfully!")

if __name__ == "__main__":
    populate()
