package com.xc.example.utils.http;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.MapperFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.xc.common.http.PythonConfig;
import com.xc.model.dto.PythonResult;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.ByteArrayResource;
import org.springframework.core.io.Resource;
import org.springframework.http.*;
import org.springframework.stereotype.Component;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

/**
 * @project untitled
 * @description 调用Python服务
 * @author capture or new
 * @date 2023/10/30 17:59:49
 * @version 1.0
 */

@Component
public class PythonClient {

    @Autowired
    RestTemplate restTemplate;

    @Autowired
    PythonConfig pythonConfig;

    public ResponseEntity<String> identify(MultipartFile file) throws IOException {
        // 构建HTTP请求，将文件发送给Python模块
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.MULTIPART_FORM_DATA);
        MultiValueMap<String, Object> body = new LinkedMultiValueMap<>();

        // 添加文件
        Resource fileResource = new ByteArrayResource(file.getBytes()) {
            @Override
            public String getFilename() {
                return file.getOriginalFilename();
            }
        };

        body.add("image", fileResource);

        HttpEntity<MultiValueMap<String, Object>> requestEntity = new HttpEntity<>(body, headers);

        // 发送POST请求到Python模块的API端点
        ResponseEntity<String> response = restTemplate.exchange(pythonConfig.getUrl()+pythonConfig.getIdentify(), HttpMethod.POST, requestEntity, String.class);

        return response;
    }


    /**
     * @author CaptureOrNew
     * @description //使用摄像头拍照并上传识别
     * @date 20:34:27 2023/10/30
     * @Param
     * @return
     * @return java.lang.String
     **/
    public ResponseEntity<String> photograph(){

        // 创建一个RestTemplate实例
        RestTemplate restTemplate = new RestTemplate();

        // 发送GET请求，并获取响应
        ResponseEntity<String> response = restTemplate.getForEntity(pythonConfig.getUrl()+pythonConfig.getPhotograph(), String.class);

        return response;
    }



    public int openCamera() throws JsonProcessingException {
        // 创建一个RestTemplate实例
        RestTemplate restTemplate = new RestTemplate();

        // 发送GET请求，并获取响应
        ResponseEntity<String> response = restTemplate.getForEntity(pythonConfig.getUrl()+pythonConfig.getOpen_camera(), String.class);

        return response.getStatusCodeValue();

    }



    public int closeCamera(){
        // 创建一个RestTemplate实例
        RestTemplate restTemplate = new RestTemplate();

        // 发送GET请求，并获取响应
        ResponseEntity<String> response = restTemplate.getForEntity(pythonConfig.getUrl()+pythonConfig.getClose_camera(), String.class);

        return response.getStatusCodeValue();
    }

    public PythonResult statistical_errors() throws JsonProcessingException {
        // 创建一个RestTemplate实例
        RestTemplate restTemplate = new RestTemplate();

        // 发送GET请求，并获取响应
        ResponseEntity<String> response = restTemplate.getForEntity(pythonConfig.getUrl()+pythonConfig.getStatistical_errors(), String.class);
        // 将JSON数据映射到实体类
        ObjectMapper objectMapper = new ObjectMapper();
        objectMapper.configure(MapperFeature.ACCEPT_CASE_INSENSITIVE_PROPERTIES, true);
        PythonResult pythonResult = objectMapper.readValue(response.getBody(), PythonResult.class);

        System.out.println(pythonResult);
        return pythonResult;
    }
}
