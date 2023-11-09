create table qualified_or_not
(
    id                     bigint auto_increment comment '条目ID'
        primary key,
    data_id                bigint                              not null comment '识别数据对应的条目ID',
    qualified_right_or_not int                                 not null comment '是否合格',
    created_at             timestamp default CURRENT_TIMESTAMP null,
    updated_at             timestamp default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP,
    is_deleted             int       default 0                 null
)
    comment '合格或者非合格数据信息表（1 表示合格，0表示不合格）' charset = utf8mb3
                                                               row_format = DYNAMIC;

