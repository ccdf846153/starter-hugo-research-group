---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'RingSFL: An Adaptive Split Federated Learning Towards Taming Client Heterogeneity'
#按照实际情况填写
authors:
  - Jinglong Shen 
  - Nan Cheng 
  - Xiucheng Wang 
  - Feng Lyu 
  - Wenchao Xu
  - Zhi Liu
  - Khalid Aldubaikhy
  - Xuemin Shen
#论文发表时间 只更改年月日
date: '2023-08-30T00:00:00Z'
#doi号
doi: '10.1109/TMC.2023.3309633'
#同论文发表时间 只更改年月日
publishDate: '2023-08-30T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# 期刊/会议名称 要求全称
publication: 'IEEE Transactions on Mobile Computing'
# 留空
publication_short: ''
# 文章摘要
abstract: Federated learning (FL) has gained increasing attention due to its ability to collaboratively train while protecting client data privacy. However, vanilla FL cannot adapt to client heterogeneity, leading to a degradation in training efficiency due to stragglers, and is still vulnerable to privacy leakage. To address these issues, this paper proposes RingSFL, a novel distributed learning scheme that integrates FL with a model split mechanism to adapt to client heterogeneity while maintaining data privacy. In RingSFL, all clients form a ring topology. For each client, instead of training the model locally, the model is split and trained among all clients along the ring through a pre-defined direction. By properly setting the propagation lengths of heterogeneous clients, the straggler effect is mitigated, and the training efficiency of the system is significantly enhanced. Additionally, since the local models are blended, it is less likely for an eavesdropper to obtain the complete model and recover the raw data, thus improving data privacy. The experimental results on both simulation and prototype systems show that RingSFL can achieve better convergence performance than benchmark methods on independently identically distributed (IID) and non-IID datasets, while effectively preventing eavesdroppers from recovering training data.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/abstract/document/10234718
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './RingSFL_An_Adaptive_Split_Federated_Learning_Towards_Taming_Client_Heterogeneity.pdf'
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
