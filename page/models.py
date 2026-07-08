from django.db import models

class User(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nom
    
class Article (models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    auteur = models.ForeignKey(User,on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.nom

    


