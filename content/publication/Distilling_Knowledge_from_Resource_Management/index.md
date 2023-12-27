---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Distilling Knowledge from Resource Management Algorithms to Neural Networks: A Unified Training Assistance Approach'
#按照实际情况填写
authors:
  - Longfei Ma
  - Nan Cheng
  - Xiucheng Wang
  - Zhisheng Yin
  - Haibo Zhou
  - Wei Quan
#论文发表时间 只更改年月日
date: '2023-08-15T00:00:00Z'
#doi号
doi: '10.48550/arXiv.2308.07511'
#同论文发表时间 只更改年月日
publishDate: '2023-08-15T00:00:00Z'

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
abstract: As a fundamental problem, numerous methods are dedicated to the optimization of signal-to-interference-plus-noise ratio (SINR), in a multi-user setting. Although traditional model-based optimization methods achieve strong performance, the high complexity raises the research of neural network (NN) based approaches to trade-off the performance and complexity. To fully leverage the high performance of traditional model-based methods and the low complexity of the NN-based method, a knowledge distillation (KD) based algorithm distillation (AD) method is proposed in this paper to improve the performance and convergence speed of the NN-based method, where traditional SINR optimization methods are employed as "teachers" to assist the training of NNs, which are "students", thus enhancing the performance of unsupervised and reinforcement learning techniques. This approach aims to alleviate common issues encountered in each of these training paradigms, including the infeasibility of obtaining optimal solutions as labels and overfitting in supervised learning, ensuring higher convergence performance in unsupervised learning, and improving training efficiency in reinforcement learning. Simulation results demonstrate the enhanced performance of the proposed AD-based methods compared to traditional learning methods. Remarkably, this research paves the way for the integration of traditional optimization insights and emerging NN techniques in wireless communication system optimization.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://arxiv.org/abs/2308.07511
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Distilling_Knowledge_from_Resource_Management.pdf'
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
