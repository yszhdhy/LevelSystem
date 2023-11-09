from django.conf import settings
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from LevelApp.utils import utils
from LevelApp.utils import minioUtils
from LevelApp.utils import TakePhotoForAIUtil
from LevelApp.utils import jsonUtil
from LevelApp.utils import linear_straightness_checker
import json
import requests
import base64
import io

"""
pip install django-storages
pip install channels
pip install django-cors-headers
"""

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# from django.core.files.storage import default_storage
from django.http import JsonResponse


# from django.views.decorators.csrf import csrf_exempt
# from minio import Minio
# from urllib3.exceptions import ResponseError
# import datetime


@csrf_exempt
def upload_photo(request):
    try:
        if request.method == 'POST' and request.FILES.get('photo'):
            photo = request.FILES['photo']
            url = minioUtils.upload_photo(photo)
            return JsonResponse({'imageUrl': url}, status=200)
        else:
            return JsonResponse({'error': 'Invalid request'}, status=400)

    except Exception as e:
        print("Error:", str(e))
        return JsonResponse({'error': 'Internal Server Error'}, status=500)


"""
主页
"""
def html(request):
    return render(request, "html.html")


"""
上传图片并识别
"""
@csrf_exempt
def baidu(request):
    print(request.method)
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']
        image_name = uploaded_image.name
        print(image_name+"============")
        results = utils.picToBase64AndRequestBaiDuApiV2(None, uploaded_image.read(), image_name)
        results1 = []
        results1.append(results)
        return JsonResponse({'data': results1, 'code': 200}, status=200)

    return JsonResponse({'data': 'fail', 'code': 500}, status=500)


"""
调用摄像头拍照上传并识别
"""
@csrf_exempt
def photograph(request):
    result, results = TakePhotoForAIUtil.takePhoto(settings.CAP)
    if result:
        results1 = []
        results1.append(results)
        return JsonResponse({'data': results1, 'code': 200}, status=200)
    return JsonResponse({'data': 'fail', 'code': 500}, status=500)


"""
开启摄像头
"""
@csrf_exempt
def openCamera(request):
    result, cap = TakePhotoForAIUtil.openCamera(settings.CAP_NUMBER)
    if result:
        settings.CAP = cap
        print(settings.CAP)
        return JsonResponse({'data': 'success', 'code': 200}, status=200)
    return JsonResponse({'data': 'fail', 'code': 500}, status=500)


"""
关闭摄像头
"""


@csrf_exempt
def closeCamera(request):
    print(settings.CAP)
    result = TakePhotoForAIUtil.closeCamera(settings.CAP)
    if result:
        return JsonResponse({'data': 'success', 'code': 200}, status=200)
    return JsonResponse({'data': 'fail', 'code': 500}, status=500)


"""
查询照片
"""

@csrf_exempt
def get_list(request):
    atlas_type = request.GET.get('atlas_type', None)
    data = jsonUtil.read_json_file(settings.JSON_FILE_PATH)
    result = jsonUtil.query_all_issue_data(data, atlas_type)
    if result:
        return JsonResponse({'data': result, 'code': 200}, status=200)
    return JsonResponse({'data': [], 'code': 200}, status=200)


"""
保存照片
"""
@csrf_exempt
def save(request):
    if request.method == 'POST':
        try:
            json_data = jsonUtil.read_json_file(settings.JSON_FILE_PATH)
            # 解析请求的JSON数据
            data = json.loads(request.body)
            atlas_type = data.get('atlas_type')

            id = json_data[settings.JSON_COUNT][atlas_type]
            data["id"] = id  # 设置id
            json_data[settings.JSON_COUNT][atlas_type] = id + 1  # 自增

            data_json = jsonUtil.add_data_json(json_data, atlas_type, data)

            return JsonResponse({'data': 'success', 'code': 200}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'data': 'fail', 'code': 500}, status=500)
    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=500)

@csrf_exempt
def update(request):
    if request.method == 'POST':
        try:
            json_data = jsonUtil.read_json_file(settings.JSON_FILE_PATH)
            # 解析请求的JSON数据
            data = json.loads(request.body)
            atlas_type = data.get('atlas_type')

            data_json = jsonUtil.update_data(json_data, atlas_type, data)

            return JsonResponse({'data': 'success', 'code': 200}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'data': 'fail', 'code': 500}, status=500)
    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=500)

"""
删除
"""
@csrf_exempt
def delete(request):
    atlas_type = request.GET.get('atlas_type', None)
    id = request.GET.get('id', None)
    print(atlas_type)
    print(id)
    data = jsonUtil.read_json_file(settings.JSON_FILE_PATH)
    result = jsonUtil.delete_data(data, atlas_type, id)
    if result:
        return JsonResponse({'data': result, 'code': 200}, status=200)
    return JsonResponse({'data': 'fail', 'code': 500}, status=500)



"""
paddlepaddle  离线模型
"""
@csrf_exempt
def pp_upload(request):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']
        image_name = uploaded_image.name
        files = {'image': uploaded_image.read()}
        # 请求模型
        response = requests.post(settings.INTERFACE_ADDRESS, files=files)

        loads = json.loads(response.text)
        print(response.text)
        image_bytes = base64.b64decode(loads["image"])  # 转bytes
        bytes_io = io.BytesIO(image_bytes)  # 为了适应工具类 使用io进行封装
        photo_url = minioUtils.upload_photo_stream(bytes_io, image_name)
        return JsonResponse({'data': photo_url, 'code': 200}, status=200)

    return JsonResponse({'data': 'fail', 'code': 500}, status=500)

@csrf_exempt
def pp_photograph(request):
    result, results, image_name = TakePhotoForAIUtil.take_photo_pp(settings.CAP)
    if result:
        files = {'image': results}
        # 请求模型
        response = requests.post(settings.INTERFACE_ADDRESS, files=files)
        loads = json.loads(response.text)
        print(loads["json_data"])
        image_bytes = base64.b64decode(loads["image"])  # 转bytes
        bytes_io = io.BytesIO(image_bytes)  # 为了适应工具类 使用io进行封装
        photo_url = minioUtils.upload_photo_stream(bytes_io, image_name)
        return JsonResponse({'data': photo_url, 'code': 200}, status=200)
    return JsonResponse({'data': 'fail', 'code': 500}, status=500)

""""
误差计算
"""
@csrf_exempt
def statistical_errors(request):
    # 读取json文件
    json_data = jsonUtil.read_json_file(settings.JSON_FILE_PATH)
    error = linear_straightness_checker.calculate_straightness_error(
        jsonUtil.query_all_issue_data(json_data, settings.DISPLACEMENTS), settings.LEVEL_LENGTH)

    # 清空 偏移数组
    json_data[settings.DISPLACEMENTS] = []
    # 写入JSON文件
    jsonUtil.write_json_file(settings.JSON_FILE_PATH, json_data)

    if error:
        return JsonResponse({'data': error, 'code': 200}, status=200)
    return JsonResponse({'data': 'fail', 'code': 500}, status=500)
