from django.urls import path, include

urlpatterns = [
    path('user/', include('user.urls')),

    path('dean/', include('apps.main.dean.urls')),
    path('deputy-dean/', include('apps.main.deputy_dean.urls')),
    path('student/', include('apps.main.student.urls')),
    path('teacher/', include('apps.main.teacher.urls')),

    path('blog/', include('apps.blog.urls')),
    path('faculty/', include('apps.faculty.urls')),
    path('group/', include('apps.group.urls')),
    path('notification/', include('apps.notification.urls')),
]
