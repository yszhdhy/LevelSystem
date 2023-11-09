# 一、开发环境

- windows 11
- jetbrains IDEA 2023

# 二、项目环境：

- jdk 1.8
- springboot 2.3.6.RELEASE
- minio latest 开源的对象存储服务器
- mysql 8.0.30



# 三、配置文件

![image-20231030163203134](./README.assets/image-20231030163203134.png)



# 四、启动项目

![image-20231030163247114](./README.assets/image-20231030163247114.png)

```
接口地址：http://localhost:8080/doc.html#/adminApi/%E5%9B%BE%E7%89%87%E4%B8%8A%E4%BC%A0%E8%AF%86%E5%88%AB%E6%8E%A5%E5%8F%A3/uploadImageFileUsingPOST
```



# 五、介绍

# 5.1 图片识别接口：

![image-20231030163406499](./README.assets/image-20231030163406499.png)

## 5.2 信息数据表

![image-20231030163725698](./README.assets/image-20231030163725698.png)

## 5.2 历史数据表

![image-20231030163514138](./README.assets/image-20231030163514138.png)

## 5.3 合格与否信息数据表

![image-20231030163657579](./README.assets/image-20231030163657579.png)







# Python端：

# 一、开发环境

- windows 11
- jetbrains IDEA 2023

# 二、项目环境：

- python 3.10    语言环境
- django 4.2.3   web框架
- 主要模块：
  - minio latest   开源的对象存储服务器
  - matplotlib 3.7.2   用于绘制数据可视化图表的 Python 库
  - numpy  1.25.1 用于科学计算的 Python 库
  - opencv-python  4.8.0.74 开源计算机视觉库
  - requests  2.31.0  发送 HTTP 请求的 Python 库
  - 其余依赖请详看 `requirements.txt` 文件

# 三、项目启动：

## 3.1 安装依赖：

```shell
pip install -r requirements.txt
```

## 3.2 配置文件

项目所有配置都在 `LevelSystem/LevelSystem/settings.py` 文件中  **（注意：以下是两个必配项）**

1. 百度API配置   模型部署的 API_KEY 以及 SECRET_KEY
   1. 需要配置 `BAIDU_API_KEY`  
   2. 需要配置 `BAIDU_SECRET_KEY`
   3. ![image-20231028164937785](./README.assets/image-20231028164937785.png)
2. minio 配置 
   1. 配置 `MINIO_ACCESS_KEY` 、`MINIO_SECRET_KEY`  都填入minio的密码
   2. 配置 `MINIO_ENDPOINT`   minio 配置的远程API地址  **（注意点： minio有两个端口一个是控制台端口、一个API端口 根据每个人所搭建的minio而定）**
   3. 配置 `MINIO_BUCKET_NAME`  minio中的一个存储桶 也就是此次项目所要使用的存储桶
   4. ![image-20231028165436821](./README.assets/image-20231028165436821.png)

## 3.3 启动项目

**完成以上的操作后 就可以启动项目了** 

1. 启动后端项目

   ```py
   cd .\LevelSystem\
   
   python manage.py runserver 0.0.0.0:8000
   ```

2. 启动前端项目  （找到项目中的前端项目）

   ```py
   yarn install  
   
   yarn dev 
   ```

## 3.4 打开前端页面

```shell
http://127.0.0.1:5173/
```

![image-20231028164136952](./README.assets/image-20231028164136952.png)



# 四、项目流程：

## 4.1 项目架构图：

![image-20231028172007988](./README.assets/image-20231028172007988.png)

## 4.2 用户操作流程

1. 进入到首页：![image-20231028171052032](./README.assets/image-20231028171052032.png)
2. 拍照上传图片![image-20231028171804498](./README.assets/image-20231028171804498.png)
3. 审核图片![image-20231028171251389](./README.assets/image-20231028171251389.png)
4. 进行审核图片![image-20231028171543131](./README.assets/image-20231028171543131.png)
5. 图片预览![image-20231028171609213](./README.assets/image-20231028171609213.png)
6. 点击合格或者不合格后也会有对应条目可以查看![image-20231028171653504](./README.assets/image-20231028171653504.png)



# 五、百度飞浆模型在线部署：

1. 首先需要你将模型训练好：

   ```
   飞浆网址：https://ai.baidu.com/easydl/app/deploy/segment/public
   ```

   ![image-20231028165850634](./README.assets/image-20231028165850634.png)

2. 在线发布模型：![image-20231028165941579](./README.assets/image-20231028165941579.png)

3. 去到API调用文档查看 API调用以及其他详情  

   ```
   网址： https://ai.baidu.com/ai-doc/EASYDL/0k38n3fho#%E6%8E%A5%E5%8F%A3%E6%8F%8F%E8%BF%B0
   ```

   ![image-20231028170440775](./README.assets/image-20231028170440775.png)

4. 去云控制平台查看API![image-20231028170120110](./README.assets/image-20231028170120110.png)

5. 即可查看API调用所需要的参数等![image-20231028170705538](./README.assets/image-20231028170705538.png)



# 六、模型训练步骤

## 6.1 数据采集

### 6.1.1更具气泡位置拍摄不同的图片

**当气泡位于左**

![image-20231028215837412](./README.assets/image-20231028215837412.png)

**当气泡位于中间**

![image-20231028220224560](./README.assets/image-20231028220224560.png)

**当气泡位于右侧**

![image-20231028220242118](./README.assets/image-20231028220242118.png)



### 6.1.2根据水平仪方向

**当水平仪非水平方向放置**

![image-20231028220316878](./README.assets/image-20231028220316878.png)



### 6.1.3 当水平仪加装摄像头时

![image-20231028220536189](./README.assets/image-20231028220536189.png)



## 6.2 图片标注

![image-20231028220655033](./README.assets/image-20231028220655033.png)

![image-20231028220711383](./README.assets/image-20231028220711383.png)

## 6.3 模型训练

### 6.3.1 模型准备

![image-20231028220830258](./README.assets/image-20231028220830258.png)

### 6.3.2 数据准备

![image-20231028221121485](./README.assets/image-20231028221121485.png)

