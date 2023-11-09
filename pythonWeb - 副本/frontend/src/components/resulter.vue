<script setup lang="ts">

import {onMounted, ref, watch} from "vue";
import {useResultStore} from "../store/baiduResult.ts";
import {storeToRefs} from "pinia";
import {message} from 'ant-design-vue';
import imgApi from "../api/imgApi.ts";


const columns = ref([
  {
    key: 'img',
    title: '原图',
    dataIndex: 'img',
    resizable: true,
  },
  {
    title: '两根刻度线之间的距离',
    dataIndex: 'ScaleLineDistance',
    resizable: true,
  },
  {
    title: '刻度线中心点',
    dataIndex: 'tickMarksCenterPoint',
    resizable: true,
  },
  {
    title: '气泡位置',
    resizable: true,
    dataIndex: 'bubblePlacement',
  },
  {
    title: '气泡轮廓左侧到右侧的距离的二分之一',
    dataIndex: 'bubblesDistanceHalf',
    resizable: true,
  },
  {
    title: '气泡中心点',
    dataIndex: 'bubblesCenterPoint',
    resizable: true,
  },
  {
    title: '刻度线中心点和气泡中心点之间的距离',
    resizable: true,
    dataIndex: 'distance',
  },
  {
    title: '上传时间',
    resizable: true,
    dataIndex: 'createTime',
  },
  {
    title: '审核',
    resizable: true,
    key: 'edit',
    dataIndex: 'edit',
  }
])

function handleResizeColumn(w, col) {
  col.width = w;
}

const tableData = ref([])
const baiduResult = useResultStore()
const {result, filterValue} = storeToRefs(baiduResult)

watch(result.value, () => {
  if (filterValue.value != '0') {
    return
  }
  tableData.value = result.value.map(item => {
    return {
      key: Math.random(),
      img: item.photo_url,
      ScaleLineDistance: Number(item.ScaleLineDistance).toFixed(3),
      tickMarksCenterPoint: `${item.tickMarks_center_point}`,
      bubblePlacement: `${item.bubble_placement} 第 ${Number((item.bubble_left_scale)).toFixed(3)} 根线到第 ${Number((item.bubble_right_scale)).toFixed(3)} 之间`,
      bubblesDistanceHalf: `${item.bubbles_distance_half}`,
      bubblesCenterPoint: `${item.bubbles_center_point}`,
      distance: Number(item.distance).toFixed(3),
      createTime: item.createTime
    }
  })
})
onMounted(async () => {
    await loadTableDate()
})
const confirm = async (img) => {
  message.loading("正在提交，请稍后")
  await imgApi.correctAtlas(img)
  message.success('审核成功！')
};

const cancel = async (img) => {
  message.loading("正在提交，请稍后")
  await imgApi.issueAtlas(img)
  message.success('审核成功！')
};
const loadTableDate = async () => {
  if (filterValue.value == '0') {
    tableData.value = result.value.map(item => {
      return {
        key: Math.random(),
        img: item.photo_url,
        ScaleLineDistance: Number(item.ScaleLineDistance).toFixed(3),
        tickMarksCenterPoint: `${item.tickMarks_center_point}`,
        bubblePlacement: `${item.bubble_placement} 第 ${Number((item.bubble_left_scale)).toFixed(3)} 根线到第 ${Number((item.bubble_right_scale)).toFixed(3)} 之间`,
        bubblesDistanceHalf: `${item.bubbles_distance_half}`,
        bubblesCenterPoint: `${item.bubbles_center_point}`,
        distance: Number(item.distance).toFixed(3),
        createTime: item.createTime
      }
    })
    return
  }
  let resData = (await imgApi.getImgs(filterValue.value)).data
  tableData.value = resData.map(item => ({
    key: item.id,
    id: item.id,
    img: item.photo_url,
    ScaleLineDistance: Number(item.ScaleLineDistance).toFixed(3),
    tickMarksCenterPoint: `${item.tickMarks_center_point}`,
    bubblePlacement: item.bubble_placement,
    bubblesDistanceHalf: `${item.bubbles_distance_half}`,
    bubblesCenterPoint: `${item.bubbles_center_point}`,
    distance: Number(item.distance).toFixed(3),
    createTime: item.createTime
  }))
}
const termsChange =async () => {
  await loadTableDate()
}

const deleted = async (img) => {
  await imgApi.deleteImg(img.id, filterValue.value)
  await loadTableDate()
}
const noDelete = () => {
  return
}
</script>

<template>
  <div>
    <a-radio-group v-model:value="filterValue" button-style="outline" @change="termsChange" style="margin: 10px 10px 10px 0">
      <a-radio-button value="correctAtlas">合格</a-radio-button>
      <a-radio-button value="issueAtlas">不合格</a-radio-button>
      <a-radio-button value="0">全部</a-radio-button>
    </a-radio-group>
  </div>
  <a-table :columns="columns" :data-source="tableData" @resizeColumn="handleResizeColumn" :scroll="{y: 600}" bordered
           :pagination="false">
    <template #bodyCell="{column, record}">
      <template v-if="column.key === 'img'">
        <a-image :src="record.img">
        </a-image>
      </template>
      <template v-if="column.key === 'edit'">
        <a-popconfirm
            title="识别是否准确？"
            ok-text="是"
            cancel-text="否"
            @confirm="confirm(record)"
            @cancel="cancel(record)"
        >
          <a-button type="primary" ghost>审核</a-button>
        </a-popconfirm>
        <a-popconfirm
            v-if="filterValue != 0"
            title="是否删除？"
            cancel-text="否"
            ok-text="是"
            @confirm="deleted(record)"
            @cancel="noDelete()"
        >
          <a-button  style="margin-left: 10px" danger>删除</a-button>
        </a-popconfirm>
      </template>
    </template>
  </a-table>
</template>

<style scoped>
</style>