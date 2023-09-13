---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'Interpretable and Secure Trajectory Optimization for UAV-Assisted Communication'
#按照实际情况填写
authors:
  - Yunhao Quan
  - Nan Cheng
  - Xiucheng Wang
  - Jinglong Shen
  - Longfei Ma
  - Zhisheng Yin
#论文发表时间 只更改年月日
date: '2023-09-05T00:00:00Z'
#doi号
doi: '10.1109/ICCC57788.2023.10233369'
#同论文发表时间 只更改年月日
publishDate: '2023-09-05T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# 期刊/会议名称 要求全称
publication: '2023 IEEE/CIC International Conference on Communications in China (ICCC)'
# 留空
publication_short: ''
# 文章摘要
abstract: Unmanned aerial vehicles (UAVs) have gained popularity due to their flexible mobility, on-demand deployment, and ability to establish line-of-sight wireless communication. However, existing UAV-assisted communication schemes often overlook the critical issue of collision avoidance during UAV flight. This paper proposes an interpretable UAV-assisted communication scheme that addresses this challenge through decomposition into two sub-problems. The first sub-problem involves constrained UAV coordinates and power allocation, solved using the Dueling Double DQN (D3QN) method. The second sub-problem deals with constrained UAV collision avoidance and trajectory optimization, addressed through the Monte Carlo tree search (MCTS) method. This approach ensures reliable and efficient UAV operation. To enhance the transparency and reliability of system decisions, a scalable explainable artificial intelligence (XAI) framework is proposed. The interpretability of the scheme generates explainable and trustworthy results, facilitating comprehension, validation, and control of UAV-assisted communication solutions. Extensive experiments demonstrate the superiority of the proposed algorithm in terms of performance and generalization compared to existing techniques. The proposed model improves the reliability, efficiency, and safety of UAV-assisted communication systems, offering a promising solution for future applications.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/abstract/document/10233369
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './Interpretable_and_Secure_Trajectory_Optimiza.pdf'
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
