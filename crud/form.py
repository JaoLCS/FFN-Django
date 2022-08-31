from .models import tema, noticia
from django.forms import ModelForm

class TemaForm(ModelForm):
    class Meta:
        model = tema
        fields = ["tema"]
    
class NoticiaForm(ModelForm):
    class Meta:
        model = noticia
        fields = ["titulo", "data" , "confiabilidade" , "not_tem_codigo"]