# -*- coding:utf-8 -*-
"""
描述作用：使用OpenCv提供的函数，进行摄像头拍照。按q键进行单张拍照，按t键拍照退出
使用说明: 直接运行即可，若程序报错，请检查打开摄像头索引方式
硬件信息：
硬件描述：工业级高清单目摄像头，H043-8814-V2。USB免驱动
购买链接："https://m.tb.cn/h.5YiNvc1?tk=glFTdGEci8S CZ3457"
"""
import time
import cv2
import io
from loguru import logger
from django.conf import settings
from LevelApp.utils import minioUtils
from LevelApp.utils import utils

def getCameraQuantity() -> int:
    """获取可用摄像头数量"""
    quantity = 0
    cap = cv2.VideoCapture()  # 视频流对象
    index = 0
    # 一般一台电脑连接的摄像头数量不会超过5个
    # 普遍情况下最多两个
    while index < 5:
        ret = cap.open(index)
        if ret:
            quantity += 1  # 可用摄像头数量+1
            cap.release()  # 释放打开的摄像头
            index += 1  # 索引+1
        else:
            break  # 一旦遇到打开失败的序号，则没有更多的摄像头了
    return quantity


def getTimeStampForImage() -> str:
    """
    获取当前时间，格式：年月日
    :return:
    """
    from datetime import datetime

    # 获取当前时间戳
    timestamp = datetime.timestamp(datetime.now())

    dt_object = datetime.fromtimestamp(timestamp)

    # 格式化成字符串
    formatted_date = dt_object.strftime("%Y%m%d%H%M%S")

    # 打印结果
    return formatted_date




def getPicturePATH():
    # 设置文件名
    currentTimestamp = getTimeStampForImage()
    fileName = f"C{currentTimestamp}.jpg"  # 组合时间戳图片名
    logger.info("拍摄文件名:" + fileName)
    pictureAddress = f"./images/{fileName}"  # 文件相对保存路径
    return pictureAddress, fileName








def timing(func):
    """
    计算程序运行耗时
    :param func: 函数，修饰器用法
    :return: 内部函数
    """

    def inner():
        startTime = time.time()
        print("开始时间：", startTime)
        func()
        endTime = time.time()
        print("结束时间：", endTime)
        timeDiff = endTime - startTime  # 计算的时间差为程序的执行时间，单位为秒/s
        logger.info("本次拍摄耗时 时间间隔（单位/秒):" + str(timeDiff))

    return inner



def readVideo(boxHeight, boxWidth) -> str:
    """  拍照  """


def openCamera(number):
    """
    打开摄像头
    :param number: 摄像头编号  0表示本机电脑摄像头
    :return: 摄像头状态,相应摄像头信息
    """

    # 打开摄像头
    logger.info("摄像头正在打开中……")
    cap = cv2.VideoCapture(number)
    if cap.isOpened():
        logger.info("摄像头已打开~")
        return True, cap

    logger.error("摄像头打开失败，请检查摄像头是否连接正常！！")
    cap= None

    return False, cap


def takePhoto(cap):
    """
    拍照
    :param cap:  摄像头信息
    :return:
    """
    try:
        # 读取摄像头画面，ret为是否成功打开摄像头,frame为视频的每一帧图像
        ret, frame = cap.read()
        if not ret:
         logger.error("无法获取摄像头画面,请检查摄像头状态!")
         return False, None
        # 获取拍照相对路径
        pictureAddress, fileName = getPicturePATH()
        # 保存校准框内的图像
        cv2.imwrite(pictureAddress, frame)  # 图片保存路径
        # 保存校准框内的图像
        image_byte_stream = io.BytesIO()
        # 将图像转换为字节流
        ret, buffer = cv2.imencode('.jpg', frame)
        if ret:
            image_byte_stream.write(buffer)
            image_byte_stream.seek(0)
            results = utils.picToBase64AndRequestBaiDuApiV2(None, image_byte_stream.read(), fileName)
            print(results)
            logger.info("拍照成功~")
            return True, results
        return False, None
    except Exception as e:
     logger.error(e)
     return False, None


"""
paddlepaddle  离线模型调用方法
"""
def take_photo_pp(cap):
    """
    拍照
    :param cap:  摄像头信息
    :return:
    """
    try:
        # 读取摄像头画面，ret为是否成功打开摄像头,frame为视频的每一帧图像
        ret, frame = cap.read()
        if not ret:
         logger.error("无法获取摄像头画面,请检查摄像头状态!")
         return False, None
        # 获取拍照相对路径
        pictureAddress, fileName = getPicturePATH()
        # 保存校准框内的图像
        cv2.imwrite(pictureAddress, frame)  # 图片保存路径
        # 保存校准框内的图像
        image_byte_stream = io.BytesIO()
        # 将图像转换为字节流
        ret, buffer = cv2.imencode('.jpg', frame)
        if ret:
            image_byte_stream.write(buffer)
            image_byte_stream.seek(0)
            logger.info("拍照成功~")
            return True, image_byte_stream.read(), fileName
        return False, None, None
    except Exception as e:
     logger.error(e)
     return False, None, None


def closeCamera(cap):
    """
    关闭摄像头
    :param cap: 摄像头信息
    """
    # 释放摄像头资源
    if cap.isOpened():
        cap.release()
        logger.info("摄像头已成功关闭~")
        return True
    logger.error("无法关闭摄像头，该摄像头已关闭！")
    return False


def main():
    result, cap = openCamera(1) # 0代表本机摄像头
    if result:
        settings.CAP = cap
        result, results = takePhoto(settings.CAP)
        result = closeCamera(settings.CAP)


if __name__ == '__main__':
    main()
