from django.shortcuts import render
from service.models import Category

def glavnaya(request):
    
    categories = Category.objects.filter(
        id__in = [1,2,3,4],
        is_visible=True
    )
    
    data = {
        
        # Герой (Hero) секция
        
        'hero_title': 'Ателье Atelier: Качество и срочность',
        'hero_subtitle': 'Ждем вас на улице Эльгера 35',
        'hero_scheduled':'Пн - Чт:	10:00 - 18:00',
        'hero_scheduled_holidays':'Пятница: 10:00 - 16:00',
        'hero_button_text': 'Посмотреть услуги',
        'hero_button_url': 'catalog',  # имя URL-маршрута
        
        
        # Преимущества
        'advantages': [
            {'icon': '🧵', 'title': 'Индивидуальный подход', 'description': 'Лекала строятся строго по вашим меркам'},
            {'icon': '✂️', 'title': 'Опыт 10+ лет', 'description': 'Мастера с многолетним стажем'},
            {'icon': '⏰', 'title': 'Точные сроки', 'description': 'Всегда сдаем работу вовремя'},
        ],
        'categories': categories
        
    }
    return render(request, 'main/index.html',data)
def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')
    
