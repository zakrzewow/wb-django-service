import pandas as pd
from django.http import Http404
from django.shortcuts import render
from django.views import View

from service.models import DNAWindow


class IndexView(View):
    """
    Klasa opisująca główny widok "Wyniki predykcji enkancerów"
    """

    http_method_names = ['get']

    def get(self, request, chromosome: str):
        # wybór danych dotyczących chromosomu
        chr_data = DNAWindow.objects.filter(chromosome=chromosome)

        # sprawdzenie, czy są dane na temat tego chromosomu
        if not chr_data.exists():
            raise Http404(f"Brak danych o chromosomie {chromosome}")

        # ramka danych
        df = pd.DataFrame(chr_data.values())

        context = {
            'chromosome': chromosome,
            'all_distinct_chromosomes': self._all_distinct_chromosomes,
            'df': df.to_html(),
        }
        return render(request, 'service/index.html', context)

    @property
    def _all_distinct_chromosomes(self):
        return DNAWindow.objects.values_list('chromosome', flat=True).distinct().order_by('chromosome')


def how_to_view(request):
    return render(request, 'service/howto.html')


def about_view(request):
    return render(request, 'service/about.html')
