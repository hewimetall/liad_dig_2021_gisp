from typing import Optional


from fastapi import APIRouter, Response, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi import Cookie
from core.config import templates
from db.model import UsersAnonModel, FilterModel, RowClickModel
from db.run_load_data import save_data


router = APIRouter()

class Item(BaseModel):
    title: str
    subtitl: str
    doc: float


class FormSearch(BaseModel):
    smallName: str
    territorialLevel: str
    regionId: str
    applianceId: str
    okvedId: str
    classificatorMera: str
    okrugId: str
    complexityId: str
    npaStartDate: str
    npaEndDate: str
    contestsStartDate: str
    contestsEndDate: str
    stageId: str
    sizeEnterpriseId: str
    date: str
    status: str
    state: str
    similarMeasures: str


@router.get("/")
async def view_proxi(request: Request, trakers: Optional[str] = Cookie(None)):
    response = templates.TemplateResponse("Nev_template.html", {"request": request, })
    if not trakers:
        await UsersAnonModel.next_user(response,request.headers)
    return response

@router.get("/navigator-measures/ru-RU")
async def view_proxi(request: Request, trakers: Optional[str] = Cookie(None)):
    regionId = [int(item_value) for item_key, item_value in request.query_params._list if "regionId" in item_key and item_value !='']
    applianceId = [int(item_value) for item_key, item_value in request.query_params._list if "applianceId" in item_key and item_value !='']
    fotex = None # recomendet row
    response = templates.TemplateResponse("Nev_template.html", {"request": request,"smallName": request.query_params.get('smallName', "Текст"), "regionId": regionId, 'applianceId': applianceId, "fotex":fotex})
    if not trakers:
        await UsersAnonModel.next_user(response,request.headers)
    user = await UsersAnonModel.get(session_seed=trakers)
    await FilterModel.create(json_data_params=request.query_params._list, url = user)
    response.set_cookie(key="old_page_url", value=request.url)
    return response


@router.get("/navigator-measures/{rest_of_path:path}")
async def link_use(gispId: int, request: Request , trakers: Optional[str] = Cookie(None)):
    response = templates.TemplateResponse("elem_selected.html",{"request":request, })
    if not trakers:
        await UsersAnonModel.next_user(response,request.headers)
    user = await UsersAnonModel.get(session_seed=trakers)

    await RowClickModel.create(click_id=gispId, user=user)
    return response


@router.get("support-measures/list/{gispId}/")
async def link_use(gispId: int, request: Request , trakers: Optional[str] = Cookie(None)):
    response = templates.TemplateResponse("elem_selected.html",{"request":request, })
    if not trakers:
        await UsersAnonModel.next_user(response,request.headers)
    user = await UsersAnonModel.get(session_seed=trakers)

    await RowClickModel.create(click_id=gispId, user=user)
    return response



@router.get("/load_data/")
async def link_use():
    await save_data()
    return "OK"
