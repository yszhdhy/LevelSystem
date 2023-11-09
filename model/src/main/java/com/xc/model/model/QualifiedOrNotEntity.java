package com.xc.model.model;

import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import com.baomidou.mybatisplus.annotation.IdType;

import java.io.Serializable;
import java.util.Date;
import lombok.Data;

/**
 * 合格或者非合格数据信息表（1 表示合格，0表示不合格）
 *
 * @author capture or new
 * @email 3129318024@qq.com
 * @date 2023-10-30 15:17:50
 */
@Data
@TableName("qualified_or_not")
public class QualifiedOrNotEntity implements Serializable {
	private static final long serialVersionUID = 1L;

	/**
	 * 条目ID
	 */
	@TableId(type = IdType.AUTO)
	private Long id;
	/**
	 * 识别数据对应的条目ID
	 */
	private Long dataId;
	/**
	 * 是否合格
	 */
	private Integer qualifiedRightOrNot;
	/**
	 * created_at
	 */
	private Date createdAt;
	/**
	 * updated_at
	 */
	private Date updatedAt;
	/**
	 * is_deleted
	 */
	private Integer isDeleted;

}
