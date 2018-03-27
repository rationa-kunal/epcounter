from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Serial
from .forms import addSerialForm



def list_serial(request):
    context = {
        'auth' : False,
        'serials' : '',
    }

    if request.user.is_authenticated():
        context['auth'] = True
        serials = Serial.objects.filter(user=request.user)
        context['serials'] = serials

    return render(request, 'counter/list_serial.html', context)



@login_required
def add_serial(request):

    if request.method == 'POST':
        form = addSerialForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            counter = form.cleaned_data['counter']
            season = form.cleaned_data['season']
            new_serial = Serial(title=title, description=description, counter=counter, season=season, user=request.user)
            new_serial.save()

        return redirect('list_serial')

    else:
        form = addSerialForm()

    return render(request, 'counter/add_serial.html', {'form':form})



@login_required
def inc_counter(request, serial_id):
    serial = get_object_or_404(Serial, pk=serial_id)
    serial.counter +=1
    serial.save()
    
    return redirect('list_serial')


@login_required
def dec_counter(request, serial_id):
    serial = get_object_or_404(Serial, pk=serial_id)
    serial.counter -= 1
    serial.save()

    return redirect('list_serial')


@login_required
def inc_season(request, serial_id):
    serial = get_object_or_404(Serial, pk=serial_id)
    serial.season += 1
    serial.counter = 0
    serial.save()

    return redirect('list_serial')


@login_required
def dec_season(request, serial_id):
    serial = get_object_or_404(Serial, pk=serial_id)
    serial.season -= 1
    serial.save()

    return redirect('list_serial')



@login_required
def edit_serial(request, serial_id):
    serial = get_object_or_404(Serial, pk= serial_id)
    
    if request.method == 'POST':
        form = addSerialForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            counter = form.cleaned_data['counter']
            season = form.cleaned_data['season']
            new_serial = Serial(title=title, description=description, counter=counter, season=season, user=request.user)
            new_serial.save()

        return redirect('list_serial')
    
    else:
        form = addSerialForm({
            'title' : serial.title,
            'description' : serial.description,
            'counter' : serial.counter,
            'season' : serial.season,
        })

    return render(request, 'counter/add_serial.html', {'form': form})