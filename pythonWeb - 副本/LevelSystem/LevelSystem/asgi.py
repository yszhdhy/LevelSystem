"""
ASGI config for LevelSystem project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LevelSystem.settings')
# 配置 settings 模块
django.setup()

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from LevelApp.consumers import DemoConsumer

# application = get_asgi_application()

django_asgi_application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': django_asgi_application,  # 处理HTTP请求的Django应用程序
    'websocket': URLRouter([  # 处理WebSocket连接的路由
        path('ws/demo/', DemoConsumer.as_asgi()),
    ]),
})
