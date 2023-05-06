from django.shortcuts import render, get_object_or_404, redirect
from .forms import VehicleForm
from .models import Vehicles


def vehicle_create_view(request):
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = VehicleForm()
    context = {
        'form': form
    }
    return render(request, "vehicles/vehicle_create.html", context)


def vehicle_update_view(request, id=id):
    obj = get_object_or_404(Vehicle, id=id)
    form = VehicleForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "vehicles/vehicle_create.html", context)


def vehicle_list_view(request):
    queryset = Vehicle.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "vehicles/vehicle_list.html", context)

def vehicle_detail_view(request, id):
    obj = get_object_or_404(Vehicle, id=id)
    context = {
        "object": obj
    }
    return render(request, "vehicles/vehicle_detail.html", context)


def vehicle_delete_view(request, id):
    obj = get_object_or_404(Vehicle, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "vehicles/vehicle_delete.html", context)
