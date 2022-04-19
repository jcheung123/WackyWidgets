from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm



def widgets(request):
    widgets = Widget.objects.all()
    form = WidgetForm()

    if request.method == 'POST':
        form = WidgetForm(request.POST) 
        if form.is_valid():
            form.save() 
        return redirect('/')

    context = {'widgets': widgets, 'form': form}
    return render(request, 'widget.html', context)


def delete_widget(request, pk):
    item = Widget.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'delete.html', context)



