from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Page,WikiDataModel
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View


# Create your views here.

from .forms import PageForm,CustomWikiDataForm


class PageListView(ListView):
    model = Page
    template_name = 'theme_adder.html'
    context_object_name = 'all_pages'
    ordering = ['the_title']
    def get_context_data(self,*args,**kwargs):
        context = super(PageListView,self).get_context_data(*args,**kwargs)
        context['form'] = PageForm()
        return context

    def post(self,request,*args,**kwargs):
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request,*args,**kwargs)
def create_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            # Save the form data to create a new Page object
            form.save()
            # Redirect to the page list view
            return redirect('page-list')
    else:
        form = PageForm()

    # Retrieve all Page objects from the database
    all_pages = Page.objects.all()

    return render(request, 'theme_adder.html', {'form': form, 'all_pages': all_pages})
#show for index.html
def index(request):
    return render(request,'index.html')

class CreateDataView(View):
    #add data
    def get(self,request):
        form = CustomWikiDataForm()
        return render(request,'create_data.html',{'form':form})
    def post(self,request):
        form = CustomWikiDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request,'create_data.html',{'form':form})
#create random page from WikiDataModel
def random_page(request):
    random_page = WikiDataModel.objects.order_by('?').first()
    return render(request,'random_page.html',{'random_page':random_page})
