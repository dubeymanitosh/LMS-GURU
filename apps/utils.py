import string
from random import choice,randint
from django.core.paginator import Paginator
from django.http.response import Http404
from apps.classroom.models import Classroom
from functools import wraps

def members_only(function):
    @wraps(function)
    def wrapper(request, unique_id, *args, **kwargs):
        classroom = Classroom.objects.get(unique_id = unique_id)
        admins = classroom.special_permissions.all()
        members =  admins | classroom.members.all()
        if request.user in members:
            return function(request, unique_id, *args, **kwargs)
        else:
            raise Http404()
    return wrapper

def extension_type(file_name):
	videos = ['WEBM','MPG', 'MP2', 'MPEG','MPE', 'MPV', 'OGG', 'MP4', 'M4P' , 'M4V', 'AVI', 'WMV', 'MOV', 'QT','FLV', 'SWF','MKV']
	images = ["JPG","PNG","GIF","PSD","RAW","BMP","SVG","AI","EPS","JPEG"]
	
	file_extension = str(file_name).split('.')[-1].upper()
	if file_extension in videos:
		return 'video'
	if file_extension in images:
		return 'image'
	return 'other'

def proper_pagination(object,index):
    start_index,end_index = 0,10
    if object.number>index:
        start_index = object.number-index
        end_index = start_index + end_index
    return (start_index,end_index)

def pagination(request,object):
        paginator = Paginator(object,6)
        page_num=1
        if request.GET.get('page'):
            page_num = request.GET.get('page')
        query = paginator.page(page_num)
        start_index,end_index = proper_pagination(query,index=4)
        page_range = list(paginator.page_range)[start_index:end_index]
        return query,page_range

def unique_id():
    characters = string.ascii_letters + string.digits
    return  "".join(choice(characters) for x in range(randint(7,15)))

def filter_fun(key):
	return not key.strip() 