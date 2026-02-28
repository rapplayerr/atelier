from django.shortcuts import render
from service.utils import get_chosen_categories

def glavnaya(request):
    chosen_categories = get_chosen_categories(3)
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
        
    }
    return render(request, 'main/index.html',data)
def about(request):
    return render(request, 'main/about.html')
    
