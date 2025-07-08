from pathlib import Path
from decouple import config

OPENAI_API_KEY = config("OPENAI_API_KEY")


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-jx9^m+1r8la66f*79)2_d1om-lzdh-z(&e=eqk7$$tr#c$qjk@"
DEBUG = True
ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'widget_tweaks',
    
    "home",
    "blog",
    "planner",
    "todo",
    "habit",
    "diary",
    "workout",
    "timetable",
    "account",
    "study",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "universe.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",  
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "universe.wsgi.application"

# SQLite DB 설정 
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# 비밀번호 검증
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

#한국 기준 (
LANGUAGE_CODE = "ko-kr"      # 언어: 한국어
TIME_ZONE = "Asia/Seoul"     # 시간대: 한국식간

USE_I18N = True              # 국제화 사용
USE_TZ = False               #  한국 시간으로  False로 설정


# 정적/미디어 파일 설정
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# 기본 AutoField
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 커스텀 유저 모델 사용
AUTH_USER_MODEL = "account.User"

# 로그인경로 설정
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
