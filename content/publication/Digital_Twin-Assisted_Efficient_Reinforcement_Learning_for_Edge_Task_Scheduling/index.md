---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Digital Twin-Assisted Efficient Reinforcement Learning for Edge Task Scheduling'
#按照实际情况填写
authors:
  - Xiucheng Wang
  - Longfei Ma
  - Haocheng Li
  - Zhisheng Yin
  - Tom. Luan
  - Nan Cheng
#论文发表时间 只更改年月日
date: '2022-08-25'
#doi号
doi: '10.1109/VTC2022-Spring54318.2022.9860495'
#同论文发表时间 只更改年月日
publishDate: '2022-08-25'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# 期刊/会议名称 要求全称
publication: ' 2022 IEEE 95th Vehicular Technology Conference: (VTC2022-Spring)'
# 留空
publication_short: ''
# 文章摘要
abstract: Task scheduling is a critical problem when one user offloads multiple different tasks to the edge server. When a user has multiple tasks to offload and only one task can be transmitted to server at a time, while server processes tasks according to the transmission order, the problem is NP-hard. However, it is difficult for traditional optimization methods to quickly obtain the optimal solution, while approaches based on reinforcement learning face with the challenge of excessively large action space and slow convergence. In this paper, we propose a Digital Twin (DT)-assisted RL-based task scheduling method in order to improve the performance and convergence of the RL. We use DT to simulate the results of different decisions made by the agent, so that one agent can try multiple actions at a time, or, similarly, multiple agents can interact with environment in parallel in DT. In this way, the exploration efficiency of RL can be significantly improved via DT, and thus RL can converges faster and local optimality is less likely to happen. Particularly, two algorithms are designed to made task scheduling decisions, i.e., DT-assisted asynchronous Q-learning (DTAQL) and DT-assisted exploring Q-learning (DTEQL). Simulation results show that both algorithms significantly improve the convergence speed of Q-learning by increasing the exploration efficiency.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/document/9860495
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Digital_Twin-Assisted_Efficient_Reinforcement_Learning_for_Edge_Task_Scheduling.pdf'
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
