from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from .models import ExampleModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ExampleModelSerializer



class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = 'login'
    template_name = 'SkyGate/index.html'
    context_object_name = 'all_objects'

    def get_queryset(self):
        return ExampleModel.objects.all()

class ExampleModelCreate(LoginRequiredMixin,CreateView):
    model = ExampleModel
    fields = [ 'example_object']
    success_url = reverse_lazy('SkyGate:index')

class ExampleModelUpdate(LoginRequiredMixin, UpdateView):
    model = ExampleModel
    fields = [ 'example_object']
    success_url = reverse_lazy('SkyGate:index')

class ExampleModelDelete(LoginRequiredMixin, DeleteView):
    model = ExampleModel
    success_url = reverse_lazy('SkyGate:index')

def logout_view(request):
    logout(request)
    return redirect('login')

class ExampleModelList(LoginRequiredMixin, APIView):

    def get(self, request):
        objects = ExampleModel.objects.all()
        serializer = ExampleModelSerializer(objects, many=True)
        return Response(serializer.data)


    def post(self):
        pass






















