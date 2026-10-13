from saleor.account.models import Address
from saleor.channel.models import Channel
from saleor.warehouse.models import Warehouse
from saleor.shipping.models import ShippingZone

# 1. Crear Canal oficial Colombia (Moneda: COP)
channel, created = Channel.objects.get_or_create(
    slug="canal-colombia",
    defaults={
        "name": "Colombia (COP)",
        "currency_code": "COP",
        "default_country": "CO",
        "is_active": True,
    }
)
if not created:
    channel.name = "Colombia (COP)"
    channel.currency_code = "COP"
    channel.default_country = "CO"
    channel.is_active = True
    channel.save()
print(f"Canal configurado: {channel.name} con moneda {channel.currency_code}")

# 2. Crear Dirección para el Almacén
address, _ = Address.objects.get_or_create(
    company_name="Almacén Principal",
    defaults={
        "country": "CO",
        "city": "Bogotá",
        "street_address_1": "Sede Principal",
    }
)

# 3. Crear Almacén Principal
warehouse, _ = Warehouse.objects.get_or_create(
    slug="almacen-principal",
    defaults={
        "name": "Almacén Principal",
        "email": "admin@example.com",
        "address": address,
    }
)
warehouse.address = address
warehouse.save()
warehouse.channels.add(channel)
print("Almacén Principal vinculado al canal")

# 4. Crear Zona de Envío para Colombia
shipping_zone, _ = ShippingZone.objects.get_or_create(
    name="Envíos Nacionales Colombia",
    defaults={
        "countries": ["CO"],
        "default": True,
    }
)
shipping_zone.countries = ["CO"]
shipping_zone.save()
shipping_zone.channels.add(channel)
shipping_zone.warehouses.add(warehouse)
print("Zona de envío configurada para Colombia")

print("INICIALIZACIÓN COMPLETADA: Base de datos limpia lista.")
