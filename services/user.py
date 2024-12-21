from django.contrib.auth import get_user_model
# from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()


def create_user(username: str, password: str, email: str = None,
                first_name: str = None,
                last_name: str = None) -> User:
    user = User.objects.create_user(username=username,
                                    password=password,
                                    email=email)
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    user.save()
    return user


def get_user(user_id: int) -> int:
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None


def update_user(user_id: int,
                username: str = None,
                password: str = None,
                email: str = None,
                first_name: str = None,
                last_name: str = None) -> None:
    try:
        user = User.objects.get(id=user_id)
        if username:
            user.username = username
        if password:
            user.set_password(password)
        if email:
            user.email = email
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        user.save()
        return user
    except User.DoesNotExist:
        return None