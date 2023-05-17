---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Physical Layer Security in Cybertwin-Enabled Integrated Satellite-Terrestrial Vehicle Networks'
#按照实际情况填写
authors:
  - Zhisheng Yin
  - Nan Cheng*
  - Tom H. Luan
  - Ping Wang
#论文发表时间 只更改年月日
date: '2021-12-09T00:00:00Z'
#doi号
doi: '10.1109/TVT.2021.3133574'
#同论文发表时间 只更改年月日
publishDate: '2021-12-09T00:00:00Z'

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
abstract: In this paper, we investigate the secure vehicle communications in cybertwin-enabled integrated satellite-terrestrial networks, where the digital twins (DTs) in the cybertwin space reflects the physical entities (i.e., satellite, terrestrial base station (BS), and vehicles). Particularly, considering the channel similarity between different satellite links versus the randomness difference in terrestrial links, it is challenging to reach the secure transmission in satellite and terrestrial links independently with limited resources. Considering the information exchange in the cybertwin space can support an information sharing between such physical entities, the secure transmission design by using the heterogeneous satellite-terrestrial resources can be conducted from a global perspective. With the channel feedback information of vehicles gathered at the cybertwin, the co-channel interference caused by the spectrum sharing is leveraged to assist the implementation of secure transmissions in the integrated satellite-terrestrial vehicle network. Specifically, the problems of maximizing the secrecy rate of satellite-to-vehicle link and the terrestrial BS-to-vehicle link are formulated, respectively. To solve such two problems, we propose two corresponding beamforming optimization approaches, where semi-definite relaxation (SDR) and semi-definite programming (SDP) are adopted due to the non-convexity. In addition, the tightness of SDR is proved and the complexity of proposed approaches is also analyzed. Finally, extensive numerical simulations are carried out and results show the effectiveness of our proposed approach.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/abstract/document/9645156
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Physical.pdf'
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
