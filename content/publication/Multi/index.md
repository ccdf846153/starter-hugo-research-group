---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Multi-domain Resource Multiplexing Based Secure Transmission for Satellite-Assisted IoT: AO-SCA Approach'
#按照实际情况填写
authors:
  - Yin Zhisheng
  - Cheng Nan
  - Hui Yilong
  - Wang Wei
  - Zhao Lian
  - Aldubaikhy Khalid
  - Alqasir Abdullah
#论文发表时间 只更改年月日
date: '2023-03-06T00:00:00Z'
#doi号
doi: ''
#同论文发表时间 只更改年月日
publishDate: '2023-03-06T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# 期刊/会议名称 要求全称
publication: 'IEEE Transactions on Wireless Communications'
# 留空
publication_short: ''
# 文章摘要
abstract: Due to the wireless broadcasting and broad coverage in satellite-supported Internet of things (IoT) networks, the IoT nodes are susceptible to eavesdropping threats. Considering the distance difference between satellite and nearby destinations is negligible, the main and wiretapping channels between satellite and IoT node are similar, it poses great challenges to reach physical layer security in satellite-assisted IoT networks. In this paper, to guarantee secure transmissions for satellite-assisted IoT downlink communications, the multi-domain resource multiplexing based secure approach is proposed. Particularly, the self-induced co-channel interference between adjacent nodes is leveraged to increase the difference of signal transmission quality over both main and wiretapping channels. By comprehensively optimizing multi-domain resources, i.e., frequency, power, and spatial domains, secure transmissions from satellite to IoT nodes are reached. Specifically, the problem to maximize the sum secrecy rate of IoT nodes is formulated with a constraint of common communication rate of IoT nodes. To solve this non-convex problem, an alternating optimization (AO) algorithm with two inner successive convex approximation (SCA) algorithms are executed to solve the power allocation, spectral multiplexing, and precoding. In addition, simulation results are carried out to evaluate the secrecy rate performance and verify the efficiency of our proposed approach.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/abstract/document/10061450/keywords#keywords
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Multi.pdf'
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
