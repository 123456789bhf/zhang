# zhang
# SQL笔记
## MYSQL
这不是SQL文件  
那么就开始学习吧
# chaptre1 MRSQL基础篇
# 第一章 基础
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
    -- 创建：
           CREATE DATABASE[IF NOT EXISTS]数据库名[DEFAULT CHARSET 字符集][COLLATE 排序规则]  
           create database if not exists 数据库名 default charset utf8mb4  
    -- 删除：
            DROP DaTABASE[IF EXISTS]数据库名  
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
- DML-介绍:对原来数据库中表的数据记录进行增删改操作
  - 添加数据（insert）
  - 修改数据（update）
  - 删除数据（delete）
- MDML - 添加数据
  1. 给指定字段添加数据
     - insert into 表名（字段名1，字典名2，...） values (值1，值2，...);
  2. 给全部字段添加数据
    - insert into 表名 values (值1，值2，...);
  3. 批量添加数据
    - insert into 表名 （字段 ，字段2，...) values (值1，值2,...),(值1，值2,...),...;
    - insert into 表名 values (值1，值2,...),(值1，值2,...),...;
  
  -  *注意* ：
    - 插入数据时，指定的字段的顺序需要与值的顺序是一一对应的
    - 字符串和日期型数据应该包含在引号中
    - 插入的数据大小，应该在字段的规定范围内
### 13SQL--DML--更新和删除
- DML- 修改数据
  - update 表名 set 字段1=值1，字段2=值2，....[where 条件]
- DML - 删除数据
  - delete from 表名 [where 条件]
  - *注意*
    - delete的条件如果没有，那么会删除整张表的所有数据
    - delete语句不能删除某个字段的值（可以使用update）
### 14SQL--DML--小节
### 15SQL--DQL--基础查询
- DQL - 介绍
  - 数据库查询语言，用来查询数据库中表的记录
  - 查询关键字：select
- DQL - 语法

  select

        字段列表

  from

        表名列表

  where

        条件列表
  
  group by

        分组字段列表

  having by

        分组后条件列表

  order by

        排序字段列表

  limit

        分页参数

- 基本查询
  1. 查询多个字段
     - select 字段1，字段2，... from 表名；
     - select * from 表名；
  2. 设置别名
     - select 字段1（as 别名1），字段2（as 别名2），... from 表名；
  3. 去除重复记录
     - select dinstinct 字段列表 from 表名；
- 条件查询（where）
- 聚合函数（count,max,min,avg,sum）
- 分组查询（group by）
- 排序查询（order by)
- 分页查询（limit）
### 16SQL--DQL--条件查询
- DQL - 条件查询
  1. 语法
     - select 字段列表 from 表名 where 条件；
  2. 条件
 
 比较运算符  | 功能
 ---  | ----
  '>'  | 大于
 '>='  | 大于等于
 <=  | 小于等于
 =  | 等于
 <或！=  | 不等于
between 最小值 and最大值  | 在某个范围之内(含最小值，最小值)
in(...)  | 在in之后的列表中的值，多选一（取值在in后面的（）里面放着）
like 占位符  | 模糊匹配（占位符由两种：_匹配单个字符，%匹配任意一个字符）
is null  | 是NULL

逻辑运算符  | 功能  
---  |----
and 或&&  | 并且
or 或'双竖线'  | 或者
not 或！  | 非，不是
> **注意**
- is not null :不是空
- c between a and b等价于c<=b and c>=a;
- a in (1,2,3) 在里面三个中取值

### 17SQL--DQL--聚合函数
1. 介绍：将一列数据作为一个整体，进行纵向计算
2. 常见的聚合函数

函数  | 功能  
---  |----
count  | 统计数量
max  | 最大值
min  | 最小值
avg  | 平均值
sum  | 求和
3. 语法

select 聚合函数（字段列表） from 表名；
-remark：所以的NULL值在聚合函数中都不会参数计算
### 18SQL--DQL--分组查询
1. 语法
- select 字段列表 from 表名[where 条件] group by 分组字段名[having 分组后过滤条件]
 
2. where与having区别
 - 执行实际不同：where是分组之前进行过滤，不满足where条件，不参与分组；而having是分组之后对结果进行过滤
 - 判断条件不同：where不能对聚合函数进行判断，而having可以
