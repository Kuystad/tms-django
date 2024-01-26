from rest_framework import viewsets, pagination


class DefaultPagination(pagination.PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 100


class QuestionViewSet(viewsets.ModelViewSet):
    pagination_class = DefaultPagination
