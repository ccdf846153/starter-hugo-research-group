---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Load-Aware Network Resource Orchestration in LEO Satellite Network: A GAT-Based Approach'
#按照实际情况填写
authors:
  - Jingchao He
  - Nan Cheng
  - Zhisheng Yin
  - Haibo Zhou
  - Conghao Zhou
  - Khalid Aldubaikhy
  - Abdullah Alqasir
  - Xuemin Sherman Shen
#论文发表时间 只更改年月日
date: '2024-01-10T00:00:00Z'
#doi号
doi: '10.1109/JIOT.2024.3350072'
#同论文发表时间 只更改年月日
publishDate: '2024-01-10T00:00:00Z'

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
abstract: As an integral component of the space-air-ground integrated network (SAGIN), the low Earth orbit (LEO) satellite network has displayed immense potential in providing ubiquitous connectivity and broadband mobile communication. However, the intrinsic dynamics of LEO satellites pose unprecedented challenges in network management and service delivery. In this paper, we investigate the service function chain (SFC) orchestration in dynamic LEO satellite networks to achieve flexible and efficient service provision. Considering the service requirements and the limitations of network resources, we formulate the SFC orchestration problem as the integer nonlinear programming (INLP) problem for maximizing the service acceptance and the load fairness of satellites. Then, an efficient heuristic algorithm is proposed to solve this problem. Addressing the situation with frequent service requests, a graph attention network (GAT)-based approach with low complexity is also presented. Simulation results demonstrate that our proposed approaches outperform the benchmarks by a substantial margin in terms of load fairness and service acceptance. Besides, the proposed GAT-based approach shows its advantage in computation complexity, and exhibits robustness in unstable network scenarios with intermittent link interruptions.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/document/10387448
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Load-Aware_Network_Resource_Orchestration_in_LEO_Satellite_Network_A_GAT-Based_Approach.pdf'
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
