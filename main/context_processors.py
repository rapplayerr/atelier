def base_context(request):
    data = {
        'tailor_shop': 'Atelier',
        'current_year': 2026,
        

        
        # Контакты
        'contact_info': {
            'address': 'ул. Тверская, д. 15, офис 5',
            'metro': 'м. Тверская / Пушкинская',
            'phone': '+7 (123) 456-78-90',
            'email': 'info@atelier.ru',
            'work_hours': 'Ежедневно с 10:00 до 20:00',
        },
        
        # Социальные сети
        'social_links': [
            {'name': 'Instagram', 'icon': '📷', 'url': 'https://instagram.com/atelier'},
            {'name': 'Telegram', 'icon': '✈️', 'url': 'https://t.me/atelier'},
            {'name': 'VK', 'icon': '📘', 'url': 'https://vk.com/atelier'},
        ],
        
        # Мета-теги для SEO
        'meta_description': 'Ателье в Москве: индивидуальный пошив, ремонт и реставрация одежды. Опытные мастера, качественные материалы.',
        'meta_keywords': 'ателье, пошив одежды, ремонт одежды, реставрация, Москва',
    }
    return data