from rest_framework.pagination import PageNumberPagination
# custom paginations
class DefaultPagination(PageNumberPagination):
    page_size = 2