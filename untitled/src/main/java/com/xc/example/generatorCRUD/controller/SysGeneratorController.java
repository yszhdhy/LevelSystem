package com.xc.example.generatorCRUD.controller;



import com.xc.example.generatorCRUD.service.SysGeneratorService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * 代码生成器
 *
 * @author yszhdhy
 */
@Controller
@RequestMapping("/sys/generator")
public class SysGeneratorController {

	@Autowired
	private SysGeneratorService sysGeneratorService;

	/**
	 * 生成代码
	 */
	@GetMapping("/code")
	public void code(@RequestParam String tables, HttpServletResponse response) throws IOException{
	}
}
