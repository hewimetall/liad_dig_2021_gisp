import csv


from db.model import RowData
from db.model import Settings


array_row = ['ID', 'URL', 'SMALL_NAME', 'FULL_NAME', 'NUMBER_NPA', 'DATE_NPA', 'NPA_NAME', 'DESCRIPTION', 'PURPOSE', 'OBJECTIVE', 'TYPE_MERA', 'TYPE_FORMAT_SUPPORT', 'SROK_VOZVRATA', 'PROCENT_VOZVRATA', 'GUARANTE_PERIODE', 'GUARANTEE_COST', 'APPLIANCE_ID', 'OKVED2', 'COMPLEXITY', 'AMOUNT_OF_SUPPORT', 'REGULARITY_SELECT', 'PERIOD', 'DOGOVOR', 'GOS_PROGRAM', 'EVENT', 'DOP_INFO', 'IS_NOT_ACTIVE', 'PRICHINA_NOT_ACT', 'REQ_ZAYAVITEL', 'REQUEST_PROJECT', 'IS_SOFINANCE', 'DOLYA_ISOFINANCE', 'BUDGET_PROJECT', 'POKAZATEL_RESULT', 'TERRITORIAL_LEVEL', 'REGION_ID', 'RESPONS_STRUCTURE', 'ORG_ID']


async def save_data():
    with open('db/data_gisp.csv', encoding="windows-1251") as File:
        if len(await Settings.filter(is_data_load=False)) >0:
            return
        File.readline()
        reader = csv.reader(File, delimiter=';')
        for row in reader:
            dict_q = {}
            for i in range(len(array_row)):
                if row[i] == '':
                    row[i] = '+'
                dict_q[array_row[i]] = row[i]
            await RowData.create(**dict_q)
        await Settings.create()
