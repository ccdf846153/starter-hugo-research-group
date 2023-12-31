---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'AoI-Oriented Context-Aware Priority Design and Vehicle Scheduling Strategy in Vehicular Networks'
#按照实际情况填写
authors:
  - Qiu Zhang
  - Nan Cheng
  - Ruijin Sun
  - Dayue Zhang
#论文发表时间 只更改年月日
date: '2022-08-11T00:00:00Z'
#doi号
doi: '10.1109/ICCCWorkshops55477.2022.9896680'
#同论文发表时间 只更改年月日
publishDate: '2022-10-04T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# 期刊/会议名称 要求全称
publication: 'IEEE International Conference on Communications in China Workshops'
# 留空
publication_short: ''
# 文章摘要
abstract: Real-time status updates are playing a key role in the emergence of autonomous driving. Due to the limited and dynamic environment, the vehicle communications may not guarantee the required quality of service (QoS) on demand. In this paper, we consider the intersection scenario with relatively heavy traffic and slightly higher risk, where the base station (BS) remotely controls multiple vehicles. The vehicles sense their own and surrounding contextual information through sensors and send them to the BS through the uplink. Since the urgency of different status information is distinct, the analytic hierarchy process (AHP) method is used to give each status information a context-aware weight so that emergency vehicles can be scheduled first by the BS. Then, age of information (AoI) is also exploited to describe the time elapsed since the generation of the status information obtained from the perspective of the BS. On this basis, the Lyapunov method is considered to optimize the average weighted AoI subject to the limited throughput constraint. Finally, a scheduling strategy based on dynamic domain value is proposed to update vehicles in real time in the long run, so as to minimize the average weighted AoI. The simulation results show that the context-aware weight proposed in this paper has a significant impact on scheduling, and the average weighted AoI of the whole system is optimized compared with other approaches.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/document/9896680
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './AoI-Oriented_Context-Aware_Priority_Design_and_Vehicle_Scheduling_Strategy_in_Vehicular_Networks.pdf'
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
