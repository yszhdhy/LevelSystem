<template>
  <a-upload-dragger
      style="width: 40vw"
      v-model:fileList="fileList"
      :before-upload="beforeUpload"
      :multiple="true"
      directory
      @change="handleChange"
      @drop="handleDrop"
      :showUploadList="false"
  >
    <p class="ant-upload-drag-icon">
      <inbox-outlined></inbox-outlined>
    </p>
    <p class="ant-upload-text">点击上传或将文件夹拖拽到此区域</p>
    <p class="ant-upload-hint">
      只支持上传图片
    </p>
  </a-upload-dragger>
  <a-progress style="width: 50vw;margin-top: 20px" :percent="progress" v-show="isUploading"/>
  <a-result
      v-show="!isUploading && result.length > 0"
      status="success"
      title="任务已完成！"
  >
  </a-result>


</template>
<script lang="ts" setup>
import {onMounted, ref, watch} from 'vue';
import cameraApi from "../api/cameraApi.ts";
import {message, UploadProps} from "ant-design-vue";
import {CameraOutlined, InboxOutlined} from "@ant-design/icons-vue";
import type {UploadChangeParam} from 'ant-design-vue';
import axiosInstance from "../api/axios-instance.ts";
import {storeToRefs} from "pinia";
import {useIsUploadingStore, useResultStore} from "../store/baiduResult.ts";
const baiduResult = useResultStore()
const useIsUploading = useIsUploadingStore()
const {isUploading, progress} = storeToRefs(useIsUploading)
const fileList = ref([]);
const {result, finishCount} = storeToRefs(baiduResult)
watch(progress, () => {
  if (progress.value >= 100) {
    setTimeout(() => {
      isUploading.value = false
      finishCount.value = 0
      progress.value = 0
      fileList.value = []
    }, 1000)
  }
})

onMounted(() => {
  if (progress.value >= 100) {
      isUploading.value = false
      finishCount.value = 0
      progress.value = 0
      fileList.value = []
    }
})
const handleChange = (info: UploadChangeParam) => {
  isUploading.value = true
};

function handleDrop(e: DragEvent) {
  message.loading('开始上传')
  isUploading.value = true
}

const beforeUpload: UploadProps['beforeUpload'] = file => {
  const type = file.type
  if (type == 'image/jpeg' || type == 'image/png' || type == 'image/jpg') {
    fileList.value.push(file)
    handleUpload(file)
  }
  return false;
};

const handleUpload = async (file) => {
  const formData = new FormData();
  formData.append('image', file as any);
  let res = ''
  try {
    res = await axiosInstance.post('http://127.0.0.1:8000/baidu/',
        formData
    )
    const obj = res.data[0]
    obj.createTime = new Date().toLocaleString()
    result.value.push(obj)
    finishCount.value++
  } catch (e) {
  }
  if (!res) {
    result.value.push({
      photo_url: '123',
    })
    finishCount.value++
  }

  progress.value = Number(((finishCount.value/ fileList.value.length) * 100).toFixed(2))
};
</script>
<style scoped>
</style>
