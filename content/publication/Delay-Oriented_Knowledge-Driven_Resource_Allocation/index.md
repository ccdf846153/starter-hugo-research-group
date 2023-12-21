---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Delay-Oriented Knowledge-Driven Resource Allocation in SAGIN-Based Vehicular Networks'
#按照实际情况填写
authors:
  - Lei Huang
  - Ruijin Sun
  - Nan Cheng
  - Yilong Hui
  - Dandan Liang
#论文发表时间 只更改年月日
date: '2023-03-26T00:00:00Z'
#doi号
doi: '10.1109/WCNC55385.2023.10118888'
#同论文发表时间 只更改年月日
publishDate: '2023-03-26T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# 期刊/会议名称 要求全称
publication: '2023 IEEE Wireless Communications and Networking Conference (WCNC)'
# 留空
publication_short: ''
# 文章摘要
abstract: Space-air-ground integrated networks (SAGIN) have been envisioned as the promising and key network architecture for the 6G vehicular networks to provide seamless coverage for the connected vehicles. To access the most appropriate network quickly, this paper proposed a knowledge-driven network access approach, where the communication knowledge is explicitly integrated into neural networks, to deal with multiple tasks in SAGIN-based vehicular networks. Specifically, the formulated long-term network access problem is handled by asynchronous advantage actor-critic algorithm (A3C) in reinforcement learning. During this process, the space-time correlation knowledge is introduced to effectively reduce the action space in channel selection and the reward shaping exploiting the problem-specific communication and mathematical knowledge is adopted to solve the sparse reward problem in reinforcement learning. In addition, by modifying the sub-net learning rate of the A3C algorithm with experimental experience, this paper speeds up the network convergence speed by 1.5%. Numerical results also show that integrating knowledge into traditional deep reinforcement learning algorithm can improve the reward by 4%.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/abstract/document/10118888
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Delay-Oriented_Knowledge-Driven_Resource_Allocation.pdf'
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
