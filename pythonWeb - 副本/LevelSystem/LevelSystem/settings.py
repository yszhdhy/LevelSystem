"""
Django settings for LevelSystem project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cv%)*q1u^f^er=3ct@9s%&#=*utis_o1df)=#y^fsp1x0j+&7i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# settings.py

"""
百度API
"""
# top_num: 返回的分类数量，不声明的话默认为 6 个
BAIDU_PARAMS = 6
# 否则，留空 ACCESS_TOKEN，于下方填入该模型部署的 API_KEY 以及 SECRET_KEY，会自动申请并显示新 ACCESS_TOKEN
BAIDU_API_KEY = "Hp2wrypKRnzZT3yMOCuVZdgO"
BAIDU_SECRET_KEY = "3ykTkyHDo1RUVKFbaGhWPFpSbhU7qC9G"
# 服务详情中的接口地址
BAIDU_MODEL_API_URL = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/segmentation/shuipingyiV3"

BAIDU_TOKEN_URL = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials"



"""
minio 配置
"""
MINIO_ACCESS_KEY = 'minio@admin'
MINIO_SECRET_KEY = 'minio@admin'
MINIO_ENDPOINT = '110.238.119.179:9000'
MINIO_BUCKET_NAME = 'levelsystem'  # 存储桶
MINIO_SECURE = False  # Set to False if you are using HTTP instead of HTTPS
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 文件大小限制

"""
cap摄像机全局变量 
"""
CAP = None
CAP_NUMBER = 0  # 摄像头，外接摄像头  1 为电脑摄像头


"""
跨域设置
"""
ALLOWED_HOSTS = ['*']


"""
jsonutil 文件配置
"""
JSON_FILE_PATH = "LevelApp/static/json/Atlas.json"
JSON_COUNT = "atlas"


"""
paddlepaddle  离线模型
"""
INTERFACE_ADDRESS = 'http://10.13.169.245:12138/img_prediction'



"""
误差计算
"""
DISPLACEMENTS = 'displacements'
LEVEL_LENGTH = 150  # 水平仪长度



"""
utils.py
"""
MEDIA_ROOT = "./"


# 定义全局变量 websocket_channels
WEBSOCKET_CHANNELS = set()


CORS_ALLOW_ALL_ORIGINS = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'LevelApp.apps.LevelappConfig',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'LevelApp.middleware.MyCustomExceptionMiddleware',
]

ROOT_URLCONF = 'LevelSystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LevelSystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
