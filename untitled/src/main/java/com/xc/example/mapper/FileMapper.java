package com.xc.example.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.xc.model.model.DataItem;
import com.xc.model.model.SysUser;
import org.apache.ibatis.annotations.Mapper;

/**
 * <p>
 * 用户表 Mapper 接口
 * </p>
 *
 * @author atguigu
 * @since 2023-02-02
 */
@Mapper
public interface FileMapper extends BaseMapper<DataItem> {

}
