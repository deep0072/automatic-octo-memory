from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


from .filters import OrderFilter
from .models import *
from .forms import OrderForm,CreateUserForm, CustomerForm 
from .decorators import unauthenticated_user, admin_only, allowed_users



@unauthenticated_user
def register_page(request):

	form  = CreateUserForm()
	
	if request.method == "POST":

		form = CreateUserForm(request.POST)

		if form.is_valid():

			user = form.save()

			username = form.cleaned_data.get('username')

			
			messages.success(request,"Account has been create for " + username)

			return redirect('login')

	context = {'form':form }

	return render(request, 'accounts/register.html', context)


		
@unauthenticated_user
def login_page(request):

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = { }
	return render(request, 'accounts/login.html', context)



def logout_page(request):
	logout(request)
	return redirect('login')




@login_required(login_url='login')
@admin_only
def home(request):
	order = Order.objects.all()
	customer = Customer.objects.all()
	total_orders =order.count()
	

	total_Delivered = order.filter(status="Delivered").count()
	total_pending =order.filter(status="Pending").count()
	context = {'order': order, 'customer': customer, 'total_orders':total_orders, 'total_Delivered': total_Delivered,
	         'total_pending': total_pending}

	return render(request, 'accounts/dashboard.html',  context)


	




@login_required(login_url='login')
@allowed_users(allowed_roles=["customer"])
def userPage(request):
	orders = request.user.customer.order_set.all()
	total_orders = orders.count()
	total_Delivered = orders.filter(status="Delivered").count()
	total_pending =orders.filter(status="Pending").count()

	context = {'order': orders, 'total_orders':total_orders, 'total_Delivered': total_Delivered,
	         'total_pending': total_pending}
	return render(request, 'accounts/users.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=["customer"])
def account_settings(request):
	user = request.user.customer
	form = CustomerForm(instance=user)
	if request.method == "POST":
		form = CustomerForm(request.POST, request.FILES,instance=user )
		if form.is_valid():
			form.save()
	context = {'form':form}

	return render(request, "accounts/account_settings.html", context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
	products = Product.objects.all()
	return render(request, 'accounts/products.html')




@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request, pk):
	customer = Customer.objects.get(id=pk)
	order = customer.order_set.all()
	order_count = order.count

	my_filter = OrderFilter(request.GET, queryset=order)
	order = my_filter.qs
	context = {'orders': order, 'customer': customer, 'order_count': order_count, 'my_filter': my_filter}

	return render(request, 'accounts/customer.html', context)






# Create your views here.
@login_required(login_url='login')	
@allowed_users(allowed_roles=['admin'])
def create_order(request, pk):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('Product', 'status'), extra=10 )
	customer = Customer.objects.get(id=pk)
	form_set = OrderFormSet(queryset=Order.objects.none(), instance=customer)

	if request.method == 'POST':
		form_set = OrderFormSet(request.POST, instance=customer)
		if form_set.is_valid():
			form_set.save()
			return redirect('/')
	context = {'form': form_set}

	return render(request, 'accounts/order_form.html', context)





@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_order(request, pk):
	order = Order.objects.get(id=pk)
	form = OrderForm(instance= order)
	if request.method == "POST":
		form = OrderForm(request.POST,instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')
			
	context = {'form': form}

	return render(request, 'accounts/order_form.html', context)







@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_order(request, pk):
	order = Order.objects.get(id=pk)
	
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item': order}

	return render(request, 'accounts/delete_form.html', context)

