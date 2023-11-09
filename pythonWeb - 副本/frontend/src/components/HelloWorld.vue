<template>
  <a-layout class="layout" style="background-color: #f5f5f5;height: 100vh">
    <a-layout-header style="background-color: #f5f5f5">
      <div class="logo"/>
      <a-row :gutter="16" justify="end">
        <a-col>
          <a-button @click="takePhoto" :loading="takePhotoLoading">
            <template #icon>
              <camera-outlined/>
            </template>
            拍张照片
          </a-button>  
        </a-col>
        <a-col style="display: flex; align-items: center">
          <span>相机：</span>
          <a-switch v-model:checked="checked" checked-children="开启" un-checked-children="关闭" :loading="switchLoading"
                    @change="cameraChange"/>
        </a-col>
      </a-row>
    </a-layout-header>
    <a-layout-content style="padding: 0 50px">
      <div ref="content" :style="{ background: '#fff', padding: '24px', minHeight: '800px' }">
        <a-menu
            v-model:selectedKeys="selectedKeys"
            mode="horizontal"
            :style="{ lineHeight: '64px' }"
        >
          <a-menu-item key="1">首页</a-menu-item>
          <a-menu-item key="2">审核</a-menu-item>
        </a-menu>
        <div v-if="selectedKeys[0] == 1" style="display: flex;justify-content: center;align-items: center;flex-direction: column;margin-top: 100px">
          <uploader />
        </div>

        <resulter v-if="selectedKeys[0] == 2"/>
      </div>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      DS@2023
    </a-layout-footer>
  </a-layout>
</template>
<script lang="ts" setup>
import {ref} from 'vue';
import cameraApi from "../api/cameraApi.ts";
import {message, UploadProps} from "ant-design-vue";
import {CameraOutlined, InboxOutlined} from "@ant-design/icons-vue";
import type {UploadChangeParam} from 'ant-design-vue';
import axiosInstance from "../api/axios-instance.ts";
import Uploader from "./uploader.vue";
import Resulter from "./resulter.vue";
import {useIsUploadingStore, useResultStore} from "../store/baiduResult.ts";
import {storeToRefs} from "pinia";

const takePhotoLoading = ref(false)
const selectedKeys = ref<string[]>(['1']);
const checked = ref(false)
const switchLoading = ref(false)
const baiduResult = useResultStore()
const {result} = storeToRefs(baiduResult)
const useIsUploading = useIsUploadingStore()
const {isUploading} = storeToRefs(useIsUploading)
const content = ref()
const cameraChange = async (val) => {
  if (val) {
    switchLoading.value = true
    let res
    try {
      res = await cameraApi.openCamera()
    } catch (e) {
      switchLoading.value = false
      console.error(e)
      message.error("未知错误")
      return
    }
    if (res.code == 200)
      message.success('打开成功！')
    switchLoading.value = false
  } else {
    switchLoading.value = true
    let res
    try {
      res = await cameraApi.closeCamera()
    } catch (e) {
      switchLoading.value = false
      console.error(e)
      message.error("未知错误")
      return
    }
    if (res.code == 200)
      message.success('已关闭！')
    switchLoading.value = false
  }
}

const takePhoto = async () => {
  takePhotoLoading.value = true
  message.loading("正在处理！")
  let res;
  try {
    res = await cameraApi.takePhoto()
  } catch (e) {
    takePhotoLoading.value = false
    message.error('未知错误')
    return
  }
  if (res.code == 500) {
    message.error('请检查相机是否打开!')
    takePhotoLoading.value = false
    return
  }
  const obj = res.data[0]
  obj.createTime = new Date().toLocaleString()
  result.value.push(obj)
  takePhotoLoading.value = false
  message.success('处理成功！')
}



</script>
<style scoped>
.logo {
  float: left;
  width: 120px;
  height: 31px;
  margin: 16px 24px 16px 0;
  background: rgba(211, 211, 211, 0.71);
}
</style>
