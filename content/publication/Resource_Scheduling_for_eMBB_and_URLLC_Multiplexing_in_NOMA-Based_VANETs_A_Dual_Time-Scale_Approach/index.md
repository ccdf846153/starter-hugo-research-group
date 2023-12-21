---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Resource Scheduling for eMBB and URLLC Multiplexing in NOMA-Based VANETs: A Dual Time-Scale Approach'
#按照实际情况填写
authors:
  - Yujie Zhang
  - Nan Cheng
  - Yanpeng Dai
  - Zhisheng Yin
  - Wei Quan
  - Yi Zhou
  - Ning Zhang
#论文发表时间 只更改年月日
date: '2023-11-28T00:00:00Z'
#doi号
doi: '10.1109/TVT.2023.3337250'
#同论文发表时间 只更改年月日
publishDate: '2023-11-28T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# 期刊/会议名称 要求全称
publication: 'IEEE Transactions on Vehicular Technology'
# 留空
publication_short: ''
# 文章摘要
abstract: Enhanced mobile broadband (eMBB) and ultra-reliable low-latency communication (URLLC) are two critical services in vehicular networks. However, the presence of both services creates a difficult resource allocation problem due to their heterogeneous requirements. To address the challenge of simultaneously providing eMBB and URLLC services in vehicular networks, we propose a resource allocation approach that maximizes eMBB rate while ensuring that both URLLC latency and reliability requirements are satisfied. Our approach utilizes non-orthogonal multiple access (NOMA) technology, where the resource for eMBB services is allocated by slot and the traffic of URLLC service is accommodated using mini-slots. To solve this dual time-scale problem, we employ a dual decomposition and sub-gradient method to solve the power allocation and resource block assignment of eMBB services, while the Vogel's approximation method (VAM) and modified distribution method (MODI) are proposed to solve the URLLC resource allocation problem. Additionally, we present two low-complexity heuristic algorithms for the URLLC sub-problem. Simulation results indicate that our proposed approach surpasses baseline methods in terms of both eMBB rate and fairness.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/document/10329465
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Resource_Scheduling_for_eMBB_and_URLLC_Multiplexing.pdf'
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
