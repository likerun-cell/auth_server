import os

if os.getenv("PYTHON_ENV") == "production":
    from .production import *
else:
    from .development import *
