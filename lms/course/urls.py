from django.urls import path
from course.views import CategoryListCreateAPIView,CategoryRetrieveUpdateDestroyAPIView,    CourseListCreateAPIView,CourseRetrieveUpdateDestroyAPIView, SectionListCreateAPIView,SectionRetrieveUpdateDestroyAPIView, LessonListCreateAPIView,LessonRetrieveUpdateDestroyAPIView
urlpatterns=[
    path("category/",CategoryListCreateAPIView.as_view(),name="category"),
    path("category/<int:pk>/",CategoryRetrieveUpdateDestroyAPIView.as_view(),name="category_detail"),
    path("course/",CourseListCreateAPIView.as_view(),name="course"),
    path("course/<int:pk>/",CourseRetrieveUpdateDestroyAPIView.as_view(),name="course_detail"),
    path("section/",SectionListCreateAPIView.as_view(),name="section"),
    path("section/<int:pk>/",SectionRetrieveUpdateDestroyAPIView.as_view(),name="section_detail"),
    path("lesson/",LessonListCreateAPIView.as_view(),name="lesson"),
    path("lesson/<int:pk>/",LessonRetrieveUpdateDestroyAPIView.as_view(),name="lesson_detail")
]