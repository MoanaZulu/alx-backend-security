INSTALLED_APPS = [
    # existing apps...
    'ip_tracking',
]



MIDDLEWARE = [
    # existing middleware...
    'ip_tracking.middleware.IPTrackingMiddleware',
]






INSTALLED_APPS = [
    ...,
    'ip_tracking',
]



MIDDLEWARE = [
    ...,
    'ip_tracking.middleware.IPTrackingMiddleware',
]
