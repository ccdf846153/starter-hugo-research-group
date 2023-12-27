---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Dynamic Neural Network-Based Resource Management for Mobile Edge Computing in 6G Networks'
#按照实际情况填写
authors:
  - Longfei Ma
  - Nan Cheng
  - Conghao Zhou
  - Xiucheng Wang
  - Ning Lu
  - Ning Zhang
  - Khalid Aldubaikhy
  - Abdullah Alqasir
#论文发表时间 只更改年月日
date: '2023-12-25T00:00:00Z'
#doi号
doi: '10.48550/arXiv.2308.07511'
#同论文发表时间 只更改年月日
publishDate: '2023-12-25T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# 期刊/会议名称 要求全称
publication: 'IEEE Transactions on Cognitive Communications and Networking'
# 留空
publication_short: ''
# 文章摘要
abstract: Mobile edge computing (MEC) can be used to reduce the task delay for users with limited computing resources. However, in 6G networks, the diversity of tasks is greatly increased. For those extremely delay-sensitive small-size computing tasks, the inference delay of neural network (NN)-based algorithms such as resource allocation and task offloading cannot be ignored. As a hyperparameter, the inference cost of NN is usually difficult to adjust. Dynamic neural network (DyNN) is an emerging technique that improves the model efficiency by adjusting the network architecture on-demand according to the sample characteristics during inference. In this paper, we propose a DyNN-based resource management method for MEC that dynamically adjusts the depth and width of the NN according to the features of the task, improving computational efficiency and achieving a balance between inference delay and the management performance of computational and communication resources. Furthermore, to reduce the training cost of DyNN, a new training method is proposed in this paper, where all the blocks in DyNN are gradually trained in the order of size. Simulation results demonstrate that the proposed DyNN-based resource management method outperforms the traditional optimization algorithm and the static-NN-based method.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/document/10373580
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Dynamic_Neural_Network-Based_Resource_Management.pdf'
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
