from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import EnvExposure, GeneMutation, Participant


def home(request):
    participants = Participant.objects
    participant_count = participants.count()
    context = {'participants': participants, 'participant_count': participant_count}
    return render(request, 'fdn_participant/home.html', context)


def update_reviewed_status(request):
    print('in update review status view')
    participant_key = request.GET['participant_key']
    new_reviewed_status = request.GET['new_reviewed_status']
    print('Data Retrieved: ' + participant_key + " : " + new_reviewed_status)
    participant = get_object_or_404(Participant, pk=participant_key)
    participant.reviewed_status = new_reviewed_status
    participant.save()

    # return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponse('success')


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
