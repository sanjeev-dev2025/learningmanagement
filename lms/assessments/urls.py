from django.urls import path
from assessments.views import AssessmentListCreateAPIView,AssessmentRetrieveUpdateDestroyAPIView,AssessmentSubmissionListCreateAPIView,AssessmentSubmissionRetrieveUpdateDestroyAPIView

urlpatterns=[
    path("assessments/",AssessmentListCreateAPIView.as_view()),
    path("assessments/<int:pk>/",AssessmentRetrieveUpdateDestroyAPIView.as_view()),
    path("assessment-submissions/",AssessmentSubmissionListCreateAPIView.as_view()),
    path("assessment-submissions/<int:pk>/",AssessmentSubmissionRetrieveUpdateDestroyAPIView.as_view()),
]   