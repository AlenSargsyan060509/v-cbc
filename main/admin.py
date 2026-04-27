from django.contrib import admin
from .models import Movie, Character, ExtraInfo, Screenshot

# Настройка вложенного интерфейса для персонажей
class CharacterInline(admin.TabularInline):
    model = Character
    extra = 1

# Настройка вложенного интерфейса для доп. инфо (миссии, сюжет)
class ExtraInfoInline(admin.StackedInline):
    model = ExtraInfo
    extra = 1

# Настройка вложенного интерфейса для скриншотов
class ScreenshotInline(admin.TabularInline):
    model = Screenshot
    extra = 3

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # Что отображать в списке всех проектов
    list_display = ('title', 'category', 'status', 'rating', 'created_at')
    
    # Фильтры справа
    list_filter = ('category', 'status')
    
    # Поиск по названию
    search_fields = ('title',)
    
    # Подключаем все созданные инлайны
    inlines = [ExtraInfoInline, CharacterInline, ScreenshotInline]

# Опционально: регистрация остальных моделей отдельно, 
# чтобы их можно было править не только внутри фильма
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'movie')
    list_filter = ('movie',)

@admin.register(Screenshot)
class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ('movie', 'caption')