3. remark：
- 在使用group by 之后前面的聚合函数字段列表都是进行分组之后的结果
- 执行顺序：where>聚合函数>having
- 分组之后，查询的字段一般为聚合函数和分组字段，查询其他字段无任何意义
### 19SQL--DQL--排序查询
1. 语法
- select 字段列表 from 表名 order by 字段1 排序方式1，字段2，排序方式2；
2. 排序方式
- ASC:升序（默认值）
- DESC:降序
3. remark：如果有多字段排序，当第一个字段值相同时，才会根据第二个字段进行排序
### 20SQL--DQL--分页查询（limit）
1. 语法
- select 字段列表 from 表名 limit 起始索引，查询记录数；
2. 注意
- 起始索引从0开始，起始索引=（查询页码-1）*每页记录数
- 分页查询是数据库的方言，不同的数据库有不同的实现，MYSLQL中是limit
- 如果查询是第一个数据，起始索引可以省略，直接简写为limit 10(每页的纪录数是10).
- 如果查询前5条数据:limit 0,5
### SQL--DDL--案例练习
1. 查询年龄20，21，22，23岁的员工信息
2. 查询性别为男，并且年龄在20~40岁（含）以内的姓名为三个字的员工信息
3. 统计员工表中，年龄小于60岁的，男性员工和女性员工的人数
4. 查询所以有年龄小于等于35岁的姓名和年龄，并对查询结果按照年龄升序排序，如果年龄相同按照入职时间降序排序
5. 查询性别为男，并且年龄在20~40(含）以内的前5个员工的信息，对查询的结果按照年龄升序排序，年龄相同的按照入职时间升序排序
### SQL--DDL--执行顺序
 select  **4**

        字段列表

  from    **1**

        表名列表

  where   ****2****

        条件列表

  group by   **3**

        分组字段列表

  having by  

        分组后条件列表

  order by  **5**

        排序字段列表

  limit  **6**

        分页参数

- 书写时候必须按照这个顺序，比如limit在最后，order by在having前面，但执行顺序不同，见黑体
### SQL--DDL--小结
### SQL--DCL--用户管理
- DCL介绍：用于管理数据库用户、控制数据库访问权限
- DCL-管理用户
1. 查询用户
- use mysql
- select * from user
2. 创建用户
- create user '用户名'@'主机名' identified by '密码'
3. 修改用户密码
- alter user '用户名'@'主机名' identified mysql_native_password by '新密码'
4. 删除用户
- drop user '用户名'@'主机名'

- **注意：**
- 直接在DG里面的mysql数据库中进行操作即可mysql->table->user,并且将右上角的改成user
- 主机名可以使用%通配（所有主机）
- 这类开发人员操作的比较少，主要是DBA（数据库管理员）使用
### SQL--DCL--权限控制
权限  | 说明  
---  |----
all,all privileges  | 所有权限
select  | 查询数据
insert  | 插入数据
update  | 修改数据
delete  | 删除数据
alter   | 修改表
drop   | 删除数据库/表/视图
create   | 创建数据库/表
- DCL—-权限控制(多个权限用逗号分隔)
1. 查询权限
- show grants for '用户名'@'主机名'
2. 授予权限
- grant 权限列表 on 数据库名 表名 to '用户名'@'主机名'
3. 撤销权限
- revoke 权限列表 on 数据库名  表名 from '用户名'@'主机名'
### SQL--DCL--小结
## 第三节 函数
- **函数**：是指一段可以直接被令一段程序调用的程序或者代码，很多函数mysql里面已经内置了
- **例如**
- 数据库中，存储的入职日期，如何快速计算入职天数？？？
- 数据库表中，存储的数学生的分数值，如98，75，如何快速判定分数的等级呢？？？
### 函数--字符串函数
MYSQL中内置了很多字符串函数，常见的有如下几个

函数  | 功能明  
---  |----
concat(s1,s2,...,sn)  | 字符串拼接，将s1,s2,...sn拼接成一个字符串
lower(Str)  | 将字符串全部转成小写
upper(str)  | 将字符串全部转成大写
lpad(str,n,pad)  | 将字符串str左边用pad进行填充，使其长度达到n
rpad(str,n,pad)  | 将字符串str右边用pad填充，使得其实长度达到n
trim(str)   | 去掉字符串头部和尾部的空格
substring(str,start,len)   | 返回字符串str从start位置器的len长的的字符串
create   | 创建数据库/表

- 使用：select 函数（参数）
- 案例：将企业员工的工号统一为5位数，目前不足5位的全部在前面补0，比如，1号员工的功耗应该是00001
### 函数--数值函数
常见的数值函数如下

函数  | 功能说明 
---  |----
ceil(x)  | 向上取值
floor(x)  | 向下取整
mod(x,y)  | x%y.x/y的余数
rand()  | 返回0-1的均匀数
round(x,y)  | 求参数x四舍五入的值，保留y位小数

使用方法：select 函数名（参数）
- 例子：利用数据库中的函数，生成一个六位数的随机验证码
### 函数--日期函数
函数  | 功能明  
---  |----
curdate   | 返回当前日期
curtime   |  返回当前时间
now()    | 返回当前的日期和时间(年月日时分秒)
year(date)    | 获取指定date的年份
mouth(date)   | 获取指定date的月份
day(date)   | 获取指定date的日期
date_add(date,interval expr type)   | 返回一个日期/时间值家伙是那个一个时间间隔expr后的时间值
datediff(date1,date2)   | 返回起始时间date1和结束时间date2之间的天数

- **例子**：查询所有员工的入职天数，并根据入职天数倒序排序
### 函数--流程函数
流程函数也是很常见的一类函数，可以在sql语句中时间条件筛选，从而提高语句的效率

函数   |  功能名
-----   | -----
if（value,t,f)   |  如果值value为true返回t,否则返回f
ifnull(value1,value2)   |  如果value不为空，那么返回value1,否则返回value2
case when [val1] then [res1] ... else[default] end (...表示when then 可以有多个)  | 如果val1是true那么返回res1,否则返回默认值default
case expr when [val1] then [res1] ... else [default] end   | 如果expr的值为val1,返回res1,否则，返回默认值default

