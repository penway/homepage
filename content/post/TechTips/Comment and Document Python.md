---
title: 【算法】01 二路归并
subtitle: 

# Summary for listings and search engines
summary: 算法，二路归并

# Link this post with a project
projects: [Algorithm]

# Date published
date: "2021-09-16T00:00:00Z"

# Date updated
lastmod: "2021-09-16T00:00:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: 'Image credit: [**Unsplash**](./featured.jpg)'
  focal_point: ""
  placement: 2
  preview_only: false

# Date published
date: "2021-10-21T00:00:00Z"

# Date updated
lastmod: "2021-10-21T00:00:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: 'Image credit: [**Unsplash**](./featured.jpg)'
  focal_point: ""
  placement: 2
  preview_only: false

authors:
- penway

tags:
- 算法

categories:
- 算法
---
## 【读书笔记】为Python写注释与文档

原文链接：[Documenting Python Code: A Complete Guide – Real Python](https://realpython.com/documenting-python-code/)

#### 注释和文档的区别

注释为开发者而写，代码的维护者和开发者是其主要受众，代码和注释相互配合阐述设计目的和方法。

文档为用户而生，表述代码的用途与用法。

#### 注释基础

- 用 # 开头
- 根据PEP8，单行注释不得超过72字符，若有超过，则换用多行注释更佳。

- 注释的目的：
  - 计划与复盘：写代码前先用注释规划步骤
  - 描述代码
  - 解释算法
  - 做标记：如 `BUG`, `FIXME`, `TODO`
- 注释要义：
  - 简洁
  - 注释应靠近代码
  - 勿用复杂格式
  - 勿重复
  - 代码本身应易于理解，而非完全依靠注释

- 使用类型说明 （python 3.5+）

  ```
  def hello_name(name: str) -> str:
  	return(f"Hello {name}")
  ```

#### 用docstring书写文档

- 文档的位置：一个类的文档是作为一个类的一个叫 `MyClass.__doc__` 的属性存在的

- docstring分类
  - 类的docstring
  - 包或模块的docstring
  - 脚本的docstring
- 类的docstring
  - 直接在类的开头写多行注释

- 包或模块的docstring
  - 在包的`__init__.py`的开头书写
- 脚本的docstring
  - 在脚本的开头书写
  - 脚本指的是可以直接在终端中执行的python文件

- docstring的格式没有强制的要求，文中列举的主要有几种被用到的格式规范
  - Google docstring
  - reStructured Text
  - Numpy/Scipy docstring
  - Epytext

#### 为工程写注释

- readme
- examples.py
- 如何做贡献 How to Contribute（共享或开源工程）
- 行为准则 （开源工程）

- 许可证（开源工程）
- 文档文件夹（开源工程）

## License

Copyright 2021 王鹏维
