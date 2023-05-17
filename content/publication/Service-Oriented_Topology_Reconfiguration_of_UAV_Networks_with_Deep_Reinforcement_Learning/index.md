---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'AI for UAV-Assisted IoT Applications A Comprehensive Review'
#按照实际情况填写
#Ziyan Chen; Nan Cheng; Zhisheng Yin; Jingchao He; Ning Lu
authors:
  - Ziyan Chen
  - Nan Cheng
  - Zhisheng Yin
  - Jingchao He
  - Ning Lu
#论文发表时间 只更改年月日
date: '2022-11-01T00:00:00Z'
#doi号
doi: '10.1109/WCSP55476.2022.10039281'
#同论文发表时间 只更改年月日
publishDate: '2023-2-15T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# 期刊/会议名称 要求全称
publication: '2022 14th International Conference on Wireless Communications and Signal Processing'
# 留空
publication_short: ''
# 文章摘要
abstract: The high mobility of UAVs makes it flexible to provide on-demand service function chains (SFCs) for users in a large geographic area where the terrestrial network is usually not available. Considering sequential and sparsely geographically distributed service requests, the UAV network topology should be dynamically adjusted to provide guaranteed quality of services. This is especially challenging since the UAV movement, data transmission, and virtual function deployment and computing are highly coupled. In this paper, we investigate the topology reconfiguring of UAV networks to construct SFCs by jointly programming multi-UAV trajectories intelligently. Specifically, the dynamic UAV-SFC construction problem is formulated to maximize the net benefit of constructing the SFC by optimizing the UAV trajectory. The net benefit is defined as the delayed benefit deducting energy consumption costs. Then, we propose a deep Q-network (DQN)-based algorithm for real-time decision-making of multi-UAV actions to program multi-UAV trajectories jointly. Simulation results show that our proposed approach of topology reconfiguration can significantly reduce the delay in completing services and save the energy consumption of UAVs.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/abstract/document/10039281
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Service-Oriented.pdf'
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
