from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Serial
from .forms import addSerialForm, searchForm



def list_serial(request):
    context = {
        'auth' : False,
        'comp_serials' : '',
        'uncomp_serials' : '',
        'search_form' : '',
    }

    if request.user.is_authenticated():
        context['auth'] = True
        serials = request.user.serial_set.all()
        comp_serials = serials.filter(is_complete=True)
        uncomp_serials = serials.filter(is_complete=False)
        context['comp_serials'] = comp_serials
        context['uncomp_serials'] = uncomp_serials

        if request.method == 'POST':
            search_form = searchForm(request.POST)
            search = ""
            if search_form.is_valid():
                search = search_form.cleaned_data['search']
                serials = serials.filter(title__icontains=search)
                comp_serials = serials.filter(is_complete=True)
                uncomp_serials = serials.filter(is_complete=False)
                context['comp_serials'] = comp_serials
                context['uncomp_serials'] = uncomp_serials
            return render(request, 'counter/list_serial.html', context)

        else:
            search_form = searchForm()
        context['search_form'] = search_form
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
    if serial.user.id is not request.user.id:
        return render(request, 'counter/wrong_access.html', {})
    serial.counter +=1
    serial.save()
    
    return redirect('list_serial')


@login_required
def dec_counter(request, serial_id):
    serial = get_object_or_404(Serial, pk=serial_id)
    if serial.user.id is not request.user.id:
        return render(request, 'counter/wrong_access.html', {})
    serial.counter -= 1
    serial.save()

    return redirect('list_serial')


@login_required
def inc_season(request, serial_id):
    serial = get_object_or_404(Serial, pk=serial_id)
    if serial.user.id is not request.user.id:
        return render(request, 'counter/wrong_access.html', {})
    serial.season += 1
    serial.counter = 0
    serial.save()

    return redirect('list_serial')


@login_required
def dec_season(request, serial_id):
    serial = get_object_or_404(Serial, pk=serial_id)
    if serial.user.id is not request.user.id:
        return render(request, 'counter/wrong_access.html', {})
    serial.season -= 1
    serial.save()

    return redirect('list_serial')



@login_required
def edit_serial(request, serial_id):
    serial = get_object_or_404(Serial, pk= serial_id)
    if serial.user.id is not request.user.id:
        return render(request, 'counter/wrong_access.html', {})
    
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



@login_required
def complete_serial(request, serial_id):
    serial = get_object_or_404(Serial, pk=serial_id)
    if serial.user.id is not request.user.id:
        return render(request, 'counter/wrong_access.html', {})
    serial.is_complete = True
    serial.save()

    return redirect('list_serial')