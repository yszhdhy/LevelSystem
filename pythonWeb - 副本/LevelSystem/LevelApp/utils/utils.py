import matplotlib

# 作为非交互的模式避免线程冲突
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
import requests
import io
import json
from loguru import logger
import base64
import math
from datetime import datetime
import os
from django.conf import settings
from LevelApp.utils import minioUtils
from django.http import JsonResponse
from LevelApp.utils import jsonUtil


# 生成当前时间戳，用于拼接日志文件名
timestamp = datetime.now().strftime("%Y-%m-%d")
logger.add(f"logs/baiduApi_{timestamp}.log", retention="1 days", level='INFO')

# 设置支持中文字符的字体为 "SimHei"
plt.rcParams['font.family'] = 'SimHei'




def picToBase64AndRequestBaiDuApiV2(ACCESS_TOKEN=None, image_data=None, image_name=None):
    # top_num: 返回的分类数量，不声明的话默认为 6 个
    PARAMS = {"top_num": settings.BAIDU_PARAMS}
    # 否则，留空 ACCESS_TOKEN，于下方填入该模型部署的 API_KEY 以及 SECRET_KEY，会自动申请并显示新 ACCESS_TOKEN
    API_KEY = settings.BAIDU_API_KEY
    SECRET_KEY = settings.BAIDU_SECRET_KEY
    # 服务详情中的接口地址
    MODEL_API_URL = settings.BAIDU_MODEL_API_URL

    base64_data = base64.b64encode(image_data)
    base64_str = base64_data.decode('UTF8')
    PARAMS["image"] = base64_str

    if not ACCESS_TOKEN:
        auth_url = settings.BAIDU_TOKEN_URL + "&client_id={}&client_secret={}".format(
            API_KEY, SECRET_KEY)
        auth_resp = requests.get(auth_url)
        auth_resp_json = auth_resp.json()
        ACCESS_TOKEN = auth_resp_json["access_token"]
    else:
        logger.info("新 ACCESS_TOKEN: {}".format(ACCESS_TOKEN))

    request_url = "{}?access_token={}".format(MODEL_API_URL, ACCESS_TOKEN)
    response = requests.post(url=request_url, json=PARAMS)
    response_json = response.json()
    response_str = json.dumps(response_json, indent=4, ensure_ascii=False)
    logger.info("结果:{}".format(response_str))

    results = response_json["results"]
    photo_url = draw_all_shapes(image_data, results, image_name)
    print(photo_url)
    return photo_url


