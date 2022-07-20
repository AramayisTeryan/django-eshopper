from django.shortcuts import render
from .models import HomeCarusel, HomeCategory, HomeSubCategory, HomeFeatureItem, HomeBrand, HomeRec, HomeBlog, HeadBlog, HeadFooter, Circle, Map, BlogSingle, BlogDavis, BlogJanis, HomeContact, ShippingBlog, ErrorBlog, ShopperLogo, HomeCart
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, FormView, TemplateView, CreateView
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")


class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homecarusels = HomeCarusel.objects.all()
        category = HomeCategory.objects.all()
        brands = HomeBrand.objects.all()
        ship = ShippingBlog.objects.all()
        items = HomeFeatureItem.objects.all()
        recs = HomeRec.objects.all()
        headfooter = HeadFooter.objects.all()
        circle = Circle.objects.all()
        map = Map.objects.all()
        return render(request, self.template_name, {'homecarusels':homecarusels, 'category':category, 'brands':brands, 'items':items, 'recs':recs, 'headfooter':headfooter, 'circle':circle, 'map':map, 'ship':ship})



class ProdListView(ListView):
    template_name = 'shop.html'

    def get(self, request):
        items = HomeFeatureItem.objects.all()
        category = HomeCategory.objects.all()
        brands = HomeBrand.objects.all()
        ship = ShippingBlog.objects.all()
        headfooter = HeadFooter.objects.all()
        circle = Circle.objects.all()
        map = Map.objects.all()
        return render(request, self.template_name, {'items':items, 'category':category, 'brands':brands, 'headfooter':headfooter, 'circle':circle, 'map':map, 'ship':ship})

class ProdDetailView(DetailView):
    template_name = 'product-details.html'

    def get(self, request, id):
        items = HomeFeatureItem.objects.get(pk=id)
        category = HomeCategory.objects.all()
        brands = HomeBrand.objects.all()
        ship = ShippingBlog.objects.all()
        headfooter = HeadFooter.objects.all()
        circle = Circle.objects.all()
        map = Map.objects.all()
        return render(request, self.template_name, {'items':items, 'category':category, 'brands':brands, 'headfooter':headfooter, 'circle':circle, 'map':map, 'ship':ship})


class BlogListView(ListView):
	template_name = 'blog.html'

	def get(self, request):
		homeblog = HomeBlog.objects.all()
		headblog = HeadBlog.objects.all()
		category = HomeCategory.objects.all()
		brands = HomeBrand.objects.all()
		ship = ShippingBlog.objects.all()
		headfooter = HeadFooter.objects.all()
		circle = Circle.objects.all()
		map = Map.objects.all()
		return render(request, self.template_name, {'homeblog':homeblog, 'headblog':headblog, 'category':category, 'brands':brands, 'headfooter':headfooter, 'circle':circle, 'map':map, 'ship':ship})



class BlogSingleListView(ListView):
	template_name = 'blog-single.html'

	def get(self, request):
		blogsingle = BlogSingle.objects.all()
		category = HomeCategory.objects.all()
		brands = HomeBrand.objects.all()
		ship = ShippingBlog.objects.all()
		headfooter = HeadFooter.objects.all()
		circle = Circle.objects.all()
		map = Map.objects.all()
		blogdavis = BlogDavis.objects.all()
		blogjanis = BlogJanis.objects.all()
		return render(request, self.template_name, {'blogsingle':blogsingle, 'category':category, 'brands':brands, 'ship':ship, 'headfooter':headfooter, 'circle':circle, 'map':map, 'blogdavis':blogdavis, 'blogjanis':blogjanis})


class ContactListView(ListView):
	template_name = 'contact-us.html'

	def get(self, request):
		homecontact = HomeContact.objects.all()
		category = HomeCategory.objects.all()
		headfooter = HeadFooter.objects.all()
		brands = HomeBrand.objects.all()
		circle = Circle.objects.all()
		map = Map.objects.all()
		return render(request, self.template_name, {'homecontact':homecontact, 'headfooter':headfooter, 'brands':brands, 'circle':circle, 'map':map, 'category':category})



class ErrorListView(ListView):
	template_name = '404.html'

	def get(self, request):
		errorblog = ErrorBlog.objects.all()
		shopperlogo = ShopperLogo.objects.all()
		return render(request, self.template_name, {'errorblog':errorblog, 'shopperlogo':shopperlogo})


class CartListView(ListView):
	template_name = 'cart.html'

	def get(self, request):
		homecart = HomeCart.objects.all()
		headfooter = HeadFooter.objects.all()
		circle = Circle.objects.all()
		map = Map.objects.all()
		return render(request, self.template_name, {'homecart':homecart, 'headfooter':headfooter, 'circle':circle, 'map':map})
