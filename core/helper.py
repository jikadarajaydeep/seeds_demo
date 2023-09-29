from .models import *
from django.http import JsonResponse
from core.schemas import TagUpdateSchema

def get_seedsdata(scan_id):
    try:
        seeds = Seed.objects.all()

        if scan_id:
            seeds = seeds.filter(scan_id=scan_id)   

        seed_data = []

        for seed in seeds:
            tags_data = []
            tags = seed.tags.all()
            assigned_short_names = set()  

            for tag in tags:
                value = tag.value
                short_name = tag.short_name

                if not short_name:
                    base_short_name = value[:1]
                    i = 1
                    while base_short_name in assigned_short_names:
                        i += 1
                        base_short_name = value[:i]

                    short_name = base_short_name
                    assigned_short_names.add(short_name)

                tag_info = {
                    "value": value,
                    "short_name": short_name
                }
                tags_data.append(tag_info)

            seed_info = {
                "id": seed.id,
                "scan_id": seed.scan_id,
                "col": seed.col,
                "row": seed.row,
                "tags": tags_data
            }

            seed_data.append(seed_info)

        return {
            "result": True,
            "data": seed_data
        }
    
    except Exception as e:
        return {
            "result": False,
            "data": None
        }



def get_all_tags_data():
    try:
        tags = Tag.objects.filter(deleted=False)

        tags_data = []

        for tag in tags:
            tag_info = {
                "id": tag.id,
                "type": tag.type,
                "value": tag.value,
                "deleted": tag.deleted,
                "short_name": tag.short_name,
                
            }

            tags_data.append(tag_info)

        return {
            "result": True,
            "data": tags_data,    
        }

    except Exception:
        return {
            "result": False,
            "data": None,
        }
    

def add_tags_data(data):
    try:
        if Tag.objects.filter(type=data.type, value=data.value).exists():
            raise Exception("A tag with the same type and value already exists.")

        tag = Tag.objects.create(
            type=data.type,
            value=data.value,
            deleted=data.deleted,
            short_name=data.short_name
        )

        saved_tag = {
            "id": tag.id,
            "type": tag.type,
            "value": tag.value,
            "deleted": tag.deleted,
            "short_name": tag.short_name,
            "created_at": tag.created_at,
            "updated_at": tag.updated_at,
        }

        response_data = {
            "result": True,
            "data": saved_tag,
        }

        return response_data

    except Exception as e:
        response_data = {
            "result": False,
            "data": str(e)
        }
        return response_data


def delete_tag_data(tag_id):
    try:
        tag = Tag.objects.get(id=tag_id)
        tag.deleted = True
        tag.save()

        response_data = {
            "result": True,
            "message": "Tag deleted successfully."
        }

        return response_data

    except Tag.DoesNotExist:
        response_data = {
            "result": False,
            "message": "Tag not found."
        }
        return JsonResponse(response_data, status=404)
    
    except Exception as e:
        response_data = {
            "result": False,
            "message": "Something went wrong."
        }
        return JsonResponse(response_data, status=400)
    

def update_tag_data(tag_id: int, data: TagUpdateSchema):
    try:
        # Check if the tag exists
        tag = Tag.objects.get(id=tag_id)

        if Tag.objects.filter(type=data.type, value=data.value).exclude(id=tag_id).exists():
            response_data = {
                "result": False,
                "data": "A tag with the same type and value already exists."
            }
            return response_data

        # Update the tag fields based on the data
        if data.type is not None:
            tag.type = data.type
        if data.value is not None:
            tag.value = data.value
        if data.deleted is not None:
            tag.deleted = data.deleted
        tag.short_name = data.short_name

        tag.save()

        updated_tag = {
            "id": tag.id,
            "type": tag.type,
            "value": tag.value,
            "deleted": tag.deleted,
            "short_name": tag.short_name,
        }

        response_data = {
            "result": True,
            "data": updated_tag,
        }

        return response_data

    except Tag.DoesNotExist:
        response_data = {
            "result": False,
            "data": "Tag not found."
        }
        return response_data
    
    except Exception as e:
        response_data = {
            "result": False,
            "data": "Something went wrong."
        }
        return response_data
