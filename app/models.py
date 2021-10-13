from django.db import models


class Topic(models.Model):
    ''' Topic Model to be used as a tagging system for both Document and Folder Models'''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Folder(models.Model):
    topic = models.ManyToManyField('Topic')
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Document(models.Model):
    topic = models.ManyToManyField('Topic')
    folder = models.ForeignKey('Folder', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} inside folder {self.folder}'

