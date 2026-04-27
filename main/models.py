from django.db import models

class Movie(models.Model):
    CATEGORY_CHOICES = [
        ('movie', 'Фильм'),
        ('series', 'Сериал'),
        ('game', 'Игра'),
    ]
    
    STATUS_CHOICES = [
        ('planned', 'В планах'),
        ('watching', 'В процессе'),
        ('completed', 'Завершено/Пройдено'),
    ]

    title = models.CharField("Название", max_length=200)
    category = models.CharField("Категория", max_length=10, choices=CATEGORY_CHOICES, default='movie')
    poster = models.ImageField("Постер", upload_to='movies/')
    description = models.TextField("Описание")
    
    # Твои личные метки
    rating = models.PositiveIntegerField("Твоя оценка (1-10)", default=0, help_text="Укажи число от 1 до 10")
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default='planned')
    verdict = models.TextField("Твой личный вердикт", blank=True, help_text="Краткий итог: стоит ли оно того?")
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"


class Character(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='characters', verbose_name="Проект")
    name = models.CharField("Имя героя", max_length=100)
    photo = models.ImageField("Фото героя", upload_to='characters/', blank=True)
    description = models.TextField("Описание героя")

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"

    def __str__(self):
        return f"{self.name} ({self.movie.title})"


class ExtraInfo(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='extras', verbose_name="Проект")
    title = models.CharField("Заголовок (н-р: Сюжет или Миссии)", max_length=200)
    content = models.TextField("Содержание")
    order = models.PositiveIntegerField("Порядок отображения", default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Доп. информация"
        verbose_name_plural = "Доп. информация"

    def __str__(self):
        return f"{self.title} — {self.movie.title}"


class Screenshot(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='screenshots', verbose_name="Проект")
    image = models.ImageField("Скриншот", upload_to='screenshots/')
    caption = models.CharField("Подпись (необязательно)", max_length=100, blank=True)

    class Meta:
        verbose_name = "Скриншот"
        verbose_name_plural = "Скриншоты"

    def __str__(self):
        return f"Скриншот для {self.movie.title}"