from django.urls import path

from product.views import products_list, ProductListView, ProductDetailView, CreateProductView, UpdateProductView, \
    DeleteProductView, ProductViewSet

urlpatterns = [
    path('func/products/', products_list)
]

urlpatterns = [
    path('cls/products/', ProductListView.as_view()),
    path('cls/products/<int:id>/', ProductDetailView.as_view()),
    path('cls/products/create/', CreateProductView.as_view()),
    path('cls/products/update/<int:id>/', UpdateProductView.as_view()),
    path('cls/products/delete/<int:id>/', DeleteProductView.as_view()),
]

urlpatterns = [
    path('publications/', ProductViewSet.as_view(
        {'get': 'list',
         'post': 'create'}
    )),
    path('publications/<int:id>/', ProductViewSet.as_view(
        {'get': 'retrieve',
         'put': 'update',
         'patch': 'partial_update',
         'delete': 'destroy'}
    )
         )
]