---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'UAV-assisted Secure Uplink Communications in Satellite-supported IoT: Secrecy Fairness Approach'
#按照实际情况填写
#Ziyan Chen; Nan Cheng; Zhisheng Yin; Jingchao He; Ning Lu
authors:
  - Zhisheng Yin
  - Nan Cheng
  -  Yunchao Song
  - Yilong Hui
  - Yunhan Li
  - Tom H. Luan
  - Shui Yu
#论文发表时间 只更改年月日
date: '2023-09-08T00:00:00Z'
#doi号
doi: '10.1109/JIOT.2023.3313197'
#同论文发表时间 只更改年月日
publishDate: '2023-09-08T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# 期刊/会议名称 要求全称
publication: 'IEEE Internet of Things Journal'
# 留空
publication_short: ''
# 文章摘要
abstract: The escalating growth of the Internet of things (IoT) has intensified the demand for dependable and efficient communication networks to accommodate the massive data volumes produced by interconnected devices. Satellite networks have emerged as a promising alternative, particularly in remote and underserved regions where terrestrial communication infrastructures are inadequate. Nevertheless, guaranteeing secure uplink communications in satellite-based IoT networks is a daunting task due to similar satellite channels and limited resources at IoT nodes. In this paper, we explore the potential of unmanned aerial vehicle (UAV) to improve the secrecy performance of uplink transmissions in satellite-supported IoT networks. Specifically, we first introduce a framework for UAV-aided secure uplink communications, presuming a secure UAV-to-satellite connection. To mitigate the risks of ground eavesdroppers intercepting uplink transmissions, we develop a max-min secrecy rate optimization problem with uplink power constraints. To address this non-convex problem, a streamlined two-stage optimization approach is proposed. In inner stage, we combine uplink power allocation and UAV beamforming and propose a successive convex approximation (SCA) based joint optimization algorithm to address them. In outer stage, we propose an synergized bisection and coordinate descent algorithm to optimize UAV positioning. Convergence is attained by alternating iterations between these two stages. Particularly, the secrecy fairness among IoT users is reached by solving the max-min problem. Additionally, we offer a complexity analysis of the proposed algorithm and validate the efficacy of the presented approach through comprehensive simulation results.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/abstract/document/10243608
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './UAV-assisted_Secure_Uplink_Communications_in_Satellite-supported_IoT_Secrecy.pdf'
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
