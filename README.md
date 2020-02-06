[toc]

## 1. Structure

```bash
.
├── README.md
├── bg.png
├── docs
├── make # 相关的执行脚本
│   ├── beauty_name.py
│   ├── build_core.py
│   ├── build_index.py
│   ├── mume_config.js
│   ├── mume_parse.js
│   └── run.sh # <-- 像vscode那样编译markdwon执行这里
└── release
    ├── cfg # 发布服务的配置
    ├── docs # 由docs编译生成link的html文件
    ├── logs # 服务的日志
    ├── server.py # <-- 启动服务走这里
```

针对make路径下的脚本解释

|脚本|描述|
|-|-|
|==*run.sh*==|完整执行生成html的脚本|
|`build_core.py -> (mume_config.js + mume_parse.js)`|core核心调用 [mume](https://github.com/shd101wyy/mume)|
|`build_index.py`|遍历docs结构建立对应的index文件|
|beauty_name.py|对原docs项目中不合法名称替换修复|

---

## 2. Docs

文档是整个项目的核心，其他模块只是为了编译markdown文档并发布静态网站
（原生的markdown文档可以从专栏中copy过来）

```vim
├── [Hive]
│   ├── HQL语法
│   │   ├── 1-常用函数积累
│   │   ├── 2-行列转换
│   │   └── 3-分区相关内容
│   ├── 开发经验
│   │   ├── 1-常用DDL操作与问题
│   │   ├── 2-UDF的困惑与学习
│   │   ├── 3-hive调优总结
│   │   └── 4-Hive作业性能的优化
│   └── 内部实现剖析
│       ├── 1-hive客户端启动
│       └── 2-HiveSQL的编译过程
```

根据长期的经验，结构统一方便整体的概念体系树立，模块文档最多三层级

---

## 3. Prepare
### 3.1. Node
1.[下载node](https://nodejs.org/dist/v10.16.3/node-v10.16.3.pkg)安装或者mac用brew安装
```bash
[likang02@xx ~]$ brew install node
```

2.配置node依赖install的全局路径
```bash
[likang02@xx ~]$ vim ~/.npmrc
prefix=/Users/likang02/.nodejs/node_global
cache=/Users/likang02/.nodejs/node_cache
```

3.安装mume的依赖到全局LIB
```bash
# 网络安装
[likang02@xx ~]$ npm install -g --save @shd101wyy/mume
or
# 源代码安装
[likang02@xx ~]$ git clone https://github.com/shd101wyy/mume.git
[likang02@xx ~]$ npm install -g
```
4.配置`import`时候查找LIB的全局变量
```bash
[likang02@xx ~]$ vim ~/.bash_profile
export NODE_PATH="/Users/likang02/.nodejs/node_global/lib/node_modules/"
```

5.测试是否可以编译md为合适的html文件
```bash
[likang02@xx ~]$ node mume_parse.js ./1.初识.md
```

### 3.2. Python

1.下载安装脚本

```bash
[likang02@xx ~]$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
[likang02@xx ~]$ sudo python get-pip.py
```

2.安装web.py服务依赖
```bash
[likang02@xx ~]$ pip install web.py
```

---

## 4. Release

### 4.1. Build md

```bash
[likang02@xx ~]$ cd make
[likang02@xx ~]$ sh run.sh
```

查看发布路径下的html文件`mk-blog-site/release/docs`

**可以将编译完的html文件，发不到S3或者Github Page 当做个人静态博客**


### 4.2. Server

启动服务

```bash
[likang02@xx ~]$ python server.py 8081
```

show index page

![2ee4dc1975efcb5366dbb3e7286f1b4d.png](https://i.loli.net/2019/09/26/9vHdDSERKr8AxNT.png)
