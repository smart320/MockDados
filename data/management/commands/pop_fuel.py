import random
import datetime
from ...models import FuelData
import datetime
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = 'Displays current time'

    #def popula_consumo(self):
    def handle(self, *args, **kwargs):
        data = []
        dts = [dt.strftime('%d-%m-%Y T%H:%M:%S') for dt in
               datetime_range(datetime.datetime(2020, 1, 1, 0, 0), datetime.datetime(2020, 1, 31, 23, 59),
               datetime.timedelta(minutes=15))]

        #print(dts)
        #print(len(dts))
        datalen = len(dts)

        for x in range(0, datalen):
            # print(random.randint(1, 10))
            # print(random.randint(1550, 3890) / 10)

            p = FuelData(fuel=random.randint(15, 30),
                            ts=converte_datetime1(dts[x]),
                            device_id=3
                            )
            data.append(p)
            print(x)
            print(converte_datetime1(dts[x]))
            #p.save()
        #print(data)
        FuelData.objects.bulk_create(data)
        return p


def converte_datetime1(hora_string):
    '''
    Converte string to date time
    :param hora_string:
    :return:
    '''
    #timereference = '00:00:00.0'
    #basetimeconcate = hora_string + ' ' + timereference
    date_time_obj = datetime.datetime.strptime(hora_string, '%d-%m-%Y T%H:%M:%S')
    return date_time_obj


def datetime_range(start, end, delta):
    '''
    Range de Time Stamp
    :param start:
    :param end:
    :param delta:
    :return:
    '''
    current = start
    while current < end:
        yield current
        current += delta