from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,DetailView

@login_required
def add_car(request):
    if request.method == 'POST':
        car_form = forms.CarForm(request.POST)
        if car_form.is_valid():
            car_form.instance.author = request.user
            car_form.save()
            return redirect('car_post')

    else:
        car_form = forms.CarForm()
    return render(request, 'add_car.html',{'form' : car_form})


# Add Post using class Based view
@method_decorator(login_required, name='dispatch')
class AddCarCreateView(CreateView):
    model = models.Car
    form_class = forms.CarForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('add_car')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class DetailCarView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = forms.CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


def ByeNow(request,id):
    car = models.Car.objects.get(pk=id)
    car.quantity -= 1
    history = models.History(
        name=car.name, 
        brand=car.brand, 
        quantity=1,
        image = car.image,
        price=car.price,
        description = car.description,
        author=car.author)
    history.save()
    car.save()
    return redirect("detail_car",id=car.id)