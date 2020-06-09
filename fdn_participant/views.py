from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import EnvExposure, GeneMutation, Participant


def home(request):
    participant_data = []
    context = {'participant_data': participant_data}
    return render(request, 'fdn_participant/home.html', context)


def add_participant(request):
    participant_data_fields = ['name', 'age', 'has_siblings', 'reviewed_status']
    env_exposures = request.POST.getlist('env_exposures')
    gene_mutations = request.POST.getlist('gene_mutations')

    direct_set_participant_data = {key: value for (key, value) in request.POST.items() if key in
                                   participant_data_fields}
    """ Converting form checkbox 'on' value to boolean """
    direct_set_participant_data['has_siblings'] = 'has_siblings' in direct_set_participant_data
    participant = Participant(**direct_set_participant_data)
    participant.save()

    participant.env_exposures.set(env_exposures)
    participant.gene_mutations.set(gene_mutations)
    return redirect('fdn_participant:home')


def register_participant(request):
    all_environmental_exposures = EnvExposure.objects
    all_genetic_mutations = GeneMutation.objects
    context = {'env_exposures': all_environmental_exposures, 'gene_mutations': all_genetic_mutations}
    return render(request, 'fdn_participant/registration.html', context)
