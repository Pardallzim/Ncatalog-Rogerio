from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Roupa (models.Model):
    name = models.CharField(max_length=240)
    descript = models.TextField()
    path = models.ImageField(upload_to="imagens/")

class Curtida(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(
        Roupa,
        through="Comentario",
        through_fields=("curtida", "roupa"),
    )

class Comentario(models.Model):
    curtida = models.ForeignKey(Curtida, on_delete=models.CASCADE)
    roupa = models.ForeignKey(Roupa, on_delete=models.CASCADE)
    conteudo = models.TextField()