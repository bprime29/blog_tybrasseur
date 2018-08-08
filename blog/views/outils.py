from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.forms.outils import calc_dens


def calc_with_densimetre(request):
    if request.method == 'POST':
        form = calc_dens(request.POST)
        if form.is_valid():
            di = form.cleaned_data['di']
            df = form.cleaned_data['df']
            sucre = form.cleaned_data['sucre']
            di = int(di)
            df = int(df)
            sucre = float(sucre)
            dens1 = (di - df) * 1.05;
            dens1 = (((dens1 / df) * 100) / 0.795);
            referm1 = (((sucre * 0.5) / 0.795) / 10);
            ref_tot1 = dens1 + referm1;
        return render(request, 'blog/calc_with_densimetre.html',
                      {'dens1': str(round(dens1, 2)), 'ref_tot1': str(round(ref_tot1, 2)), 'df': df, 'di': di,
                       'sucre': sucre})

    else:
        di = "1068"
        df = "1015"
        sucre = "7.0"
        return render(request, 'blog/calc_with_densimetre.html', {'di': di, 'df': df, 'sucre': sucre})


def calc_with_refracto(request):
    return render(request, 'blog/calc_with_refracto.html')
