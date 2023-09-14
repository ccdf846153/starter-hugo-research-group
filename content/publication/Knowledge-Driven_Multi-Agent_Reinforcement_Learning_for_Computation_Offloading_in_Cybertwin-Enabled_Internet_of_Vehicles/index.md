---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Knowledge-Driven Multi-Agent Reinforcement Learning for Computation Offloading in Cybertwin-Enabled Internet of Vehicles'
#按照实际情况填写
authors:
  - Ruijin Sun 
  - Xiao Yang
  - Nan Cheng
  - Xiucheng Wang
  - Changle Li
#论文发表时间 只更改年月日
date: '2023-08-04T00:00:00Z'
#doi号
doi: '10.48550/arXiv.2308.02603'
#同论文发表时间 只更改年月日
publishDate: '2023-08-04T00:00:00Z'

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
abstract: By offloading computation-intensive tasks of vehicles to roadside units (RSUs), mobile edge computing (MEC) in the Internet of Vehicles (IoV) can relieve the onboard computation burden. However, existing model-based task offloading methods suffer from heavy computational complexity with the increase of vehicles and data-driven methods lack interpretability. To address these challenges, in this paper, we propose a knowledge-driven multi-agent reinforcement learning (KMARL) approach to reduce the latency of task offloading in cybertwin-enabled IoV. Specifically, in the considered scenario, the cybertwin serves as a communication agent for each vehicle to exchange information and make offloading decisions in the virtual space. To reduce the latency of task offloading, a KMARL approach is proposed to select the optimal offloading option for each vehicle, where graph neural networks are employed by leveraging domain knowledge concerning graph-structure communication topology and permutation invariance into neural networks. Numerical results show that our proposed KMARL yields higher rewards and demonstrates improved scalability compared with other methods, benefitting from the integration of domain knowledge.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://arxiv.org/abs/2308.02603
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Knowledge-Driven_Multi-Agent_Reinforcement.pdf'
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
