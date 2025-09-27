from pathlib import Path
import os
import environ

# -------------------------
# 基础路径
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# 环境变量
# -------------------------
env = environ.Env(
    DEBUG=(bool, True)
)
# 可以放一个 .env 文件存放 SECRET_KEY、DB 密码
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# -------------------------
# 安全配置
# -------------------------
SECRET_KEY = env('SECRET_KEY', default='django-insecure-placeholder')
DEBUG = env('DEBUG', default=True)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['127.0.0.1','localhost'])

# -------------------------
# 应用
# -------------------------
INSTALLED_APPS = [
    # Django 默认
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 第三方
    'rest_framework',
    'django_filters',
    'corsheaders',
    'crispy_bootstrap5',
    'crispy_forms',

    # 自建 app
    'accounts',
    'student',
    'club',
    'forum',
    'adminsys',
    'ocr',
    'ai',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# -------------------------
# 中间件
# -------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '社团系统.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 全局模板目录
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

WSGI_APPLICATION = '社团系统.wsgi.application'

# -------------------------
# 数据库配置（MySQL）
# -------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME', default='community_forum'),  # 数据库名，先建好再改
        'USER': env('DB_USER', default='root'),
        'PASSWORD': env('DB_PASSWORD', default='828388'),
        'HOST': env('DB_HOST', default='127.0.0.1'),
        'PORT': env('DB_PORT', default=3306),
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# -------------------------
# 自定义用户模型
# -------------------------
AUTH_USER_MODEL = 'accounts.User'  # 自定义 User 模型，放在 accounts/models.py

# -------------------------
# 密码验证
# -------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,  # 这里设置你想要的最小密码长度，例如 6 位
        }
    },
]

# -------------------------
# 国际化
# -------------------------
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_TZ = True

# -------------------------
# 静态 & 媒体文件
# -------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -------------------------
# 默认主键类型
# -------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------
# Django REST Framework 默认配置
# -------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# -------------------------
# CORS（前端跨域支持）
# -------------------------
CORS_ALLOW_ALL_ORIGINS = True  # 开发阶段允许全部，生产可改为白名单
