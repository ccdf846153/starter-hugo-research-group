---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Service-Oriented Network Resource Orchestration in Space-Air-Ground Integrated Network'
#按照实际情况填写
#Ziyan Chen; Nan Cheng; Zhisheng Yin; Jingchao He; Ning Lu
authors:
  - Jingchao He
  - Nan Cheng
  - Zhisheng Yin
  - Conghao Zhou
  - Haibo Zhou
  - Wei Quan
  - Xiao-Hui Lin
#论文发表时间 只更改年月日
date: '2023-08-03T00:00:00Z'
#doi号
doi: '10.1109/TVT.2023.3301676'
#同论文发表时间 只更改年月日
publishDate: '2023-08-03T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# 期刊/会议名称 要求全称
publication: 'IEEE Transactions on Vehicular Technology'
# 留空
publication_short: ''
# 文章摘要
abstract: Space-air-ground integrated networks (SAGINs) are envisioned to provide seamless coverage and enhanced flexibility compared with traditional terrestrial mobile networks, which has attracted much attention from both industry and academia. However, orchestrating heterogeneous resources in such a large-scale and dynamic network is challenging, especially encountering diverse services with multi-dimensional requirements. In this paper, we first propose a software-defined networking (SDN) and network function virtualization (NFV)-based reconfigurable SAGIN architecture for constructing service function chains (SFCs). Based on that, we investigate the SFC orchestration and wireless resource management where the virtual link rate adaption between each virtual network function (VNF) is introduced to improve the network resource utilization. Considering the limited physical resource and the heterogeneity in SAGINs, we jointly formulate the VNF embedding, virtual link rate adaption, and wireless resource allocation as a mixed-integer nonlinear programming (MINLP) problem to maximize the network profit. Due to the NP-hardness of the problem, we first transform the problem into a continuous optimization problem by successive convex approximation. By introducing an additional penalty into the objective function, an iterative alternation algorithm is proposed to find a near-optimal solution of the transformed problem. Extensive simulation results show that our proposed approach outperforms the benchmarks in average network revenue, successfully serving probability, and resource consumption.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/abstract/document/10207691
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Service-Oriented_Network_Resource_Orch.pdf'
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
