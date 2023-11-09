import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import 'ant-design-vue/dist/reset.css';
import Antd from 'ant-design-vue';
import {createPinia} from "pinia";

const app = createApp(App);

const pinia = createPinia()

app.use(pinia)
app.use(Antd)
app.mount('#app')
