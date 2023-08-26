
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

          #尽量避免使用select*
          explain select id,profession,age  from tb_user where profession='软件工程' and age=31 and status='0';
          #extra:Using where; Using index
          explain select id,profession,age,status  from tb_user where profession='软件工程' and age=31 and status='0';
          #extra:Using where; Using index,性能高
          explain select id,profession,age,status,name  from tb_user where profession='软件工程' and age=31 and status='0';
          #与前面的extra不同:Using index condition,与前面相比，那么性能会更低
- 知识小贴士
  - using index condition:查找使用了索引，但需要会表查询数据
  - using where,using index:查找使用了索引，但需要的数据都在索引列这种能找到，所以不需要会表查询数据。
- 上面语句的解释
  - 实际上id,profession,age,status都是联合索引，联合索引采用的是二级索引，其叶子节点存储的是id
  - 但name字段是不是二级索引，所以需要根据
- 回表查询
  - 覆盖索引
  - 聚集索引
  
[![2023-08-23-205913.png](https://i.postimg.cc/6pch71cH/2023-08-23-205913.png)](https://postimg.cc/v41nkhp9)
  - 不需要回表查询

[![2023-08-23-210908.png](https://i.postimg.cc/LXPqKn0c/2023-08-23-210908.png)](https://postimg.cc/2bzjn8YG)
  - 需要回表的查询，此时性能较低（因为name是二级索引，所以先根据name找到id，然后根据找到的id在从聚集索引中找到该行数据，然后找到对应的gender值）

[![2023-08-23-211536.png](https://i.postimg.cc/02n0HBSp/2023-08-23-211536.png)](https://postimg.cc/8jFv7wt5)
- 使用select *极有可能出现会表查询
- **思考**
  - 一张表，有四个字段（id,username,password,status）由于数据量大，需要对以下sql语句及逆行优化，该如何进行才是最有方案：

      select id,username,password from tb_user where username='itcast';
     - 针对username和password建立联合索引，此时不需要回表查询
### 进阶--索引--使用规则--前缀索引
- 前缀索引
  - 当字段类型为字符串（varchar,text等）时， 有时候需要索引很长的字符串（比如：一篇文章的标题或者内容），这会让索引变得很大，查询时候，浪费大量的磁盘IO,影响查询效率。此时可以只将字符串的一部分前缀建立索引，这样可以大大节约索引空间，从而提高索引效率。
  - 语法

          create index idx_XXXX on table(column(n))
  - 前缀长度
    - 可以根据索引的选择性来觉电工，而选择性是指不重复的索引值（基数）和数据表的记录总数的壁纸，索引选择性越高查询效率越高，唯一索引的选择性是1，这是最高的索引选择性，性能也是最好的。实际上要根据选择性地要求来决定截取前几个。如果选择行为1，那么就要截取的为1的最短的哪个。
    - 语法
      
          select count(distinct email)/count(*) from tb_user;
          selecy count(distinct substring(email,1,5))/count(*) from tb_user;
- 前缀索引查询流程
  - 辅助索引存储的是email的钱5个字符

[![2023-08-23-213818.png](https://i.postimg.cc/XNrwgkcv/2023-08-23-213818.png)](https://postimg.cc/5jMY4vrc)
  - 查询的时候，根据前五个字符的辅助索引查询到id,再回表查询，根据id找到该行数据，此时将查询结果中的email与查询要求email的值之间对比（因为前面对比只是对应的前缀），如果是，存储该条结果，在辅助索引中lvbu6叶子节点后面的叶子节点是不是lvbu6，如果不是那么停止查询，直接返回上面存储的结果，如果是，需要将该条数据存储起来，继续，最后返回存储的数据（可能有多条 ）
### 进阶--索引--使用规则--单列&联合索引
- 单列索引：一个索引只包含单个列
- 联合索引：一个索引只包含多个列
- 在业务场景中，如果存在多个查询条件吉安，考虑针对于查询字段建立索引时候，建议建立联合索引，而非单列索引
  - 单列索引情况

[![2023-08-23-215609.png](https://i.postimg.cc/LsGhmwhY/2023-08-23-215609.png)](https://postimg.cc/67LB0Hrt)
    - **注意**
      - 多条件联合查询时候，mysql优化器会评估那个字段的索引效率更高，会选择该索引完成本次查询
 - 联合索引情况
   - 每个节点键值存储的各个字段的组合情况，先按照手机号排序，如果手机号一致，那么按照name字段排序，叶子节点挂的是行记录对应的主键（id），所以联合索引可以避免回表查询的

[![2023-08-23-220124.png](https://i.postimg.cc/j2DbCd9R/2023-08-23-220124.png)](https://postimg.cc/gLb5Tdm7)
- **注意**
  - 根据最左前缀法则，可以知道联合索引字段的前后顺序不同，结果也可能不同。
### 进阶--索引--设计原则
1. 针对于数据量较大，并且查询比较频繁的表建立索引（当大于1万的数据量时）
2. 认真对常作为查询条件（where）,排序（order by）,分组（group by）操作的字段建立索引
3. 尽量选择分区度高（也就是能为一确定一行数据的，比如人的身份证）的列作为索引，尽量建立唯一索引，区分度越高，使用索引的效率越高，区分度地时候，效率不高（比如人的性别）
4. 如果四字符串类型的字段，字段长度越长（一篇文章内容），可以针对字段的特点建立前缀索引，此时要考虑前缀区分度
5. 尽量使用联合索引，减少单列索引，查询时，联合索引很多时候可以覆盖索引，节省存储空间，避免回表，提高查询效率，遵循最左前缀法则
6. 要控制索引的数量，索引不是多多益善，索引越多，维护索引结构的代价也就越大，会影响增删改的效率，而且会占用磁盘
7. 如果索引列不能存储null值，请在创建表时使用not null。当优化器知道每一列是否包含null值时，他可以更好的确定哪个索引有效地用于查询
### 进阶--索引--小结
[![2023-08-23-221539.png](https://i.postimg.cc/vmDjyS6V/2023-08-23-221539.png)](https://postimg.cc/PLsKzyyX)
[![2023-08-23-221825.png](https://i.postimg.cc/B6SjtH4H/2023-08-23-221825.png)](https://postimg.cc/p9SW699L)
## 进阶--sql优化
### 进阶--sql优化--插入数据
- insert优化
  - 批量操作(500-1000条合适,当几万条时候，可以分成几次进行批量插入）
    
          insert into tb_test values(1,'tom'),(2,'bob'),...
  - 手动提交事务

          insert into tb_test values(1,'tom'),(2,'bob')
          insert into tb_test values(3,'tom1'),(4,'bob1')
          insert into tb_test values(5,'tom2'),(6,'bob2')
          commit;
  - 主键顺序插入
    - 主键乱序插入：8 1 9 21 88 2 4 15 89
    - 主键顺序插入：1 2 3 4 5 6 7 8 9 15 88
- 大批量数据插入
  - 如果一次性需要插入大批量数据，使用insert语句插入性能较低，此时可以使用mysql数据库提供的load指令进行插入。操作如下：

[![2023-08-23-222548.png](https://i.postimg.cc/s2N0n9x4/2023-08-23-222548.png)](https://postimg.cc/gw3Djhvx)

          #客户端连接服务器时，加上参数--local-infile
           mysql --local-infile -u root -p
          #设置全局参数local_infile为1，开启从本地加载文件导入数据的开关
          set global local_infile=1;
          #执行load指令将准备好的数据加载到表结构中
          load data local infile '/home/user1/load_user_100w_sort.sql' into table tb_user fields terminated by ',' lines terminated by '\n';
          #上面表示每个字段用逗号分割，每行数据用\n分割

          #load_user_100w_sort.sql文件所在位置（建立一个新的测试服务器）
          load_user_100w_sort.sql
- 在执行上面三条语句的时候还需要新建一个测试服务器，进行如下操作

[![2023-08-23-225139.png](https://i.postimg.cc/yxBkgG9f/2023-08-23-225139.png)](https://postimg.cc/5Y7xDnsv)
[![2023-08-23-225150.png](https://i.postimg.cc/8Pzz2Mbr/2023-08-23-225150.png)](https://postimg.cc/7bj47Cdx)
[![2023-08-23-225204.png](https://i.postimg.cc/WbzsWj2G/2023-08-23-225204.png)]
(https://postimg.cc/JGww0fH0)
- **注意**
  - 主键顺序插入性能高于乱序插入
### 进阶--sql优化--主键优化
- 数据组织方式
  - 在innoDB存储引擎中，表数据都是根据主键顺序组织存放的，这种存储方式的表称为索引组织表（index orginalized table IOT），因为innoDB有两种索引，聚集索引叶子节点存储的行数据，并且唯一，一张表默认主键采用的是聚集索引，所以表数据都是根据主键顺序组织存放的
  - 看叶子节点从左到右增大，叶子节点存储的是主键，主键挂的是行数据

[![2023-08-23-230329.png](https://i.postimg.cc/Z5cFT1B5/2023-08-23-230329.png)](https://postimg.cc/k22tsYv0)
[![2023-08-23-230329.png](https://i.postimg.cc/Z5cFT1B5/2023-08-23-230329.png)](https://postimg.cc/k22tsYv0)

- 页分裂
  - 页可以是空，也可以填充一半，也可以填充100%。每个页至少包含了2行数据（如果一行数据，那么就是链表）（如果一行数据过大，会行溢出），根据主键排列。
  - 主键顺序插入:前一个页插满在查下一个页
    
[![2023-08-23-230837.png](https://i.postimg.cc/zBmnp54p/2023-08-23-230837.png)](https://postimg.cc/FfZdHtrJ)
  - 主键乱序插入：因为叶子节点是有序的，所以50插入时，不应该开启新的数据页数（第三个数据页），放在前面的页，存放在47之后，第一个数据页没有写满（大小代表了所占内存的多少），但50没办法插入了，此时会开启一个新的数据页，找到第一个数据页50%位置，将右边的数据全部移动到第三个数据页

[![2023-08-23-231454.png](https://i.postimg.cc/SNrRvqYV/2023-08-23-231454.png)](https://postimg.cc/2V1C1swB)
[![2023-08-23-231500.png](https://i.postimg.cc/k4QqRFxw/2023-08-23-231500.png)](https://postimg.cc/34xPPGfD)
[![2023-08-23-231530.png](https://i.postimg.cc/tJr0Fr7d/2023-08-23-231530.png)](https://postimg.cc/D4bYTPrm)
- 页合并
  - 当删除一行数据时候，实际上记录并没有被物理删除，只是记录被标记（flaged）为删除并且它的空间变得允许被其他记录声明使用
  - 当页中删除的记录达到merge_threshold(默认为页的50%)，innoDB会开始寻找最靠近的页（前或后）看看是否可以将两个页合并以优化空间使用
  - 删除数据16，在innoBDB并不会直接删除，而是将对应空间标识为删除空间，此时可以插入其他数据
[![2023-08-23-232141.png](https://i.postimg.cc/QCc2yX6b/2023-08-23-232141.png)](https://postimg.cc/1V57gZ1n)
[![2023-08-23-232209.png](https://i.postimg.cc/Kvkk4C15/2023-08-23-232209.png)](https://postimg.cc/3dhJcSCy)
[![2023-08-23-232221.png](https://i.postimg.cc/d0BDzYfJ/2023-08-23-232221.png)](https://postimg.cc/nsXHD6ZW)
   - 知识小贴士
     - merge_threshold:合并的阈值，可以自己设置，在创建表或者创建索引时指定
- 主键设置原则
  - 满足业务需求的情况下，尽量降低主键长度（因为二级索引叶子节点下面挂的是主键需要占用内存，搜索时候效率也会降低）
  - 插入数据时，尽量选择顺序插入，选择使用auto_increment自增主键（因为会存在页分类）
  - 尽量不要使用UUID或者其他自然主键，如：身份证（因为没有顺序，容易乱序并且比较长）
  - 业务操作时，尽量避免对主键修改（因为需要动索引结构）
### 进阶--sql优化--order by优化
1. using filesort:通过表的索引或者全表索引，读取满足条件的数据行，然后在排序缓冲去sort buff中完成排序操作，所有不是通过索引直接返回排序结果的排序都叫filesort排序.
2. using index:通过有序索引顺序扫描直接返回有序数据，这种情况即为using index,不需要额外排序，操作效率高。性能高，即优化时候，尽量优化到using index

[![2023-08-24-105814.png](https://i.postimg.cc/rm8HKWM2/2023-08-24-105814.png)](https://postimg.cc/d7x6fhh5)
- order by优化
  - 如果同为升序索引，那么叶子节点存储数据已经是有序的
  - 如果一升一降，那么先对age升序排序，age相同在对phone降序排序，按照age升序，phone降序，那么直接返回结果也是符合要求的
  - **注意**：优化得到using index的前提是已经使用覆盖索引（也就是不需要额外查询，不需要回表查询，select *就不行）
[![2023-08-24-110029.png](https://i.postimg.cc/cJc9yHY9/2023-08-24-110029.png)](https://postimg.cc/Z9CF6Jwp)
- 总结
  - 根据排序字段建立合适的索引，多字段排序时，页遵循最左前缀法则
  - 尽量使用覆盖索引
  - 对字段排序，一个升序，一个降序，此时需要注意联合索引在创建时候的规则（asc/desc）
  - 如果不可避免地出现filesort,大数据排序时候，可以适当增大排序缓冲区的大小sort_buffer_size(默认256K)，如果缓冲区满了，会在磁盘中排序，此时效率降低

          show variables like 'sort_buffer_size' #查找默认大小
### 进阶--sql优化--group by 优化

          #删除删掉目前的联合索引idx_user_pro_age_sta;
          drop index idx_user_pro_age_sta on tb_user;
          #执行分组操作，根据profession字段分组
          explain select profession,count(*) from tb_user group by profession;
          #创建索引
          create index idx_user_pro_age_sta on tb_user(profession,age,status);
          #执行分组，根据profession进行分组
          explain select profession,count(*) from tb_user group by profession;
          #执行分组，根据profession，age进行分组
          explain select profession,count(*) from tb_user group by profession,age;
- 分组操作时，可以通过索引来提高效率
- 分组操作时，索引的使用也是满足最左前缀法则的
### 进阶--sql优化--limit分页查询的优化
- 一个常见又非常头疼的问题就是limit 2000000，10，此时需要mysql排序前2000010激励，仅仅返回2000000~2000010的记录，其他记录弄丢，查询排序的代价非常大。
- 优化思路：一般分页查询时，通过创建覆盖索引能够较好的提高性能，可以通过覆盖索引加子查询的方式优化

            select s.* from tb_sku s,(select id from tb_sku order by id limit 7000000,10) a where s.id=a.id;

### 进阶--sql优化--count优化
          explain select count(*) from tb_sku;
- 在myisam引擎把一个表的总行数存放在磁盘上，因此执行count(*)的时候会直接返回这个数，效率很高
- innoDB就麻烦了，他执行count(*)的时候，需要把数据一行一行地从引擎中读取出来，然后累积计数，所以在大数据情况下，计算非常耗时
- 优化思路：自己计数
- count的几种用法
  - count()是一个聚合函数，对应返回的结果集，一行行地判断，如果count函数的参数不是null，累计值就加1，否则不加，最后返回累计值
  - 用法：count(*),count(主键)，count(字段)，count(1);
- count的几种用法
  - count(主键）
    - innoDB引擎会遍历整张表，把每一行的主键id的值都取出来，返回给服务层。服务层拿到主键后，直接按行进行累加,不用判断是否为null（主键不可能为null）
  - count(字段)
    - 没有not null约束：innoDB引擎会遍历整张表把每一行的字段都取出来，返回给服务层。服务层判断是否为null,不为null，技术累加。
    - 有not null约束：innoDB引擎会遍历整张表吧每一行的字段都取出来，返回给服务层，直接按行进行累加。
  - ccount(1)（count(-1)也可以，方-1进去）
    - innoDB会遍历整张表，但不取值。服务层对于返回的每一行，放一个数字‘1’进去，直接进行累加。
  - count(*)
    - innoDB引擎并不会把全部字段取出来，而是做了专门的优化，不取值，服务层直接按行进行累加。
- 按照效率排序：count(字段）<count(主键id）<count(1)~count(*),所以尽量使用count(*)
### 进阶--sql优化--update优化（避免行锁升级为表锁）
- update优化
  
            update student set no='2000100100' where id=1;
            update student set no='2000100105' where name='韦一笑';
  - innoDB的行锁是针对索引加的锁，不是针对记录加的锁，并且该索引不能失效，否则会从行锁升级为表锁
### 进阶--sql优化--小结
[![2023-08-24-151413.png](https://i.postimg.cc/bvbcv4D4/2023-08-24-151413.png)](https://postimg.cc/gwYBSSKK)
## 进阶--视图/存储过程/触发器
- 介绍
  - 视图（view）是一种虚拟存在的表。视图中的数据并不在数据库中实际存在，行和列数据来自定义视图查询中使用规则图时动态生成的。
  - 通俗的讲，视图只保存了查询sql逻辑，不保存查询结果。所以我们在创建视图的时候，主要的工作就落在创建这条sql查询语句上。
- 创建

        create [or replace] view 视图名称（列明列表） as select语句 [with[cascade|local|check option]]
- 查询

        查看创建视图的语句：show create view 视图名称；
        查看视图数据：select * from 视图名称...;
- 修改

          方式一：create [or replace] view 视图名称（列明列表） as select语句 [with [cascaded|local|check option]]
          方式二：alter view 视图名称（列明列表） as select语句 [with [cascaded|local|check option]]
- 删除

          drop view [if existis] 视图名称[,视图名称]...

### 进阶--视图--检查选项（cascaded）
- 试图检查选项
  - 当使用with check option子句创建视图时，mysql会通过视图检查正在更改的每个行，例如：插入，更新，删除，以使其其符合视图的定义。mysql允许基于另一个视图创建视图，他还会检查依赖试图中的规则以保持一致性。为了确定检查的范围，mysql提供了两个选项：cascaded和local,默认值为cascaded。
   - cascaded:比如，v2视图是基于v1视图的，如果在v2视图创建的时候指定了检查选项为 cascaded，但是v1视图创建时未指定检查选项。 则在执行检查时，不仅会检查v2，还会级联检查v2的关联视图v1。
     - v2在v1的基础上创建的视图，在对v2操作时，不仅要检查是否满足v2的条件还要检查是否满足v1的条件，虽然v1创建时没有加上cascaded选项，这种现象称为**级联**
       
         create view vl ad select id,name from student where id<20;
         create view v2 ad select id,name from v1 where id<20 with cascaded check option;
       
[![2023-08-24-162148.png](https://i.postimg.cc/ZqJJVR6Y/2023-08-24-162148.png)](https://postimg.cc/87n8CTyx)
- 注意：一旦在创建某个视图中加入了cascadede选项，那么当前视图的之前依赖（基于的视图创建的视图）视图都会满足，如果后面的没有加入cascaded,那么不需要满足
### 进阶--视图--检查选项（local）
- 试图检查选项
  - 当使用with check option子句创建视图时，mysql会通过视图检查正在更改的每个行，例如：插入，更新，删除，以使其其符合视图的定义。mysql允许基于另一个视图创建视图，他还会检查依赖试图中的规则以保持一致性。为了确定检查的范围，mysql提供了两个选项：cascaded和local,默认值为cascaded。
  - local：比如，v2视图是基于v1视图的，如果在v2视图创建的时候指定了检查选项为 local ，但是v1视图创 建时未指定检查选项。 则在执行检查时，知会检查v2，不会检查v2的关联视图v1。

          create view v1 as select id,name from student where id<=15 #检查
          create view v2 as select id,name from v1 where id>=10 with local check option; #检查
          create view v3 as select id,name from v2 where id>=10； #不检查
[![2023-08-24-165012.png](https://i.postimg.cc/7YzRLJLB/2023-08-24-165012.png)](https://postimg.cc/mtbjXDCM)
### 进阶--视图--更新及作用
- 视图的更新
  - 要使视图可更新，视图中的行与基础表中的行之间必须存在一对一的关系(视图中的一行数据对应数据表中的一行数据)。如果试图包含一下任何选项，那么该视图不可更新。
    1. 聚合函数或窗口函数（sum(),min(),max(),count()等）
    2. distinct
    3. having
    4. union 或union all
    5. group by
- 视图的作用
  - 简单
    - 视图不亲可以简化拥护对数据的理解，也可以简化他们的操作。那些被经常使用的查询可以被定义为试图，从而使得拥护不必为以后的操作每次指定全部条件。
  - 安全
    - 数据库可以授权，但不能授权到特定的行和特定的列上。通过视图，用户只能查询和修改他们所能见到的数据。这样就可以保证数据安全性
  - 数据独立
    - 视图可以帮助用户屏蔽真实表结构变化带来的影响。比如，对数据列重新命名，真是表的字段名变化不会改变视图中的字段名

            create or replace view stu_v_4 as select id,studentname as name from student where id<=15；

### 进阶--视图--案例
1. 为了保证数据库的安全性，开发人员在操作tb_user表时，只能看到用户的基本字段，屏蔽手机号和邮箱两个个字段
2. 查询每个学生所选的课程（三张表联查），这个功能在很多的业务中都有使用到，为了简化操作，定义一个视图。
### 进阶--存储过程-介绍
- 介绍
  - 存储过程是事先经过编译并存储在数据库中的一段sql语句的集合，调用存储过程可以简化应用开发人员的很多工作，减少数据在数据库中和应用服务器之间的传输，对于提高数据处理的效率是有好处的
  - 存储过程思想上很简单，就是数据库sql语言层面的代码封装与重用。
- 特点
  - 封装，复用
  - 可以接受参数，也可以返回数据
  - 减少网络交互，效率提升
[![2023-08-24-180005.png](https://i.postimg.cc/yxc0J93y/2023-08-24-180005.png)](https://postimg.cc/0K5zFzfz)
### 进阶--存储过程--基本语法
- 创建
  
            create procedure 存储过程名称（[参数列表]）
            begin
                -- sql语句
            end;
- 调用(也就是执行封装的sql语句)

           call 名称（[参数]）
- 查看存储过程
  
          select *from information_schema.routinues where rountine_schema='XXX';--查询指定数据库存储过程及状态信息
          show create procedure 存储过程名称；-- 查询某个存储过程的定义
- 删除存储过程
 
          drop procedure [if exists] 存储过程名称；
- **注意**：在命令行中，执行创建存储过程的sql时，需要通过关键字delimiter指定sql语句的结束符

[![2023-08-24-182112.png](https://i.postimg.cc/6pXfZ9Kf/2023-08-24-182112.png)](https://postimg.cc/xc6mDVcX)

### 进阶--存储过程--变量--系统变量
- 变量分类
  - 系统变量
    - 全局变量
    - 会话变量
  - 用户变量
  - 用户自定义变量
- 系统变量：是mysql服务器提供，不是用户定义的，属于服务器层面。分为全局变量（global）、会话变量（session）。
  - 查看系统变量(session ,global可以不指定，默认是session)
    
          show [session|global] variables;  -- 查看所有的系统变量
          show [session|global] variables like '...'  --通过模糊匹配的方式查找变量
          select @@[session |global] 系统变量名 -- 查看指定变量名
  - 设置系统变量名
    
          set [session|global] 系统变量名=值
          set @@[session|global].系统变量名=值
  - 注意：
    - 如果没有指定session/global,默认是session,会话变量
    - mysql服务器重新启动之后，所设置的全局参数会失效，如果不想失效，可以在/etc/my.cnf中配置
### 进阶--存储过程--变量--用户自定义变量
- 用户自定义变量：是指用户根据需要自己定义的变量，永辉变量不用提前声明，在用的时候直接使用’@变量名‘使用就可以，其作用域为当前连接。@@是系统变量，@s是用户自定义变量
- 赋值
  
          set @var_name=expr[,@var_name=expr]...;
          set @var_name:=expr[,@var_name:=expr]...;
          selectt @var_name:=expr[,@var_name=expr]...;
          select 字段名 into @var_name from 表名  --从表中查询的数据赋值给 @var_name 
- 使用
  
          select @var_name;
- 注意：用户自定义的变量不需要对其进行声明或初始化，只不过获取到的值为null。

### 进阶--存储过程--变量--局部变量
- **局部变量**：是根据需要定义一的在局部生效的变量，访问之前，需要declare声明。可用作存储过程内的局部变量和输入参数，局部变量的范围是在其内声明的begin...end(procedure封装)块,超出该范围局部变量不可用。
- 声明
  
          declare 变量名 变量类型[default...]
          declare stu_count int default 0;-- 后面表示默认值是0
  - 变量类型就是数据库字段类型：int,bigint,char,varchar,date,time等。
- 赋值
  
          set 变量名=值
          set 变量名:=值
          select 字段名 into 变量名 from 表名;

### 进阶--存储过程--if判断
- if
  - 语法

          if 条件1 then
            ...
          elseif 条件2 then --可选
            ...
          else              --可选
            ...
          end if;
- 练习

[![2023-08-24-210234.png](https://i.postimg.cc/rmvJmnrY/2023-08-24-210234.png)](https://postimg.cc/N9kTCxb1)
### 进阶--存储过程--参数（in,out,inout）
- 参数
  
类型  | 含义  | 备注
-----  | ---------  | ------
in  | 该类参数作为输入，也就是需要调用时传入值  | 默认
out  | 该类参数作为输出，也就是该参数可以作为返回值  | 
inout  | 即可以作为输入参数也可以作为输出参数  | 

- 语法
- 
          create prodecure 存储过程名称（[in/out/inout 参数名 参数类型]）
          begin
             --sql语句
          end;
- 练习
  
[![2023-08-24-211303.png](https://i.postimg.cc/nrj5zShX/2023-08-24-211303.png)](https://postimg.cc/Mfwt3DRw)
2. 将传入的200分制的分数进行换算，换算成百分制，然后返回
### 进阶--存储过程--case
- case
  - 语法一
  
          case case_value
                when when_value1 then statement_list1
                [when when_value2 then statement_list2]...
                [else statement_list]
          end case;
  - 语法二
 
          case
              when condition1 then statemen_list1;
              [when condition2 then statemen_list2;]...
              [else statemen_list;]
          end case;
- 案例
[![2023-08-24-213957.png](https://i.postimg.cc/G3qWtL15/2023-08-24-213957.png)](https://postimg.cc/G9T7S1tF)
### 进阶--存储过程--循环--while
- while循环是有条件的循环控制语句，满足条件后，再执行循环体中的sql语句。
- 语法
#先判断条件，如果条件为true,你们执行逻辑，否则，不执行逻辑

          while 条件 do
              sql逻辑...
          end while;
- 练习
  - 计算从1累加到n的值，n为传入参数值
### 进阶--存储过程--循环--repeat
- repeate
  - repeate是有条件的循环控制语句，但满足条件的时候退出循环，具体语法为：

#先执行一次逻辑，然后判断逻辑是否满足，如果满足，那么退出，如果不满足，那么继续下一个循环

          repeat
                 sql逻辑...
                 until 条件
          end repeat;
### 进阶--存储过程--循环--loop
- loop
  - loop实现简单的循环，如果不在sql逻辑中增加退出循环的条件，可以用其来实现简单的死循环。loop可以配合以下两个语句使用：
    - leave:配合循环使用，退出循环
    - iterate:必须用在循环，作用是跳过当前循环剩下的语句，直接进入下一次循环。
      
          [lable:] loop 
              SQL逻辑...
          end loop[label];
          
          leave label:--退出指定标记的循环体
          iterate label:--直接进行下一次循环
- 练习
1. 计算从1到n的累加值，n为传入的参数值
2. 计算从1到n之间的偶数累加的值，n为传入的参数值。
### 进阶--存储过程--游标--cursor
- 游标
  - **游标**:是用来存储查询结果集的数据类型，在存储过程和函数中可以使用游标对结果集进行循环的处理。游标的使用包括游标的声明、open、fetch和close，其使用方法如下。
  - 声明游标
  - 
          declare 游标名称 cursor for 查询语句；
    
  - 打开游标

          open 游标名称
  - 获取游标记录

          fetech 游标名称 into 变量[,变量]
  - 关闭游标

          close 游标名称；
- 案例：根据传入的参数uage来查询用于年龄小于等于uage的用户姓名（name）和专业（professuim）,并将用户的姓名和专业插入到所创建的一张信标（id,name,profession）中
- **注意**：注意：普通变量声明在游标声明之前
### 进阶--存储过程--条件处理器--handler
- 条件处理程序
  - 条件处理程序：可以用来定于在流程控制结构执行过程中遇到问题时相应的处理步骤。
  - 语法
          declare handle_action handler for condition_value [,condition_value]...statement;
    
          hander_action
              continue:继续执行当前程序
              exit:停止执行当前程序
          condition_value
              sqlstate sqlstate_value:异常的状态码，如02000
              sqlwarning:所有以01开异常状态码头的sqlstate代码的简写
              not found:所有以02开头的异常状态码sqlstate代码的简写
              sqlexception:所有没有被sqlwarning或not found铺货的sqlstate代码的简写
### 进阶--存储函数
- 存储函数
  - 存储函数是有返回值的存储过程，存储函数的参数只能是in（输入)类型的。也就是存储函数必须有返回值，并且参数只能是输入类型
  - 语法
  
          create function 存储函数名称（[参数列表]）
          returns type[characteristic...]  ——type:返回参数的类型
          begin
               -- sql语句
              return....
           
          end;
          
          characterstic说明
          - determinstic:相同输入参数总是产生相同的结果，也就是传入的参数一样返回值也是一样的
          - no sql:不包含sql语句
          - reads sql data:包含读取数据的sql语句，但不包含写入数据的语句
- 案例
  - 从1到n的累加
- 存储函数用的少，因为存储函数的地方一定可以使用存储过程，并且存储函数必须有返回值，所以存储过程的用的更多。
### 进阶--触发器--介绍
- 触发器是与表有关的数据库对象，指在insert/update/delete之前或之后，触发并执行触发器中定义的SQL语句集合。触发器的这种特性可以协助应用在数据库端确保数据的完整性，日志记录，数据校验等操作。
- 使用别名old和new来引用触发器中发生变化的记录内容，这与其它的数据库是相似的。现在触发器还只支持行级触发，不支持语句级触发。
- 行级触发器：如果一个update语句影响了五行数据，并且触发了五次，这种称为行级触发器
- 语句级触发器：执行一条update，不管update影响了多少行，只能触发一次

触发器类型  | new和old
-----  | ------
insert触发器  | new表示将要或者已经新增的数据。old没有用
update触发器  | old表示修改之前的数据，new表示将要或者修改后的数据
delete触发器  | old表示将要或者已经删除的数据，new没有用，因为数据已经删除
### 进阶--触发器--案例1（insert类型）
- 语法
  - 创建（对哪张表的数据在增删改之前还是之后触发）
    
          create trigger trigger_name
          before/after insert/update/delete --在增删改之前还是之后
          on tbl_name for each row   --行级触发器
          begin
                trigger_stmt; --具体的逻辑实现
          end;
  - 查看
  
          show triggers;
  - 删除
  
          drop trigger [schema_name（数据库的名字）]trigger_name; --如果没有指定schema_name，默认为当前数据库。
- 练习
  - 通过触发器记录tb_user表的数据变更体制，将变更日志插入到日志表user_log中，包括增加，删除，更新


### 进阶--触发器--案例2（update类型）
- 修改数据的触发器
### 进阶--触发器--案例3（delete类型）
- 删除数据的触发器
### 进阶--视图/存储过程/触发器--小结
[![2023-08-25-204609.png](https://i.postimg.cc/nLkSNPM9/2023-08-25-204609.png)](https://postimg.cc/PLCMwKWd)
## 进阶--锁

### 进阶--锁--介绍
- 介绍
  - 锁是计算机协调多个进程或线程并访问某一资源的机制。在数据库中描绘，除传统的计算资源（cpu,RAM,I/O）的征用以外，数据也是一种供许多用户共享的资源。如何保证数据并发访问的一致性、有效性是所有数据库必须解决的一个问题，锁冲突也是影响数据库并发访问性能的一个重要因素。从这个角度来说，锁对数据库而言尤其重要，也更加复杂。
- 分类：mysql中的锁，按照锁的颗粒度分，分为以下三类
  1. 全局锁：锁定数据库中的所有表，范围最大
  2. 表级锁：每次操作锁住整张表
  3. 行级锁：每次操作锁住对应的行数据，范围最小
    
### 进阶--锁--全局锁--介绍
- 介绍
  - 全局锁就是对整个数据库实例加锁，加锁后整个实例就处于只读状态，后续的DML的写语句，DDL语句，已经更新操作的事务提交语句都将被阻塞。
  - 典型的使用场景是做全库的逻辑备份，对所有的表进行锁定，从而获取一致性视图，保证数据的完整性。（为什么备份数据时候，需要对表进行锁定？）
  - 备份完tb_stock数据之后，又有业务进行，那么后面的两张表改变，第一个备份的数据没有改变，违背数据一致性

 
[![2023-08-25-212213.png](https://i.postimg.cc/tJDN52td/2023-08-25-212213.png)](https://postimg.cc/K3kTc7W4)

  - mysqldump是数据备份的东西


[![2023-08-25-212327.png](https://i.postimg.cc/yxf0SqmF/2023-08-25-212327.png)](https://postimg.cc/9w7DvnNM)

- 语法

           flush tables wuth read lock;--创建全局锁
           mysqldump -uroot（用户名） -p1234（密码1314521zcx） itcast>itcast.sql --备份数据库itcast中的数据存放到itcast.sql文件中
           unlock tables;--解锁，此时解除锁定锁


[![2023-08-25-212745.png](https://i.postimg.cc/zvMVrqwP/2023-08-25-212745.png)](https://postimg.cc/Mf7W02Fy)

### 进阶--锁--全局锁--一致数据备份
- 一旦加入全局锁之后，只能查询数据，不能更新
[![2023-08-25-215423.png](https://i.postimg.cc/qRZ3kP2S/2023-08-25-215423.png)](https://postimg.cc/34mR1bSF)
- 下面备份数据库
[![2023-08-25-215642.png](https://i.postimg.cc/tJWhCXpJ/2023-08-25-215642.png)](https://postimg.cc/K3cK0hKh)
- 解除锁
[![2023-08-25-220217.png](https://i.postimg.cc/BnWVg6XY/2023-08-25-220217.png)](https://postimg.cc/QHbmNjg1)
- 特点
  - 数据库中加全局锁，是一个比较重的操作，存在以下的问题
  1. 如果在主库上备份，那么备份期间都不能执行更新，业务基本上就要停摆
  2. 如果从主库上备份（这样就可以在原来库中进行增删改），那么在备份期间从不能执行主库同步过来的二进制日志（binlog）,会导致从延迟。
- 在innoDB引擎中，我们可以在备份时加上参数--single-transaction参数来完成不加锁的一致性数据备份

          mysqldump --single-transaction -uroot -p123456 itcast>itcast.sql

[![2023-08-25-220858.png](https://i.postimg.cc/XYm1Jv0c/2023-08-25-220858.png)](https://postimg.cc/Js35YM0G)
- h后面的是192.168.174.129
### 进阶--锁--表级锁--表锁
- 介绍
  - 表级锁，每次操作锁住整张表。锁定力度越大，发生锁冲突的概率越高，并发度越底。应用myisam,innoDB,BOB等存储引擎中。
  - 对于表级锁，分为以下三种
    1. 表锁
    2. 元数据锁（meta data lock,MDL）
    3. 意向锁
- 表锁
  - 对于表锁，分为两类
    1. 表共享锁（read lock）:只能读取不能写入，读锁不会阻塞其他客户端的读，但是会阻塞其他客户端的写
    2. 表独占锁(write lock)

  - 语法
    1. 加锁：lock tables 表名 ...read（读锁）/write（写锁）
    2. 释放锁：unlock tables /客户端断开连接
  - 案例：创建两个，使用的是db01数据库。此时左边的建立了读锁，两个都可以读取数据，左边的不可以更新数据，右边的更新数据时会处于阻塞状态 ，直至左边的可无端释放表锁才可以运行
[![2023-08-26-093424.png](https://i.postimg.cc/yN5VnQNK/2023-08-26-093424.png)](https://postimg.cc/sBYdgJSH)
- 下面图片的说明：左边的是当前建立读锁的可无端，右边的是其他客户端，绿色表示可以，红色表示不可以
[![2023-08-26-093146.png](https://i.postimg.cc/Kz68cqXf/2023-08-26-093146.png)](https://postimg.cc/gXKWNK2L)

  - 案例：创建两个，使用的是db01数据库。此时左边的建立了写锁，左边可无端可以读写数据，其他的客户端不可以读取也不可以写数据，并且处于组赛状态知道左边客户端解锁为止。
[![2023-08-26-094121.png](https://i.postimg.cc/MG0Dm45M/2023-08-26-094121.png)](https://postimg.cc/WD3g25QT)
- 下面图片的说明
[![2023-08-26-093905.png](https://i.postimg.cc/3JWtQt8V/2023-08-26-093905.png)](https://postimg.cc/XpSfwcyk)
- **注意**：读锁不会阻塞其他客户端的读取，但是会阻塞写。写锁及回族赛其他客户端的读取，也会阻塞其他客户端的写。
### 进阶--锁--表级锁--元数据锁
- 元素据锁（meta data lock,MDL）
  - MDL枷锁过程是系统自动控制，无序显式使用，在访问一张表的时候会自动加上。MDL锁主要作用是维护表元素据的数据一致性，在表上有活动事务的时候，不可以对元数据进行写入操作。简单来说如果一张表存在未提交的事务，我们不能修改表的数据，为了避免DML与DDL冲突，保证读写正确性。
  - 在MYSQL5.5中引入了MDL,当对一张表进行增删改查的时候，会自动的加MDL读锁（共享）；当对表结构进行变更操作的时候，会自动的加MDL写锁（排他），读锁（共享）之间是自动兼容的，也就是可以同时执行，对写锁以及写锁与读锁之间不是自动兼容的。
  - 更对MDL相关介绍参照：https://blog.csdn.net/weixin_48943299/article/details/123927176

对应SQL  | 锁类型 | 说明
----  | ---------  |--------
lock tables XXX read/write  | shared_read_only/shared_no_read_write  | 
select、select...lock in share mode  | shared_read  | 与shared_read、shared_write兼容，与excusive互斥
insert、update、delete、select...for update  | shared_write（读锁（共享））  | 与shared_read、shared_write兼容，与excusive互斥
alter table...  | excusive  | 与其他的MDL都互斥
- 案例
  - select，update是自动用的 shared_write（读锁（共享））也就是之间相互兼容，可以同时执行
[![2023-08-26-103138.png](https://i.postimg.cc/KjzM6s2Y/2023-08-26-103138.png)](https://postimg.cc/7GFh79bv)
  - slect与alter之间不能同时执行，因为shared_write，exclusive之间不兼容此时右侧处理阻塞装袋，直至左侧的解锁才会执行
[![2023-08-26-103207.png](https://i.postimg.cc/59RYHgJw/2023-08-26-103207.png)](https://postimg.cc/t7FCwhYT)
- 查看元数据锁(查询系统中的metadata_locks，这里面存储了元数据所
  
          select object_type,objet_schema,object_name,lock_type,lock_duration from performance_schema.metadata_locks;

[![2023-08-26-103708.png](https://i.postimg.cc/VkbVyKf4/2023-08-26-103708.png)](https://postimg.cc/75wV0MTT)
- 下面是左边执行了select语句右边执行了alter语句，这时候有新加了一个锁，并且是不兼容的，此时处于阻塞状态
[![2023-08-26-103807.png](https://i.postimg.cc/V6Hqkc4t/2023-08-26-103807.png)](https://postimg.cc/1nwnv2kR)


### 进阶--锁--表级锁--意向锁
- 左边是加了行锁，右边加了表锁此时之间会冲突，此时右边的会判定是否加了行锁，从第一条数据出发一直到最后一行数据，此时效率极低，为了提高效率，避免DML执行时，家的行锁与表锁的冲突，在innoDB中引入了意向锁，使得表锁不用检查每行数据是否加锁，使用意向锁来减少表锁的检查。
- 意向锁主要解决innoDB引擎中的行锁与表锁之间冲突的问题
  - 一开始没有使用意向锁的时候
  
[![2023-08-26-104648.png](https://i.postimg.cc/SxvDD5wD/2023-08-26-104648.png)](https://postimg.cc/Mn17GsZQ)
  - 使用了意向锁之后：左边的会先添加行锁之后再添加意向锁，右边的再添加了表锁之后，会检查当前表的意向锁，如果意向锁与表锁之间是兼容的，那么会运行，如果不兼容，右侧会处于阻塞状态，直到左边的意向锁释放。此时不用每行检查。
[![2023-08-26-105012.png](https://i.postimg.cc/3JPk1Ft2/2023-08-26-105012.png)](https://postimg.cc/mtyZ2Cfr)
- 分类
  1. 意向共享锁（IS）:由语句select...lock in share mode添加,也就是需要我们手动添加
  2. 意向排他锁（IX）:由insert,update,delete,select...for update添加
- 兼容情况
  1.  意向共享锁（IS）:与表锁共享锁（read）兼容，与表锁排他锁（write）互斥。
  2. 意向排他锁（IX）与表锁共享锁（read）以及排他锁（write）都互斥。意向锁之间不会互斥。
- 语法：查看意向锁以及行锁的加锁情况
  
          select objet_schema,object_name,index_name,lock_type,lock_mode,lock_data from performance_schema.data_locks;

### 进阶--锁--表级锁--意向锁--测试
- 意向共享锁IS与read的表锁之间是兼容的，所以能创建read的表锁，意向共享锁IS与write的表锁之间是互斥的的，所以能会阻塞，直到左边提交事务。
[![2023-08-26-110718.png](https://i.postimg.cc/qvc4VsGf/2023-08-26-110718.png)](https://postimg.cc/bZvK12ML)
- 意向排他锁IX与read之间互斥，所以会处于阻塞状态
[![2023-08-26-110718.png](https://i.postimg.cc/qvc4VsGf/2023-08-26-110718.png)](https://postimg.cc/bZvK12ML)

### 进阶--锁--行级锁--介绍
- 行级锁：每次操作锁住对应的行数据。锁定粒度最小，发生锁冲突的改率最低，并发度最高。在innoDB存储引擎中。innoDB支持行级锁，但是MYISAM是不支持行级锁的
- innoDB的数据是基于索引组织的，行锁是通过对索引上的索引项加锁来实现的（索引结构是B+tree，分为聚集索引以及二级索引，聚集索引下面挂的是行数据，二级索引下面是id值，行数据是基于聚集索引的，并且B+Tree下面的叶子节点是顺序存储的），而不是对记录加的锁。对于行级锁，主要分为以下三类：
- 分类
  1. 行锁（record lock）:锁定单个行记录，防止其他食物对此进行update和delete，在RC，RR隔离级别下都支持。
  2. 间隙锁（gap lock）:锁定索引记录间隙（不含该记录），确保索引记录间隙不变，防止其他事务在这个间隙进行insert,产生幻读。在RR隔离级别下都支持。比如6到12之间的间隙，不包含6和12，16到18之间的间隙
[![2023-08-26-112119.png](https://i.postimg.cc/DyNk9CGY/2023-08-26-112119.png)](https://postimg.cc/jLyFN4Zz)
  3. 临建锁（next-key lock）:行锁和间隙锁的组合，同时锁住数据，并锁住数据前面的间隔gap。在RR隔离级别下支持。
[![2023-08-26-112301.png](https://i.postimg.cc/DzgCTZDy/2023-08-26-112301.png)](https://postimg.cc/2q1ddzrP)
### 进阶--锁--行级锁--行锁
- 行锁
  - innnoDB实现了以下两种类型的行锁
    1. 共享锁（S）：允许一个事务去读一行，组织其他事务获得相同数据集的排他锁，也就是共享锁与共享锁之间兼容，与排他锁之间互斥。
    2. 排他锁（X）：允许获取排他锁的事务更新数据，阻止其他事务获得相同数据集的共享锁和排他锁，也就是第一个事务获取了某一数据的排他锁，其他事务就不能获得共享锁和排他锁
   - **解释**
     - 事务a获取了共享锁，那么事务b也可以获取共享锁，
     - 事务a获取了共享锁，那么事务b不可以获取排他锁

当前锁类型\请求锁类型  | S(共享锁)  | X(排他锁）
-----  | ----  |------
S(共享锁)  | 兼容  | 冲突
X(排他锁)  | 冲突  | 冲突

- 行锁

sql  | 行锁类型  | 说明
------  | ------  | ------
insert  | 排他锁 | 自动加锁
update  | 排他锁 | 自动加锁
delete  | 排他锁 | 自动加锁
select(正常)  | 不加任何锁  | 
select ...lock in share mode  | 共享锁 | 需要手动在select之后加lock in share mode
select ... for update  | 排他锁 | 需要手动在select之后加for update
- 演示
  - 在默认情况下，innoDB在repeatable read事务隔离级别运行，innoDB使用next-key锁进行搜索和索引扫描，以防幻读。
  1. 针对唯一索引进行检索时，对已经存在的记录进行等值匹配，将会自动化优化为行锁
  2. innoDB行锁是针对索引加的锁，不通过索引条件检索数据，那么innoDB将对表中的所有记录加锁，此时就会升级为表锁
- 语法：通过以下sql语句，查看意向锁以及行锁的加锁情况
          elect objet_schema,object_name,index_name,lock_type,lock_mode,lock_data from performance_schema.data_locks;
  
[![2023-08-26-122423.png](https://i.postimg.cc/gJFbZ0dW/2023-08-26-122423.png)](https://postimg.cc/cKmzq0r9)
- 共享锁与共享锁之间兼容

[![2023-08-26-122829.png](https://i.postimg.cc/htTrG4Cx/2023-08-26-122829.png)](https://postimg.cc/zyDWtNYX)
- id为1的数据加了共享锁，共享锁与排他锁之间互斥，所以阻塞状态
  
[![2023-08-26-123017.png](https://i.postimg.cc/d1xdBgHw/2023-08-26-123017.png)](https://postimg.cc/njqCVSfP)
- 左侧排他锁，右侧也是，所以回阻塞，直到左边的解锁
  
[![2023-08-26-123117.png](https://i.postimg.cc/c4qTG8hZ/2023-08-26-123117.png)](https://postimg.cc/23wn4ygX)
- 2. innoDB行锁是针对索引加的锁，不通过索引条件检索数据，那么innoDB将对表中的所有记录加锁，此时就会升级为表锁
- 左边加上了行锁（update）,因为name没有索引，那么innoDB将对表中的所有记录加锁，此时就会升级为表锁，表锁与行锁互斥，所以右边阻塞

[![2023-08-26-123450.png](https://i.postimg.cc/8CqffLjz/2023-08-26-123450.png)](https://postimg.cc/TyJ3ZLVz)
- 左侧是行锁，name有索引，右边的不会升级为表锁此时可以执行成功。
  
[![2023-08-26-123538.png](https://i.postimg.cc/vm9HjkZG/2023-08-26-123538.png)](https://postimg.cc/hJDBQCmY)
### 进阶--锁--行级锁--间隙锁&临建锁1
- 演示
  - 默认情况下，innoDB在repeatable read事务隔离级别运行，innoDB使用next-key（临建锁）锁进行搜索和索引扫描，以防幻读。
  1. 索引上的等值查询（唯一索引），给不存在的记录加锁时，此时将优化为间隙锁
  2. 索引上的等值查询（普通索引），向右遍历时最后一个值不满足查询需求时，next-key lock退化为间隙锁。
  3. 索引上的查询范围（唯一索引）--访问到不满足条件的第一个值为止。

[![2023-08-26-154236.png](https://i.postimg.cc/bJBRh5zJ/2023-08-26-154236.png)](https://postimg.cc/KktT7J3S)
- **注意：**
  - **间隙锁唯一目的**是防止其他事务插入间隙。间隙锁可以共存，一个事务采用的间隙不会阻止另一个事务在同一间隙上采用间隙锁。
  - 间隙锁包含的是两个数据之间的间隙，不包含这两个数据，临建锁包含了这两个数据，还包含了这两个数据之间的间隙。
- 演示
  -  1. 索引上的等值查询（唯一索引），给不存在的记录加锁时，此时将优化为间隙锁
  - record是行级锁，x是排他锁，gap是间隙锁，是3到8之间的间隙（不包括3和8），此时之间的数据没法插入，处于阻塞状态
    
[![2023-08-26-154105.png](https://i.postimg.cc/28JgwHhC/2023-08-26-154105.png)](https://postimg.cc/nC4dVG3W)
### 进阶--锁--行级锁--间隙锁&临建锁2
- 2. 索引上的等值查询（普通索引），向右遍历时最后一个值不满足查询需求时，next-key lock退化为间隙锁。此时未必是唯一索引
   - 插入18  此时加入的是16和18之间的间隙，以及18与24之间的索引，也就是在18之前以及之后都几上间隙索引。

     
[![2023-08-26-154926.png](https://i.postimg.cc/CL1s1SZK/2023-08-26-154926.png)](https://postimg.cc/BtrK7WBW)
  - 此时加入了行锁，锁住了第19行数据的信息，加入了临建锁在25之间的间隙，以及25之后的到无穷大的间隙。
### 进阶--锁--小结
1. 概述
   - 在并发访问时，解决数据访问的一致性、有效性问题
   - 全局锁、表级锁、行级锁
   - 所得力度越小，性能越高
3. 全局锁
   - 对整个数据库实例加锁，枷锁后整个实例就处于只读状态
   - 性能较差，数据逻辑备份时时候
5. 表级锁
   - 操作锁住整张表，颗粒粒度大，发生所冲突的概率高
   - 表锁、元数据锁、意向锁
7. 行级锁
   - 操作锁住对应的行数据，颗粒粒度最霄，发生所冲突的概率最低
   - 行锁、间隙锁、临建锁
## 进阶--innoDB引擎

### 进阶--innoBD引擎--逻辑存储结构
- innoDB存储结构

[![2023-08-26-160100.png](https://i.postimg.cc/pTMYsjXG/2023-08-26-160100.png)](https://postimg.cc/qtQ3RzKy)

[![2023-08-26-160606.png](https://i.postimg.cc/q73Wt25j/2023-08-26-160606.png)](https://postimg.cc/sB3TqGyh)

### 进阶--innoBD引擎--架构--内存结构1
- 在mysql5.5版本开始，默认使用innoDB存储引擎，他擅长事务处理，具有崩溃恢复特性，在日常开发中使用广泛。下面是innDB架构图，左侧为内存结构，右侧为磁盘结构（架构复杂）

[![2023-08-26-160850.png](https://i.postimg.cc/k4ZVj3cn/2023-08-26-160850.png)](https://postimg.cc/Q9QxtzwP)
- 架构--内存架构
   - 如果没有缓冲区，那么在增删改时候，每次都会操作磁盘文件，这样会有大量的IO
   - 因为数据没有上传到磁盘中，所以会不一致
  

### 进阶--innoBD引擎--架构--内存结构2
- 非唯一二级索引页：也就是对唯一索引或主键索引不会有更改缓冲区
- 不用每次操作磁盘IO,每次操作时，先操作change buffer,然后在以一定的频率把change buffer中的数据同步到buffer pool 然后在刷新到磁盘中，这样就减少了磁盘的ISO,提高了效率

[![2023-08-26-161227.png](https://i.postimg.cc/q7WCk6ts/2023-08-26-161227.png)](https://postimg.cc/06dNnQ0j)

- hash索引
  
            show variables like 'hasg_index';-- 查看hash是否开启

[![2023-08-26-164837.png](https://i.postimg.cc/httDzDP3/2023-08-26-164837.png)](https://postimg.cc/tY8Q8H6h)
- log缓冲区

            show variables like '%flush_log';--查看日志刷新到磁盘时机

[![2023-08-26-165317.png](https://i.postimg.cc/cJTf74Qg/2023-08-26-165317.png)](https://postimg.cc/jWwWtT3t)
### 进阶--innoBD引擎--架构--磁盘结构
- 架构--磁盘结构

           show variables like 'data_file_path';-- 查看系统表空间文件
           show variables like 'data_per_path';-- .ibd文件每个文件都是表空间文件

[![2023-08-26-170136.png](https://i.postimg.cc/rs5HwrrR/2023-08-26-170136.png)](https://postimg.cc/sGDmn1K3)
- 通用表空间

            create tablespace ts_itheima add datafile 'myitheima.ibd' engine =innodb;--创建通用表空间
            use itheima;
            create table a(id int primary key auto_increment,name varchar(10) engine=innodb tablespace ts_itheima;--指定关联的表空间
- 撤销表空间

[![2023-08-26-170840.png](https://i.postimg.cc/RFJSGXkr/2023-08-26-170840.png)](https://postimg.cc/47ZRxb4w)

[![2023-08-26-171055.png](https://i.postimg.cc/0NJFBFyC/2023-08-26-171055.png)](https://postimg.cc/CZScZvDZ)
### 进阶--innoBD引擎--架构--后台线程
- 后台线程作用：将innoDB存储引擎后台缓冲区的数据加载到磁盘中

          show engine innodb status;--查看innoDB引擎状态信息，包括事务情况，IO情况

[![2023-08-26-171713.png](https://i.postimg.cc/tRfrLD8S/2023-08-26-171713.png)](https://postimg.cc/nM4YmKFB)

[![2023-08-26-171818.png](https://i.postimg.cc/x1V6d8fL/2023-08-26-171818.png)](https://postimg.cc/kBwQ1nt5)
### 进阶--innoBD引擎--事务原理--概述

[![2023-08-26-172734.png](https://i.postimg.cc/vB70fd0c/2023-08-26-172734.png)](https://postimg.cc/xJCGVBD2)

[![2023-08-26-172842.png](https://i.postimg.cc/yNyRTYz4/2023-08-26-172842.png)](https://postimg.cc/7CbbH46m)
### 进阶--innoBD引擎--事务原理--redolog
- redo log：解决事务的持久性
  - 当处理数据的时候，现在缓冲区中，看是否有数据，如果没有数据，会通过后台线程将数据从磁盘当中读取出来，缓冲到缓冲区中，之后直接在缓冲区中的数据进行增删改操作，但是磁盘中的数据不会更改，此时称为脏页，会在一定时机，通过后台线程将脏页刷新到磁盘当中，如果脏页的数据刷入到磁盘中出错，此时，内存中的数据没有刷新到磁盘中，此时持久性就会失效。为解决上面问题，innoDB存储引擎会将数据变化存储到redolog buffer当中,在redolpg buffer中会记录数据页的物理变化，当事务在提交时，会将redolog中的数据直接刷新到磁盘结构中，进而持久化保存到磁盘中，后面脏页数据刷新出错时，redolog会进行数据恢复。为什么不直接将buffer pool中数据刷新到磁盘中，这样会存在严重的性能问题（因为每次操作的时候是随机的，不是顺序的，这样会有严重的IO问题），当用redo log文件时，是顺序存储的，性能更高，这种机制为WAL。
  - 当脏页数据刷新到磁盘中，此时redo log记录的数据变更不再需要，所以每段时间都会清理redo logg文件，所以是循环的

[![2023-08-26-174947.png](https://i.postimg.cc/xTYLc4JF/2023-08-26-174947.png)](https://postimg.cc/5j7Xrpmw)
### 进阶--innoBD引擎--事务原理--undolog
[![2023-08-26-181313.png](https://i.postimg.cc/KYfJc354/2023-08-26-181313.png)](https://postimg.cc/SXXWDs3p)
### 进阶--innoBD引擎--MVCC--基本概念
- 当前读
  - 读取的是记录的最新版本，读取时还要保证其他并发事务不能修改当前记录，会对读取的记录进行加锁。对于我们日常的操作，如：select...lock in share mode(共享锁)，select...for update,update,insert,delete（排他锁）都是一种当前读
- 快照读
  - 简单的select(不加锁)就是快照读，读的是记录数据的可见版本，有可能是历史数据，不加锁，是非阻塞读。
    - read committed:每次select都生成一个快照读
    - repeatable read:开启事务之后第一个select语句才是快照读的地方
    - serializable:快照读会退化为当前读
- MVCC
  - 全程multi-version concurrency control ,多版本并发控制。只维护一个数据的多个版本，使得读写操作没有冲突，快照读为mysql实现MVCC提供了一个非阻塞读的功能。MVCC的具体实现还需要依赖于数据库记录中的三个隐式字段、undo log日志、readview;
### 进阶--innoBD引擎--MVCC--隐藏字段
- 记录中的隐藏字段：有两个或者三个，取决于当前表有没有主键
  - 后面三个是隐式字段

[![2023-08-26-205508.png](https://i.postimg.cc/mr2LZSp0/2023-08-26-205508.png)](https://postimg.cc/HrRDBbg2)
- 语法

          ibd2sdi stu.idb -- 查询数据表stu的idb文件，下面是表的隐藏字段
  
[![2023-08-26-205848.png](https://i.postimg.cc/65nnC96B/2023-08-26-205848.png)](https://postimg.cc/bsYZhf25)
[![2023-08-26-205906.png](https://i.postimg.cc/rytrL8r5/2023-08-26-205906.png)](https://postimg.cc/3WYRXQ9w)
### 进阶--innoBD引擎--MVCC--undolog
- undo log
  - 回滚日志，在insert、update\delete的时候产生的便于数据回滚的日志
  - 当insert的时候，产生的undo log日志只在回滚时需要，在事务提交之后可被立即删除
  - 而update、delete的时候，产生的undo log日志不仅在回滚时候需要，在快照读时也需要，不会被立即删除。
- undo log版本链
- 
[![2023-08-26-211118.png](https://i.postimg.cc/hthkj31W/2023-08-26-211118.png)](https://postimg.cc/Mn2P35Ld)

[![2023-08-26-211231.png](https://i.postimg.cc/rFZHvNXh/2023-08-26-211231.png)](https://postimg.cc/8jWwvWCW)

[![2023-08-26-211327.png](https://i.postimg.cc/htJYgQKK/2023-08-26-211327.png)](https://postimg.cc/75k9n6CR)

[![2023-08-26-211352.png](https://i.postimg.cc/Wzb9yh9L/2023-08-26-211352.png)](https://postimg.cc/MMNbMK2d)

- 不同事务或相同事务对同一条记录进行修改，会导致该记录的undolog生成一条记录版本链表，链表的头部是最新的旧纪录，链表尾部是最早的旧记录。
### 进阶--innoBD引擎--MVCC--readview
- readview
  - readview（读视图）：是快照读sql执行时MVCC提取数据的依据，记录并维护系统当前活跃事务（未提交的）i，也就是readview决定了到底读取哪一条事务记录
  - readview中包含了四个核心字段,其提取就是依据这四个核心字段

字段 | 含义
-----  | ------
m_ids  | 当前活跃的事务ID集合
min_trx_id  | 最小活跃事务ID
max_trx_id  | 预分配事务ID,当前最大事务ID+1(因为事务ID是自增的),也就是下一个事务ID
creator_trx_id  | readview创建者的事务ID

[![2023-08-26-214713.png](https://i.postimg.cc/rsxXNhwZ/2023-08-26-214713.png)](https://postimg.cc/CnhQFsDb)
### 进阶--innoBD引擎--MVCC--原理分析（RC级别）
- 第一条：最上面一条记录是trx_id是4， 不满足右边的四条规则，进行下一条数据的读取，下一条是3，3也不满足右边的四条规则，继续下一条记录，是2，2满足右边的第二个条件，此时快照读就是左边的第三条记录，将当前版本记录30 3 A30 2 0x00003直接返回,也就是事务2的记录。
- 第二条:左边的第2条记录满足右边的第2个条件，直接返回该版本的记录即可

[![2023-08-26-220226.png](https://i.postimg.cc/4d5X9fB2/2023-08-26-220226.png)](https://postimg.cc/wy1KKpKD)
### 进阶--innoBD引擎--MVCC--原理分析（RR级别）
[![2023-08-26-220418.png](https://i.postimg.cc/bYgQz1Hk/2023-08-26-220418.png)](https://postimg.cc/Bt88pLzn)

[![2023-08-26-220543.png](https://i.postimg.cc/VkQspVrR/2023-08-26-220543.png)](https://postimg.cc/KRfygQ5k)
### 进阶--innoBD引擎--小结
[![2023-08-26-221020.png](https://i.postimg.cc/vZgqg03p/2023-08-26-221020.png)](https://postimg.cc/sMz9b4Fc)
## 进阶--mysql管理
- 系统数据库
- 常用工具

### 进阶--mysql管理--系统数据库介绍
- 系统数据库
  - mysql数据库安装完成后，自带了四个数据库，具体操作如下：

数据库 | 含义
---  | -------
mysql  | 存储mysql服务器正常运行所需要的各种信息（时区、主从、用户、权限），user表中存储了有哪些数据库可以访问，以及相关权限
information_schema  | 提供了访问数据库元数据的各种表和视图，包含数据库、库、字段类型以及访问权限等，engine:innoDB支持的各种引擎
performance_schema  | 为mysql服务器运行时状态提供了一个底层监控功能，主要用于收集数据库服务器性能参数。
sys  | 包含了一系列方便DBA和开发人员利用performance_schema性能数据库进行性能调优和诊断的视图
### 进阶--mysql管理--常用工具1
- mysql
[![2023-08-26-223724.png](https://i.postimg.cc/FKgj76JF/2023-08-26-223724.png)](https://postimg.cc/f3y3PBK1)

          mysql -h192.168.174.129 -uroot -p1314521zcx itcast -e "select * from stu"--此时没有进入sql里面
- mysqladmin

[![2023-08-26-224357.png](https://i.postimg.cc/rsFHsWns/2023-08-26-224357.png)](https://postimg.cc/Pp9yFLkn)

          mysqladmin -uroot -p1314521zcx version --查看当前数据库版本
          mysqladmin -uroot -p1314521zcx variables --查看当前系统变量以及对应的值
          mysqladmin -uroot -p1314521zcx create db02；--创建数据库，此时并没有登录进去
          mysqladmin -uroot -p1314521zcx -e "show database";
          mysqladmin -uroot -p1314521zcx drop db02;
- mysqlbinglog

[![2023-08-26-224501.png](https://i.postimg.cc/tTRkNbhm/2023-08-26-224501.png)](https://postimg.cc/p97KPgcD)

          cd/var/lib/mysql; --查看二进制日志，二进制日志的默认编号是从000001往上编的，前面的会自动清理
          mysqlbinglog -s -binlog.000008;--binlog.000008是二进制文件
- mysqlshow

[![2023-08-26-225302.png](https://i.postimg.cc/tTCJ5q2f/2023-08-26-225302.png)](https://postimg.cc/t1w9Rj0t)

          mysqlshow -uroot -p1234 db01 course id --count;--表的某一具体字段
### 进阶--mysql管理--常用工具2

### 进阶--mysql管理--小结

### 进阶篇总结
# capter3 运维
## 运维--日志
### 运维--日志--错误日志
### 运维--日志--二进制日志
### 运维--日志--查询日志
### 运维--日志--慢查询日志
### 运维--主从复制--概述
### 运维--主从复制--原理
### 运维--主从复制--主库配置
### 运维--主从复制--从库配置
### 运维--主从复制--测试
### 运维--分库分表--介绍
### 运维--分库分表--介绍--拆分方式
### 运维--分库分表--mycat概述--安装
### 运维--分库分表--mycat概述--核心概念
### 运维--分库分表-
# 数据类型

## 整型

| 类型名称      | 取值范围                                  | 大小    |
| ------------- | ----------------------------------------- | ------- |
| TINYINT       | -128〜127                                 | 1个字节 |
| SMALLINT      | -32768〜32767                             | 2个宇节 |
| MEDIUMINT     | -8388608〜8388607                         | 3个字节 |
| INT (INTEGHR) | -2147483648〜2147483647                   | 4个字节 |
| BIGINT        | -9223372036854775808〜9223372036854775807 | 8个字节 |

无符号在数据类型后加 unsigned 关键字。

## 浮点型

| 类型名称            | 说明               | 存储需求   |
| ------------------- | ------------------ | ---------- |
| FLOAT               | 单精度浮点数       | 4 个字节   |
| DOUBLE              | 双精度浮点数       | 8 个字节   |
| DECIMAL (M, D)，DEC | 压缩的“严格”定点数 | M+2 个字节 |

## 日期和时间

| 类型名称  | 日期格式            | 日期范围                                          | 存储需求 |
| --------- | ------------------- | ------------------------------------------------- | -------- |
| YEAR      | YYYY                | 1901 ~ 2155                                       | 1 个字节 |
| TIME      | HH:MM:SS            | -838:59:59 ~ 838:59:59                            | 3 个字节 |
| DATE      | YYYY-MM-DD          | 1000-01-01 ~ 9999-12-3                            | 3 个字节 |
| DATETIME  | YYYY-MM-DD HH:MM:SS | 1000-01-01 00:00:00 ~ 9999-12-31 23:59:59         | 8 个字节 |
| TIMESTAMP | YYYY-MM-DD HH:MM:SS | 1980-01-01 00:00:01 UTC ~ 2040-01-19 03:14:07 UTC | 4 个字节 |

## 字符串

| 类型名称   | 说明                                         | 存储需求                                                   |
| ---------- | -------------------------------------------- | ---------------------------------------------------------- |
| CHAR(M)    | 固定长度非二进制字符串                       | M 字节，1<=M<=255                                          |
| VARCHAR(M) | 变长非二进制字符串                           | L+1字节，在此，L< = M和 1<=M<=255                          |
| TINYTEXT   | 非常小的非二进制字符串                       | L+1字节，在此，L<2^8                                       |
| TEXT       | 小的非二进制字符串                           | L+2字节，在此，L<2^16                                      |
| MEDIUMTEXT | 中等大小的非二进制字符串                     | L+3字节，在此，L<2^24                                      |
| LONGTEXT   | 大的非二进制字符串                           | L+4字节，在此，L<2^32                                      |
| ENUM       | 枚举类型，只能有一个枚举字符串值             | 1或2个字节，取决于枚举值的数目 (最大值为65535)             |
| SET        | 一个设置，字符串对象可以有零个或 多个SET成员 | 1、2、3、4或8个字节，取决于集合 成员的数量（最多64个成员） |

## 二进制类型

| 类型名称       | 说明                 | 存储需求               |
| -------------- | -------------------- | ---------------------- |
| BIT(M)         | 位字段类型           | 大约 (M+7)/8 字节      |
| BINARY(M)      | 固定长度二进制字符串 | M 字节                 |
| VARBINARY (M)  | 可变长度二进制字符串 | M+1 字节               |
| TINYBLOB (M)   | 非常小的BLOB         | L+1 字节，在此，L<2^8  |
| BLOB (M)       | 小 BLOB              | L+2 字节，在此，L<2^16 |
| MEDIUMBLOB (M) | 中等大小的BLOB       | L+3 字节，在此，L<2^24 |
| LONGBLOB (M)   | 非常大的BLOB         | L+4 字节，在此，L<2^32 |

# 权限一览表

> 具体权限的作用详见[官方文档](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html "官方文档")

GRANT 和 REVOKE 允许的静态权限

| Privilege                                                    | Grant Table Column           | Context                               |
| :----------------------------------------------------------- | :--------------------------- | :------------------------------------ |
| [`ALL [PRIVILEGES]`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_all) | Synonym for “all privileges” | Server administration                 |
| [`ALTER`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_alter) | `Alter_priv`                 | Tables                                |
| [`ALTER ROUTINE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_alter-routine) | `Alter_routine_priv`         | Stored routines                       |
| [`CREATE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_create) | `Create_priv`                | Databases, tables, or indexes         |
| [`CREATE ROLE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_create-role) | `Create_role_priv`           | Server administration                 |
| [`CREATE ROUTINE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_create-routine) | `Create_routine_priv`        | Stored routines                       |
| [`CREATE TABLESPACE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_create-tablespace) | `Create_tablespace_priv`     | Server administration                 |
| [`CREATE TEMPORARY TABLES`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_create-temporary-tables) | `Create_tmp_table_priv`      | Tables                                |
| [`CREATE USER`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_create-user) | `Create_user_priv`           | Server administration                 |
| [`CREATE VIEW`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_create-view) | `Create_view_priv`           | Views                                 |
| [`DELETE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_delete) | `Delete_priv`                | Tables                                |
| [`DROP`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_drop) | `Drop_priv`                  | Databases, tables, or views           |
| [`DROP ROLE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_drop-role) | `Drop_role_priv`             | Server administration                 |
| [`EVENT`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_event) | `Event_priv`                 | Databases                             |
| [`EXECUTE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_execute) | `Execute_priv`               | Stored routines                       |
| [`FILE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_file) | `File_priv`                  | File access on server host            |
| [`GRANT OPTION`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_grant-option) | `Grant_priv`                 | Databases, tables, or stored routines |
| [`INDEX`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_index) | `Index_priv`                 | Tables                                |
| [`INSERT`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_insert) | `Insert_priv`                | Tables or columns                     |
| [`LOCK TABLES`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_lock-tables) | `Lock_tables_priv`           | Databases                             |
| [`PROCESS`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_process) | `Process_priv`               | Server administration                 |
| [`PROXY`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_proxy) | See `proxies_priv` table     | Server administration                 |
| [`REFERENCES`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_references) | `References_priv`            | Databases or tables                   |
| [`RELOAD`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_reload) | `Reload_priv`                | Server administration                 |
| [`REPLICATION CLIENT`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_replication-client) | `Repl_client_priv`           | Server administration                 |
| [`REPLICATION SLAVE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_replication-slave) | `Repl_slave_priv`            | Server administration                 |
| [`SELECT`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_select) | `Select_priv`                | Tables or columns                     |
| [`SHOW DATABASES`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_show-databases) | `Show_db_priv`               | Server administration                 |
| [`SHOW VIEW`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_show-view) | `Show_view_priv`             | Views                                 |
| [`SHUTDOWN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_shutdown) | `Shutdown_priv`              | Server administration                 |
| [`SUPER`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_super) | `Super_priv`                 | Server administration                 |
| [`TRIGGER`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_trigger) | `Trigger_priv`               | Tables                                |
| [`UPDATE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_update) | `Update_priv`                | Tables or columns                     |
| [`USAGE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_usage) | Synonym for “no privileges”  | Server administration                 |

GRANT 和 REVOKE 允许的动态权限

| Privilege                                                    | Context                                           |
| :----------------------------------------------------------- | :------------------------------------------------ |
| [`APPLICATION_PASSWORD_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_application-password-admin) | Dual password administration                      |
| [`AUDIT_ABORT_EXEMPT`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_audit-abort-exempt) | Allow queries blocked by audit log filter         |
| [`AUDIT_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_audit-admin) | Audit log administration                          |
| [`AUTHENTICATION_POLICY_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_authentication-policy-admin) | Authentication administration                     |
| [`BACKUP_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_backup-admin) | Backup administration                             |
| [`BINLOG_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_binlog-admin) | Backup and Replication administration             |
| [`BINLOG_ENCRYPTION_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_binlog-encryption-admin) | Backup and Replication administration             |
| [`CLONE_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_clone-admin) | Clone administration                              |
| [`CONNECTION_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_connection-admin) | Server administration                             |
| [`ENCRYPTION_KEY_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_encryption-key-admin) | Server administration                             |
| [`FIREWALL_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_firewall-admin) | Firewall administration                           |
| [`FIREWALL_EXEMPT`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_firewall-exempt) | Firewall administration                           |
| [`FIREWALL_USER`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_firewall-user) | Firewall administration                           |
| [`FLUSH_OPTIMIZER_COSTS`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-optimizer-costs) | Server administration                             |
| [`FLUSH_STATUS`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-status) | Server administration                             |
| [`FLUSH_TABLES`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-tables) | Server administration                             |
| [`FLUSH_USER_RESOURCES`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-user-resources) | Server administration                             |
| [`GROUP_REPLICATION_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_group-replication-admin) | Replication administration                        |
| [`GROUP_REPLICATION_STREAM`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_group-replication-stream) | Replication administration                        |
| [`INNODB_REDO_LOG_ARCHIVE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_innodb-redo-log-archive) | Redo log archiving administration                 |
| [`NDB_STORED_USER`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_ndb-stored-user) | NDB Cluster                                       |
| [`PASSWORDLESS_USER_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_passwordless-user-admin) | Authentication administration                     |
| [`PERSIST_RO_VARIABLES_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_persist-ro-variables-admin) | Server administration                             |
| [`REPLICATION_APPLIER`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_replication-applier) | `PRIVILEGE_CHECKS_USER` for a replication channel |
| [`REPLICATION_SLAVE_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_replication-slave-admin) | Replication administration                        |
| [`RESOURCE_GROUP_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_resource-group-admin) | Resource group administration                     |
| [`RESOURCE_GROUP_USER`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_resource-group-user) | Resource group administration                     |
| [`ROLE_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_role-admin) | Server administration                             |
| [`SESSION_VARIABLES_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_session-variables-admin) | Server administration                             |
| [`SET_USER_ID`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_set-user-id) | Server administration                             |
| [`SHOW_ROUTINE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_show-routine) | Server administration                             |
| [`SYSTEM_USER`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_system-user) | Server administration                             |
| [`SYSTEM_VARIABLES_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_system-variables-admin) | Server administration                             |
| [`TABLE_ENCRYPTION_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_table-encryption-admin) | Server administration                             |
| [`VERSION_TOKEN_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_version-token-admin) | Server administration                             |
| [`XA_RECOVER_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_xa-recover-admin) | Server administration                             |

# 图形化界面工具

- Workbench(免费): http://dev.mysql.com/downloads/workbench/
- navicat(收费，试用版30天): https://www.navicat.com/en/download/navicat-for-mysql
- Sequel Pro(开源免费，仅支持Mac OS): http://www.sequelpro.com/
- HeidiSQL(免费): http://www.heidisql.com/
- phpMyAdmin(免费): https://www.phpmyadmin.net/
- SQLyog: https://sqlyog.en.softonic.com/

# 安装

# 小技巧

1. 在SQL语句之后加上`\G`会将结果的表格形式转换成行文本形式
2. 查看Mysql数据库占用空间：
```mysql
SELECT table_schema "Database Name"
     , SUM(data_length + index_length) / (1024 * 1024) "Database Size in MB"
FROM information_schema.TABLES
GROUP BY table_schema;
```

# 参考文献
> https://dhc.pythonanywhere.com/entry/share/?key=3ad29aad765a2b98b2b2a745d71bef715507ee9db8adbec98257bac0ad84cbe4#h1-u6743u9650u4E00u89C8u8868
> 这篇笔记是在别人的基础上完善而来，感谢B站的黑马程序员up主，也感谢路途博客。
