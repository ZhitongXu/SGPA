"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'network',
    'users.apps.UsersConfig',
    'crispy_forms',
    'sgpa',
    'ball',
    'likes',
    'import_export',
)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
            'libraries': {
                "likes_tags":"likes.templatetags.likes_tags",
            },
        },
    },
]

WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



TYPE_CHOICES = (
    ('硕博连读', '硕博连读'),
    ('直博', '直博'),
    ('专硕', '专硕'),
)

FIELD_CHOICES = (
    ('数据科学', '数据科学'),
    ('数理统计', '数理统计'),
    ('经济社会统计', '经济社会统计'),
    ('风险管理与精算', '风险管理与精算'),
    ('生物卫生医学统计', '生物卫生医学统计'),
)

COURSE_CHOICES = (
    ('非参数统计', '非参数统计'),
    ('多元统计分析', '多元统计分析'),
    ('时间序列分析', '时间序列分析'),
    ('试验设计', '试验设计'),
    ('数据挖掘', '数据挖掘'),
    ('机器学习', '机器学习'),
    ('应用随机过程', '应用随机过程'),
    ('保险精算', '保险精算'),
    ('统计计算', '统计计算'),
    ('不完全数据分析', '不完全数据分析'),
    ('生存分析与可靠性', '生存分析与可靠性'),
    ('纵向数据分析', '纵向数据分析'),
    ('金融学', '金融学'),
    ('管理学', '管理学'),
    ('质量控制', '质量控制'),
    ('统计学原理', '统计学原理'),
    ('微观经济学', '微观经济学'),
    ('宏观经济学', '宏观经济学'),
    ('计量经济学', '计量经济学'),
    ('风险理论', '风险理论'),
    ('国民经济统计学', '国民经济统计学'),
    ('社会统计学', '社会统计学'),
    ('金融统计分析', '金融统计分析'),
    ('市场调查与分析', '市场调查与分析'),
)


ASSESS_CHOICES = (
    (5, '完全掌握'),
    (4, '熟练'),
    (3, '良好'),
    (1, '一般'),
    (-5, '几乎为零'),
)


POJ_CHOICES = (
    ('参与老师的项目', '参与老师的项目'),
    ('大创或小创', '大创或小创'),
    ('老师指导论文', '老师指导论文'),
    ('海外交流一年及以上', '海外交流一年及以上'),
    ('夏令营30天及以上', '夏令营30天及以上'),
)

GOAL_CHOICES = (
    (1, '完成硕士生基本要求拿到学位'),
    (2, '在完成硕士生基本要求拿到学位的基础上在导师指导下完成一篇高质量的硕士论文，并获得老师的认可'),
    (3, '在前两个目标的基础上，为获得国内一流大学博士学位做好准备，打好基础'),
    (4, '在前两个目标的基础上，为获得国际一流大学博士学位做好准备，打好基础'),
)

KEYWORD_CHOICES = (
    ('level1', 'level1'),
    ('level21', 'level21'),
    ('model selection', 'model selection'),
    ('machine learning', 'machine learning'),
    ('theoretic statistics', 'theoretic statistics'),
    ('bayesian inference', 'bayesian inference'),
    ('bio statistics', 'bio statistics'),
    ('mm', 'mm'),
    ('level23', 'level23'),
    ('level3', 'level3')
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

#CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


LOGIN_REDIRECT_URL = 'network-home'
LOGIN_URL = 'login'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'RSSKnowledgeGraph@163.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'RSSKnowledgeGraph@163.com' #这一项一定需要添加
EMAIL_FROM = 'SGPA official<RSSKnowledgeGraph@163.com>' #可加可不加
#EMAIL_USE_TLS = False
#
#EMAIL_FROM = 'SGPA official<RSSKnowledgeGraph@163.com>'