- 例子：查询emp表的员工的姓名和工作地址（北京/上海--->一线城市，其他---->二线城市）

### 函数--小结
1. 字符串函数：concat,lower, upper,lpad,rpad,trim,substring
2. 数值函数：ceil,floor,rand(),round()
3. 日期函数：curdate，curtime,now,year,month,day,date_add,datefidd
4. 流程函数：if ,ifnull,case when then  else end
## 第四节 约束
### 约束--概述
1. 概念：约束时作用域表中字段上的规则，用于限制存储在表中的数据
2. 目的：保证数据库中数据的正确性、有效性、完整性
3. 分类

约束   | 描述   |  关键字
---- | -----  | ----
非空约束   | 限制该字段的数据不能为null   | not null
唯一约束   | 保证该字段的所有数据都是唯一、不重复的   | nuique
主键约束    | 主键是一行数据的唯一标识，要求非空且唯一    | primary key
默认约束   | 保存数据时，如果为指定该字段的值，那么采用的默认值   | default 默认值
检查约束    | 保证字段值满足某一个人条件   | check(判断条件)
外键约束    | 用来让两张表的数据之间建立连接，保证数据的一致性和完整性   | foreing key

- 注意：约束是作用域表中的字段上的，可以在创建表/修改表的时候添加约束
### 约束--演示
根据需求，完成表结构创建

字段名|字段含义|字段类型|约束条件|约束关键字
---|----|---- |-----|-----
id|id唯一标识|int|主键，并且自动增长(1,之后是2，之后是3，。。。)|primary key,auto_increment
name|姓名|varchar(10)|不为空，并且唯一|not null,unique
age|年龄|int|大于0，并且小于等于120|check
status|状态|char(1)|如果没有指定该值，默认为1|default
gender|性别|char(1)|无| 

### 约束--外键约束
- 概念：外键是用来让两张表的数据之间建立联系，从而保持数据的一致性和完整性、
- 具有外键的表称为**子表（从表）**，外键所关联的表称为**父表（主表）**
- **注意**：如果两张表只是在逻辑层面上有关联关系，但是在数据层面并未建立外键关联，所以是无法保证数据的一致性与完整性的
- 添加外键语法

         create table 表名（

                    字段名 数据类型,

                      ...

                    [constraint] [外键名称] foreign key(外键字段名) references 主表（主表列名）

        ）;

        alter table 表名 add constraint (外键名称) foreign key 外键字段名 references 主表（主表列名）
- 删除外键语法

         alter table 表名 drop foreign key 外键名称；

### 约束--外键删除更新行为
- 删除/更新行为

