from django.core.management.base import BaseCommand
from django.utils.text import slugify
from service.models import Category, Service
from service.services_data import SERVICES_DATA

class Command(BaseCommand):
    help = 'Импортирует категории и услуги из services_data.py в базу данных'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Очистить существующие категории и услуги перед импортом',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🚀 Начинаю импорт услуг...'))
        
        if options['clear']:
            self.clear_database()
        
        categories_created = 0
        categories_updated = 0
        services_created = 0
        services_updated = 0
        
        for slug, category_data in SERVICES_DATA.items():
            # Создаем или обновляем категорию
            category, created = Category.objects.update_or_create(
                slug=slug,
                defaults={
                    'name': category_data['name'],
                    'description': category_data.get('description', ''),
                    'order': 0,
                    'is_visible': True,
                }
            )
            
            if created:
                categories_created += 1
                self.stdout.write(f'  ✅ Создана категория: {category.name}')
            else:
                categories_updated += 1
                self.stdout.write(f'  🔄 Обновлена категория: {category.name}')
            
            # Создаем услуги для этой категории
            for service_name, price in category_data['services'].items():
                # Пытаемся найти услугу по названию и категории
                try:
                    service = Service.objects.get(category=category, name=service_name)
                    # Обновляем существующую услугу
                    service.price = price
                    service.slug = self.generate_unique_slug(category, service_name)
                    service.save()
                    services_updated += 1
                except Service.DoesNotExist:
                    # Создаем новую услугу
                    service = Service.objects.create(
                        category=category,
                        name=service_name,
                        slug=self.generate_unique_slug(category, service_name),
                        price=price,
                        description='',
                        order=0,
                        is_visible=True
                    )
                    services_created += 1
        
        self.stdout.write(self.style.SUCCESS('\n📊 Итоги импорта:'))
        self.stdout.write(f'  Категории: создано {categories_created}, обновлено {categories_updated}')
        self.stdout.write(f'  Услуги: создано {services_created}, обновлено {services_updated}')
        self.stdout.write(self.style.SUCCESS('✅ Импорт успешно завершен!'))
    
    def generate_unique_slug(self, category, name):
        """Генерирует уникальный slug для услуги в категории"""
        base_slug = slugify(name)[:50]
        slug = base_slug
        counter = 1
        
        # Проверяем, есть ли уже услуга с таким slug в этой категории
        while Service.objects.filter(category=category, slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
            if counter > 100:
                slug = f"{base_slug}-{counter}"
                break
        
        return slug
    
    def clear_database(self):
        """Очищает базу данных перед импортом"""
        self.stdout.write(self.style.WARNING('🧹 Очистка базы данных...'))
        Service.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('  ✅ База данных очищена'))