---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'On-Demand Resource Management for 6G Wireless Networks Using Knowledge-Assisted Dynamic Neural Networks'
#按照实际情况填写
authors:
  - Longfei Ma
  - Nan Cheng
  - Xiucheng Wang
  - Ruijin Sun
  - Ning Lu
#论文发表时间 只更改年月日
date: '2022-05-16T00:00:00Z'
#doi号
doi: '10.1109/ICC45855.2022.9882279'
#同论文发表时间 只更改年月日
publishDate: '2022-05-16T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# 期刊/会议名称 要求全称
publication: 'ICC 2022 - IEEE International Conference on Communications'
# 留空
publication_short: ''
# 文章摘要
abstract: On-demand service provisioning is a critical yet challenging issue in 6G wireless communication networks, since emerging services have significantly diverse requirements and the network resources become increasingly heterogeneous and dynamic. In this paper, we study the on-demand wireless resource orchestration problem with the focus on the computing delay in orchestration decision-making process. Specifically, we take the decision-making delay into the optimization problem. Then, a dynamic neural network (DyNN)-based method is proposed, where the model complexity can be adjusted according to the service requirements. We further build a knowledge base representing the relationship among the service requirements, available computing resources, and the resource allocation performance. By exploiting the knowledge, the width of DyNN can be selected in a timely manner, further improving the performance of orchestration. Simulation results show that the proposed scheme significantly outperforms the traditional static neural network, and also shows sufficient flexibility in on-demand service provisioning.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/document/9882279
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './On-Demand_Resource_Management_for_6G_Wireless_Networks.pdf'
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
