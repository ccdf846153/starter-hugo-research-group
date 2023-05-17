---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Delay-Oriented Caching Strategies in D2D Mobile Networks'
#按照实际情况填写
authors:
  - Ruijin Sun
  - Ying Wang
  - Ling Lyu
  - Nan Cheng
  - Shan Zhang
  - Tingting Yang
  - Xuemin Shen
#论文发表时间 只更改年月日
date: '2020-05-21T00:00:00Z'
#doi号
doi: '10.1109/TVT.2020.2996238'
#同论文发表时间 只更改年月日
publishDate: '2020-05-21T00:00:00Z'

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
abstract: Caching-enabled device-to-device (D2D) networks have the potential to make mobile users directly fetch requested files from nearby users, resulting in low network delay. In addition, user mobility can increase the communication chances among different users, and therefore, the network delay can be further effectively reduced by proper designing the caching strategy. In this paper, mobility-aware caching strategies in D2D networks are studied to minimize the network delay. Specifically, based on the inter-contact user mobility model, the expression of the average file delivery delay is analytically obtained. Considering the limited cache capacity, a delay minimization cache placement problem considering the user mobility is investigated. To optimally solve this nonlinear integer programming problem, we reformulate it as a multistage decision problem. According to the recursive relationship between adjacent stages, dynamic programming is adopted to obtain the optimal mobility-aware caching strategy stage-by-stage. Furthermore, to lower the complexity, we also demonstrate that the original problem can be recasted as a monotone submodular function maximization problem over a matroid constraint. Then, a low-complexity greedy mobility-aware caching strategy with (1-1/e)-optimality performance guarantee is put forward. Numerical results show that, in the scenario with high user mobility, the file delivery delay can be reduced by 47% with our proposed mobility-aware caching strategy, as compared with the most popular caching. Furthermore, the superiority of the proposed caching strategy is verified by real-world data set.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/document/9097928
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Delay-Oriented_Caching_Strategies_in_D2D_Mobile_Networks.pdf'
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
