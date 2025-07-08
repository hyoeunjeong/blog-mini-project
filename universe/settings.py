from pathlib import Path
from decouple import config

OPENAI_API_KEY = config("OPENAI_API_KEY")


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-jx9^m+1r8la66f*79)2_d1om-lzdh-z(&e=eqk7$$tr#c$qjk@"
DEBUG = True
ALLOWED_HOSTS = ["*"]

# 앱 구성
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 로컬 앱들
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
        "DIRS": [BASE_DIR / "templates"],  # 공통 템플릿 경로
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",  # 로그인 상태 등 확인 가능
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "universe.wsgi.application"

# SQLite DB 설정 (개발용)
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

# ✅ 전세계 기준 (국제화 설정)
LANGUAGE_CODE = "ko-kr"  # 언어: 영어
TIME_ZONE = "UTC"  # 시간대: 국제 표준
USE_I18N = True
USE_TZ = True  # UTC 기준 저장

# 정적/미디어 파일 설정
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# 기본 AutoField
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ✅ 커스텀 유저 모델 사용
AUTH_USER_MODEL = "account.User"

# ✅ 로그인 관련 경로 설정
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
