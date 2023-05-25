import re

import pandas as pd
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views import View

from service.models import DNAWindow


class IndexView(View):
    """
    Klasa opisująca główny widok "Wyniki predykcji enkancerów"
    """

    http_method_names = ['get']

    def get(self, request, chromosome: str):
        # sprawdzenie, czy są dane na temat tego chromosomu
        if not DNAWindow.objects.filter(chromosome=chromosome).exists():
            raise Http404(f"Brak danych o chromosomie {chromosome}")

        context = {
            'chromosome': chromosome,
            'all_distinct_chromosomes': self._all_distinct_chromosomes,
        }
        return render(request, 'service/index.html', context)

    @property
    def _all_distinct_chromosomes(self):
        distinct_chromosomes = DNAWindow.objects.values_list('chromosome', flat=True).distinct()
        return sorted(list(distinct_chromosomes), key=lambda x: int(re.search(r"\d+", x).group(0)))


def how_to_view(request):
    return render(request, 'service/howto.html')


def about_view(request):
    return render(request, 'service/about.html')


def export_view(request, chromosome: str):
    chr_data = DNAWindow.objects.filter(chromosome=chromosome)
    df = pd.DataFrame(chr_data.values())
    csv = df.to_csv(index=False)
    return HttpResponse(csv, headers={
        'Content-Type': 'text/csv',
        'Content-Disposition': f'attachment; filename="{chromosome}.csv"',
    })
