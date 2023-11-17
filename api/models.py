from django.db import models


class Token(models.Models):
    id = models.AutoField(primary_key=True)  #- primary key
    unique_hash = models.CharField(max_length=64, unique=True, null=True) #- уникальный хэш
    tx_hash = models.TextField(max_length=255)  #- хэш транзакции создания токена
    media_url = models.TextField(null=True)  #- урл с произвольным изображением
    owner = models.TextField(null=True)  #- адрес пользователя в сети Ethereum
