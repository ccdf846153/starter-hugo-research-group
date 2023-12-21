---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Label-free Deep Learning Driven Secure Access Selection in Space-Air-Ground Integrated Networks'
#按照实际情况填写
authors:
  - Zhaowei Wang
  - Zhisheng Yin
  - Xiucheng Wang
  - Nan Cheng
  - Yuan Zhang
  - Tom H. Luan
#论文发表时间 只更改年月日
date: '2023-08-23T00:00:00Z'
#doi号
doi: '10.48550/arXiv.2308.14348'
#同论文发表时间 只更改年月日
publishDate: '2023-08-23T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# 期刊/会议名称 要求全称
publication: 'IEEE Global Communications Conference'
# 留空
publication_short: ''
# 文章摘要
abstract: In Space-air-ground integrated networks (SAGIN), the inherent openness and extensive broadcast coverage expose these networks to significant eavesdropping threats. Considering the inherent co-channel interference due to spectrum sharing among multi-tier access networks in SAGIN, it can be leveraged to assist the physical layer security among heterogeneous transmissions. However, it is challenging to conduct a secrecy-oriented access strategy due to both heterogeneous resources and different eavesdropping models. In this paper, we explore secure access selection for a scenario involving multi-mode users capable of accessing satellites, unmanned aerial vehicles, or base stations in the presence of eavesdroppers. Particularly, we propose a Q-network approximation based deep learning approach for selecting the optimal access strategy for maximizing the sum secrecy rate. Meanwhile, the power optimization is also carried out by an unsupervised learning approach to improve the secrecy performance. Remarkably, two neural networks are trained by unsupervised learning and Q-network approximation which are both label-free methods without knowing the optimal solution as labels. Numerical results verify the efficiency of our proposed power optimization approach and access strategy, leading to enhanced secure transmission performance.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://arxiv.org/abs/2308.14348
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Label-free Deep Learning Driven Secure Access Selection in Space-Air-Ground Integrated Networks.pdf'
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
