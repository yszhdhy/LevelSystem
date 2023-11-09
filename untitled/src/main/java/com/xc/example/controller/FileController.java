package com.xc.example.controller;

import com.alibaba.fastjson.JSON;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.MapperFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.xc.common.http.PythonConfig;
import com.xc.common.result.Result;
import com.xc.example.service.DataItemService;
import com.xc.example.service.FileService;
import com.xc.example.utils.http.PythonClient;
import com.xc.model.dto.PythonResult;
import com.xc.model.model.DataItem;
import com.xc.model.model.DataItemEntity;
import com.xc.model.model.ResponseData;
import freemarker.template.utility.StringUtil;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.ByteArrayResource;
import org.springframework.core.io.Resource;
import org.springframework.http.*;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.multipart.MultipartFile;


import javax.servlet.http.HttpServletRequest;
import java.io.IOException;
import java.util.List;

/**
 * @project untitled
 * @description 图片上传识别接口
 * @author capture or new
 * @date 2023/10/30 12:53:19
 * @version 1.0
 */
@Api(tags = "图片上传识别接口")
@RestController
@RequestMapping("/admin/file")
public class FileController {



    @Autowired
    DataItemService dataItemService;

    @Autowired
    PythonClient pythonClient;


    /**
     * 上传图片文件
     * @param prefix 文件前缀
     * @param file   文件对象
     * @return 文件的URL路径
     */
    @ApiOperation("BAIDU_API图片识别接口")
    @PostMapping(value = "/upload/image", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
    public Result<Object> uploadImageFile(@RequestParam(value = "prefix", required = false) String prefix,
                                          @RequestPart("image") MultipartFile file,
                                          HttpServletRequest request) throws IOException {
        List<DataItem> dataItems = dataItemService.identify(file,request);
        if(dataItems != null){
            // 返回Python模块的响应
            return Result.ok(dataItems);
        }
        return Result.fail();
    }


    /**
     * @author CaptureOrNew
     * @description //开启摄像头
     * @date 20:09:18 2023/10/30
     * @Param
     * @return
     * @return com.xc.common.result.Result
     **/
    @ApiOperation("打开摄像头")
    @GetMapping("openCamera")
    public Result openCamera() throws JsonProcessingException {

        int code = pythonClient.openCamera();
        if(code==200){
            return Result.ok();
        }
        return Result.fail();

    }

    /**
     * @author CaptureOrNew
     * @description //拍照识别
     * @date 20:09:18 2023/10/30
     * @Param
     * @return
     * @return com.xc.common.result.Result
     **/
    @ApiOperation("点击开始拍照识别")
    @GetMapping("photograph")
    public Result photograph(HttpServletRequest request) throws JsonProcessingException {

        List<DataItem> dataItems =  dataItemService.photograph(request);
        if(dataItems != null){
            // 返回Python模块的响应
            return Result.ok(dataItems);
        }
        return Result.fail();
    }


    /**
     * @author CaptureOrNew
     * @description //关闭摄像头
     * @date 20:09:18 2023/10/30
     * @Param
     * @return
     * @return com.xc.common.result.Result
     **/
    @ApiOperation("关闭摄像头")
    @GetMapping("closeCamera")
    public Result closeCamera(){

        int code = pythonClient.closeCamera();
        if (code==200){
            return Result.ok();
        }
        return Result.fail();
    }

    /**
     * @author CaptureOrNew
     * @description //计算误差
     * @date 20:09:18 2023/10/30
     * @Param
     * @return
     * @return com.xc.common.result.Result
     **/
    @ApiOperation("计算误差")
    @GetMapping("statistical_errors")
    public Result statistical_errors() throws JsonProcessingException {

        PythonResult result = pythonClient.statistical_errors();
        if (result.getCode()==200){
            return Result.ok(result.getData());
        }
        return Result.fail();
    }

}
