package com.xc.common.http;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

/**
 * @project untitled
 * @description Python请求的配置等
 * @author capture or new
 * @date 2023/10/30 17:44:48
 * @version 1.0
 */

@Data
@ConfigurationProperties(prefix = "pythonurl")  // 文件上传 配置前缀file.oss
@Component
public class PythonConfig {

    private String url;
    private String identify;
    private String open_camera;
    private String close_camera;
    private String photograph;
    private String statistical_errors;

}
