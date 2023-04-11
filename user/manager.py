from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    def _create_user(self, USER_ID, ROLE, password, is_superuser=False, is_staff=False):
        user = self.model(USER_ID=USER_ID, ROLE=ROLE, is_superuser=is_superuser, is_staff=is_staff)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, USER_ID, password):
        return self._create_user(USER_ID=USER_ID, ROLE='ADMIN', password=password, is_superuser=True, is_staff=True)

    def create_rector(self, USER_ID, password):
        return self._create_user(USER_ID=USER_ID, ROLE='RECTOR', password=password, is_staff=True)

    def create_dean(self, USER_ID, password):
        return self._create_user(USER_ID=USER_ID, ROLE='DEAN', password=password, is_staff=True)

    def create_deputy_dean(self, USER_ID, password):
        return self._create_user(USER_ID=USER_ID, ROLE='DEPUTY_DEAN', password=password, is_staff=True)

    def create_teacher(self, USER_ID, password):
        return self._create_user(USER_ID=USER_ID, ROLE='TEACHER', password=password, is_staff=True)

    def create_manager(self, USER_ID, password):
        return self._create_user(USER_ID=USER_ID, ROLE='MANAGER', password=password, is_staff=True)

    def create_student(self, USER_ID, password):
        return self._create_user(USER_ID=USER_ID, ROLE='STUDENT', password=password)

    def create_parent(self, USER_ID, password):
        return self._create_user(USER_ID=USER_ID, ROLE='PARENT', password=password)
