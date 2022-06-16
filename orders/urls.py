from django.urls import path
from orders import views

urlpatterns=[ 
    path('',views.OrderCreateView.as_view(),name='get-all'),
    path('<int:id>',views.OrderDetailView.as_view(),name='dtails'),
    path('update/<int:id>',views.Update_status.as_view(),name='update-status'),
    path('user/<int:id>/orders',views.UserOrder_all.as_view(),name='user-orders'),
    path('user/<int:user_id>/<int:order_id>/',views.UserOrder_one.as_view(),name='user-order-one'),
    
    
]