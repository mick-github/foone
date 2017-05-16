from functools import wraps
from flask import abort
from flask_login import current_user


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def site_permitted(site):
    # here site is an instance of the property defined in models
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.check_site(site):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
