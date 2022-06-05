from django.db import models
from datetime import datetime
from Core.models import User
from .modelchoices import category_choices, state_choices
# Create your models here.
class Listing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100, choices=category_choices)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, choices=state_choices)
    cep = models.CharField(max_length=20,null=True)
    descricao = models.TextField(blank=True)
    preco = models.IntegerField()
    total_rating = models.IntegerField(null=True)
    no_of_rating = models.IntegerField(null=True)
    foto_1 = models.FileField(upload_to="media/%Y/%m/%d/", blank=True)
    foto_2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    foto_3 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.titulo
    
    