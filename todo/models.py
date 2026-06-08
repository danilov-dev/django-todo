from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Наименование")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания дела")
    due_date = models.DateTimeField(verbose_name="Дата выполнения дела")
    note = models.TextField(blank=True, null=True, verbose_name="Примечание")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', verbose_name="Пользователь")

    class Meta:
        verbose_name = "Дело"
        verbose_name_plural = "Дела"
        ordering = ['-due_date']

    def __str__(self):
        return self.title