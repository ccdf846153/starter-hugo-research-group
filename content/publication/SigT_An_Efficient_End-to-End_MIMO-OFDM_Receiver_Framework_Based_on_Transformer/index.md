---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'AI for UAV-Assisted IoT Applications A Comprehensive Review'
#按照实际情况填写
authors:
  - Ziyou Ren
  - Nan Cheng
  - Ruijin Sun
  - Xiucheng Wang
  - Ning Lu
  - Wenchao Xu
#论文发表时间 只更改年月日
date: '2023-01-24T00:00:00Z'
#doi号
doi: '10.1109/ICCSPA55860.2022.10019001'
#同论文发表时间 只更改年月日
publishDate: '2023-01-24T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# 期刊/会议名称 要求全称
publication: '2022 5th International Conference on Communications, Signal Processing, and their Applications'
# 留空
publication_short: ''
# 文章摘要
abstract: Multiple-input multiple-output and orthogonal frequency-division multiplexing (MIMO-OFDM) are the key technologies in 4G and subsequent wireless communication systems. Conventionally, the MIMO-OFDM receiver is performed by multiple cascaded blocks with different functions and the algorithm in each block is designed based on ideal assumptions of wireless channel distributions. However, these assumptions may fail in practical complex wireless environments. The deep learning (DL) method has the ability to capture key features from complex and huge data. In this paper, a novel end-to-end MIMO-OFDM receiver framework based on transformer, named SigT, is proposed. By regarding the signal received from each antenna as a token of the transformer, the spatial correlation of different antennas can be learned and the critical zero-shot problem can be mitigated. Furthermore, the proposed SigT framework can work well without the inserted pilots, which improves the useful data transmission efficiency. Experiment results show that SigT achieves much higher performance in terms of signal recovery accuracy than benchmark methods, even in a low SNR environment or with a small number of training samples.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/document/10113154
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './AI_for_UAV-Assisted_IoT_Applications_A_Comprehensive_Review.pdf'
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
