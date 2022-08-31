from django.db import models

# Create your models here.
class tema(models.Model): 
    tema = models.CharField(max_length = 45)

class noticia(models.Model):
    titulo = models.CharField(max_length = 150)
    data = models.DateField()
    confiabilidade = models.DecimalField(max_digits=4, decimal_places=2)
    not_tem_codigo = models.ForeignKey(tema, default= None, on_delete= models.CASCADE)