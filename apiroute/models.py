from collections.abc import Iterable
from django.db import models
import hashlib
import random

# Create your models here.
class HashKey(models.Model):
    name = models.CharField(max_length=200)
    hash = models.CharField(max_length=200, blank=True, null=True, editable=False)

    def __str__(self) -> str:
        return self.hash
    
    def save(self, *args, **kwargs):
        number = random.random()
        mystr = f"{number}"
        mystr_encoded = mystr.encode('utf-8')
        self.hash = hashlib.sha256(mystr_encoded).hexdigest()
        return super().save( *args, **kwargs)