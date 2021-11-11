from django.db import models
# from django.contrib.postgres.fields import ArrayField

class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __str__(self):
        return  str(self.id)+". "+str(self.tag)

class Quote(models.Model):
    frase = models.TextField()
    autor = models.CharField(max_length=150)
    tags = models.ManyToManyField('Tag', related_name='quotes',blank=True)

    def __str__(self):
        return  str(self.id)+". "+str(self.autor)
