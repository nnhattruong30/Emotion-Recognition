from django.urls import path
from . import views

urlpatterns = [
	#path('', views.ImageUploadView.as_view()),
	path('', views.homepage, name='upload_file'),
]