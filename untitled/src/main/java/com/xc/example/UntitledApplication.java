package com.xc.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import java.io.IOException;

@SpringBootApplication
@ComponentScan(value = {"com.xc"})
public class UntitledApplication {
    public static void main(String[] args) {
        SpringApplication.run(UntitledApplication.class, args);
        openBrowser("http://localhost:8080/admin/web/crud");
    }

    /**
     * @author CaptureOrNew
     * @description 获取本地浏览器并自动打开项目首页
     * @date 16:30:43 2023/7/16
     * @param url
     **/
    private static void openBrowser(String url) {
        try {
            // 根据不同操作系统执行不同的命令
            String os = System.getProperty("os.name").toLowerCase();
            if (os.contains("win")) {
                // Windows
                Runtime.getRuntime().exec("rundll32 url.dll,FileProtocolHandler " + url);
            } else if (os.contains("mac")) {
                // macOS
                Runtime.getRuntime().exec("open " + url);
            } else if (os.contains("nix") || os.contains("nux")) {
                // Linux
                Runtime.getRuntime().exec("xdg-open " + url);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}