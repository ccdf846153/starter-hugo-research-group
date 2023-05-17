---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'AoI-Oriented Content Caching and Updating in Maritime Internet of Things'
#按照实际情况填写
authors:
  - Ruijin Sun
  - Yujie Zhang
  - Nan Cheng
  - Rong Chai
  - Tingting Yang
  - Meng Qin
#论文发表时间 只更改年月日
date: '2022-12-08T00:00:00Z'
#doi号
doi: '10.1109/GLOBECOM48099.2022.10001473'
#同论文发表时间 只更改年月日
publishDate: '2022-12-08T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# 期刊/会议名称 要求全称
publication: '2022 IEEE Global Communications Conference'
# 留空
publication_short: ''
# 文章摘要
abstract: Caching popular contents at the base station (BS) in maritime Internet of Things (IoT) networks makes sensor nodes be free from frequently responding to user requests, which can remarkably save the energy consumption of sensor nodes. However, to ensure the freshness of contents, cached contents need to be updated periodically. Frequent content updating can minimize the age of information (AoI) of contents while increase the energy consumption of sensor nodes. To make a better tradeoff between the AoI and energy consumption, in this paper, both the cache placement and content updating interval are jointly optimized to minimize the weighted sum of AoI of contents and energy consumption of sensor nodes. As the formulated problem is a mixed integer nonlinear programming problem, the cache placement and the content updating interval are alternatively optimized. For the cache placement problem, a local optimal solution is achieved via the binary constraint reformulation and successive convex approximation. For the content updating problem, the optimal solution with semi-closed form is derived. Simulation results show that our proposed algorithm outperforms other benchmarks in terms of the weighted sum of AoI and energy consumption.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/document/10113154
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './AI_for_UAV-Assisted_IoT_Applications_A_Comprehensive_Review.pdf'
# 都留空
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''


image:
  caption: 
  focal_point: ''
  preview_only: false

projects: []
slides:
---
