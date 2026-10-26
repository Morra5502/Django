from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    ROLE_CHOICES = (
        ("organizer", "Организатор"),
        ("participan", "Участник")
    )

    role = models.CharField(
        max_length= 20,
        choices= ROLE_CHOICES,
        default="participant"
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"

class Event(models.Model):
    EVENT_TYPE_CHOICES = (
        ('marathon', 'Марафон'),
        ('competition', 'Соревнование'),
        ('tournament', 'Турнир'),
        ('other', 'Другое'),
    )

    title = models.CharField(max_length= 20, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    date = models.DateTimeField(verbose_name="Дата и время")
    location = models.CharField(verbose_name="Место проведения")

    event_type = models.CharField(
        max_length=20, 
        choices=EVENT_TYPE_CHOICES, 
        default='other', 
        verbose_name='Тип мероприятия'
    )
    
    organizer = models.ForeignKey(
        # хз что это, вроде как динамическая ссылка на текущего пользователя без явной привязки к названию класса
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='organized_events',
        verbose_name='Организатор'
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['-date']

    def __str__(self):
        return self.title

class Registration(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Ожидает подтверждения'),
        ('confirmed', 'Подтверждено'),
        ('canceled', 'Отменено'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='registrations',
        verbose_name='Участник'
    )
    event = models.ForeignKey(
        Event, 
        on_delete=models.CASCADE, 
        related_name='registrations',
        verbose_name='Мероприятие'
    )
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='pending', 
        verbose_name='Статус'
    )
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрации'
        unique_together = ('user', 'event') 

    def __str__(self):
        return f"{self.user.username} на '{self.event.title}'"
  
class Result(models.Model):
    registration = models.OneToOneField(
        Registration, 
        on_delete=models.CASCADE, 
        related_name='result',
        verbose_name='Регистрация'
    )
    
    time_result = models.DateTimeField(
        max_length=50, 
        blank=True, 
        null=True, 
        verbose_name='Время (формат ЧЧ:ММ:СС)'
    )
    place = models.PositiveIntegerField(blank=True, null=True, verbose_name='Место')
    points = models.PositiveIntegerField(blank=True, null=True, verbose_name='Баллы')

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

    def __str__(self):
        return f"Результат {self.registration.user.username}: {self.place} место"