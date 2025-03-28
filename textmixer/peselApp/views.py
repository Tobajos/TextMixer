from django.shortcuts import render
from .forms import PeselForm
from datetime import datetime

def is_valid_pesel(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        return False

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    control = sum(int(pesel[i]) * weights[i] for i in range(10))
    control = (10 - control % 10) % 10
    return control == int(pesel[10])

def extract_info(pesel):
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    if month > 80:
        year += 1800
        month -= 80
    elif month > 60:
        year += 2200
        month -= 60
    elif month > 40:
        year += 2100
        month -= 40
    elif month > 20:
        year += 2000
        month -= 20
    else:
        year += 1900

    birthdate = f"{year}-{month:02d}-{day:02d}"
    gender = "Kobieta" if int(pesel[9]) % 2 == 0 else "Mężczyzna"
    return birthdate, gender

def check_pesel(request):
    result = None
    info = {}
    if request.method == 'POST':
        form = PeselForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data['pesel']
            valid = is_valid_pesel(pesel)
            if valid:
                birthdate, gender = extract_info(pesel)
                info = {'valid': True, 'birthdate': birthdate, 'gender': gender}
            else:
                info = {'valid': False}
    else:
        form = PeselForm()
    return render(request, 'pesel_form.html', {'form': form, 'info': info})
