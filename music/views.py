from django.views import generic 
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from django.urls import reverse_lazy
from .models import Album
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    
    def get_queryset(self):
        return Album.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['all_albums'] = Album.objects.all()
        return context


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # display blank form for a new user whoo doesn have account yet
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #process form data for people who resister and then hit the submit button
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            #it creates object from form but it doesnt save it to the database
            #thus at this time we havent added it into the databae but we can 
            #use it locally
            #cleaned (normalized) data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            #after this line of code the users are entered into the database

            #returns user objects if credentials are correct

            user = authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:

                    login(request,user)
                    #request.user.username - this can be used to retrieve info 
                    return redirect('music:index')

        return render(request,self.template_name,{'form':form})
