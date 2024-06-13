---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Knowledge-Driven Resource Allocation for Wireless Networks: A WMMSE Unrolled Graph Neural Network Approach'
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
date: '2024-02-22T00:00:00Z'
#doi号
doi: '10.1109/JIOT.2024.3368516'
#同论文发表时间 只更改年月日
publishDate: '2024-02-22T00:00:00Z'

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
abstract: This article proposes a novel knowledge-driven approach for resource allocation in wireless networks using the graph neural network (GNN) architecture. To meet the millisecond-level timeliness and scalability required for the dynamic network environment, our proposed approach, named UWGNN, incorporates the deep unrolling of the weighted minimum mean-square error (WMMSE) algorithm, referred to as domain knowledge, into GNN, thereby reducing computational delay and sample complexity while adapting to various data distributions. Specifically, by unrolling the WMMSE algorithm into a series of interconnected submodules, UWGNN aligns closely with the optimization steps of the algorithm. Our analysis reveals the effectiveness of the deep unrolling method within UWGNN, which decomposes complicated end-to-end mappings, leading to a reduction in model complexity and parameter count. Experimental results demonstrate that UWGNN maintains optimal performance with computation latency 3–4 orders of magnitude lower than the WMMSE algorithm and exhibits strong performance and generalization across diverse data distributions and communication topologies without the need for retraining. Our findings contribute to the development of efficient and scalable wireless resource management solutions for distributed and dynamic networks with strict latency requirements.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/abstract/document/10443615
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Knowledge-Driven_Resource_Allocation_for_Wireless.pdf'
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
