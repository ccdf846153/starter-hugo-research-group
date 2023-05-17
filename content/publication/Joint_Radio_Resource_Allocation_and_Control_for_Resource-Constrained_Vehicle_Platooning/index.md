---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Joint Radio Resource Allocation and Control for Resource-Constrained Vehicle Platooning'
#按照实际情况填写
authors:
  - Dayue Zhang
  - Nan Cheng
  - Ruijin Sun
  - Feng Lyu
  - Yilong Hui
  - Changle Li
#论文发表时间 只更改年月日
date: '2022-12-04T00:00:00Z'
#doi号
doi: '10.1109/GLOBECOM48099.2022.10000903'
#同论文发表时间 只更改年月日
publishDate: '2022-12-04T00:00:00Z'

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
abstract: Vehicle platooning is an effective way to improve the efficiency and safety of transportation systems, in which a group of vehicles maintains a moving pattern by minimizing the tracking error of each vehicle. In this paper, a joint optimiza tion of radio resource allocation for kinetic status information transmission and platoon control is considered under resource constrained conditions to maintain the targeted inter-vehicle spacing. The formulated problem is approximately solved by the decomposition method, where the radio resource allocation and the platoon control are considered alternatively in two stages. In the first stage, a tracking error based scheduling strategy is presented for radio resource allocation. In the second stage, the control inputs of each vehicle are optimized based on the model predictive control (MPC). Simulation results show that the proposed scheme can achieve the objective of platoon control while having a low tracking error compared with other scheduling strategies.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/abstract/document/10000903
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Joint_Radio.pdf'
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