行为   | 说明
----------  | --------
no action  | 当在父表中删除/更新对用记录时，首先检查该记录是否有对应外键，如果有则不允许删除/更新。（与restrict一致）
restrict  | 当在父表中删除/更新对应记录时，首先检查该记录是否有对应外键，如果有那么不允许删除/更新。（与no action一致）
cascade  | 当在父表中删除/更新对应记录时，首先检查该记录是否有对应外键，如果有那么也更删除/更新外键在子表中的记录
set null  | 当在父表中伤处对应记录时，首先检查该记录是否有对应外键，如果有那么设置子表中该外键的值为null .(这就要求该外键允许取值null)
set default  | 父表有变更时，子表将外键列设置成一个默认值。

- 语法
  
      alter table 表名 add constraint 外键名称（自己定义） foreign key (外键字段名) referencces 主表（主表字段名） on update on delete cascade;
### 约束--小结
1. 非空约束:not null
2. 唯一约束:unique
3. 主键约束primary key(自动增长：auto_increment)
4. 默认约束：default
5. 检查约束:check
6. 外键约束：foreign key
## 第五节 多表查询

### 多表查询--多表关系介绍
- 项目开发中，在进行数据库结构设计时，会根据额业务需求以及业务模块之间的关系，分析并设计表结构，由于业务之间相互关联，所以各个表结构之间也存在着各种联系，基本上分为三种：
  - 一对多（多对一）
  - 多对多
  - 一对一
-  一对多
  >- 案例：部门与员工的关系
  >- 关系：一个部门对应多个员工，一个员工对应一个部门
  >- 实现：再多的一方建立外键，指向一的一方的主键。

<center><img src="https://cdn.nlark.com/yuque/0/2022/png/22965791/1648822097962-e8d48edc-6867-435c-8f85-1735e7b5079b.png" width="500" hegiht="" ></center>
<center><br>一对多</br></center>

- 多对多
  - 案例：学生与课程之间的关系
  - 关系：一个学生可以选修多个课程，一个课程也可以供多个学生选择
  - 实现：建立第三张中间表，中间表至少包含两个外键，分别关联两方主键

<center><img src="https://cdn.nlark.com/yuque/0/2022/png/22965791/1648821871427-3a3b103c-a076-468a-91de-68cde38dd476.png" width="500" hegiht="" ></center>
<center><br>多对多</br></center>

<center><img src="https://cdn.nlark.com/yuque/0/2022/png/22965791/1648821992724-aea16c43-a3a7-4f35-a9b6-718b6d2e9eb7.png" width="500" hegiht="" ></center>
<center><br>建立多对多表的关系图</br></center>

- 一对一
  - 案例：用户与拥护详情的关系
  - 关系：一对一关系，用于单表拆分，将一张表的基础字段放在一张表中，其他详情字段放在另外一张表中，以提升操作效率
  - 实现：在任意一方加入外键，关联另一方的主键，并且设置外键为唯一的（unique）

<center><img src="https://cdn.nlark.com/yuque/0/2022/png/22965791/1648822177791-4d9fe174-8c64-46cc-8de7-10c4742ad0ca.png" width="500" hegiht="" ></center>
<center><br>建立多对多表的关系图</br></center>

<center><img src="https://cdn.nlark.com/yuque/0/2022/png/22965791/1648822177791-4d9fe174-8c64-46cc-8de7-10c4742ad0ca.png" width="500" hegiht="" ></center>
<center><br>建立多对多表的关系图</br></center>

### 多表查询--概述
- 概述：指从多张表中进行数据查询
- 笛卡尔积：笛卡尔乘积是指在数学中，两个集和A和集合B的所有组合情况。（再多表查询时，需要消除无效的笛卡尔积：用where条件进行消除）

<center><img src="https://cdn.nlark.com/yuque/0/2022/png/22965791/1648822177791-4d9fe174-8c64-46cc-8de7-10c4742ad0ca.png" width="500" hegiht="" ></center>
<center><br>建立多对多表的关系图</br></center>

- 多表查询分类
  - 连接查询
    - 内链接：相当于查询A,B交集部分数据
    - 外连接：
      - 左外连接查询：查询左表的所有数据，以及两张表交集部分数据
      - 右外连接：查询右表所有数据，以及两张表交集部分数据
    - 自链接：当前表与自身的连接查询，自连接必须使用表别名
  - 子查询
  
<center><img src="https://cdn.nlark.com/yuque/0/2022/png/22965791/1648824100562-7ca2fbfa-76e5-40db-b175-1aaa9ec5b4cd.png" width="500" hegiht="" ></center>
<center><br>建内连接</br></center>
  
      

