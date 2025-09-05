# truck/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Truck
from .forms import TruckForm

class TruckListView(ListView):
    model = Truck
    template_name = "truck/truck_list.html"
    context_object_name = "trucks"

class TruckCreateView(CreateView):
    model = Truck
    form_class = TruckForm
    template_name = "truck/truck_form.html"
    success_url = reverse_lazy("truck_list")

class TruckUpdateView(UpdateView):
    model = Truck
    form_class = TruckForm
    template_name = "truck/truck_form.html"
    success_url = reverse_lazy("truck_list")

class TruckDeleteView(DeleteView):
    model = Truck
    template_name = "truck/truck_confirm_delete.html"
    success_url = reverse_lazy("truck_list")
