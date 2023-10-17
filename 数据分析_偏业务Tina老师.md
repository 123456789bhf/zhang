## 数据分析（偏业务方向）
详细见iypn文件
### 数据分析岗位职责和数据分析师
[![2023-10-15-213940.png](https://i.postimg.cc/TwHyRt0s/2023-10-15-213940.png)](https://postimg.cc/PpYfyzBb)
[![2023-10-15-214014.png](https://i.postimg.cc/JzcGyrKZ/2023-10-15-214014.png)](https://postimg.cc/nXrHgtyh)
[![2023-10-15-214256.png](https://i.postimg.cc/x8cssjt4/2023-10-15-214256.png)](https://postimg.cc/GTnJtR0F)
- 关于技术
  - 练习
- 关于思维
1. 看到别人的报告。把看报告融入生活：总结别人图表中的信息
2. 看指标，从一个熟悉的行业开始。解读别人如何搭建指标体系
3. 利用统计学，查看数据分布，图表本无对错，按照自己想法可视化
### 指标与
#### 指标与指标体系
-  指标:是统计学的范畴，将说明总体特征的概念称为指标。传统的指标有GDP、GNP、CPI
-  数据指标有别于传统意义上的统计指标，它是将业务单元精分和量化后的度量值，使得业务目标可描述、可度量、可拆解、通过对数据进行分析得到一个汇总结果
-  指标构成
1. 维度
2. 汇总方式
3. 量度
[![2023-10-16-221103.png](https://i.postimg.cc/Nfyw1qtb/2023-10-16-221103.png)](https://postimg.cc/Mv84SLvj)
- 指标的类型
1. 基础指标（业务实体的总和和）：订单数,DAU（日活）
2. 符合指标（建立基础指标、由规则运算形成）：ARPU(平均每个用户的收入)、好评率
3. 派生指标（建立基础and派生，与维度、统计、管理等属性相结合）：双十一成都订单数、近7日的活跃用户数
- 指标体系
1. 体系化的本质是将数据指标系统的组织起来，具体会按照业务模型、按标准对指标不同的属性分类及分层
2. 不同的业务阶段、不同业务类型会有不同阶段的划分标准
3. 数据指标体系含有十分丰富的统计量，从宏观上看，他是一个相对全面的有机体；从微观上看，每个数据指标都有其特定的含义，反映了某一细节的客观事实
- 电商指标体系
1. 总体运营（一级指标）：
2. 网站流量：规模，PV（一天内页面被打开多少次），UV（一天内有多少人浏览该网页）,DAU(每日的活跃人数，又称为日活，每个公司记录的方式不同)
3. 销售转化：
4. 客户价值
5. 商品主题：SKU(每个商品独特的编码)
6. 营销活动：LR(收益除以成本)
7. 风险控制：投诉率
8. 市场竞争：市场份额，APP排名等
  - 更多的指标见："C:\Users\23665\Desktop\研一上课资料\111\sql\数据分析_偏业务_tina老师\5.数据指标体系.rar"
  - 指标不需要掌握，需要做到的是，拿到一个新的行业，从各个指标体系将业务拆分出来
- 指标体系的作用
  - 全部面支持决策
  - 指导业务运营
  - 驱动用户增长
  - 统一统计口径
- 核心指标变化了，需要知道：
  1. 为什么变化？
  2. 和哪些因素有关？
  3. 如何解决
#### 如何搭建指标体系
- OSM方法
  - 目标：希望实现的业务目标
  - 策略：为了达成目标采取的具体的行动策略
  - 度量：衡量策略是否有效、策略的量化
- O确定核心指标
  - 唯一重要指标
  - 全公司的核心主动目标
  - 指引公司方向
- S:关键路径
  - UJM模型：User JOunary Map(用户旅程地图)
  - 梳理用户（使用者）的生命旅程
    - 将每个用户所处的每一个阶段，做行为拆解。明确每个阶段的目标，找到产品和用户的接触点，从中找到痛点和机会点。比如：汽车行业的关键路径就是造车的全部过程（对于汽车行业用户就是车）
  - 优酷、爱奇艺、腾讯 用户路径分析
    - 打开APP-->打开甄嬛传-->看甄嬛传
#### 常用行业用户路径解析
- 在看之前就是整个用户的生命旅程
- 如果想让用户继续观看就是连续看
- 如果想挣钱就可以让用户买，比如让第几集是VIP
[![2023-10-16-231941.png](https://i.postimg.cc/Sj0gbgr9/2023-10-16-231941.png)](https://postimg.cc/JHqNbcS7)
[![2023-10-16-232206.png](https://i.postimg.cc/R0sYWQd3/2023-10-16-232206.png)](https://postimg.cc/McB54Bhx)
[![2023-10-16-232550.png](https://i.postimg.cc/J0vmjCQk/2023-10-16-232550.png)](https://postimg.cc/hQLHqw6D)
- **搭建指标的注意事项**
  - 从0到1搭建指标体系对于初级数据分析师来说是非常困难的，一般情况下以及、二级（基础、复合）是由业务leader带领团队一起建立的，但是三级指标（派生指标）的细化与拆解，是我们作为分析师找到关键问题细化业务的必备技能。
  - 找运营的，了解一下他们的工作，这个时候就会知道其核心指标
  - 或者自己下载APP体验一下，看有上面问题
[![2023-10-16-234044.png](https://i.postimg.cc/L8bCRkVN/2023-10-16-234044.png)](https://postimg.cc/68CLfvgv)
#### Dog东指标的拆解与分析
- 指标的拆解
  - APP上的弹窗（比如：网易云弹出京东）
[![2023-10-16-234243.png](https://i.postimg.cc/7hN4Qt0B/2023-10-16-234243.png)](https://postimg.cc/jnCBDX8N)
[![2023-10-16-234333.png](https://i.postimg.cc/2y9c64Dk/2023-10-16-234333.png)](https://postimg.cc/0KmdXKjF)
[![2023-10-16-234644.png](https://i.postimg.cc/hPcnknCp/2023-10-16-234644.png)](https://postimg.cc/s16bWkCh)
- 营销落地页：通过他人达到的某个商品购买的页面
- BI可以给定数据将各中指标求出
[![2023-10-16-234921.png](https://i.postimg.cc/d3HjqwKg/2023-10-16-234921.png)](https://postimg.cc/SY9Md0RG)
- 内容平台：比如：抖音、微博都是
- UGC:最好的状态，也就是用户就是内容生成者，比如：B站。
- OGC：内容创造平台，公司、媒体创造内容，这个比较贵
- PGC：行业领袖、专业生产内容的平台
[![2023-10-17-204450.png](https://i.postimg.cc/qMs9WBDR/2023-10-17-204450.png)](https://postimg.cc/qz7b3rTV)
- 京东指标拆解
  - GMV:总的营业额
  - 只要细分的人数够细就可以找到更好的用户增长方式，比如说年龄段、性别
[![2023-10-17-205321.png](https://i.postimg.cc/2yZVCLbg/2023-10-17-205321.png)](https://postimg.cc/y37VPdTT)
[![2023-10-17-205716.png](https://i.postimg.cc/65SXN6dx/2023-10-17-205716.png)](https://postimg.cc/QHpPQ34f)
[![2023-10-17-210127.png](https://i.postimg.cc/PrFwsD3f/2023-10-17-210127.png)](https://postimg.cc/gn8J3xb1)
- 支付宝买入网易云、b站等对用户打标签，其他的app会购买支付宝的标签，对每个用户，根据标签预测其点击率，计算GTR数据，有的在使用标签之后的点击率从0.3%上升至48%
### 数据分析的方法和模型
- 如何锻炼思维？
  - 看之前的报告（用了哪些指标，大纲是什么，采用的什么图表），模仿
- 数据敏感性（抽象）
- 数据分析方法-抖音教育直播
[![2023-10-17-212914.png](https://i.postimg.cc/cJL65LZy/2023-10-17-212914.png)](https://postimg.cc/RW2MW9NX)
- 蓝V(有企业认证的)，达人（自己开指标）
[![2023-10-17-213152.png](https://i.postimg.cc/DwgcR6JW/2023-10-17-213152.png)](https://postimg.cc/75572gND)
- 京东的一级品类：衣服、蔬菜这一栏
[![2023-10-17-213302.png](https://i.postimg.cc/zfyRpFnY/2023-10-17-213302.png)](https://postimg.cc/VSc6kMGK)
- 对于缓慢上升、下降需要分析
[![2023-10-17-213730.png](https://i.postimg.cc/Gtw7b2c9/2023-10-17-213730.png)](https://postimg.cc/phCYZP5t)

[![2023-10-17-214149.png](https://i.postimg.cc/9QmWWXMx/2023-10-17-214149.png)](https://postimg.cc/3dqM1T2p)
- 原点是横纵坐标的均值
[![2023-10-17-214415.png](https://i.postimg.cc/q7tgTBbP/2023-10-17-214415.png)](https://postimg.cc/t1j9dbHk)
- 看是否存在长尾效应，左边越尖越短就是常委效益给，下面的哪个就是长尾效应，长尾的不好，就比如说财富集中在少部分人手中。
[![2023-10-17-214616.png](https://i.postimg.cc/jSHZhK4r/2023-10-17-214616.png)](https://postimg.cc/Wd4G2By9)
[![2023-10-17-215016.png](https://i.postimg.cc/x8rSznPb/2023-10-17-215016.png)](https://postimg.cc/hz0wFF6S)
[![2023-10-17-215209.png](https://i.postimg.cc/4xYwrVGs/2023-10-17-215209.png)](https://postimg.cc/cvNQ3K6b)
- 根据图标可以知道目标应该放在一线、二线城市中
- 主要做的是用户的拆解
[![2023-10-17-215333.png](https://i.postimg.cc/yYgZKPDQ/2023-10-17-215333.png)](https://postimg.cc/BX36c2cH)
[![2023-10-17-215454.png](https://i.postimg.cc/8PS78SV5/2023-10-17-215454.png)](https://postimg.cc/w3wqJnM8)
- **数据分析模型**
  - 开放性问题：比如，如何估计疫情对生活的影响
    - 先构造一些指标（体现数据思维），之后在分析各个指标的计算方法，再按照一些维度进行分析
- 北京有多少加油站？
  - 前提：具备基本的数据常识
  - 比如：人口数、占地面积、物品价格
[url=https://postimg.cc/5HX77YqS][img]https://i.postimg.cc/5HX77YqS/2023-10-17-220232.png[/img][/url]
[![2023-10-17-220441.png](https://i.postimg.cc/5ycT7gTH/2023-10-17-220441.png)](https://postimg.cc/vgz0DrQM)
- 总共需要3000充电桩
[![2023-10-17-220604.png](https://i.postimg.cc/wvD0vp4v/2023-10-17-220604.png)](https://postimg.cc/Kkvnqd2S)
[![2023-10-17-220734.png](https://i.postimg.cc/W3phDmXk/2023-10-17-220734.png)](https://postimg.cc/zLMJ6hmz)
[![2023-10-17-221238.png](https://i.postimg.cc/sg96PSpc/2023-10-17-221238.png)](https://postimg.cc/yDxysDpg)
- 因为每10天需要加一次油，所以需要乘以3
[![2023-10-17-221309.png](https://i.postimg.cc/WzkSdJN0/2023-10-17-221309.png)](https://postimg.cc/Wqs0KzJ4)

[![2023-10-17-221344.png](https://i.postimg.cc/637fPGGF/2023-10-17-221344.png)](https://postimg.cc/k6mS6Gsy)

[![2023-10-17-221441.png](https://i.postimg.cc/bwJDLfnB/2023-10-17-221441.png)](https://postimg.cc/56h2NGnB)
- 你们现在准备一个电动汽车上市的推广策划，预算是20w，一个月的时间准备，你会怎么样规划？
  - 先提问：问hr
[![2023-10-17-221745.png](https://i.postimg.cc/KvXhJPMS/2023-10-17-221745.png)](https://postimg.cc/DmcNzb6B)
[![2023-10-17-221931.png](https://i.postimg.cc/cJ7vL1G6/2023-10-17-221931.png)](https://postimg.cc/d71sWY1K)
[![2023-10-17-222026.png](https://i.postimg.cc/Nf7GXJPP/2023-10-17-222026.png)](https://postimg.cc/mtkGfw4Q)
- 答案不唯一，只要有思路就可以
[![2023-10-17-222104.png](https://i.postimg.cc/fTKZy3JG/2023-10-17-222104.png)](https://postimg.cc/TppBH3j0)
- 对该问题找一写指标哦
[![2023-10-17-223100.png](https://i.postimg.cc/CM4khNsS/2023-10-17-223100.png)](https://postimg.cc/7bffXSRW)
- 用户画像：付费的总金额，还有玩家的付费频率，上一次付费的时间，如果有姓名和年龄也可以加上
- 付费流畅度：整个流程的转化率，从一开始点击，到最后买成功（付费）这一整个过程的转换率
[![2023-10-17-224228.png](https://i.postimg.cc/T1mCHWWC/2023-10-17-224228.png)](https://postimg.cc/p5WfmrCF)
[![2023-10-17-224318.png](https://i.postimg.cc/prYKFQjb/2023-10-17-224318.png)](https://postimg.cc/XBqZMCxQ)
[![2023-10-17-224632.png](https://i.postimg.cc/yxcCXx6z/2023-10-17-224632.png)](https://postimg.cc/Lg9WmHZy)
- 拼多多是下面的方式
[![2023-10-17-224913.png](https://i.postimg.cc/906FCs0c/2023-10-17-224913.png)](https://postimg.cc/K35y5qtW)
[![2023-10-17-224951.png](https://i.postimg.cc/pyMxg8cT/2023-10-17-224951.png)](https://postimg.cc/7J9pzCk8)
- 当一个游戏具有上面8种属性的时候就是最好的，拼多多就有上面的8种属性
[![2023-10-17-225135.png](https://i.postimg.cc/fbd4hkXS/2023-10-17-225135.png)](https://postimg.cc/QBjYQ8fj)
- 也可用用八角分析法分析这种角度分析数据
- 总结
  - 分析问题可以采用费米问题分析方法或者5W2H、AARRR模型来分析数据
### 统计的世界
[![2023-10-17-231244.png](https://i.postimg.cc/YqrnMRTw/2023-10-17-231244.png)](https://postimg.cc/nMWY14Hd)
[![2023-10-17-232238.png](https://i.postimg.cc/4xSh26DG/2023-10-17-232238.png)](https://postimg.cc/CRb1zqMr)
[![2023-10-17-232329.png](https://i.postimg.cc/wvdMn0FC/2023-10-17-232329.png)](https://postimg.cc/XZQnCKRL)
- （离散变量的相关性检验：卡方检验
[![2023-10-17-232628.png](https://i.postimg.cc/KcCGW9zJ/2023-10-17-232628.png)](https://postimg.cc/K4rhkDtM)
[![2023-10-17-233520.png](https://i.postimg.cc/pV30njGm/2023-10-17-233520.png)](https://postimg.cc/jCQ6pDrT)
[![2023-10-17-233607.png](https://i.postimg.cc/284xbKLt/2023-10-17-233607.png)](https://postimg.cc/Wh1ZxSnm)
- 连续变量的相关性检验
[![2023-10-17-233810.png](https://i.postimg.cc/bJpPPMbj/2023-10-17-233810.png)](https://postimg.cc/nsRgY30d)
[![2023-10-17-233923.png](https://i.postimg.cc/DfNNdHZy/2023-10-17-233923.png)](https://postimg.cc/jCzvR8PG)
- 皮尔相关系数前提是数据是正态分布，但是斯皮尔曼相关系数对分布没有要求，判断数据是否服从正态分布
[![2023-10-17-234820.png](https://i.postimg.cc/7P72LJpP/2023-10-17-234820.png)](https://postimg.cc/kDJ41GJL)
### EXCEL
### 商业智能_Power BI
### Tableau
### 数据分析介绍
