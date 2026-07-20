"""
Django settings for cv_project.
پروژه میان‌دوره: وبسایت رزومه (CV) با جنگو
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ⚠️ برای محیط پروداکشن حتما این مقدار را تغییر بده و مخفی نگه دار
SECRET_KEY = 'django-insecure-change-this-key-before-deploy-!!!'

# در حالت توسعه True، قبل از دیپلوی حتما False کن
DEBUG = True

ALLOWED_HOSTS = ['*']  # برای دیپلوی، دامنه/آی‌پی واقعی خودت رو جایگزین کن

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'resume',  # اپلیکیشن رزومه
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cv_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'cv_project.wsgi.application'

# دیتابیس: پیش‌فرض SQLite (برای تمرین کافیه، برای پروداکشن می‌تونی Postgres بذاری)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'fa-ir'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
# فایل استاتیک داخل resume/static/ قرار داره و به‌صورت خودکار توسط
# AppDirectoriesFinder پیدا می‌شه، پس نیازی به STATICFILES_DIRS نیست.
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
