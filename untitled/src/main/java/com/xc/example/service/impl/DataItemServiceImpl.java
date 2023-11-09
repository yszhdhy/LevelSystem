package com.xc.example.service.impl;

import com.alibaba.fastjson.JSON;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.MapperFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.xc.common.http.PythonConfig;
import com.xc.common.jwt.JwtHelper;
import com.xc.example.service.HistoryTableService;
import com.xc.example.utils.http.PythonClient;
import com.xc.model.model.DataItem;
import com.xc.model.model.HistoryTableEntity;
import com.xc.model.model.ResponseData;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.ByteArrayResource;
import org.springframework.core.io.Resource;
import org.springframework.http.*;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.List;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;

import com.xc.example.mapper.DataItemDao;
import com.xc.model.model.DataItemEntity;
import com.xc.example.service.DataItemService;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletRequest;


@Service("dataItemService")
public class DataItemServiceImpl extends ServiceImpl<DataItemDao, DataItemEntity> implements DataItemService {

//    @Autowired
//    RestTemplate restTemplate;

    @Autowired
    HistoryTableService historyTableService;

    @Autowired
    PythonClient pythonClient;

//    @Autowired
//    PythonConfig pythonConfig;

    @Transactional
    @Override
    public List<DataItem> identify(MultipartFile file, HttpServletRequest request) throws IOException {

        //1 从请求头获取用户信息（获取请求头token字符串）
        String token = request.getHeader("token");

        //2 从token字符串获取用户id 或者 用户名称
        Long userId = JwtHelper.getUserId(token);
        if(userId==null){
            // 默认用户 避免报错
            userId = 1111111L;
        }
        ResponseEntity<String> response = pythonClient.identify(file);

        if (response.getStatusCodeValue() == 200) {
            // 将JSON数据映射到实体类
            ObjectMapper objectMapper = new ObjectMapper();
            objectMapper.configure(MapperFeature.ACCEPT_CASE_INSENSITIVE_PROPERTIES, true);
            ResponseData responseData = objectMapper.readValue(response.getBody(), ResponseData.class);
            List<DataItem> dataItems = responseData.getData();


            for (DataItem dataItem : dataItems) {
                DataItemEntity dataItemEntity = new DataItemEntity();
                BeanUtils.copyProperties(dataItem,dataItemEntity);
                dataItemEntity.setTick_marks_center_point(JSON.toJSONString(dataItem.getTickMarks_center_point()));
                dataItemEntity.setBubbles_center_point(JSON.toJSONString(dataItem.getBubbles_center_point()));
                dataItemEntity.setDisplacements(JSON.toJSONString(dataItem.getDisplacements()));

                // 存储识别数据信息
                save(dataItemEntity);
                DataItemEntity one = getOne(new LambdaQueryWrapper<DataItemEntity>().eq(DataItemEntity::getPhoto_url,dataItem.getPhoto_url()));
                // 存储历史数据
                historyTableService.save(new HistoryTableEntity(null,userId,one.getId(),null,null,null));

            }
            return dataItems;
        }
        return null;
    }


    @Transactional
    @Override
    public List<DataItem> photograph(HttpServletRequest request) throws JsonProcessingException {

        //1 从请求头获取用户信息（获取请求头token字符串）
        String token = request.getHeader("token");

        //2 从token字符串获取用户id 或者 用户名称
        Long userId = JwtHelper.getUserId(token);
        if(userId==null){
            // 默认用户 避免报错
            userId = 1111111L;
        }
        ResponseEntity<String> response = pythonClient.photograph();

        if (response.getStatusCodeValue() == 200) {
            // 将JSON数据映射到实体类
            ObjectMapper objectMapper = new ObjectMapper();
            objectMapper.configure(MapperFeature.ACCEPT_CASE_INSENSITIVE_PROPERTIES, true);
            ResponseData responseData = objectMapper.readValue(response.getBody(), ResponseData.class);
            List<DataItem> dataItems = responseData.getData();

            for (DataItem dataItem : dataItems) {
                DataItemEntity dataItemEntity = new DataItemEntity();
                BeanUtils.copyProperties(dataItem,dataItemEntity);
                dataItemEntity.setTick_marks_center_point(JSON.toJSONString(dataItem.getTickMarks_center_point()));
                dataItemEntity.setBubbles_center_point(JSON.toJSONString(dataItem.getBubbles_center_point()));
                dataItemEntity.setDisplacements(JSON.toJSONString(dataItem.getDisplacements()));

                // 存储识别数据信息
                save(dataItemEntity);
                DataItemEntity one = getOne(new LambdaQueryWrapper<DataItemEntity>().eq(DataItemEntity::getPhoto_url,dataItem.getPhoto_url()));
                // 存储历史数据
                historyTableService.save(new HistoryTableEntity(null,userId,one.getId(),null,null,null));

            }
            return dataItems;
        }
        return null;
    }

}
