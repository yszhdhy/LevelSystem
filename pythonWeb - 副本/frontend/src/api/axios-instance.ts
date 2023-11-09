import axios, {AxiosInstance} from 'axios';
import {message} from "ant-design-vue";
export const url = 'http://127.0.0.1:8000/'
const axiosInstance: AxiosInstance = axios.create({
    baseURL: url,
    timeout: 60000,
});

// 添加请求拦截器
axiosInstance.interceptors.request.use(
    (config: any) => {
        // 在发送请求之前做些什么
        return config;
    },
    (error: any) => {
        // 处理请求错误
        return Promise.reject(error);
    },
);

// 添加响应拦截器
axiosInstance.interceptors.response.use(
    (response: any) => {
        const data = response.data
        if (data.code != 200) {
            message.error(data.msg)
            // throw new Error(data.msg);
        }
        return data;
    },
    (error: any) => {
        // 处理响应错误
        return Promise.reject(error);
    },
);

export default axiosInstance;

