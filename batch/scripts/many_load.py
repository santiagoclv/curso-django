import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Region, Iso, State, Category

def get_float_or_none(value):
    try:
        ft = float(value)
    except:
        ft = None
    return ft

def get_int_or_none(value):
    try:
        it = int(value)
    except:
        it = None
    return it

def run():
    print("Comenzando el proceso. \n")
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)

    print("Limpiando tablas. \n")
    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()

    print("Cargando datos: \n")
    # name,description,justification,year,longitude,latitude,area_hectares,category,states,region,iso
    for row in reader:
        print('\t {} \n'.format(row[0]))
        year = get_int_or_none(row[3])
        longitude = get_float_or_none(row[4])
        latitude = get_float_or_none(row[5])
        area_hectares = get_float_or_none(row[6])
        category, created = Category.objects.get_or_create(name=row[7])
        state, created = State.objects.get_or_create(name=row[8])
        region, created = Region.objects.get_or_create(name=row[9])
        iso, created = Iso.objects.get_or_create(name=row[10])

        s = Site( name=row[0], description=row[1],
                  justification=row[2], year=year,
                  longitude=longitude, latitude=latitude, area_hectares=area_hectares,
                  region=region, iso=iso,
                  state=state, category=category)
        s.save()

    print("El proceso ha terminado. \n")