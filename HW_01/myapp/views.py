from django.http import HttpResponse
import logging

# Настройка логирования
logger = logging.getLogger(__name__)

def home(request):
    logger.info('Страница "Главная" была посещена')
    html = """
    <html>
    <body>
    <h1>Добро пожаловать на мой первый сайт на Django!</h1>
    <p>Это главная страница.</p>
    </body>
    </html>
    """
    return HttpResponse(html)

def about(request):
    logger.info('Страница "О себе" была посещена')
    html = """
    <html>
    <body>
    <h1>О себе</h1>
    <p>Вот краткая информация обо мне...</p>
    </body>
    </html>
    """
    return HttpResponse(html)
