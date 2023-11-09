package com.xc.model.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

import java.util.List;

@Data
@AllArgsConstructor
@NoArgsConstructor
@ToString
public class DataItem {
    private double ScaleLineDistance;
    private List<Double> tickMarks_center_point;
    private String bubble_placement;
    private double bubbles_distance_half;
    private List<Double> bubbles_center_point;
    private double distance;
    private double bubble_left_scale;
    private double bubble_right_scale;
    private String photo_url;
    private List<Double> displacements;
}
