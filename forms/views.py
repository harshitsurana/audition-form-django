from .models import Form
from .forms import CreateForm, UserRegisterForm
from myauth.models import Profile
from myauth.forms import ProfileRegisterForm
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.contrib.auth import authenticate, login

class FormListView(ListView):
    model = Form
    template_name = "forms/form_list.html"
    def get(self, request) :
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('myauth:login'))
        start_date =  request.GET.get("start_date", False)
        end_date =  request.GET.get("end_date", False)
        name = request.GET.get("name", False)
        email = request.GET.get("email",False)
        if not start_date and not end_date and not name and not email:
            try:
                if request.user.is_superuser:
                    form_list = Form.objects.all().order_by('-updated_at')[:10]
                    ctx = {'form_list' : form_list}
                    return render(request, self.template_name, ctx);
                else:
                    form_list = Form.objects.filter(owner = request.user).order_by('-updated_at')[:10]
                    ctx = {'form_list' : form_list}
                    return render(request, self.template_name, ctx);
            except:
                form_list = None
                ctx = {'form_list' : form_list}
                return render(request, self.template_name, ctx);
        else:
            if request.user.is_superuser:
                if start_date:
                    objects = Form.objects.filter(submitted_at__gte=start_date)
                if end_date:
                    objects = Form.objects.filter(submitted_at__lte=end_date)
                if name:
                    objects = Form.objects.filter(name__contains=name)
                if email:
                    objects = Form.objects.filter(email=email)
            else:
                if start_date:
                    objects = Form.objects.filter(submitted_at__gte=start_date, owner=request.user)
                if end_date:
                    objects = Form.objects.filter(submitted_at__lte=end_date, owner=request.user)
                if name:
                    objects = Form.objects.filter(name__contains=name, owner=request.user)
                if email:
                    objects = Form.objects.filter(email=email, owner=request.user)

            objects = objects.order_by('-updated_at')[:10]
            ctx = {'form_list' : objects,'start_date': start_date,
                 'end_date': end_date, 'name':name, 'email':email}
            return render(request, self.template_name, ctx)

class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile 
    template_name = 'forms/profile.html'
    def get(self, request) :
        form_instance = Profile.objects.get(user=request.user)
        context = { 'form' : form_instance, 'username' :request.user.username, 'email':request.user.email }
        return render(request, self.template_name, context)

class ProfileUpdateView(View):
    template_name = 'forms/profile_update.html'
    success_url = reverse_lazy('forms:profile')
    def get(self, request) :
        form_instance = get_object_or_404(Profile, user=self.request.user)
        form = ProfileRegisterForm(instance=form_instance)
        ctx = { 'form': form }
        return render(request, self.template_name, ctx)

    def post(self, request) :
        form_instance = get_object_or_404(Profile, user=self.request.user)
        form = ProfileRegisterForm(request.POST, request.FILES or None , instance=form_instance)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template_name, ctx)

        form_instance.save()
        return redirect(self.success_url)


class FormDetailView(DetailView):
    model = Form
    template_name = 'forms/form_detail.html'
    def get(self, request, pk) :
        form_instance = Form.objects.get(id=pk)
        context = { 'form' : form_instance}
        return render(request, self.template_name, context)

class FormDeleteView(DeleteView):
    model = Form
    def get_queryset(self):
        qs = super(DeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)

class FormCreateView(LoginRequiredMixin, View):
    template_name = 'forms/form_form.html'
    success_url = reverse_lazy('forms:all')
    def get(self, request, pk=None) :
        form = CreateForm()
        ctx = { 'form': form }
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None) :
        form = CreateForm(request.POST,request.FILES or None)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template_name, ctx)

        form_instance = form.save(commit=False)
        form_instance.owner = self.request.user
        form_instance.save()
        return redirect(self.success_url)

class FormUpdateView(LoginRequiredMixin, View):
    template_name = 'forms/form_form.html'
    success_url = reverse_lazy('forms:all')
    def get(self, request, pk) :
        form_instance = get_object_or_404(Form, id=pk, owner=self.request.user)
        form = CreateForm(instance=form_instance)
        ctx = { 'form': form }
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None) :
        form_instance = get_object_or_404(Form, id=pk, owner=self.request.user)
        form = CreateForm(request.POST,request.FILES or None, instance=form_instance)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template_name, ctx)

        form_instance.save()

        return redirect(self.success_url)
