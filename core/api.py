from ninja import NinjaAPI
from typing import List
from core.helper import *
from core.schemas import *
api = NinjaAPI()

@api.get("/seeds/{scan_id}", response={200: SeedsDataResponse, 400: dict, 401: dict})
def get_seed(request, scan_id: int):
    try:
        return get_seedsdata(scan_id) 
    except Exception as e:
        raise Exception(status_code=500, detail=str(e))


@api.get("/tags", response={200: Taginfos, 400: dict, 401: dict})
def get_tag(request):
    try:
        return get_all_tags_data() 
    except Exception as e:
        raise Exception(status_code=500, detail=str(e))


@api.post("/tags", response={200: TagAddOut, 400: dict, 401: dict})
def add_tag(request, data: TagData):
    try:
        return add_tags_data(data) 

    except Exception as e:
        raise Exception(status_code=500, detail=str(e))
    

@api.delete("/tags/{tag_id}",response={200: DeleteOut, 401: dict, 400:dict})
def delete_tag(request, tag_id):
    try:    
        return delete_tag_data(tag_id)
    except Exception as e:
        raise Exception(status_code=500, detail=str(e))
    

@api.put("/tags/{tag_id}", response={200: TagUpdateResponse, 401: dict, 400:dict})
def update_tag(request, tag_id:int, data: TagUpdateSchema):
    try:
        return update_tag_data(tag_id,data)
    except Exception as e:
        raise Exception(status_code=500, detail=str(e))
    