from django.db.models import (
    Model, CharField, ForeignKey, ImageField, BooleanField, CASCADE)


class Owner(Model):
    name = CharField(max_length=50, default='', null=False)
    last_name = CharField(max_length=50, default='', null=False)
    rut = CharField(max_length=30, default='', null=False)


class Auto(Model):
    patente = CharField(max_length=50, default='', null=False)
    owner = ForeignKey(Owner, on_delete=CASCADE)
    picture = ImageField(blank=True, null=True)
    is_rented = BooleanField(default=False)
