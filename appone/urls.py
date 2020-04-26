from django.urls import path
from . import views 

urlpatterns = [
	#path('',views.,name="")

	path('',views.new,name="new"),
	path('<code_id>/',views.indextest,name="index"),
]
