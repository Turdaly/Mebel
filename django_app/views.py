from django.shortcuts import render
from django.views.generic import \
    ListView, \
    DetailView, \
    CreateView, \
    UpdateView, \
    DeleteView
from .models import *
from django.urls import reverse_lazy
from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.

def JihazListView(request):
    categoria = request.GET.get('category')
    
    if categoria == None:
        jihaz = Jihaz.objects.all()
    else:   
        jihaz = Jihaz.objects.filter(categoria__type=categoria)
    categoria = Categoria.objects.all()
    return render(request, 
                  template_name="jihaz.html", 
                  context={
                      "jihazs": jihaz,
                      "categories": categoria
                  })
    
class JihazDetailView(DetailView):
    model = Jihaz
    template_name = 'jihaz_detail.html'
    context_object_name = 'jihaz'
    
class JihazCreateView(CreateView):
    model = Jihaz
    template_name = 'jihaz_create.html'
    fields = '__all__'
    
class JihazUpdateView(UpdateView):
    model = Jihaz
    template_name = 'jihaz_update.html'
    fields = '__all__'
    
    
class JihazDeleteView(DeleteView):
    model = Jihaz
    template_name = 'jihaz_delete.html'
    success_url = reverse_lazy('jihaz') 

def ProfileView(request):
    klient = Klient.objects.get(user_id=request.user)
    return render(request=request, 
            template_name="profile.html",
            context={
                "klient": klient
            })
    
def SortPriceView(request):
    jihazs = Jihaz.objects.order_by('price')
    
    return render(request, 
                  template_name="sort_price.html",
                  context={
                      "jihazs": jihazs
                  })

def SearchResultsView(request):
    jihazs = Jihaz.objects.all()
    search_results = []
    query = request.GET.get('q')
             
    for jihaz in jihazs:
        if str(jihaz.name).find(query) != -1:    
            search_results.append(jihaz)
            
            
    if len(search_results) == 1:
        return render(request=request, 
        template_name="search_results.html",
        context={
            "jihaz": search_results[0],
        })
    elif len(search_results) > 1:
        return render(request=request, 
        template_name="jihaz.html",
        context={   
            "jihazs": search_results,
        })
        
    return render(request,
                  template_name='notfound.html')


def add_to_cart(request, jihaz_id):
    jihaz = Jihaz.objects.get(id=jihaz_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        jihaz=jihaz
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart')


def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.jihaz.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', 
                  context={
                      'cart_items': cart_items, 
                      'total_price': total_price
                      })