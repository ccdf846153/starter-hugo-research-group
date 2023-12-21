---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Spectral Efficient TSB Scheme With User Scheduling for FDD Massive MIMO Systems'
#按照实际情况填写
authors:
  - Tianbao Gao
  - Chen Liu
  - Yunchao Song
  - Zhisheng Yin
  - Huibin Liang
  - Nan Cheng
#论文发表时间 只更改年月日
date: '2023-09-01T00:00:00Z'
#doi号
doi: '10.1109/JIOT.2023.3311044'
#同论文发表时间 只更改年月日
publishDate: '2023-09-01T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# 期刊/会议名称 要求全称
publication: 'IEEE Internet of Things Journal'
# 留空
publication_short: ''
# 文章摘要
abstract: This paper proposes a two-stage beamforming (TSB) scheme with user scheduling for FDD massive MIMO. The developed TSB scheme designs the analog pre-beamformer and schedules the users using statistical channel state information (S-CSI), reducing the overhead of the pilot and the feedback. Particularly, in the one-ring local scattering channel model, the pre-beamformer design and user scheduling problem is formulated as a 0-1 quadratic constrained quadratic programming (QCQP), which is further linearized to a mixed integer linear programming (MILP). In the multiple scattering clusters channel model, we design the pre-beamformer and schedule the users based on graph theory, where the chromatic number of the equivalent matrix represents the minimum number of orthogonal pilots. Then, we propose an iterative beam selection and user scheduling (I-BSUS) scheme that approximates the minimum pilot constraint by the maximum vertex degree. Moreover, the net spectrum efficiency (NSE) is improved using a multi-user digital precoder, which depends on the effective instantaneous CSI (EI-CSI). Simulation results validate the superiority of the proposed scheme in enhancing the NSE over the existing schemes.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/abstract/document/10237313
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Spectral_Efficient_TSB_Scheme_With_User_Scheduling_for_FDD_Mass.pdf'
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
