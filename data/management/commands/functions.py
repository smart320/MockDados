#import Django
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required, user_passes_test
#import Django User
from company.models import Company
#from supplier.models import Supplier
#from .prices import calc_tar_azul_seco
# Import Python
import decimal
import json
import datetime
from datetime import timedelta
from pandas import pandas as pd


def permission_group(user):
    '''
    Verifica grupo( empresa ) logada
    :param user:
    :return:
    '''
    group_user_qs = Group.objects.filter(user=user)
    group_user_str = list(group_user_qs)
    if len(group_user_str) >= 1:
        group_user_str_1 = str(group_user_str[0])
        print(group_user_str_1)
        print(type(group_user_str_1))
    else:
        return None

    if group_user_str_1 == 'Admin':
        return group_user_str_1
    else:
        return group_user_str_1


def validate_date(day, month, year):
    '''
    Valida date if values == 0
    :param day:
    :param month:
    :param year:
    :return:
    '''
    if day == '0':
        d = 1
    else:
        d = day

    if month == '0':
        m = 1
    else:
        m = month

    if year == '0':
        y = 2016
    else:
        y = year

    return (d, m, y)


def concat_date(day, month, year):
    '''
    Concate date to date time string
    :param day:
    :param month:
    :param year:
    :return:
    '''
    dict = {}
    vardate = str(day) + '-' + str(month) + '-' + str(year)
    start_date = vardate + ' 00:00'
    end_date = vardate + ' 23:59'
    start_datep = vardate + ' 18:00'
    end_datep = vardate + ' 20:59'
    dict['start_date'] = start_date
    dict['end_date'] = end_date
    dict['start_datep'] = start_datep
    dict['end_datep'] = end_datep
    return dict





def day_in_month(month, year=2016):
    '''
     Retorna a quantidade de dias no mes correspondente
     checa se ano é bissexto ou não
    :param month: mes
    :return: dias dos meses
    '''
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        bissexto = True
    else:
        bissexto = False

    if month <=12 and month >=1:
        if bissexto == False:
            DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            return  DAYS_IN_MONTH[month]
        else:
            DAYS_IN_MONTH = [-1, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            return DAYS_IN_MONTH[month]
    else:
        return None


def statistics_pd(df, field):
    '''
    Calcula Estatisticas de um Data Frame Usando Pandas Describe
    :param pd:
    :return:
    '''
    pdf = pd.to_numeric(df[field], errors='coerce')
    df_describe = pdf.mask(df == 0.00).describe(percentiles=[0.1, 0.25, 0.50, 0.80], include='all')
    #df_describe = pdf.describe(percentiles=[0.1, 0.25, 0.50, 0.80], include='all')
    df_describe_json = df_describe.to_json()
    return df_describe


def sum_mean_pd(df, *args):
    '''
    Calcula Estatisticas de um Data Frame Usando Pandas Describe
    :param pd:
    :return:
    'consumo_total_day'
    'consumo_ponta_day'
    'consumo_fora_ponta_day'
    '''
    dict = {}
    len_args = len(args)
    print(f'len array: {len_args}')
    co_total_f = pd.to_numeric(df[args[0]], errors='coerce')
    sum_total = co_total_f.sum()
    co_ponta_f = pd.to_numeric(df[args[1]], errors='coerce')
    sum_ponta = co_ponta_f.sum()
    mean_ponta = co_ponta_f.mean()
    co_fponta_f = pd.to_numeric(df[args[2]], errors='coerce')
    sum_fponta = co_fponta_f.sum()
    mean_fponta = co_fponta_f.mean()
    dict['sum'] = sum_total
    dict['sum_ponta'] = sum_ponta
    dict['sum_fora_ponta'] = sum_fponta
    dict['mean_ponta'] = mean_ponta
    dict['mean_fora_ponta'] = mean_fponta
    result = json.dumps(dict)
    return result


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


def converte_datetime(hora_string):
    '''
    Converte string to date time
    :param hora_string:
    :return:
    '''
    timereference = '00:00:00.0'
    basetimeconcate = hora_string + ' ' + timereference
    date_time_obj = datetime.datetime.strptime(basetimeconcate, '%d-%m-%Y %H:%M:%S.%f')
    return date_time_obj


class DecimalEncoder(json.JSONEncoder):
    '''
    Conver em Decimal
    '''
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return {'__Decimal__': str(obj)}
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


