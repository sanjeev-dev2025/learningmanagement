from django.urls import path
from enrollement.views import EnrollmentListCreateAPIView,EnrollementRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('enrollments/',EnrollmentListCreateAPIView.as_view()),
    path('enrollments/<int:pk>/',EnrollementRetrieveUpdateDestroyAPIView.as_view()),
]
        