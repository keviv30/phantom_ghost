import csv
from django.core.exceptions import ObjectDoesNotExist
from ghosts.models import GhostName, GhostUser


def crate_ghost_names():
    '''
    Bulk upload ghost names
    '''
    with open('ghosts/resources/ghost_names.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            GhostName.objects.get_or_create(
                name=row[0], description=row[1]
            )


def get_ghost_user(request):
    '''
    Return ghost user if available
    '''
    if request.user and request.user.id is not None:
        try:
            return GhostUser.objects.get(user=request.user)
        except ObjectDoesNotExist:
            # log the exception if needed
            pass

    return None
