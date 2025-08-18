from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # AbstractUser đã có username, password, email, last_login, is_active, ...

    full_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(
        max_length=30, unique=True, null=True, blank=True
    )
    occupation = models.CharField(max_length=30, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    avatar_url = models.URLField(default='default.img')
    cover_url = models.URLField(default='default_cover.img')
    hometown = models.CharField(max_length=30, null=True, blank=True)
    current_city = models.CharField(max_length=30, null=True, blank=True)
    is_online = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Cần set email là trường xác thực chính
    REQUIRED_FIELDS = []  # các trường cần thêm khi tạo superUser

    def __str__(self):
        return f"{self.full_name} : {self.date_of_birth}"

    class Meta:
        db_table = "users"  # tên bảng trong db
        verbose_name = "User"  # tên trong admin
        verbose_name_plural = "users"  # tên số nhiều
        ordering = ['-created_at']  # thứ tự truy vấn trong db theo created time
        # unique_together = (('username', 'phone_number'),)  # đảm bảo không cặp username và phone là duy nhất





