# zhang
# SQL笔记
## MYSQL
这不是SQL文件  
那么就开始学习吧
# chaptre1 MRSQL基础篇
## 第一节 MYSQL概述
### 01数据库概念
名称  | 全称  | 简称
---- | -----  | ----
数据库  | 储存数据的仓库，数据是有组织的进行存储  | Database
数据库管理系统  | 操纵和管理数据库的大型软件 |  DataBase Management System(DBMS)
SQL  |操作关系型数据库的编程语言，定义了一套操作关系型数据库统一标准  | Structured Quert Language(SQL)  

通过SQL管理数据库管理系统，进而操作数据库  
### 02主流的关系型数据库管理系统
1. oracle
2. mysql
3. sql server
4. postgresql  
  
以上四个都是SQL来操作的，也就是SQL是统一标准
### 03MYSQL数据库
### 04基础-概述-数据模型
#### 05MYSQLs数据库
+ 关系型数据库
+ 概念：建立在关系模型的基础上，有多涨相互连接的二维表组成的数据库
+ 特点：
1. 使用表存储数据，格式统一，便于维护
2. 使用SQL语言操作，标准统一，使用方便
## 第二节 SQL
### 06基础-SQL-通用于法以及分类
+ SQl通用语法
1. SQL语句可以单行或多行书写，分号结尾
2. SQL语句可以使用空格/缩写来增强语句可读性
3. MYSQL数据库的SQL语句不区分大小写，关键字建议使用大写
4. 注释：
  - 单行注释：--注释内容或#注释内容（MYSQL特有）
  - 多行注释：/ * 注释内容 * /
+ SQL分类
  
分类  | 全程  | 说明
---- | -----  | ----
DDL  | Data Definition Lanaguage  | 数据定义语言，用来定义数据库对象（数据库，表，字段）
DML  | Data MAnipulation Lanaguage  | 数据操作语言，用来堆数据库表中的数据进行增删改
DQL  | Data Query Language  | 数据查询语言，用来查询数据库中表的记录
DCL  | Data Control Lanaguage  | 数据控制语言，用来创建数据库用户，控制数据库的访问权限（控制数据库中的增删改权限）
### 07基础--SQL--DDL--数据库操作
+ DDL-数据库操作
  - 查询  
    -- 查询所有数据库：SHOW DATABASES  
    -- 查询当前数据库：SELECT DATABASE()  
    select databases();  
    -- 创建：CREATE DATABASE[IF NOT EXISTS]数据库名[DEFAULT CHARSET 字符集][COLLATE 排序规则]  
    create database if not exists 数据库名 default charset utf8mb4  
    -- 删除：DROP DaTABASE[IF EXISTS]数据库名  
    drop database if exists itheima    
    -- 使用：USE 数据库名  
    use itheima  
### 08基础--SQL--DDL--表查询--创建&查询
> DDL--表操作--查询 
>- 查询当前数据库所有表：SHOW TABLES; 
>- 查询表结构(表头的类型，以及表头名称):DESC 表名;  
   desc tb_user;  
>- 查询指定表达建表语句:SHOW CREATE TABLE 表明;    
   show create table tb_user;  
>  DDL-表操作-创建  
>-  CREATE TABLE 表名（  
    字段1 字段1类型[COMMENT 字段1注释]， 
    字段2 字段2类型[COMMENT 字段2注释],  
    字段3，字段3类型[COMMENT 字段3注释],  
    ...  
    字段n 字段n类型[COMMENT 字段n注释]      
    )[COMMENT 标注释];
>   create table tb_user(  
    -> name varchar(50) comment '姓名',  
    -> id int comment '编号',  
    -> age int comment '年龄',  
    -> gender varchar(1) comment '性别')  
    -> comment '用户表';  
>   不要再系统库sys中执行操作
>   SQL语句一；结尾，所以只有不加；就没结束
### 09基础--SQL--DDL--数据类型以及案例
> DDL-表操作-数据类型
>- MYSQL中的数据类型有很多，主要分为三类：数值类型，字符串类型，日期时间类型
- 数值类型：https://www.runoob.com/mysql/mysql-data-types.html  
  精度：数的长度。标度：小数位的个数
  3.321 精度：4。标度：3
  age：没有负数，并且在三位数之内，所以用TINYINT UNSIGNED
  sore:double(4,1):最多是100.0 ,最长精度维4，标度维1
- 字符串类型：https://www.runoob.com/mysql/mysql-data-types.html  
  - 二进制字符串用的不多
  - char(10):占用10个内存空间，未达到10的用空格站位。性能高  
  - varchar(10)：有多长就占多少内存，根据内容计算所占用的储存空间，所以性能低。
  - 用户名name:varchar(50)
  - 性别 gender：char(1)
- 日期时间类型：https://www.runoob.com/mysql/mysql-data-types.html
  - birthday:DAY
- 案例
### 10 基础--SQL--DDL小结
> 添加字段
> - ALTER TABLE 表名 ADD 字段名 类型(长度)[COMMENT 字段注释][约束];
> - 案例：emp添加一个新字段
> 修改字段
>- 修改指定类型：alter table 表明 modify 字段名 新的数据类型(长度)；
>- 修改字段名和字段类型：alter table change 旧字段名 新字段名 新数据类型(长度)[comment 注释][注释]
   案例：
>  删除字段
>- alter table 表名 drop 字段名；  
  案例：
>  修改表名
>-  alter table 表名 rename to 新表名；
> 删除表
>- 删除表：drop table[if exisets] 表名；
>- 删除指定表，并且重新创建该表：truncate table 表名（为了删除原来表中的数据，在重新创建新表）
### 11ASQL--图形化界面工具DataGrip
> MySQL图形化界面
>- sqlyog
>- navicat
>- datagrip
### 12SQL--DML--插入
### 13SQL--DML--更新和删除
### 14SQL--DML--小节
### 15SQL--DQL--基础查询
### 16SQL--DQL--条件查询
### 17SQL--DQL--聚合函数
### 18SQL--DQL--分组查询
### 19SQL--DQL--排序查询
### 20SQL--DQL--分页查询
## 第三节 函数
## 第四节 约束
## 第五节 多表查询
## 第六节 事务
