from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def example1(request, id):
    return HttpResponse('you type {}.'.format(id))


def example2(request, id, name):
    return HttpResponse('you type id {} and the name {}'.format(id, name))

def redirect1(request):
    return HttpResponseRedirect('/')

def redirect2(request):
    url = reverse('home')
    return HttpResponseRedirect(url)


def redirect2(request):
    return redirect('home')





# ----------- TEMPLATES ---------------

from django.template import loader
def home1(request):
    template = loader.get_template('home.html')
    context = {'title': 'SLUD - 2019'}

    rd = template.render(context, request)

    return HttpResponse(rd)


def home2(request):
    context = {'title': 'SLUD - 2019'}

    return render(request, 'home.html', context)



# CBV

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update({
            'title': 'SLUD - 2019',
        })

        return context