### 多表查询--内连接
- 内连接查询语法
  - 隐式内连接
  
         select 字段列表 from 表1，表2 where 条件...;
  - 显示内连接

        select 字段列表 from 表1 [inner] join 表2 on 连接条件...;
- 内连接查询是两张表的交集部分
  
<center><img src="https://cdn.nlark.com/yuque/0/2022/png/22965791/1648824100562-7ca2fbfa-76e5-40db-b175-1aaa9ec5b4cd.png" width="500" hegiht="" ></center>
<center><br>建立多对多表的关系图</br></center>

### 多表查询--外连接
- 左外连接:相当于查询表1（左表）的所有数据包含表1和表2交集部分数据
  
      select 字段列表 from 表1 left [outer] join 表2 on 条件...
  
- 右外连接：相当于查询表2（右表）的所有数据包含表1和表2交集部分数据
  
      select 字段列表 from 表1 right [outer] join 表2 on 条件...


### 多表查询--自链接
- 自链接查询语法
- 自连接查询可以是内连接查询也可以是外连接查询
  
      select 字段列表 from 表A 别名A join 表2 别名2 on 条件...
  
### 多表查询--联合查询union
- 对于联合（union）查询,就是把多次查询的结果合并起来，形成一个新的查询结果集
  
        select 字段列表 from 表A，....
        union [all]
        select 字段列表 from 表B,....
- **注意**
  - 对于联合查询多张表的列数必须保持一致，字段类型也需要保持一致
  - union all 会将全部的数据直接合并在一起，union会对合并之后的数据去重
### 多表查询--子查询介绍
- 概念：sql语句中嵌套select语句，称为嵌套查询，又称为子查询
- 
       select * fron t1 where column=(select column1 from t2);

- **注意**
  - 子查询的外部语句可以是insert/update/delete/select中的任意一个
- 根据子查询结果不同，分为：
  - 标量子查询（子查询的结果为单个值）
  - 列子查询（子查询的结果为一列）
  - 行子查询（子查询结果为一行）
  - 表子查询（子查询的结果为多行多列）
- 根据子查询的位置，又可以分为：where之后，from之后，select之后
### 多表查询--标量子查询
- 标量子查询：子查询返回的结果是单个值（数字，字符串，日期等），最简单的形式，这种子查询称为标量子查询
- 常用操作符：= <> > >= < <=
### 多表查询--列子查询
- 列子查询
  - 子查询返回的结果是一列（可以是多行），这种子查询成为列子查询
  - 常用的操作符有：in ,not in ,any ,some ,all

操作符  | 描述
-----  |------
in  | 在指定范围之内，多选一
not in  | 不在指定的范围之内
any  | 在查询返回列表中，有任意一个满足即可
some  | 与any等同，使用some的地方都可以使用any
all  | 子查询返回列表的所有值都必须满足

### 多表查询--行子查询
- 行子查询
  - 组查询返回的结果是一行（也可以是多列），这种子查询称为行子查询
  - 常见的操作符：=，<>,in,not in
                
            #查询与张无忌的薪资以及直属领导相同的员工共信息
            -- a.查询张无忌薪资以及直属领导信息
            select salary,managerid from emp1 where name='张无忌';
            -- b. 根据结果查询
            select * from emp1 where salary=12500 and managerid='1';
            select * from emp1 where (salary,managerid)=(select salary,managerid from emp1 where name='张无忌')

### 多表查询--表子查询
- 表子查询
  - 子查询的结果是多行多列，这种子查询称为表子查询
  - 常见操作符：in
    
        查询与‘鹿杖客’，‘宋远桥’的职位和薪资相同的员工信息
        -- a.查询薪资和职位
        select job,salary from emp1 where name in('鹿杖客','宋远桥');
        -- b.查询员工
        select * from emp1 where (job,salary) in (select job,salary from emp1 where name in('鹿杖客','宋远桥'));
        
        查询入职日期是2006-01-01之后的员工信息以及部门信息
        -- a.入职是日期之后的员工信息
        select * from emp1 where entrydate>'2006-01-01';
        -- b.查询这部分员工对应的部门信息
        select e.*,d.name from (select * from emp1 where entrydate>'2006-01-01') e left outer join dept d on e.dept_id=d.id;

