from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone
from django.urls import reverse


class Ad(models.Model):
    objects = None
    Tanks = 'TN'
    Healers = 'HL'
    DD = 'DD'
    Merchants = 'ME'
    GuildMasters = 'GM'
    QuestGivers = 'QG'
    Blacksmiths = 'BS'
    Tanners = 'TS'
    PotionMakers = 'PM'
    SpellMasters = 'SM'

    CATEGORIES = [
        (Tanks, 'Танки'),
        (DD, 'ДД'),
        (Healers, 'Хиллы'),
        (Merchants, 'Торговцы'),
        (GuildMasters, 'Гилдмастера'),
        (QuestGivers, 'Квестгиверы'),
        (Blacksmiths, 'Кузнецы'),
        (Tanners, 'Кожевники'),
        (PotionMakers, 'Зельевары'),
        (SpellMasters, 'Мастера заклинаний'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    categories = models.CharField(max_length=2, choices=CATEGORIES)
    description = models.TextField()
    price = models.FloatField(default=0)
    file = models.ImageField(upload_to='media/', null=True, blank=True)
    created_at = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return f'{self.title}: {self.description}: {self.price}: {self.categories}: {self.author}'

    def get_absolute_url(self):
        return reverse('ad', args=[str(self.pk)])


class Reply(models.Model):
    objects = None
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Ad, related_name='reply', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    reply_text = models.TextField()
    accept = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('r_update', args=[str(self.pk)])

    def __str__(self):
        return f'{self.reply_text}: {self.author}: {self.data}'
