package com.xc.example.controller;

import java.util.Arrays;
import java.util.Map;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import io.swagger.annotations.Api;
import org.apache.commons.lang.StringUtils;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.*;

import com.xc.model.model.QualifiedOrNotEntity;
import com.xc.example.service.QualifiedOrNotService;
import com.xc.common.result.Result;



/**
 * 合格或者非合格数据信息表（1 表示合格，0表示不合格）
 *
 * @author capture or new
 * @email 3129318024@qq.com
 * @date 2023-10-30 15:17:50
 */
@Api(tags = "合格与否信息数据集")
@RestController
@RequestMapping("admin/qualifiedornot")
@CrossOrigin
public class QualifiedOrNotController {
    @Autowired
    private QualifiedOrNotService qualifiedOrNotService;

    /**
     * 列表
     */
    @GetMapping("{page}/{limit}")
    public Result list(@PathVariable Long page,
                       @PathVariable Long limit,
                       String key
                       /* 自定义查询条件 vo 可以根据SysUserController 接口实现*/){

        //创建page对象
        Page<QualifiedOrNotEntity> pageParam = new Page<>(page,limit);

       String columnNames = "id,data_id,qualified_right_or_not,created_at,updated_at,is_deleted,";
        String[] fieldNames = columnNames.split(",");

        //封装条件，判断条件值不为空
        QueryWrapper<QualifiedOrNotEntity> wrapper = new QueryWrapper<>();
        if(!StringUtils.isEmpty(key)){
            // 打印每个字段名
            for (String fieldName : fieldNames) {
                wrapper.or().like(fieldName.trim(), key);
            }
        }

        //调用mp的方法实现条件分页查询
        IPage<QualifiedOrNotEntity> pageModel = qualifiedOrNotService.page(pageParam, wrapper);

        return Result.ok(pageModel);
    }


    /**
     * 信息
     */
    @GetMapping("/info/{id}")
    public Result info(@PathVariable("id") Long id){
		QualifiedOrNotEntity qualifiedOrNot = qualifiedOrNotService.getById(id);

        return Result.ok(qualifiedOrNot);
    }

    /**
     * 保存
     */
    @PostMapping("/save")
    public Result save(@RequestBody QualifiedOrNotEntity qualifiedOrNot){
		qualifiedOrNotService.save(qualifiedOrNot);

        return Result.ok();
    }

    /**
     * 修改
     */
    @PostMapping("/update")
    public Result update(@RequestBody QualifiedOrNotEntity qualifiedOrNot){
		qualifiedOrNotService.updateById(qualifiedOrNot);

        return Result.ok();
    }

    /**
     * 删除
     */
    @PostMapping("/delete")
    public Result delete(@RequestBody Long[] ids){
		qualifiedOrNotService.removeByIds(Arrays.asList(ids));

        return Result.ok();
    }

    /**
     * 根据单个id删除
     */
    @GetMapping("/deleteById/{id}")
    public Result deleteById(@PathVariable Long id){
            qualifiedOrNotService.removeById(id);

        return Result.ok();
    }

}
