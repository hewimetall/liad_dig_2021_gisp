import datetime
import string, random

from fastapi import Response
from tortoise import fields, models

class FilterModel(models.Model):
    """
    The User model
    """
    json_data_params = fields.JSONField()
    date_create = fields.DatetimeField(auto_now_add=True)
    url = fields.ForeignKeyField('models.UsersAnonModel', related_name="urlclick", null=True)


class RowClickModel(models.Model):
    """
    The click model for clicks on url
    """
    click_id = fields.CharField(max_length=25)
    date_create = fields.DatetimeField(auto_now_add=True)
    user = fields.ForeignKeyField('models.UsersAnonModel', related_name="filters", null=True)


class UsersAnonModel(models.Model):
    """
    The User model
    """
    session_seed = fields.CharField(125)
    reques_data = fields.TextField()
    date_create = fields.DatetimeField(auto_now_add=True)

    @classmethod
    async def next_user(cls, response,meta_data, filters = None):
        value = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(24))
        max_age = 365 * 24 * 60 * 60  # one year

        event = await cls.create(session_seed=value ,reques_data=meta_data)
        response.set_cookie(
            key="trakers",
            value=value,
            max_age=max_age,
        )


class Settings(models.Model):
    is_data_load = fields.BooleanField(default=False)


class RowData(models.Model):
    ID = fields.IntField()
    URL= fields.CharField(128,null=True)
    SMALL_NAME = fields.TextField()
    FULL_NAME = fields.TextField()
    NUMBER_NPA = fields.TextField()
    DATE_NPA = fields.TextField()
    NPA_NAME = fields.TextField()
    DESCRIPTION = fields.TextField()
    PURPOSE = fields.TextField()
    OBJECTIVE = fields.TextField()
    TYPE_MERA = fields.TextField()
    TYPE_FORMAT_SUPPORT = fields.TextField()
    SROK_VOZVRATA = fields.TextField()
    PROCENT_VOZVRATA = fields.TextField()
    GUARANTE_PERIODE = fields.TextField()
    GUARANTEE_COST = fields.TextField()
    APPLIANCE_ID = fields.TextField()
    OKVED2 = fields.TextField()
    COMPLEXITY = fields.TextField()
    AMOUNT_OF_SUPPORT = fields.TextField()
    REGULARITY_SELECT = fields.TextField()
    PERIOD = fields.TextField()
    DOGOVOR = fields.TextField()
    GOS_PROGRAM = fields.TextField()
    EVENT = fields.TextField()
    DOP_INFO = fields.TextField()
    IS_NOT_ACTIVE = fields.TextField()
    PRICHINA_NOT_ACT = fields.TextField()
    REQ_ZAYAVITEL = fields.TextField()
    REQUEST_PROJECT = fields.TextField()
    IS_SOFINANCE = fields.TextField()
    DOLYA_ISOFINANCE = fields.TextField()
    BUDGET_PROJECT = fields.TextField()
    POKAZATEL_RESULT = fields.TextField()
    TERRITORIAL_LEVEL = fields.TextField()
    REGION_ID = fields.TextField()
    RESPONS_STRUCTURE = fields.TextField()
    ORG_ID = fields.TextField()
