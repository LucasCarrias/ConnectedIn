from django.db import models

# Create your models here.
class Enquete(models.Model):
    texto = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto
    