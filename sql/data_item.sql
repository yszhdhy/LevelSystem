create table data_item
(
    id                      bigint auto_increment comment '图片ID'
        primary key,
    scale_line_distance     double                              null comment '两刻度线之间的距离',
    bubble_placement        varchar(255)                        null comment '气泡位置',
    bubbles_distance_half   double                              not null comment '气泡距离的一半',
    distance                double                              null comment '距离',
    bubble_left_scale       double                              null comment '气泡左侧刻度线',
    bubble_right_scale      double                              null comment '气泡右侧刻度线',
    photo_url               varchar(1024)                       null comment '图片URL',
    displacements           json                                null comment '误差图片集',
    created_at              timestamp default CURRENT_TIMESTAMP null,
    updated_at              timestamp default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP,
    is_deleted              int       default 0                 null,
    tick_marks_center_point json                                null comment '标记中心点',
    bubbles_center_point    json                                null comment '气泡中心点'
)
    charset = utf8mb3
    row_format = DYNAMIC;

INSERT INTO generator.data_item (id, scale_line_distance, bubble_placement, bubbles_distance_half, distance, bubble_left_scale, bubble_right_scale, photo_url, displacements, created_at, updated_at, is_deleted, tick_marks_center_point, bubbles_center_point) VALUES (2, 85.33333333333333, '左侧', 223, 428.47068161077254, 2.4078595501262408, 7.634422050126241, 'http://110.238.119.179:9000/levelsystem/20231030/WIN_20230728_11_30_19_Pro.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minio%40admin%2F20231030%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231030T081824Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=d35dc81ca4af4107aef83e37533892e48f2cc547e05b6a0d149ac65aa6c1064a', '[-150.6342240037872, -150.6342240037872, -150.6342240037872, -150.6342240037872, -150.6342240037872, -150.6342240037872, -150.6342240037872, -150.6342240037872, -150.6342240037872, -150.6342240037872, -150.6342240037872, -150.6342240037872, -150.6342240037872, -150.6342240037872, -150.6342240037872]', '2023-10-30 16:18:25', '2023-10-30 16:18:25', 0, '[1960.25, 1324.75]', '[1532.0, 1311.0]');
