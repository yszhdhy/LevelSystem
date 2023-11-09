package com.xc.example.mapper;

import com.xc.model.model.QualifiedOrNotEntity;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import org.apache.ibatis.annotations.Mapper;

/**
 * 合格或者非合格数据信息表（1 表示合格，0表示不合格）
 *
 * @author capture or new
 * @email 3129318024@qq.com
 * @date 2023-10-30 15:17:50
 */
@Mapper
public interface QualifiedOrNotDao extends BaseMapper<QualifiedOrNotEntity> {

}
