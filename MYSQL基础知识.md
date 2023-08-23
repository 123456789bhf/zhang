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

- **auto_increment注意点**
  - 一个表中只能有一个自动增长字段，该字段的数据类型是整数类型，且必须定义为键，如 UNIQUE KEY 、PRIMARY KEY。

  - 若为自动增长字段插入 NULL、0、DEFAULT 或在插入时省略该字段，则该字段就会使用自动增长值；若插入的是一个具体值，则不会使用自动增长值。

  -  自动增长值从 1 开始自增，每次加 1。若插入的值大于自动增长的值，则下次插入的自动增长值会自动使用最大值加 1；若插入的值小于自动增长值，则不会对自动增长值产生影响。

  -  使用 DELETE 删除记录时，自动增长值不会减小或填补空缺

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
1. 多表关系
   - 一对多：在多的一方设置外键，关联一方的主键
   - 多对多：建立中间表，中间表包含两个外键，关联两张表的主键
   - 一对一：用于表结构拆分，在其中任何一方设置外键（union),关联另一方主键
2. 多表查询
   - 内连接
     - 隐式：select ...from 表A,表B where 条件...
     - 显式：select...from 表A inner join 表B on 条件
   - 外连接
     - 左外：select ...from 表A left join 表B on 条件
     - 右外：select ...from 表A right join 表B on 条件
   - 自连接：select...from 表A 别名1，表2 别名2 where 条件...
   - 子查询：标量子查询，列子查询，行子查询，表子查询
## 第六节 事务
### 事务--简介
- **事务**是一组操作集合，它是一个不可分割的工作单位，事务会把所有的操作作为一个整体一起向系统提交或撤销操作请求，即这些操作**要么同时成功，要么同时失败**
- 下面的操作李四的钱没有增加1000，那么转账过程不成功，此时张三的钱也不应该减少1000
  
<center><img src="https://i.postimg.cc/tJ4ZrXMh/2023-08-20-214538.png" width="500" hegiht="" ></center>
<center><br> </br></center>

- 默认mysql的事务是自动提交的，也就是说，当执行一条DML语句，mysql会立即隐式的提交事务
### 事务--操作演示
- 查看/设置事务提交方式
  
      select @@autocommit;
      set autocommit=0;(1:自动提交（默认），0：手动提交)
- 提交事务
  
      commit;
- 回滚事务
  
      rollback
- 开启事务
  
      start transaction 或begin;

- 提交事务
  
      commit 
- 回滚事务

      rollback
### 事务--四大特征ACID（面试问）
##### 事务四大特性
- 原子性（automicity）:事务是不可分割的最小原子单元，要么全部成功，要么全部失败。
- 一致性（consistency):事务完成时，必须使所有的数据都保持一致状态。
- 隔离性（isolation):数据库系统提供的隔离机制，保证事务在不受外部并发操作影响的独立环境下运行。
- 持久性（durability）:事务一旦提交或回滚，它对数据库的改变就是永久的。
### 事务--开发事务问题
问题  | 描述
------  | -------
脏读  | 一个事务读取带另外一个数据还没有提交的数据
不可重复读  | 一个事务先读取同一条记录，但两次读取的数据不同，称之为不可重复读
幻读  | 一个事务按照条件查询数据时，没有对应的数据行（此时可以执行插入操作），但在插入数据时，又发现这行数据已经存在，好像出现了’幻影‘
- 脏读：事务B在读取id=1的数据时，事务A正在更改id=1的数据，但还没有提交

  <center><img src="https://i.postimg.cc/8C6TSs31/1.png" width="500" hegiht="" ></center>
- 不可重复读：事务B更新了id=1的数据并且提交了，此时事务A在事务B更新id=1的数据之前查询过一次，在更新之后又查询了id=1的数据，这就出现了两次读取数据不一样的情况

 <center><img src="https://i.postimg.cc/wMchbqH2/2.png" width="500" hegiht="" ></center>

- 幻读：在事务A读取完id=1的数据之后（此时发现没有id=1的数据，id是主键），事务B提交了修改id=1的语句，此时数据库中已经有id==1的数据，那么事务A在执行插入id=1的数据就会出错，因为id是主键，违背唯一性，然后事务A在执行查询id=1仍然没有（因为前面已经解决了不可重复读取的问题了，所以在此查询id=1仍然没有），也就是出现了幻影

 <center><img src="https://i.postimg.cc/0Q1ntHD8/3.png" width="500" hegiht="" ></center>

### 事务--并发事务演示及隔离级别
##### 事务隔离级别用于解决并发问题
- 事务隔离级别

隔离级别  | 脏读  | 不可重复读  | 幻读
-------  | ------ | -------  | -------
read uncommitted  | 会出现  |  会出现  | 会出现
read committed（oracle 的默认）  | 会出现  |不会出现  | 不会出现
repeatable read(mysql的默认)  | 会出现  | 会出现  | 不会出现
serializable  | 会出现  | 会出现  | 会出现

