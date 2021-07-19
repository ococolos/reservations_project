import csv, io
from django.core.exceptions import ValidationError

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


from .models import City, Reservations
from .forms import UploadFileForm, CityForm
from .utils import calculate_rate_for_city, calculate_total_gr_commision, calculate_gr_commision_per_month


def index(request):
    context = {'reservations': Reservations.objects.all()}

    return render(request, 'commision_calculator/home.html', context)

def upload_csv(request):
    template = 'commision_calculator/upload_csv.html'

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The file you are attempting to upload is not a CSV file, please check if it has the correct extension.')
                return render(request, template, {'form': form})
            
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            for row_index, row_data in enumerate(csv.reader(io_string, delimiter=',', quotechar="|")):
                try:
                    _, created = Reservations.objects.update_or_create(
                            property_name=row_data[0],
                            city=row_data[1],
                            net_income=row_data[2],
                            date=row_data[3],
                            )
                except:
                    messages.warning(request, f'Incorrect data on row {row_index + 1} (excluding headers), please check that you submit properly formatted data.')
                    messages.warning(request,"Hint: Net income should be a decimal number.")
                    messages.warning(request,"Hint: Date format should be YYYY-MM-DD.")
                    return render(request, template, {'form': form})
            
            messages.success(request, 'File uploaded successfully.')
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UploadFileForm()
    return render(request, template, {'form': form})

def generate_reports(request):
    template = 'commision_calculator/generate_reports.html'
    context = {}

    context['GR_total_commision'], context['cities_not_in_db']  = calculate_total_gr_commision()
    context['GR_commision_per_month']= calculate_gr_commision_per_month()
    

    if request.method == 'POST':
        form = CityForm(request.POST)
        context['form'] = form
        if form.is_valid():
            context['city_name'] = form.cleaned_data['city_name']
            context['city_commision'] = calculate_rate_for_city(form.cleaned_data['city_name'])
            return render(request, template, context)

    else:
        context['form'] = CityForm()
    #print(calculate_rate_for_city('Pariss'))


    return render(request, template, context)
