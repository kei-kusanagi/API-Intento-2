from rest_framework import routers
from drfCRUD_app.api import views

router = routers.DefaultRouter()

router.register('api/projects', views.ProjectViewset, 'projects')

urlpatterns = router.urls