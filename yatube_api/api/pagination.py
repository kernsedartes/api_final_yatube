from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination
)
from rest_framework.response import Response


class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 100


class CustomLimitOffsetPagination(LimitOffsetPagination):
    def get_paginated_response(self, data):
        return Response(data)
