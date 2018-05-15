DEBUG = True

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'shop',
            'USER': 'django',
            'PASSWORD': 'djangopwd',
            'HOST': 'localhost',
            'PORT': 3306
        }
    }
    REDIS = {
        'HOST': 'localhost',
        'PORT': '6379',
        'USER': None,
        'PASSWORD': None
    }
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels_redis.core.RedisChannelLayer',
            'CONFIG': {
                "hosts": [('127.0.0.1', 6379)],
            },
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'shop',
            'USER': 'django',
            'PASSWORD': 'djangopwd',
            'HOST': 'localhost',
            'PORT': 3306
        }
    }
    REDIS = {
        'HOST': 'localhost',
        'PORT': '6379',
        'USER': None,
        'PASSWORD': None
    }
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels_redis.core.RedisChannelLayer',
            'CONFIG': {
                "hosts": [('127.0.0.1', 6379)],
            },
        },
    }
