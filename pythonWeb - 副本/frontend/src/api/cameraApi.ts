import axiosInstance from "./axios-instance.ts";

export default {
    async openCamera() {
        return axiosInstance.get('/openCamera')
    },
    async closeCamera() {
        return axiosInstance.get('/closeCamera')
    },
    async takePhoto() {
        return axiosInstance.get('/photograph')
    }
}