---
# 请注意 任何参数（如摘要）值内出现的任何双引号（“）或反斜杠（如LaTeX\times）都应使用反斜杠（\）进行转义。例如，符号“和LaTeX text\times分别变为\”和\\times。有关详细信息，请参阅YAML或TOML文档。
#title：论文标题可以使用空格注意引号
title: 'RadioDiff: An Effective Generative Diffusion Model for Sampling-Free Dynamic Radio Map Construction'
#按照实际情况填写
authors:
  - Xiucheng Wang
  - Keda Tao
  - Nan Cheng
  - Zhisheng Yin
  - Zan Li
  - Yuan Zhang
#论文发表时间 只更改年月日
date: '2024-11-22T00:00:00Z'
#doi号
doi: '10.1109/TCCN.2024.3504489'
#同论文发表时间 只更改年月日
publishDate: '2024-11-22T00:00:00Z'

# 选填 1 或者 2 注意引号
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# 期刊/会议名称 要求全称
publication: 'IEEE Transactions on Cognitive Communications and Networking'
# 留空
publication_short: ''
# 文章摘要
abstract: Radio map (RM) is a promising technology that can obtain pathloss based on only location, which is significant for 6G network applications to reduce the communication costs for pathloss estimation. However, the construction of RM in traditional is either computationally intensive or depends on costly sampling-based pathloss measurements. Although the neural network (NN)-based method can efficiently construct the RM without sampling, its performance is still suboptimal. This is primarily due to the misalignment between the generative characteristics of the RM construction problem and the discrimination modeling exploited by existing NN-based methods. Thus, to enhance RM construction performance, in this paper, the sampling-free RM construction is modeled as a conditional generative problem, where a denoised diffusion-based method, named RadioDiff, is proposed to achieve high-quality RM construction. In addition, to enhance the diffusion model’s capability of extracting features from dynamic environments, an attention U-Net with an adaptive fast Fourier transform module is employed as the backbone network to improve the dynamic environmental features extracting capability. Meanwhile, the decoupled diffusion model is utilized to further enhance the construction performance of RMs. Moreover, a comprehensive theoretical analysis of why the RM construction is a generative problem is provided for the first time, from both perspectives of data features and NN training methods. Experimental results show that the proposed RadioDiff achieves state-of-the-art performance in all three metrics of accuracy, structural similarity, and peak signal-to-noise ratio. The code is available at https://github.com/UNIC-Lab/RadioDiff.

# 这些都留空 不要删除
summary:  
tags:
featured: false

links:
  - name: IEEE Link
        #这里替换成IEEE网站的链接
    url: https://ieeexplore.ieee.org/document/10764739
        #这里替换成文件夹中pdf的相对路径 应为'./xxxxx.pdf' 注意引号和反斜杠
url_pdf: './RadioDiff.pdf'
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
