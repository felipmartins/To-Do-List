from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    status_list = [
        (0, "Pendente"),
        (1, "Em andamento"),
        (2, "Finalizado")
    ]

    title = models.CharField(max_length=150, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=status_list, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f"""{self.title} -
                    Criada em {str(self.created_at)[0:19]} - 
                    Por {self.user.username} - 
                    Atualizada a última vez em {str(self.updated_at)[0:19]}""")
