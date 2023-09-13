---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Effectively Heterogeneous Federated Learning: A Pairing and Split Learning Based Approach'
#按照实际情况填写
authors:
  - Jinglong Shen
  - Xiucheng Wang
  - Nan Cheng
  - Longfei Ma
  - Conghao Zhou
  - Yuan Zhang
#论文发表时间 只更改年月日
date: '2023-08-26T00:00:00Z'
#doi号
doi: '10.48550/arXiv.2308.13849'
#同论文发表时间 只更改年月日
publishDate: '2023-08-26T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# 期刊/会议名称 要求全称
publication: 'arXiv'
# 留空
publication_short: ''
# 文章摘要
abstract: As a promising paradigm federated Learning (FL) is widely used in privacy-preserving machine learning, which allows distributed devices to collaboratively train a model while avoiding data transmission among clients. Despite its immense potential, the FL suffers from bottlenecks in training speed due to client heterogeneity, leading to escalated training latency and straggling server aggregation. To deal with this challenge, a novel split federated learning (SFL) framework that pairs clients with different computational resources is proposed, where clients are paired based on computing resources and communication rates among clients, meanwhile the neural network model is split into two parts at the logical level, and each client only computes the part assigned to it by using the SL to achieve forward inference and backward training. Moreover, to effectively deal with the client pairing problem, a heuristic greedy algorithm is proposed by reconstructing the optimization of training latency as a graph edge selection problem. Simulation results show the proposed method can significantly improve the FL training speed and achieve high performance both in independent identical distribution (IID) and Non-IID data distribution.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://arxiv.org/abs/2308.13849
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Effectively_Heterogeneous_Federated_Learning_A_Pairing_and_Split_Learning.pdf'
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
