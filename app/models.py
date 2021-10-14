from django.db import models


class Topic(models.Model):
    """
    Topic Model to be used as a tagging system
    for Document and Folder Models
    """
    name = models.CharField(max_length=50)
    short_desc = models.CharField(max_length=150,
                                  verbose_name='short description')
    long_desc = models.TextField(verbose_name='long description')

    def __str__(self):
        return self.name


class Folder(models.Model):
    """
    Represents a Folder that contains Documents and can be tagged with Topics
    """
    topic = models.ManyToManyField('Topic')
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Document(models.Model):
    """
    Documents that can be tagged with Topics and related to/stored in a Folder
    """
    topic = models.ManyToManyField('Topic')
    folder = models.ForeignKey('Folder', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Document title')
    raw_text = models.TextField(verbose_name='Document body')
    file = models.FileField(upload_to='documents/',
                            verbose_name='Document upload',
                            null=True, blank=True, unique=True)

    def __str__(self):
        return self.title
