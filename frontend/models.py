from django.db import models

# Create your models here.


class Client(models.Model):
    name=models.CharField(null=True,blank=True,max_length=100,unique=True)
    email=models.EmailField(null=True,blank=True)
    message=models.TextField(null=True,blank=True,max_length=50000)


    def __str__(self):
        return f'message from {self.email}'
    


# class ClientExtended(models.Model):

#     user=models.OneToOneField(Client,null=True,blank=True,to_field='name',on_delete=models.CASCADE)
  


#     def __str__(self):
#         return f'message from {self.user}'
    