— 从上到下隔离级别升高，随着隔离级别的升高，性能越低，数据安全性越高，选择隔离级别要根据实际情况选择
- 查看隔离级别
  
     select @@transaction_isolation
- 设置事务隔离级别
  
      select [session|global] transaction isolation level {read uncommitted|read committed|repeatable_read|serializable}
      session:仅对当前窗口有效
      global :对所有的客户端会话窗口有效

- 采用两个对话框来进行两个事务
  
[![4.png](https://i.postimg.cc/KjrjN8L5/4.png)](https://postimg.cc/Lg5m4Rxq)

- 判断read uncommitted是否会出现脏读问题

  [![2023-08-21-101125.png](https://i.postimg.cc/QM4yFQyQ/2023-08-21-101125.png)](https://postimg.cc/CZ8NtqY5)
- 判断read committed是否解决了脏读问题

[![2023-08-21-101454.png](https://i.postimg.cc/8Cz18bvM/2023-08-21-101454.png)](https://postimg.cc/YvTcYYbC)

- 幻影现象

[![2023-08-21-102642.png](https://i.postimg.cc/8CX6hPWv/2023-08-21-102642.png)](https://postimg.cc/94T022LX)

- seralizable解决幻影现象：只能有一个事务进行操作，如果事务A,事务B同时操作同一个表，那么事务B会等事务A提交（commit）之后才会进行操作

[![2023-08-21-103201.png](https://i.postimg.cc/sfwt7k0r/2023-08-21-103201.png)](https://postimg.cc/PNv3kRj3)

### 事务--小结
1. 十五简介：事务是一组操作的经济和，这组操作，妖魔全部执行成功，要么全部执行失败
2. 事务操作

        start tansaction :开启事务
        commit/rollback:提交/回滚事务
3. 事务四大特征
   - 原子性（A）,一致性（C）,隔离性（I),持久性（D）
4. 并发事务问题
   - 脏读，不可重复读，幻读
5. 事务隔离级别
   - read uncommitted，read committed，repeatible read,serializable;
## 第六节 基础篇总结

# 第二章--进阶
## 进阶--存储引擎
### 进阶--存储引擎--mysql体系结构

[![2023-08-21-110354.png](https://i.postimg.cc/595Q930T/2023-08-21-110354.png)](https://postimg.cc/bdJw3119)

- 连接层：最上层是一些客户端和连接服务，主要完成一些类似于连接处理、授权认证、以及相关的安全方案。服务器也会为安全接入的每个客户端验证它所具有的操作权限
- 服务层：第二层架构主要完成大多数服务功能，如SQL接口，并完成缓存查询，SQL分析和优化，部分内置函数执行。所有跨存储引擎功能也爱这一层实现，如：过程、函数。
- 引擎层：存储引擎真正的负责了MTYSQL中数据的存储和提取，服务器同各国APP和存储引擎进行通信。不同存储引擎具有不同功能，这样我们可以根据自己的需求，来选取合适的存储引擎
- 存储层：主要讲数据存储在文件系统之上，并完成与存储引擎的交互
- **注意**
- 索引是在引擎层实现的们也就是说不同的存储引擎，索引的实现方式可能不同
- innoDB引擎是sql5.5版本之后默认的
### 进阶--存储引擎--简介
- **存储引擎**就是存储数据、建立索引、更新/查询数据等技术的实现方式。存储引擎是基于表的，而不是基于库的（在一个数据库中不同表可以有多个存储引擎），所以存储引擎也可被称为表类型。
1. 创建表时，指定存储引擎
   
         create table 表名（
               字段1 字段1类型 [comment 字段1注释],
               ....
               字段n 字段n类型 [comment 字段n注释]
         )engine=innodb [comment 标注释]
2. 查看当前数据库支持的存储引擎
   
        show engines;
   
### 进阶--存储引擎--innoDB介绍
- **介绍**：innoDB是一种兼顾该可靠性和高性能性的通用存储引擎，在mysql5.5之后，innoDB是默认的mysql存储引擎。
- **特点**
  - DML操作遵循ACID模型，支持**事务**
  - **行级锁**，提高并发访问性能
  - 支持外键foreign key约束，保证数据的完整性和正确性。
- 文件
  - xxx.ibd：xxx代表表名，innoDB引擎的每张表都会对应这样一个表空间文件，存储该表的表结构（frm,sdi）、数据和引擎
  - 参数：innodb_file_per_table(每张表都对应一个表空间文件)
- 存储引擎的特点
  - innoDB
    
[![2023-08-21-142831.png](https://i.postimg.cc/Vkn5rVhw/2023-08-21-142831.png)](https://postimg.cc/SnQmHDq1)
- 一个区里面存储64个页，并且区的大小固定为1M
- 一个页里面存储16个行，固定大小为16K
- 表空间有段组成
### 进阶--存储引擎--mysiam和Memory
- myisam
  - 介绍
    - myisam是mysql早期的默认存储引擎
  - 特点
    - 不支持事务，不支持外键
    - 支持表锁，不支持行锁
    - 访问速度快
  - 涉及三个文件
    - tb_book_MYD  MYD文件
      - 存储放结构信息
    - tb_book_MYI  MYI文件
      - 存放数据
    - tb_book_448.sdi  SDI文件
      - 存放索引
- memory
  - **介绍**：memmory引擎的表数据存储在内存中，由于受到硬件问题、或断电问题的影响，只能将这些表作为临时表或缓存使用。
  - **特点**
    - 内存存放（所以访问速度比较快）
    - hash索引（默认）
  - 文件
    - XXX.sdi:存储表结构信息（因为数据存放在内存中，那么不需要单独的文件）
- 存储索引的特点（面试考）

 特点 | innoDB  | MyISAM  | Memory
 ----  | ------  | -------  | -----
 存储限制  | 64TB  | 有  | 有
 事务安全  | 支持  |  -   |  -
 锁机制  | 行锁  | 表锁  | 表锁
 B+tree索引  | 支持  |  支持  | 支持
 hash索引  | -  | -  | -
 全文索引  | 支持（5.6版本之后）  | 支持  | -
 空间使用  | 高  | 低  | N/A
 内存使用  | 高  | 低  | 中等
 批量插入速度  | 低  | 高 | 高
 支持外键  | 支持  | -   | -
 
### 进阶--存储引擎--选择
- 在选择存储引擎时，应根据应用系统的特点选择合适的存储引擎。对于复杂的应用系统，还可以根据与实际情况选择多种存储引擎进行组合。
  - innoBDB（绝大多数场景使用）:是mysql的默认引擎，支持事务、外键。如果应用对事务完整性有比较高的要求，在并发条件下要求数据的一致性，数据操作除了插入和查询之外，还包含更多的更新、删除操作，那么innoDB存储引擎是比较合适的选择。
  - myisam:如果应用是以读取操作和插入操作为主，只有很少的更新和删除操作，并且对事物的完整性、并发性要求不是很高，那么选择这个存储引擎是非常合适的。比如：电商中的足迹以及评论相关数据，虽然不支持事务，但该数据不是核心数据，丢几条也没有很大的关系。
  - memory:将所有数据保存在内存中，访问速度快，通常用于临时表以及缓存。memory的缺陷就是对表的大小的限制，太大的表无法缓存在内存中，而且无法保证数据的安全性。
### 进阶--存储引擎--小结
1. 体系结构
   - 连接层、服务层、引擎层、存储层
2. 存储引擎简介
   
        show engines;
        create table XXX(...)engine=innodb;
## 进阶--mysql安装（linux版本）
## MySQL8.0.26-Linux版安装

### 1. 准备一台Linux服务器

云服务器或者虚拟机都可以; 

Linux的版本为 CentOS7;



### 2. 下载Linux版MySQL安装包

https://downloads.mysql.com/archives/community/

![image-20211031230239760](assets/image-20211031230239760.png) 



### 3. 上传MySQL安装包

![image-20211031231930205](assets/image-20211031231930205.png) 



### 4. 创建目录,并解压

```
mkdir mysql

tar -xvf mysql-8.0.26-1.el7.x86_64.rpm-bundle.tar -C mysql
```



### 5. 安装mysql的安装包

```
cd mysql

rpm -ivh mysql-community-common-8.0.26-1.el7.x86_64.rpm 

rpm -ivh mysql-community-client-plugins-8.0.26-1.el7.x86_64.rpm 

rpm -ivh mysql-community-libs-8.0.26-1.el7.x86_64.rpm 

rpm -ivh mysql-community-libs-compat-8.0.26-1.el7.x86_64.rpm

yum install openssl-devel

rpm -ivh  mysql-community-devel-8.0.26-1.el7.x86_64.rpm

rpm -ivh mysql-community-client-8.0.26-1.el7.x86_64.rpm

rpm -ivh  mysql-community-server-8.0.26-1.el7.x86_64.rpm

```



### 6. 启动MySQL服务

```
systemctl start mysqld
```

```
systemctl restart mysqld
```

```
systemctl stop mysqld
```



### 7. 查询自动生成的root用户密码

```
grep 'temporary password' /var/log/mysqld.log
```

命令行执行指令 :

```
mysql -u root -p
```

然后输入上述查询到的自动生成的密码, 完成登录 .



### 8. 修改root用户密码

登录到MySQL之后，需要将自动生成的不便记忆的密码修改了，修改成自己熟悉的便于记忆的密码。

```
ALTER  USER  'root'@'localhost'  IDENTIFIED BY '1234';
```

执行上述的SQL会报错，原因是因为设置的密码太简单，密码复杂度不够。我们可以设置密码的复杂度为简单类型，密码长度为4。

```
set global validate_password.policy = 0;
set global validate_password.length = 4;
```

降低密码的校验规则之后，再次执行上述修改密码的指令。



### 9. 创建用户

默认的root用户只能当前节点localhost访问，是无法远程访问的，我们还需要创建一个root账户，用户远程访问

```
create user 'root'@'%' IDENTIFIED WITH mysql_native_password BY '1234';
```



### 10. 并给root用户分配权限

```
grant all on *.* to 'root'@'%';
```



### 11. 重新连接MySQL

```
mysql -u root -p
```

然后输入密码



### 12. 通过DataGrip远程连接MySQL

## 进阶--索引
### 进阶--索引--概述
- **介绍**：索引是一种数据结构，邦族MYSQL**高校获取数据**的**数据结构**。在数据之外，数据库系统还维护着满足特定查找算法的数据结构，这些数据结构以某种方式引用（指向）数据，这样就可以在这些数据结构上实现高级查找算法，这种数据结构就是索引。

[![2023-08-22-215029.png](https://i.postimg.cc/XvrWfPtN/2023-08-22-215029.png)](https://postimg.cc/NyvZYdgZ)

- 演示
  - 无索引：也就是全表扫描，从第一条数据开始查找
  - 有索引：使用二叉树（并不是真实的索结构），每个节点都存储着对应数据的索引

[![2023-08-22-215430.png](https://i.postimg.cc/Kcw9q84y/2023-08-22-215430.png)](https://postimg.cc/ThjqhGrk)

- 优缺点
  
优势  | 劣势
-----  | ------
提高数据索引的效率  | 索引列也是需要占用空间的
通过索引对数据进行排序，降低数据排序成本，降低CPU的消耗  | 索引大大提高了查询效率，同时也降低更新表的速度，如对表进行insert,update,delete时，效率降低

- **注意**：一般缺点可以忽略，因为硬盘比较便宜，可以存储很多数据，其次，现实中增删改的操作比较少。
### 进阶--索引--结构--介绍
- 索引在存储引擎层中实现，也就意味着不同的存储引擎有不同的结构，主要包括以下几种：

索引结构  | 描述
------  | ---------
B+Tree索引  | 最常见的索引类型，大部分存储引擎都支持B+树索引
Hash索引  | Hash索引的底层数据结构使用哈希表实现的，只有精确匹配索引列的查询才有效，不支持范围查询
R-Tree(空间索引，了解即可)  | 空间索引是MYISAM引擎的一个特殊引类型，主要用于地理空间数据类型，通常使用较少
Full-text(全文索引)  | 是一种通过建立倒排索引，快速匹配文档的方式。类似于Lucene,Sokr,ES

索引 | InnoDB  | MYSIAM  | Memory
-----  | -----  | ------  |------
B+Tree索引  | 支持  | 支持  | 支持
Hash索引  | 不支持  | 不支持 | 支持
R-Tree索引 | 不支持 | 支持  | 不支持
Full-text  | 5.6版本之后  | 支持 | 不支持

- **注意**：我们平常所说的索引，如果没有特别声明，都是指B+Tree索引。
### 进阶--索引--结构--btree
- <font color="red">二叉树</font>

[![2023-08-22-221309.png](https://i.postimg.cc/0j3vBRFy/2023-08-22-221309.png)](https://postimg.cc/8fhx73T2)

- 左边的的是平衡二叉树，左子节点比父节点小，右子节点比父节点大，
- 二叉树缺点：顺序插入时，会形成一个链表，查询性能大大降低。大数据量情况下，层级较深，检索速度慢。红黑树可以防止出现链表的情况。
- 红黑树：大数据量情况下，层级较深，检索速度慢。
- <font color="red">B-Tree(多路平衡查找树)</font>
  - 以一颗最大度数（max-degree）为5（5阶）的b-tree为例（每个几点最多存储4个key,5个指针）。k个key有k+1个指针，k+1个子节点
  - 树的度数：指的是一个结点的子结点个数。
  - 下面的图表示4个key,小于20，大于20小于30，大于30小于62，大于62小于89，大于89，共五个指针（也就是5个子节点）

[![2023-08-22-222016.png](https://i.postimg.cc/2jPhWq9g/2023-08-22-222016.png)](https://postimg.cc/V5WJQN8F)

- data structure visualization网站（https://www.cs.usfca.edu/~galles/visualization/Algorithms.html）找到B-Tree可以看到插入过程

[![2023-08-22-222933.png](https://i.postimg.cc/XvkXrqBS/2023-08-22-222933.png)](https://postimg.cc/7CbqcxNm)

- B-Tree介绍：https://blog.csdn.net/yin767833376/article/details/81511377
  
### 进阶--索引--结构--B+tree
- B+Tree
  - 以一颗最大度数（max-degree）为4（4阶）的b+tree为例子
  - 介绍：https://blog.csdn.net/yin767833376/article/details/81511377
  - 特点
    - 所有数据都会出现在叶子节点，其他节点只是起到索引数据作用，叶子节点存放数据
    - 叶子节点形成了一个单向链表，每一个节点都会通过一个指针指向下一个元素，最终形成了单向链表

[![2023-08-22-223638.png](https://i.postimg.cc/gcLF4Jmv/2023-08-22-223638.png)](https://postimg.cc/G9R5mbB2)

- B+Tree
  - Mysql索引数据结构对经典的B-Tree进行了优化。在原B+Tree的基础上，增加一个指向相邻叶子结点的链表指针，就形成了带有顺序指针的B-Tree，提高区间访问性能，利于数据库的排序操作。

[![2023-08-22-223852.png](https://i.postimg.cc/D0pS2wpQ/2023-08-22-223852.png)](https://postimg.cc/30p81YTW)

- InnoDB中提过页

### 进阶--索引--结构--hash
- Hash:哈希索引就是采用一定的hash算法，将键值换算成新的hash值，映射到对应的槽位上，然后存储在hash表中。如果两个（或多个）简直映射到一个相同的槽位上，他们就产生了hash冲突，可以通过链表来解决。

[![2023-08-22-224307.png](https://i.postimg.cc/mD2MRJ2s/2023-08-22-224307.png)](https://postimg.cc/NySLkNHJ)

- hash索引的特点
  1. Hash索引只能用于对等比较（=，in）,不支持范围查询（between，>,<,...）（因为在存储的时候没有顺序）
  2. 无法利用索引完成排序操作（因为hash运算出来的结果无序）
  3. 查询效率高，通常只要一次检索就可以了，效率通常要高于B+tree索引）
- 存储引擎支持
  - 在MYSQL中，支持hash索引的是Memory引擎，而innoDB中具有自适应hash功能，hash索引是存储引擎根据B+tree索引在指定条件下自动创建的。
### 进阶--索引--结构--思考题
为什么INnoDBb存储引擎选择适应B+tree索引结构
- 相对于二叉树，层级更少，搜索效率更高（二叉树在顺序数据条件下会形成一个链表，这样搜索效率降低，红黑树虽然能解决二叉树情况，但本质上是树，大数据量情况下，层级较深，检索速度慢。）
- B-Tree,无论是叶子节点还是非叶子节点，都会保存数据，这样导致一页中存储的键值减少，指针跟着减少，要同样保存大量数据，只能增加树的高度,导致性能降低。、
- 对于hash索引，B-Tree支持范围匹配以及排序操作。
### 进阶--索引--分类
- 索引分类
  
分类  | 含义  | 特点  | 关键字
----  |-------  | -------  | -------
主键索引  | 针对于表中主键创建的索引  | 默认自动创建,只能有一个  | primary
唯一索引  | 避免同样一个表中某数据列中的值重复  | 可以有多个  | unique
常规索引  | 快速定位特定数据  | 可以有多个 |  
全文索引  | 全文索引查找的是文本中的关键词，而不是比较索引中的值 | 可以有多个 | fulltext

- **注意**
  -  实际上当进行唯一约束的时候会自动创建一个唯一索引
  - 只有主键索引只有一个，其他索引可以有多个

- 在innoDB存储引擎中，根据存储引擎的形状可以分为以下两种：
  
分类  | 含义 | 特点
-----  | --------  | -------
聚集索引(clustered index)  | 将数据存储与索引存放到一块，索引结构的叶子节点保存了行数据  | 一张表中聚集索引必须有，并且只有一个
二级索引（secondary index）  | 将数据与索引分开存储，索引结构的叶子节点关联的是对应的主键  | 一张表中聚集索引可以存在多个
- 聚集索引的选取规则
  - 如果存在主键，主键索引就是聚集索引
  - 如果不存在主键，将使用第一个唯一（union）索引作为聚集索引
  - 如果表没有主键，或没有合适的唯一索引，那么innoDB会自动生成一个rowid作为隐藏的聚集索引
- 下面图中id是主键，所以是聚集索引，name不是主键，所以是二级索引，叶子节点挂的是主键

[![2023-08-23-102732.png](https://i.postimg.cc/256ZsjRr/2023-08-23-102732.png)](https://postimg.cc/w1CMJpjG)

- 查找时候，先根据name='Arm‘，在二级索引中找到叶子节点对应的id值，再根据id值在聚集索引中找到整行数据。

[![2023-08-23-103026.png](https://i.postimg.cc/bvQ7jPQV/2023-08-23-103026.png)](https://postimg.cc/XZYHwT19)

### 进阶--索引--思考题
1. 以下SQL语句哪个执行效率高？为什么？

       select * from user where id=10;
       select * from user where name='Arm';
       注意：id为主键，name字段创建的有索引
- 第一条直接在聚集索引中查找即可，也就是扫描一个索引
- 第二条需要现在二级索引中扫描，再在聚集索引中扫描，也就是扫描两个索引，所以第一条语句的效率高
2. innoDB主键索引的B+tree高度有多个呢？
 - 假设一行数据大小为1K,一页中可以存储16行这样的数据(一页大小为16K)。innoDB的指针占用6个字节的空间，主键为bigint（如果主键是int,占用4个字节，住建为bigint占用8个字节）,占用字节数为8
 - 假设B+Tree的高度为2，其中n为一个非子结点存储的主键个数，那么指针个数为n+1，一页的大小为16K
   - n*8+(n+1)*6=16*1024 计算n约为1170，也就是该非叶子节点最多有1171个指针
   - 1171*16=18736也就是B+Tree最多存储的数据量
  - 假设高度为3

[![2023-08-23-104722.png](https://i.postimg.cc/sDT67XcR/2023-08-23-104722.png)](https://postimg.cc/F7JVQh8P)

    - 1171*1171*16=21939856，也就是B+Tree最多存储的数据量
### 进阶--索引--语法
- 创建索引
  
        create [unique|fulltext] index index_name on table_namen (index_col_name,...);
        如果没有 [unique|fulltext]就表示创建的是常规索引
        index_col_name,...表示一个索引可以关联多个字段的
  - 如果一个索引关联一个字段称为**单列索引**
  - 如果一个索引关联多个字段称为**组合索引/关联索引**
- 查看索引

        show index from table_name;
 
- 删除索引

        drop index index_name on table_name
- 案例：
  1. name字段为姓名字段，该字段的只可能重复，为该字段创建索引
  2. phone手机字段的值，是非空，并且唯一，为该字段创建唯一索引
  3. 为profession,age,status创建联合索引
  4. 为email建立合适的索引来提高查询效率

### 进阶--索引--性能分析--查看执行频次
- sql执行频率：如果实习频率较低，那么没必要进行优化
  - MYSQL客户端连接成功后，可通过show[sessionlglobal]status命令可以提供服务器状态信息。同各国如下指令，可以查询当前数据库的insert,update,delete,select的访问次数

            show global status like 'com____';
            一个下划线代表一个字符
  
### 进阶--索引--性能分析--慢查询日志
- 慢日志查询:如果前面已经知道那条语句执行频频次高，之后就可以对该语句进行优化
  - 慢查询日志记录了所有执行时间超过指定参数（long_query_time,单位：秒，默认10秒）的所有SQL语句日志。
  - MYSQL的慢查询日志默认没有开启，需要在MYSQL的配置文件（/etc/my.cnf）中配置如下信息：
    
          show variables like 'slow_query_log';#查询慢查询日志是否打开
          #开启mysql慢日志查询开关
          slow_query_log=1;
          #设置慢日志的时间为2秒，SQL语句执行时间超过2秒，就会视为慢查询，记录慢查询日志
          long_query_time=2;
    
   - 配置完成之后，通过以下指令重新启动MYSQL服务器进行测试，查看慢日志文件记录信息/Var/lib/mysql/localhost-slow.log.
### 进阶--索引--性能分析--show profiles
- 慢查询日志是根据语句执行时间来判断执行效率，但是要求是耗时在直接定时间以上才会显示，比如说2s,低于2s就不会显示，但是我们也相对该语句进行优化
- profile详情
  - show profiles能够在做SQL优化时帮助我们了解事件都耗去哪里了。通过have_profiling参数，能够看到当前MYSQL是否支持profile操作。

          select @@have_profiling
  - 默认profiling是关闭的，可以通过set语句在session/global级别开启profiling
           select @@profiling; #查看是否打开
           set profiling=1;#打开
           show profiles; #查看强档操作所有语句耗时操作
- profile详情
  - 执行一系列业务SQL的操作，然后通过如下指令查看指令的执行耗时
    
        #查看每一条语句的耗时基本情况
        show profiles;
        #查看指定query_id的SQL语句各个阶段的耗时情况
        show profile for query query id;#query_id在show profiles的第一列显示
        #产看指定query_id的SQL语句的CPU使用情况
        show profile cpu for query query_id;
### 进阶--索引--性能分析--explain
- 前面都是根据时间判断sql语句的执行效率，实际上这只是粗略的判断，并不能完全判断sql语句执行性能，我们还需要explain来判断sql语句执行效率
- explain执行计划
  - explain或者desc命令获取mysql如何执行select语句的信息，包括select语句执行过程中表如何连接和连接顺序
- 语法
  
          #直接在select语句之前加上关键字explain/desc
          explain select 字段列表 from 表名 where 条件；

[![2023-08-23-152748.png](https://i.postimg.cc/RFNqKKDH/2023-08-23-152748.png)](https://postimg.cc/5YWxMY14)

- explain执行计划各个字段的含义
  - id
    - select 查询序列号，表示查询中执行select子句或者是操作表的顺序（id相同，执行顺序从上到下；id不同，值越大，越先执行）(相对于多表查询来说的)
  - select_type
    - 表示select的类型，常见的取值有simple（简单表，即不使用表连接或者子查询）、primary(著查询，即外层查询)、union(union中的第二个或者后面的查询语句）、subquery(select/where之后包含了子查询）等
  - type(重点关注)
    - 表示连接类型，性能由好到差的连接类型为NULL,system,const,eq_ref,ref(使用非唯一索引查询时会出现ref),range,index（用了索引，但是也是对全表进行扫描）,all(表示全表扫描),优化时候，尽量将类型往好的优化。实际上，一般不容易出现null,只有当不访问任何表的时候才会出现null
  - possible_key（重点关注）
    - 显示可能应用在这张表上的索引，一个或者多个
  - key（重点关注）
    - 实际使用的索引，如果为NULL,那么没有使用索引
  - key_len（重点关注）
    - 表示索引中使用的字节数，该值为索引字段最大可能长度，并非实际使用长度，在不损失精确性的前提下，长度越短越好。
  - rows（参考）
    - mysql认为必须执行查询的行数，在innoDB引擎表中，是一个古居之，可能并不总是准确的
  - filtered
    - 表示返回结果的行数占需读取行数的百分比，filtered的值越大越好。
  - extra
    - 额外信息
### 进阶--索引--使用规则--验证索引效率
- 索引使用
- 验证索引效率
  - 在未建立索引之前，执行sql语句，查看sql语句的耗时

          select* from tb_sku where sn='100000003145001';
  - 针对字段创建索引
  
          create index idx_skn_sn on tb_sku(sn);
### 进阶--索引--使用规则--最左前缀法则
- 最左前缀法则
  - 如果索引了多列（联合索引），要遵循最左前缀法则。最左前缀法则指的是查询从索引的最左列开始，并且不跳过索引中的列（也就是最左列必须存在，中间列可以没有，但是后面的部分会失效）。
  - 如果跳过了某一列，索引将部分失效（后面的字段索引失效）
  - **联合索引**就是依次按照各个字段来进行二分查找，先定位到第一个字段对应的值在哪个页里，然后如果第一个字段有多条数据值都一样，就根据第二个字段来找，以此类推，一定可以定位到某条或者某几条数据。
    
            select * from tb_user where profession='软件工程' and age=31 and status='0';
            explain select * from tb_user where profession='软件工程' and age=31 and status='0';
            explain select * from tb_user where profession='软件工程' and age=31;
            #去掉status='0'之后，索引长度从51变为49，说明该索引长度为2
            explain select * from tb_user where profession='软件工程' ;
            #去掉age=31之后，索引长度从49变为47，说明该索引长度为2
            explain select * from tb_user where age=31 and status='0';
            #根据结果可知这样做不是索引，是全部扫描，因为 profession='软件工程'没有，也就是不满足最左前缀法则
            explain select * from tb_user where status='0';
            #根据结果可possible_keys=null知这样做不是索引，是全部扫描，因为 profession='软件工程'以及age=31 没有，不满足最左前缀法则
            explain select * from tb_user where profession='软件工程' and status='0';
            #根据key_len profession有索引，status没有索引，因为跳过了age列
            explain select * from tb_user where age=31 and status='0' and profession='软件工程';
            #此时仍有索引，并且key_len=54 ,也就是三个字段都用上了
- 范围查询
  - 联合索引中，会出此案范围（<,>），范围查询右侧的列索引失效

          explain select * from tb_user where profession='软件工程' and age>30 and status=0;
          #key_len是49 ，因为age使用了范围索引，后面的列status会失效，也就是只有profession，age
          explain select * from tb_user where profession='软件工程' and age>=30 and status=0;
          #如果是>=,那么索引长度变为54，也就是全部索引，但是自己尝试的仍是49

### 进阶--索引--使用规则--索引失效情况一
- 索引列运算
  - 不要再索引列上进行运算操作，否则索引将失效
- 字符串不加引号
- 模糊查询
  - 如果仅仅是尾部模糊匹配，索引不会失效。如果是头部模糊胡匹配，索引会失效。
- 去掉索引，也就是全表扫描，效率极低
  
          explain select * from tb_user where profession like '软件%';
          #走索引，是联合索引的最左边的字段，长度为47
          explain select * from tb_user where profession like '%工程';
          #不走索引
          explain select * from tb_user where profession like '%工%';
          #前后都加%，索引也失效，只要前面加了索引都会失效
### 进阶--索引--使用规则--索引失效情况二
- or连接条件
  - 用or分割的条件，如果or前面的条件中有索引，而后面的列中没有索引，那么设计的索引都不会被用到。
  - 前后条件都有索引时才会生效
- 数据分布影响
  - 如果mysql评估使用索引比全表更慢，那么不会使用索引，也就是需要根据数据分布情况来决定是否使用索引，如果查询条件大部分数据满足，那么使用全局扫描，否则使用索引

          #数据分布影响
          select * from tb_user;
          explain select * from tb_user where phone>='17799990020';
          #此时使用全局索引
          explain select * from tb_user where phone>='17799990000';
          #根据type=all可知是全局扫描，因为是第一个数据，所有数据都满足条件，所以走全局扫描更亏啊
          explain select * from tb_user where phone>='17799990010';
          #此时因为表中绝大部分数据满足条件，索引消失，也就是全局扫描
          explain select * from tb_user where phone>='17799990013';
          #此时少部分满足条件，走索引
          explain select * from tb_user where profession is null;
          #此时有索引
          explain select * from tb_user where profession is not null;
          #没有索引，因为绝大部分数据满足条件，所以全局扫描
          update tb_user set profession=null;
          explain select * from tb_user where profession is null;
          #此时因为大部分数据满足条件，所以是全局扫描
### 进阶--索引--使用规则--SQL提示
- sql提示
  - sql提示，是优化数据库的一个重要手段，简单来说，就是在sql语句中加入一些人为的提示来达到优化操作的目的。也当有联合索引和但只索引值，可以指定到底是用哪个索引
  - user index(告诉数据库使用哪个索引,可能不使用该索引):
    
            explain select * from tb_user use index(index_user_pro) where profession='软件工程'；
  - ignore index(高数数据库不是用哪个索引)：
    
            explain select * from tb_user ignore index(index_user_pro) where profession='软件工程'；
  - force index(告诉数据库必须使用哪个索引):

            explain select * from tb_user force index(index_user_pro) where profession='软件工程'；
### 进阶--索引--使用规则--覆盖索引&回表查询
- 覆盖索引
  - 尽量使用覆盖索引（查询时用了索引，并且需要返回的列，在该索引中已经全部找到），减少selece *的使用
### 进阶--索引--使用规则--前缀索引
### 进阶--索引--使用规则--单列&联合索引
### 进阶--索引--设计原则
### 进阶--索引--小结
## 进阶--sql优化
### 进阶--sql优化--插入数据
### 进阶--sql优化--主键优化
### 进阶--sql优化--order by优化
### 进阶--sql优化--group by 优化
### 进阶--sql优化--limit优化
### 进阶--sql优化--count优化
### 进阶--sql优化--update优化（避免行锁升级为表锁）
### 进阶--sql优化--小结
## 进阶--视图/存储过程/触发器
### 进阶--视图--检查选项（cascaded）
### 进阶--视图--检查选项（local）
### 进阶--视图--更新及作用
### 进阶--视图--案例
### 进阶--存储过程-介绍
### 进阶--存储过程--基本语法
### 进阶--存储过程--变量--系统变量
### 进阶--存储过程--变量--用户自定义变量
### 进阶--存储过程--变量--局部变量
### 进阶--存储过程--if判断
### 进阶--存储过程--参数（in,out,inout）
### 进阶--存储过程--case
### 进阶--存储过程--循环--while
### 进阶--存储过程--循环--repeat
### 进阶--存储过程--循环--loop
### 进阶--存储过程--游标--cursor
### 进阶--存储过程--条件处理器--handler
### 进阶--存储函数
### 进阶--触发器--介绍
### 进阶--触发器--案例1（insert类型）
### 进阶--触发器--案例2（update类型）
### 进阶--触发器--案例3（delete类型）
### 进阶--视图/存储过程/触发器--小结
## 进阶--锁
### 进阶--锁--介绍
### 进阶--锁--全局锁--介绍
### 进阶--锁--全局锁--一致数据备份
### 进阶--锁--表级锁--表锁
### 进阶--锁--表级锁--元数据锁
### 进阶--锁--表级锁--意向锁
### 进阶--锁--表级锁--意向锁--测试
### 进阶--锁--行级锁--介绍
### 进阶--锁--行级锁--行锁
### 进阶--锁--行级锁--间隙锁&临建锁1
### 进阶--锁--行级锁--间隙锁&临建锁2
### 进阶--锁--小结
## 进阶--innoDB引擎

## 进阶--mysql管理
