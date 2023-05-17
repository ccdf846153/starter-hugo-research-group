---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'UAV-Assisted Physical Layer Security in Multi-Beam Satellite-Enabled Vehicle Communications'
#按照实际情况填写
authors:
  - Zhisheng Yin
  - Min Jia
  - Nan Cheng
  - Wei Wang
  - Feng Lyu
  - Qing Guo
  - Xuemin Shen
#论文发表时间 只更改年月日
date: '2021-06-23T00:00:00Z'
#doi号
doi: '10.1109/TITS.2021.3090017'
#同论文发表时间 只更改年月日
publishDate: '2021-06-23T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# 期刊/会议名称 要求全称
publication: 'IEEE Transactions on Intelligent Transportation Systems'
# 留空
publication_short: ''
# 文章摘要
abstract: In this paper, we investigate unmanned aerial vehicle (UAV) assisted physical layer security in multi-beam satellite enabled vehicle communications. Particularly, the UAV is exploited as a relay to improve the secure satellite-to-vehicle link, and simultaneously serves as a jammer by deliberately generating artificial noise (AN) to confuse Eve. The satellite beamforming (BF) and UAV power allocation (PA) are jointly optimized to maximize the secrecy rate of the legitimate user within a target beam while guaranteeing the quality of service (QoS) of users within other beams. Since the problem is nonconvex, we first convert it into an equivalent two-stage problem. Then, the outer-stage problem is solved by using one-dimensional search, and the inner-stage problem is transformed to a bi-convex problem by using the semi-definite relaxation (SDR) and Charnes Cooper transformation. To solve the inner-stage bi-convex problem, we propose an iterative alternating optimization algorithm, where the optimal BF is obtained by semi-definite programming (SDP), and the optimal UAV PA is subsequently obtained by solving the reformulated fractional programming problem with an iterative Dinkelbach method. The tightness of SDR and the complexity of our proposed approach are analyzed, and extensive simulations are carried out to evaluate the effectiveness of our proposed approach.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/document/9463880
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './UAV-Assisted.pdf'
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
