package com.xc.model.model;

import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import com.baomidou.mybatisplus.annotation.IdType;

import java.io.Serializable;
import java.util.Date;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * 历史数据表
 *
 * @author capture or new
 * @email 3129318024@qq.com
 * @date 2023-10-30 15:17:32
 */
@Data
@TableName("history_table")
@AllArgsConstructor
@NoArgsConstructor
public class HistoryTableEntity implements Serializable {
	private static final long serialVersionUID = 1L;

	/**
	 * 条目ID
	 */
	@TableId(type = IdType.AUTO)
	private Long id;
	/**
	 * 用户ID
	 */
	private Long userId;
	/**
	 * 识别数据对应的条目ID
	 */
	private Long dataId;
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
