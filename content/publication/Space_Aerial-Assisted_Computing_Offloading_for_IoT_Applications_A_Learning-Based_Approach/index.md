---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Space/Aerial-Assisted Computing Offloading for IoT Applications: A Learning-Based Approach'
#按照实际情况填写
authors:
  - Nan Cheng
  - Feng Lyu
  - Wei Quan
  - Conghao Zhou
  - Hongli He
  - Weisen Shi
  - Xuemin Shen
#论文发表时间 只更改年月日
date: '2019-03-21T00:00:00Z'
#doi号
doi: '10.1109/JSAC.2019.2906789'
#同论文发表时间 只更改年月日
publishDate: '2019-03-21T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# 期刊/会议名称 要求全称
publication: 'IEEE Journal on Selected Areas in Communications'
# 留空
publication_short: ''
# 文章摘要
abstract: Internet of Things (IoT) computing offloading is a challenging issue, especially in remote areas where common edge/cloud infrastructure is unavailable. In this paper, we present a space-air-ground integrated network (SAGIN) edge/cloud computing architecture for offloading the computation-intensive applications considering remote energy and computation constraints, where flying unmanned aerial vehicles (UAVs) provide near-user edge computing and satellites provide access to the cloud computing. First, for UAV edge servers, we propose a joint resource allocation and task scheduling approach to efficiently allocate the computing resources to virtual machines (VMs) and schedule the offloaded tasks. Second, we investigate the computing offloading problem in SAGIN and propose a learning-based approach to learn the optimal offloading policy from the dynamic SAGIN environments. Specifically, we formulate the offloading decision making as a Markov decision process where the system state considers the network dynamics. To cope with the system dynamics and complexity, we propose a deep reinforcement learning-based computing offloading approach to learn the optimal offloading policy on-the-fly, where we adopt the policy gradient method to handle the large action space and actor-critic method to accelerate the learning process. Simulation results show that the proposed edge VM allocation and task scheduling approach can achieve near-optimal performance with very low complexity and the proposed learning-based computing offloading algorithm not only converges fast but also achieves a lower total cost compared with other offloading approaches.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/document/8672604
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Space_Aerial.pdf'
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
