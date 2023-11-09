import { defineStore } from 'pinia'
import {ref} from "vue";

// 你可以对 `defineStore()` 的返回值进行任意命名，但最好使用 store 的名字，同时以 `use` 开头且以 `Store` 结尾。(比如 `useUserStore`，`useCartStore`，`useProductStore`)
// 第一个参数是你的应用中 Store 的唯一 ID。
export const useResultStore = defineStore('result',() => {
    const result = ref([])
    const filterValue = ref('0')
    const finishCount = ref(0)
    return {result, filterValue, finishCount}
})

export const useIsUploadingStore = defineStore('isUpload', () => {
    const isUploading = ref(false)
    const progress = ref(0)
    return {isUploading, progress}
})