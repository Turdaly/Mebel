from django .urls import path, include
from django.views.generic.base import TemplateView
from .views import *
urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'), 
    path('profile/', ProfileView, name='profile'),
    path('profile_update/', profile_update, name='profile_update'),
    path('jihaz/', JihazListView, name="jihaz"),
    path('jihaz/<int:pk>/', JihazDetailView.as_view(), name='jihaz_detail'), 
    path('jihaz/new/', JihazCreateView.as_view(), name='jihaz_create'),  
    path('jihaz/<int:pk>/update/', JihazUpdateView.as_view(), name='jihaz_update'),  
    path('jihaz/<int:pk>/delete/', JihazDeleteView.as_view(), name='jihaz_delete'),  
    path('search/', SearchResultsView, name='search_results'), 
    path('sort/price/jihaz', SortPriceView, name='sort_price'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('add-to-cart/<int:jihaz_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', cart, name='cart'),
    
]
