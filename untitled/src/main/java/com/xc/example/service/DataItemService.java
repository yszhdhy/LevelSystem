package com.xc.example.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.xc.model.model.DataItem;
import com.xc.model.model.DataItemEntity;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletRequest;
import java.io.IOException;
import java.util.List;

/**
 *
 *
 * @author capture or new
 * @email 3129318024@qq.com
 * @date 2023-10-30 15:16:15
 */
public interface DataItemService extends IService<DataItemEntity> {

    List<DataItem> identify(MultipartFile file, HttpServletRequest request) throws IOException;

    List<DataItem> photograph(HttpServletRequest request) throws JsonProcessingException;


}

