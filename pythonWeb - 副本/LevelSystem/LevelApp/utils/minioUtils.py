from django.conf import settings
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from minio import Minio
from urllib3.exceptions import ResponseError
import datetime


"""
上传图片
"""
def upload_photo(photo):
    try:
        minio_client = Minio(
            settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=settings.MINIO_SECURE,
        )

        # Ensure the bucket exists
        bucket_name = settings.MINIO_BUCKET_NAME
        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name)

        # Generate a unique file name
        current_datetime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        file_name = f"{current_datetime}/{photo.name}"

        # Upload the photo to MinIO
        minio_client.put_object(
            bucket_name,
            file_name,
            photo,
            length=photo.size,
            content_type=photo.content_type,
        )

        # Generate a pre-signed URL for the uploaded photo
        photo_url = minio_client.presigned_get_object(bucket_name, file_name)

        return photo_url
    except Exception as e:
        print("Error:", str(e))
        return JsonResponse({'error': 'Internal Server Error'}, status=500)


def upload_photo_stream(photo, image_name):
    try:
        minio_client = Minio(
            settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=settings.MINIO_SECURE,
        )

        # Ensure the bucket exists
        bucket_name = settings.MINIO_BUCKET_NAME
        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name)

        # Generate a unique file name
        current_datetime = datetime.datetime.now().strftime('%Y%m%d')
        file_name = f"{current_datetime}/{image_name}"

        # Create a new BytesIO object and copy the contents of image_byte_stream into it
        # photo_copy = io.BytesIO()
        photo.seek(0)  # Move the pointer to the beginning of the stream
        # photo_copy.write(photo.read())  # Copy the data from image_byte_stream to photo_copy


        # Upload the photo to MinIO
        minio_client.put_object(
            bucket_name,
            file_name,
            photo,
            length=photo.getbuffer().nbytes,
            content_type='image/png',
        )
        # Generate a pre-signed URL for the uploaded photo
        photo_url = minio_client.presigned_get_object(bucket_name, file_name)
        return photo_url
    except Exception as e:
        print("Error:", str(e))
        return JsonResponse({'error': 'Internal Server Error'}, status=500)
