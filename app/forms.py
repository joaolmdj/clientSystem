from django.forms import ModelForm
from app.models import Pedidos


# Create the form class.
class PedidosForm(ModelForm):
    class Meta:
        model = Pedidos
        fields = ['nome', 'preco', 'multiplo']
