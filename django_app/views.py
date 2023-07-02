from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def main(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'main.html', context=context)
    elif request.method == 'POST':
        age_years = request.POST.get('age_years')
        age_months = request.POST.get('age_months')
        age_category = request.POST.get('age_category')
        gender = request.POST.get('gender')
        weight = request.POST.get('weight')
        substance = request.POST.get('substance')
        dose = request.POST.get('dose')
        unit = request.POST.get('unit')
        concentration = request.POST.get('concentration')
        chronicity = request.POST.get('chronicity')
        mdd_dose = request.POST.get('mdd_dose')
        mdd_unit = request.POST.get('mdd_unit')
        mdd_concentration = request.POST.get('mdd_concentration')
        serum_levels = request.POST.getlist('serum_levels')
        other_labs = request.POST.get('other_labs')
        # Perform necessary calculations and validations based on the given conditions
        # Save the data or perform further actions as required
        # Render the appropriate response or redirect to another page

    return render(request, 'main.html')
