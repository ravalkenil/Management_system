from student.models import student_custom,application_model
from student.api.serializer import studentserializer,applicationserializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

class mypage(PageNumberPagination):
    page_size=5


class userviewset(viewsets.ModelViewSet):
    queryset=student_custom.objects.all()
    serializer_class=studentserializer
    pagination_class=mypage

class applicationviewset(viewsets.ModelViewSet):
    queryset=application_model.objects.all()
    serializer_class=applicationserializer
    pagination_class=mypage
