# Generated by Django 4.1.3 on 2022-11-16 18:14

from django.db import migrations

def load_initial_data(apps, schema_editor):
    # get our model
    # get_model(appname, modelname)
    room_model = apps.get_model('reservations', 'Room')
    room_model.objects.create (
        room_number=1, room_type="Single", floor=1
        )
    room_model.objects.create(
        room_number=2, room_type="Double", floor=1
    )
    room_model.objects.create(
        room_number=3, room_type="Triple", floor=2
    )
    room_model.objects.create(
        room_number=4, room_type="Quad", floor=2
    )
    room_model.objects.create(
        room_number=5, room_type="King", floor=2
    )
    room_model.objects.create(
        room_number=6, room_type="Queen", floor=3
    )
    room_model.objects.create(
        room_number=7, room_type="Studio", floor=3
    )

class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_room_floor_room_room_number_room_room_type'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]
