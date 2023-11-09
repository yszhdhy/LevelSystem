package com.xc.model.model;

import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import com.baomidou.mybatisplus.annotation.IdType;

import java.io.Serializable;
import java.util.Date;
import java.util.List;

import lombok.Data;

/**
 *
 *
 * @author capture or new
 * @email 3129318024@qq.com
 * @date 2023-10-30 15:16:15
 */
@Data
@TableName("data_item")
public class DataItemEntity implements Serializable {
	private static final long serialVersionUID = 1L;

	/**
	 * 图片ID
	 */
	@TableId(type = IdType.AUTO)
	private Long id;
	/**
	 * 两刻度线之间的距离
	 */
	private Double ScaleLineDistance;

	private String tick_marks_center_point;

	/**
	 * 气泡位置
	 */
	private String bubble_placement;
	/**
	 * 气泡距离的一半
	 */
	private double bubbles_distance_half;

	private String bubbles_center_point;
	/**
	 * 距离
	 */
	private Double distance;
	/**
	 * 气泡左侧刻度线
	 */
	private Double bubble_left_scale;
	/**
	 * 气泡右侧刻度线
	 */
	private Double bubble_right_scale;
	/**
	 * 图片URL
	 */
	private String photo_url;

	/**
	 * 误差图片集
	 */
	private String displacements;
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
