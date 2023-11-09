create table history_table
(
    id         bigint auto_increment comment '条目ID'
        primary key,
    user_id    bigint                              not null comment '用户ID',
    data_id    bigint                              not null comment '识别数据对应的条目ID',
    created_at timestamp default CURRENT_TIMESTAMP null,
    updated_at timestamp default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP,
    is_deleted int       default 0                 null
)
    comment '历史数据表' charset = utf8mb3
                         row_format = DYNAMIC;

INSERT INTO generator.history_table (id, user_id, data_id, created_at, updated_at, is_deleted) VALUES (1, 13, 2, '2023-10-30 16:18:25', '2023-10-30 16:18:25', 0);