def draw_all_shapes(image_data, results, image_name):
    try:
        # 将图片数据转换为PIL图像
        img = Image.open(io.BytesIO(image_data))
        # img = Image.open(image_path)
        plt.imshow(img)
        plt.axis('off')  # 关闭坐标轴标签
        ax = plt.gca()

        colors = ['r', 'g', 'b', 'c', 'm', 'y']

        # 绘制所有识别到的图形
        for i, result in enumerate(results):
            location = result["location"]
            color = colors[i % len(colors)]
            left, top, right, bottom = (
                location["left"],
                location["top"],
                location["left"] + location["width"],
                location["top"] + location["height"],
            )
            rect = plt.Rectangle((left, top), location["width"], location["height"],
                                 linewidth=1, edgecolor=color, facecolor='none')
            ax.add_patch(rect)

        # 根据 top 值对刻度点进行排序
        results_sorted = sorted([result for result in results if result["name"] == "刻度点"],
                                key=lambda x: x["location"]["top"])

        # 寻找 top 值最相近的两个刻度点
        min_diff = float('inf')
        closest_ticks = None

        for i in range(len(results_sorted) - 1):
            diff = abs(results_sorted[i]["location"]["top"] - results_sorted[i + 1]["location"]["top"])
            if diff < min_diff:
                min_diff = diff
                closest_ticks = [results_sorted[i], results_sorted[i + 1]]

        """
        计算出两根刻度线之间的距离
        """
        ScaleLineDistance = abs(closest_ticks[0]["location"]["left"] - closest_ticks[1]["location"]["left"]) / 6
        logger.info("两根刻度线之间的距离：'{}'".format(ScaleLineDistance))

        center_point = {}
        # 绘制两个刻度点的中心点
        for i, tick in enumerate(closest_ticks):
            location = tick["location"]
            color = colors[i % len(colors)]
            left, top, right, bottom = (
                location["left"],
                location["top"],
                location["left"] + location["width"],
                location["top"] + location["height"],
            )
            center_x = (left + right) / 2
            center_y = (top + bottom) / 2
            plt.scatter(center_x, center_y, color=color, marker='x', s=10, label=f'刻度点 {i + 1}')

            center_point["point" + str(i)] = [center_x, center_y]
            # 输出 top 值

        center_x1, center_y1 = center_point["point0"]
        center_x2, center_y2 = center_point["point1"]
        # 绘制连接线
        # 绘制连接线
        plt.plot([center_x1, center_x2], [center_y1, center_y2], color='k', linestyle='-', linewidth=1, label='top连接线')

        # 计算连接线的中心点坐标
        center_x_line = (center_x1 + center_x2) / 2
        center_y_line = (center_y1 + center_y2) / 2

        # 绘制连接线的中心点
        plt.scatter(center_x_line, center_y_line, color='y', marker='o', s=10, label='top连接线中心点')
        top_center_point = [center_x_line, center_y_line]  # 保存中心点

        # 根据 left 值对刻度点进行排序
        results_sorted_left = sorted([result for result in results if result["name"] == "刻度点"],
                                     key=lambda x: x["location"]["left"])

        # 寻找 top 值最相近的两个刻度点
        min_diff_left = float('inf')
        closest_ticks_left = None
        print(min_diff_left)
        for i in range(len(results_sorted_left) - 1):
            diff = abs(results_sorted_left[i]["location"]["left"] - results_sorted_left[i + 1]["location"]["left"])
            if diff < min_diff_left:
                min_diff_left = diff
                closest_ticks_left = [results_sorted_left[i], results_sorted_left[i + 1]]

        # 绘制两个刻度点的中心点
        for i, tick in enumerate(closest_ticks_left):
            location = tick["location"]
            color = colors[i % len(colors)]
            left, top, right, bottom = (
                location["left"],
                location["top"],
                location["left"] + location["width"],
                location["top"] + location["height"],
            )
            center_x = (left + right) / 2
            center_y = (top + bottom) / 2
            plt.scatter(center_x, center_y, color=color, marker='x', s=10, label=f'刻度点 {i + 1}')

            center_point["point" + str(i)] = [center_x, center_y]
            # 输出 top 值
            # plt.text(center_x, center_y, str(location["top"]), fontsize=12, color=color, ha='center', va='bottom')

        center_x1, center_y1 = center_point["point0"]
        center_x2, center_y2 = center_point["point1"]
        # 绘制连接线
        plt.plot([center_x1, center_x2], [center_y1, center_y2], color='k', linestyle='-', linewidth=1, label='left连接线')

        # 计算连接线的中心点坐标
        center_x_line = (center_x1 + center_x2) / 2
        center_y_line = (center_y1 + center_y2) / 2

        # 绘制连接线的中心点
        plt.scatter(center_x_line, center_y_line, color='b', marker='o', s=10, label='left 连接线中心点')

        left_center_point = [center_x_line, center_y_line]  # 保存中心点

        """
        绘制刻度线的中心点
        """
        tickMarks_center_point = [top_center_point[0], left_center_point[1]]
        plt.scatter(tickMarks_center_point[0], tickMarks_center_point[1], color='g', marker='o', s=10, label='刻度线中心点')
        logger.info("度线中心点：'{}'".format(tickMarks_center_point))

        bubbles_center_point = []
        bubbles_distances = []
        # 绘制气泡的中心点
        bubbles = [result for result in results if result["name"] == "气泡"]
        for i, bubble in enumerate(bubbles):
            location = bubble["location"]
            color = colors[i % len(colors)]
            left, top, right, bottom = (
                location["left"],
                location["top"],
                location["left"] + location["width"],
                location["top"] + location["height"],
            )
            center_x = (left + right) / 2
            center_y = (top + bottom) / 2
            plt.scatter(center_x, center_y, color=color, marker='o', s=10, label='气泡中心点')
            bubbles_center_point = [center_x, center_y]  # 保存气泡中心点

            # 计算气泡轮廓左上角和右上角的点之间的距离（水平距离）
            distance = right - left
            bubbles_distances.append(distance)  # 保存气泡轮廓的距离


        """
        计算气泡轮廓左侧到右侧的距离的二分之一  ScaleLineDistance
        """
        bubbles_distance_half = bubbles_distances[0] / 2
        logger.info("气泡轮廓左侧到右侧的距离的二分之一：'{}'".format(bubbles_distance_half))

        """
        绘制连接线 并计算距离
        """
        logger.info("气泡中心点：'{}'".format(bubbles_center_point))
        # 计算两点之间的距离
        distance = distance_between_points(tickMarks_center_point[0], tickMarks_center_point[1],
                                           bubbles_center_point[0], bubbles_center_point[1])

        logger.info("两点之间的距离：'{}'".format(distance))
        bubble_left_scale = (distance - bubbles_distance_half) / ScaleLineDistance
        bubble_right_scale = (distance + bubbles_distance_half) / ScaleLineDistance

        logger.info("气泡在刻度线：'第{}根'到'{}根之间'".format(bubble_left_scale, bubble_right_scale))

        # 添加图例
        plt.legend(loc='upper right', fontsize=7)


        # 计算偏移
        displacement = distance / ScaleLineDistance * 30

        """
        计算气泡在刻度线中心点的左侧还是右侧
        """
        bubble_placement = ''
        if (tickMarks_center_point[0] - bubbles_center_point[0]) > 0:
            bubble_placement = '左侧'
            displacement = -displacement
        elif (tickMarks_center_point[0] - bubbles_center_point[0]) == 0:
            bubble_placement = '中心'
        else:
            bubble_placement = '右侧'

        logger.info("气泡在刻度线中心点的：'{}'".format(bubble_placement))
        logger.info("气泡偏移为：'{}'".format(displacement))


        # 保存绘制的图片到本地
        # save_path = os.path.join(settings.MEDIA_ROOT, "result_image.png")
        # plt.savefig(save_path, bbox_inches='tight')

        # plt.show()
        # 将绘制的图像保存到字节流中而不是本地文件
        image_byte_stream = io.BytesIO()
        plt.savefig(image_byte_stream, format='png', bbox_inches='tight')
        # 上传到minio中
        photo_url = minioUtils.upload_photo_stream(image_byte_stream, image_name)
        plt.close()

        # 读取json文件
        json_data = jsonUtil.read_json_file(settings.JSON_FILE_PATH)


        # 写如json中
        jsonUtil.add_data_json(json_data, settings.DISPLACEMENTS, displacement)


        photo_results = {}

        photo_results.setdefault('ScaleLineDistance', ScaleLineDistance)
        photo_results.setdefault('tickMarks_center_point', tickMarks_center_point)
        photo_results.setdefault('bubble_placement', bubble_placement)
        photo_results.setdefault('bubbles_distance_half', bubbles_distance_half)
        photo_results.setdefault('bubbles_center_point', bubbles_center_point)
        photo_results.setdefault('distance', distance)
        photo_results.setdefault('bubble_left_scale', bubble_left_scale)
        photo_results.setdefault('bubble_right_scale', bubble_right_scale)
        photo_results.setdefault('photo_url', photo_url)
        photo_results.setdefault('displacements', jsonUtil.query_all_issue_data(json_data, settings.DISPLACEMENTS))
        return photo_results

    except Exception as e:
        print("Error:", str(e))
        return {}
        # return JsonResponse({'error': f'绘图时出现错误:{e}', 'code': 500}, status=500)


def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


"""
电脑像素值
"""
def ppi():
    # Given values
    horizontal_pixels = 2560
    vertical_pixels = 1440
    screen_size_inch = 15.6
    # Calculate PPI
    ppi = math.sqrt(horizontal_pixels ** 2 + vertical_pixels ** 2) / screen_size_inch
    return ppi
