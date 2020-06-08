from django.shortcuts import render


def home(request):
    participant_data = []
    context = {'participant_data': participant_data}
    return render(request, 'fdn_participant/home.html', context)


def register_participant(request):
    all_environmental_exposures = ['Metals', 'Dust or fibers (note: not household dust)', 'Chemicals',
                                   'Fumes (e.g., exhaust)', 'Radiation',
                                   'Biological agents (e.g., bacteria, viruses, mold)']
    all_genetic_mutations = ['PAH', 'CFTR', 'HBB', 'OCA2', 'HTT', 'DMPK', 'LDLR', 'APOB', 'NF1', 'PKD1', 'PKD2', 'F8',
                             'DMD', 'PHEX', 'MECP2', 'USP9Y']
    context = {'env_exposures': all_environmental_exposures, 'gene_mutations': all_genetic_mutations}
    return render(request, 'fdn_participant/registration.html', context)
