---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Scalable Resource Management for Dynamic MEC: An Unsupervised Link-Output Graph Neural Network Approach'
#按照实际情况填写
#Ziyan Chen; Nan Cheng; Zhisheng Yin; Jingchao He; Ning Lu
authors:
  - Xiucheng Wang
  - Nan Cheng
  - Lianhao Fu
  - Wei Quan
  - Ruijin Sun
  - Yilong Hui
  - Tom Luan
  - Xuemin Shen
#论文发表时间 只更改年月日
date: '2023-07-15T00:00:00Z'
#doi号
doi: '10.48550/arXiv.2306.08938'
#同论文发表时间 只更改年月日
publishDate: '2023-07-15T00:00:00Z'

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
abstract: Deep learning has been successfully adopted in mobile edge computing (MEC) to optimize task offloading and resource allocation. However, the dynamics of edge networks raise two challenges in neural network (NN)-based optimization methods: low scalability and high training costs. Although conventional node-output graph neural networks (GNN) can extract features of edge nodes when the network scales, they fail to handle a new scalability issue whereas the dimension of the decision space may change as the network scales. To address the issue, in this paper, a novel link-output GNN (LOGNN)-based resource management approach is proposed to flexibly optimize the resource allocation in MEC for an arbitrary number of edge nodes with extremely low algorithm inference delay. Moreover, a label-free unsupervised method is applied to train the LOGNN efficiently, where the gradient of edge tasks processing delay with respect to the LOGNN parameters is derived explicitly. In addition, a theoretical analysis of the scalability of the node-output GNN and link-output GNN is performed. Simulation results show that the proposed LOGNN can efficiently optimize the MEC resource allocation problem in a scalable way, with an arbitrary number of servers and users. In addition, the proposed unsupervised training method has better convergence performance and speed than supervised learning and reinforcement learning-based training methods. The code is available at https://github.com/UNIC-Lab/LOGNN.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://arxiv.org/abs/2306.08938
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Scalable_Resource_Management_for_Dynamic_MEC_An_Unsupervised.pdf'
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
