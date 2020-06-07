from django.shortcuts import render


def register_participant(request):
    all_environmental_exposures = ['pollution', 'lead']  # todo: introduce data provider service for mock data
    all_genetic_mutations = ['PAH', 'CFTR', 'HBB', 'OCA2', 'HTT', 'DMPK', 'LDLR', 'APOB', 'NF1', 'PKD1', 'PKD2', 'F8',
                             'DMD', 'PHEX', 'MECP2', 'USP9Y']
    context = {'env_exposures': all_environmental_exposures, 'gene_mutations': all_genetic_mutations}
    return render(request, 'fdn_participant/registration.html', context)
