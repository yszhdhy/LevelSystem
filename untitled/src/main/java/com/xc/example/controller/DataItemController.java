package com.xc.example.controller;

import java.util.Arrays;
import java.util.Map;

import com.alibaba.fastjson.JSON;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.xc.model.model.DataItem;
import io.swagger.annotations.Api;
import org.apache.commons.lang.StringUtils;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.*;

import com.xc.model.model.DataItemEntity;
import com.xc.example.service.DataItemService;
import com.xc.common.result.Result;



/**
 * @author capture or new
 * @email 3129318024@qq.com
 * @date 2023-10-30 15:16:15
 */
@Api(tags = "信息数据接口")
@RestController
@RequestMapping("admin/dataitem")
@CrossOrigin
public class DataItemController {
    @Autowired
    private DataItemService dataItemService;

    /**
     * 列表
     */
    @GetMapping("{page}/{limit}")
    public Result list(@PathVariable Long page,
                       @PathVariable Long limit,
                       String key
                       /* 自定义查询条件 vo 可以根据SysUserController 接口实现*/){

        //创建page对象
        Page<DataItemEntity> pageParam = new Page<>(page,limit);

       String columnNames = "id,scale_line_distance,bubble_placement,bubbles_distance_half,distance,bubble_left_scale,bubble_right_scale,photo_url,displacements,created_at,updated_at,is_deleted,";
        String[] fieldNames = columnNames.split(",");

        //封装条件，判断条件值不为空
        QueryWrapper<DataItemEntity> wrapper = new QueryWrapper<>();
        if(!StringUtils.isEmpty(key)){
            // 打印每个字段名
            for (String fieldName : fieldNames) {
                wrapper.or().like(fieldName.trim(), key);
            }
        }

        //调用mp的方法实现条件分页查询
        IPage<DataItemEntity> pageModel = dataItemService.page(pageParam, wrapper);

        return Result.ok(pageModel);
    }


    /**
     * 信息
     */
    @GetMapping("/info/{id}")
    public Result info(@PathVariable("id") Long id){
		DataItemEntity dataItem = dataItemService.getById(id);

        return Result.ok(dataItem);
    }

    /**
     * 保存
     */
    @PostMapping("/save")
    public Result save(@RequestBody DataItemEntity dataItem){
		dataItemService.save(dataItem);

        return Result.ok();
    }

    /**
     * 修改
     */
    @PostMapping("/update")
    public Result update(@RequestBody DataItemEntity dataItem){
		dataItemService.updateById(dataItem);

        return Result.ok();
    }

    /**
     * 删除
     */
    @PostMapping("/delete")
    public Result delete(@RequestBody Long[] ids){
		dataItemService.removeByIds(Arrays.asList(ids));

        return Result.ok();
    }

    /**
     * 根据单个id删除
     */
    @GetMapping("/deleteById/{id}")
    public Result deleteById(@PathVariable Long id){
            dataItemService.removeById(id);

        return Result.ok();
    }

}
