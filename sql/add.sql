use saltadmin

create table log_type(
    id int PRIMARY KEY,
    name VARCHAR(15) NOT NULL COMMENT '名称',
    status INT  NOT NULL  COMMENT  '启用或者禁用',

)