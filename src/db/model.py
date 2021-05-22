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

