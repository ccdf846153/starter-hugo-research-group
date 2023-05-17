---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Optimal Charging Profile Design for Solar-Powered Sustainable UAV Communication Networks'
#按照实际情况填写
authors:
  - Longxin Wang
  - Tripathi Saugat 
  - Nan Cheng
  - Zhisheng Yin
  - Miao Wang
#论文发表时间 只更改年月日
date: '2023-02-01T00:00:00Z'
#doi号
doi: '10.48550/arXiv.2302.06092'
#同论文发表时间 只更改年月日
publishDate: '2023-02-01T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# 期刊/会议名称 要求全称
publication: 'IEEE International Conference on Communications'
# 留空
publication_short: ''
# 文章摘要
abstract: This work studies optimal solar charging for solar-powered self-sustainable UAV communication networks, considering the day-scale time-variability of solar radiation and user service demand. The objective is to optimally trade off between the user coverage performance and the net energy loss of the network by proactively assigning UAVs to serve, charge, or land. Specifically, the studied problem is first formulated into a time-coupled mixed-integer non-convex optimization problem, and further decoupled into two sub-problems for tractability. To solve the challenge caused by time-coupling, deep reinforcement learning (DRL) algorithms are respectively designed for the two sub-problems. Particularly, a relaxation mechanism is put forward to overcome the "dimension curse" incurred by the large discrete action space in the second sub-problem. At last, simulation results demonstrate the efficacy of our designed DRL algorithms in trading off the communication performance against the net energy loss, and the impact of different parameters on the tradeoff performance.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ui.adsabs.harvard.edu/abs/2023arXiv230206092W/abstract
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Optimal.pdf'
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
