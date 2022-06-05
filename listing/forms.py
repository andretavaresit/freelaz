from django.forms import ModelForm
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['titulo', 'categoria', 'endereco', 'cidade', 'estado', 'cep', 'descricao', 'preco', 'foto_1', 'foto_2', 'foto_3']
    
class UpdateForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['titulo','descricao','preco','foto_1']