from django.urls import path
from assessments.views import AssessmentListCreateAPIView,AssessmentRetrieveUpdateDestroyAPIView

urlpatterns=[
    path("assessments/",AssessmentListCreateAPIView.as_view()),
    path("assessments/<int:pk>/",AssessmentRetrieveUpdateDestroyAPIView.as_view()),
]   