# from django.contrib import admin
# from django.urls import path
# from repos import views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('organizations/', views.OrganizationView.as_view(), name='organization'),
# ]


from django.urls import path
from repos import views

urlpatterns = [
    path('organizations/', views.OrganizationView.as_view()),
    path('organizations/<int:org_pk>', views.organization_repos),
]