### 多表查询--练习1
        -- 案例
        -- 数据准备
        create table salgrade
        (
            grade int,
            losal int,
            hisal int
        ) comment '薪资等级表';
        
        insert into salgrade values (1, 0, 3000);
        insert into salgrade values (2, 3001, 5000);
        insert into salgrade values (3, 5001, 8000);
        insert into salgrade values (4, 8001, 10000);
        insert into salgrade values (5, 10001, 15000);
        insert into salgrade values (6, 15001, 20000);
        insert into salgrade values (7, 20001, 25000);
        insert into salgrade values (8, 25001, 30000);
        
        -- 1. 查询员工的姓名、年龄、职位、部门信息 (隐式内连接)
        select e.name, e.age, e.job, d.name from emp as e, dept as d where e.dept_id = d.id;
        
        -- 2. 查询年龄小于30岁的员工的姓名、年龄、职位、部门信息 (显示内连接)
        select e.name, e.age, e.job, d.name from emp as e, dept as d where e.dept_id = d.id and age < 30;
        select e.name, e.age, e.job, d.name from emp as e inner join dept as d on e.dept_id = d.id where age < 30;
        
        -- 3. 查询拥有员工的部门ID、部门名称
        select distinct e.dept_id, d.name from emp as e, dept as d where e.dept_id = d.id;
        
        -- 4. 查询所有年龄大于40岁的员工, 及其归属的部门名称; 如果员工没有分配部门, 也需要展示出来(左外连接)
        select e.name, d.name from emp as e left join dept as d on e.dept_id = d.id where age > 40;
        
        -- 5. 查询所有员工的工资等级
        -- 表: emp , salgrade
        -- 连接条件 : emp.salary >= salgrade.losal and emp.salary <= salgrade.hisal
        select e.*, s.grade from emp as e, salgrade as s where e.salary >= s.losal and e.salary <= s.hisal;
        -- 方式一
        select e.*, s.grade, s.losal, s.hisal from emp e, salgrade s where e.salary >= s.losal and e.salary <= s.hisal;
        -- 方式二
        select e.*, s.grade, s.losal, s.hisal from emp e, salgrade s where e.salary between s.losal and s.hisal;
        
        -- 6.  查询 "研发部" 所有员工的信息及 工资等级
        select id from dept where name = '研发部';
        select e.*, s.grade from emp e, dept d, salgrade s where e.dept_id = d.id and (e.salary between s.losal and s.hisal) and d.name = '研发部';
        
        -- 7. 查询 "研发部" 员工的平均工资
        select id from dept where name = '研发部';
        select avg(e.salary) from emp e, dept d where e.dept_id = d.id and d.id = (select id from dept where name = '研发部');
        select avg(e.salary) from emp e, dept d where e.dept_id = d.id and d.name = '研发部';
        
        -- 8. 查询工资比 "灭绝" 高的员工信息
        select salary from emp where name = '灭绝';
        select * from emp where salary > (select salary from emp where name = '灭绝');
        
        -- 9. 查询比平均薪资高的员工信息
        select avg(salary) from emp; select * from emp where salary > (select avg(salary) from emp);
        
        -- 10. 查询低于本部门平均工资的员工信息 (假设查2)
        select avg(e1.salary) from emp e1 where e1.dept_id = 1;
        select avg(e1.salary) from emp e1 where e1.dept_id = 2;
        select e2.* from emp e2 where e2.salary < (select avg(e1.salary) from emp e1 where e1.dept_id = e2.dept_id);
        
        -- 11. 查询所有的部门信息, 并统计部门的员工人数
        select d.id, d.name, count(e.dept_id) as numbers from emp e, dept d where e.dept_id = d.id group by e.dept_id;
        select d.id, d.name , ( select count(*) from emp e where e.dept_id = d.id ) '人数' from dept d;
        
        -- 12. 查询所有学生的选课情况, 展示出学生名称, 学号, 课程名称
        -- 表: student , course , student_course
        -- 连接条件: student.id = student_course.studentid , course.id =student_course.courseid
        select s.name, s.id, c.name from student s, course c, student_course sc where s.id = sc.studentid and c.id =sc.courseid;
### 多表查询--练习2
### 多表查询--小结
## 第六节 事务
### 事务--简介
### 事务--操作演示
### 事务--四大特征ACID
### 事务--开发事务问题
### 事务--开发事务演示及隔离级别
### 事务--小结
## 第六节 基础篇总结
# 第二章--进阶
