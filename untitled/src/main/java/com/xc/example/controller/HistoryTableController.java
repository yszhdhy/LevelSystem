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

import com.xc.model.model.HistoryTableEntity;
import com.xc.example.service.HistoryTableService;
import com.xc.common.result.Result;



/**
 * 历史数据表
 *
 * @author capture or new
 * @email 3129318024@qq.com
 * @date 2023-10-30 15:17:32
 */
@Api(tags = "历史数据表")
@RestController
@RequestMapping("admin/historytable")
@CrossOrigin
public class HistoryTableController {
    @Autowired
    private HistoryTableService historyTableService;

    /**
     * 列表
     */
    @GetMapping("{page}/{limit}")
    public Result list(@PathVariable Long page,
                       @PathVariable Long limit,
                       String key
                       /* 自定义查询条件 vo 可以根据SysUserController 接口实现*/){

        //创建page对象
        Page<HistoryTableEntity> pageParam = new Page<>(page,limit);

       String columnNames = "id,user_id,data_id,created_at,updated_at,is_deleted,";
        String[] fieldNames = columnNames.split(",");

        //封装条件，判断条件值不为空
        QueryWrapper<HistoryTableEntity> wrapper = new QueryWrapper<>();
        if(!StringUtils.isEmpty(key)){
            // 打印每个字段名
            for (String fieldName : fieldNames) {
                wrapper.or().like(fieldName.trim(), key);
            }
        }

        //调用mp的方法实现条件分页查询
        IPage<HistoryTableEntity> pageModel = historyTableService.page(pageParam, wrapper);

        return Result.ok(pageModel);
    }


    /**
     * 信息
     */
    @GetMapping("/info/{id}")
    public Result info(@PathVariable("id") Long id){
		HistoryTableEntity historyTable = historyTableService.getById(id);

        return Result.ok(historyTable);
    }

    /**
     * 保存
     */
    @PostMapping("/save")
    public Result save(@RequestBody HistoryTableEntity historyTable){
		historyTableService.save(historyTable);

        return Result.ok();
    }

    /**
     * 修改
     */
    @PostMapping("/update")
    public Result update(@RequestBody HistoryTableEntity historyTable){
		historyTableService.updateById(historyTable);

        return Result.ok();
    }

    /**
     * 删除
     */
    @PostMapping("/delete")
    public Result delete(@RequestBody Long[] ids){
		historyTableService.removeByIds(Arrays.asList(ids));

        return Result.ok();
    }

    /**
     * 根据单个id删除
     */
    @GetMapping("/deleteById/{id}")
    public Result deleteById(@PathVariable Long id){
            historyTableService.removeById(id);

        return Result.ok();
    }

}
