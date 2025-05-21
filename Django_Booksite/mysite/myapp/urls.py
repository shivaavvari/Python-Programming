from django.urls import path
from  . import  views

app_name = 'myapp'
urlpatterns = [
    path('',views.index,name="index"),
    #path('products/',views.products,name="Products"),
    #book1/2
    path('book/<int:book_id>/',views.detail,name='detail'),
    path('add/',views.add_book,name='add_book'),
    path('update/<int:id>/',views.update,name='update'),
     path('delete/<int:id>/',views.delete,name='delete')
]
