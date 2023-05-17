---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Cost-effective Vehicular Data Offloading in ISTNs: A Reinforcement Learning Approach'
#按照实际情况填写
authors:
  - Shen Wu  
  - Nan Cheng
  - Zhisheng Yin
  - Jingchao He
  - Haibo Zhou
#论文发表时间 只更改年月日
date: '2023-01-11T00:00:00Z'
#doi号
doi: ''
#同论文发表时间 只更改年月日
publishDate: '2023-01-11T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# 期刊/会议名称 要求全称
publication: 'IEEE Global Communications Conference'
# 留空
publication_short: ''
# 文章摘要
abstract: Integrated satellite-terrestrial network (ISTN) can provide a continuous service for vehicular users in remote areas with a seamless network coverage. However, considering the difference in the usage costs between satellite and terrestrial networks and the variability of services for latency requirements, it is of great significance to design a cost-effective data offloading decision for reducing network overhead and ensuring task delay requirements. In this paper, we design a cost-effective data offloading mechanism for vehicles in ISTN. The default transmission for remote areas is via the satellite, where the terrestrial networks can offload the data with intermittent coverage in an opportunistic manner due to the vehicle mobility. To model the diversity in service delay requirements, a virtual queue is exploited to capture the residual maximum delay tolerance of each service as time elapses. We formulate the satellite-terrestrial collaborative transmission as a non-linear programming (NLP) problem. To solve the problem, we propose a reinforcement learning (RL)-based data offloading algorithm for real-time decision making. Simulation results show that the RL-based data offloading algorithm reduces the network overhead and outperforms other baseline schemes we proposed.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/abstract/document/10000949
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Cost.pdf'
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
