---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Joint Flying Relay Location and Routing Optimization for 6G UAV-IoT Networks: A Graph Neural Network-Based Approach'
#按照实际情况填写
authors:
  - Xiucheng Wang
  - Fu, Lianhao
  - Nan Cheng
  - Sun, Ruijin
  - Luan, Tom
  - Quan, Wei
  - Aldubaikhy, Khalid
#论文发表时间 只更改年月日
date: '2022-09-03T00:00:00Z'
#doi号
doi: 'https://doi.org/10.3390/rs14174377'
#同论文发表时间 只更改年月日
publishDate: '2022-09-03T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# 期刊/会议名称 要求全称
publication: 'Remote Sensing'
# 留空
publication_short: 'Remote Sens.'
# 文章摘要
abstract: Unmanned aerial vehicles (UAVs) are widely used in Internet-of-Things (IoT) networks, especially in remote areas where communication infrastructure is unavailable, due to flexibility and low cost. However, the joint optimization of locations of UAVs and relay path selection can be very challenging, especially when the numbers of IoT devices and UAVs are very large. In this paper, we formulate the joint optimization of UAV locations and relay paths in UAV-relayed IoT networks as a graph problem, and propose a graph neural network (GNN)-based approach to solve it in an efficient and scalable way. In the training procedure, we design a reinforcement learning-based relay GNN (RGNN) to select the best relay path for each user. The theoretical analysis shows that the time complexity of RGNN is two orders lower than the conventional optimization method. Then, we jointly exploit location GNN (LGNN) and RGNN trained to optimize the locations of all UAVs. Both GNNs can be trained without relying on the training data, which is usually unavailable in the context of wireless networks. In inference procedure, LGNN is first used to optimize the location of UAVs, and then RGNN is used to select the best relay path based on the output of LGNN. Simulation results show that the proposed approach can achieve comparable performance to brute-force search with much lower time complexity when the network is relatively small. Remarkably, the proposed approach is highly scalable to large-scale networks and adaptable to dynamics in the environment, which can hardly be achieved using conventional methods.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: Remote Sens. Link
        #这里替换成IEEE网站的链接
    url: https://www.mdpi.com/2072-4292/14/17/4377
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Joint_Flying_Relay_Location.pdf'
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
