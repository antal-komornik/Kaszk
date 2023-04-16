from django.db import models

groups = [
    ("KAC", 'KAC'),
    ("GTSZK", 'GTSZK'),
    ("PKSZK", 'PKSZK'),
    ("MSZK", 'MSZK')
]


class News(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    group = models.CharField(choices=groups, max_length=50)
    
    def __str__(self):
        return f"{self.group}-{self.title}-{self.date}"