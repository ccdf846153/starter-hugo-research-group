---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'DT-Assisted Multi-point Symbiotic Security in Space-air-ground Integrated Networks'
#按照实际情况填写
#Ziyan Chen; Nan Cheng; Zhisheng Yin; Jingchao He; Ning Lu
authors:
  - Zhisheng Yin
  - Nan Cheng
  - Tom H. Luan
  - Yunchao Song
  - Wei Wang
#论文发表时间 只更改年月日
date: '2023-09-08T00:00:00Z'
#doi号
doi: '10.1109/TIFS.2023.3313326'
#同论文发表时间 只更改年月日
publishDate: '2023-09-08T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# 期刊/会议名称 要求全称
publication: 'IEEE Transactions on Information Forensics and Security'
# 留空
publication_short: ''
# 文章摘要
abstract: In this paper, we investigate the secure transmission of multi-resource heterogeneous radio access networks (RANs) in space-air-ground integrated network (SAGIN) from the perspective of physical layer security. Considering the network heterogeneity, resource constrain, and channel similarity, it is challenging to implement the physical layer security in SAGIN. Particularly, digital twin (DT) is considered in the cyberspace of SAGIN to reflect the physical network entities (i.e., satellite, unmanned aerial vehicle (UAV), and terrestrial base station), which is assumed to comprehensively control and manage the heterogeneous RANs’ resources. To ensure secure transmissions of multi-tier heterogeneous downlink communications in SAGIN, a multi-point symbiotic security scheme is proposed through DT-assisted multi-dimensional domain synergy precoding, where the co-channel interference due to spectrum sharing among these heterogeneous RANs is recast to unevenly corrupt the main and wiretap channels of each legitimate user. Specifically, to realize the multi-point symbiotic security, a max-min problem is formulated to maximize the minimum secrecy rate of three heterogeneous downlinks. Since this problem is non-convex and challenging, a list of mathematical reformulations is derived and the successive convex approximation (SCA) based multi-dimensional domain synergy precoding algorithm is proposed to solve it. Moreover, the computational complexity of our proposed approach is analyzed and meaningful discussions are made. In addition, extensive simulations are carried out to evaluate the secrecy rate performance and verify the efficiency of our proposed approach.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/abstract/document/10244089
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './DT-Assisted_Multi-point_Symbiotic_Security_in_Space-air-ground_Integrated.pdf'
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
