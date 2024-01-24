---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Value Matters: A Novel Value of Information-Based Resource Scheduling Method for CAVs'
#按照实际情况填写
authors:
  - Wei Wang
  - Nan Cheng
  - Mushu Li
  - Tingting Yang
  - Conghao Zhou
  - Changle Li
  - Fangjiong Chen
#论文发表时间 只更改年月日
date: '2024-01-17T00:00:00Z'
#doi号
doi: '10.1109/TVT.2024.3355119'
#同论文发表时间 只更改年月日
publishDate: '2024-01-17T00:00:00Z'

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
abstract: The Internet of Vehicles (IoV) can support applications in connected autonomous vehicles (CAVs), the implementation of which can effectively improve traffic efficiency. However, safety-related CAV applications have very strict requirements on the reliability and latency of each packet, which is difficult to achieve due to limited resources and the high dynamics of CAVs. In this paper, we investigate communication resource scheduling for remote autonomous driving (AD) to improve the performance of the remote control system when network resources are constrained. Specifically, we introduce a novel performance metric, i.e., value of information (VoI), to capture how sending a packet will affect the performance of CAV driving safety and efficiency, i.e., the value of the packet on the considered CAV system. The formulation of VoI is derived using the Lyapunov optimization method, and the lower-bound for the performance of the AD system with a VoI-based scheduling strategy is analyzed. Then, a communication resource scheduling approach is proposed based on the VoI of each packet. Simulation results demonstrate that the proposed VoI-based resource scheduling approach is capable of accurately assessing the impact of information transfer on system performance, while ensuring the CAV's safety and enhancing traffic efficiency.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/document/10402048
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Value_Matters_A_Novel_Value_of_Information-Based_Resource_Sche.pdf'
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
