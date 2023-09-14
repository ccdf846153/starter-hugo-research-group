---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Knowledge-Driven Resource Allocation for D2D Networks: A WMMSE Unrolled Graph Neural Network Approach'
#按照实际情况填写
authors:
  - Hao Yang
  - Nan Cheng
  - Ruijin Sun
  - Wei Quan
  - Rong Chai
  - Khalid Aldubaikhy
  - Abdullah Alqasir
  - Xuemin Shen
#论文发表时间 只更改年月日
date: '2023-07-12T00:00:00Z'
#doi号
doi: '10.48550/arXiv.2307.05882'
#同论文发表时间 只更改年月日
publishDate: '2023-07-12T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# 期刊/会议名称 要求全称
publication: 'arXiv'
# 留空
publication_short: ''
# 文章摘要
abstract: This paper proposes an novel knowledge-driven approach for resource allocation in device-to-device (D2D) networks using a graph neural network (GNN) architecture. To meet the millisecond-level timeliness and scalability required for the dynamic network environment, our proposed approach incorporates the deep unrolling of the weighted minimum mean square error (WMMSE) algorithm, referred to as domain knowledge, into GNN, thereby reducing computational delay and sample complexity while adapting to various data distributions. Specifically, the aggregation and update functions in the GNN architecture are designed by utilizing the summation and power calculation components of the WMMSE algorithm, which leads to improved model generalization and interpretabiliy. Theoretical analysis of the proposed approach reveals its capability to simplify intricate end-to-end mappings and diminish the model exploration space, resulting in increased network expressiveness and enhanced optimization performance. Simulation results demonstrate the robustness, scalability, and strong performance of the proposed knowledge-driven resource allocation approach across diverse communication topologies without retraining. Our findings contribute to the development of efficient and scalable wireless resource management solutions for distributed and dynamic networks with strict latency requirements.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://arxiv.org/abs/2307.05882
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Knowledge-Driven_Resource_Allocation_for_D2D_Networks_A_WMMSE.pdf'
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
