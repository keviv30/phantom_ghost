import csv
from ghosts.models import GhostName


def crate_ghost_names():
    '''
    Bulk upload ghost names
    '''
    with open('ghosts/resources/ghost_names.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print(row[1])
            GhostName.objects.get_or_create(
                name=row[0], description=row[1]
            )
