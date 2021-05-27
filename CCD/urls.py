from django.contrib import admin
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from django.urls import include, path
from rest_framework import routers
from contactus import views

router = routers.DefaultRouter()
router.register(r'head_of_centers', views.Head_of_centerViewSet)
router.register(r'faculty_members', views.Faculty_membersViewSet)
router.register(r'department_reps', views.Department_repsViewSet)
router.register(r'ccd_office_conts', views.Ccd_office_contViewSet)
router.register(r'admin_staffs', views.Admin_staffViewSet)
router.register(r'contacts', views.ContactsViewSet)
router.register(r'placement_coordinators', views.Placement_coordinatorsViewSet)
router.register(r'intern_coordinators', views.Intern_coordinatorsViewSet)

app_name="home"
urlpatterns = [
    # YOUR PATTERNS
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
