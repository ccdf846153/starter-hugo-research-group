---
title: Tour
date: 2022-10-24

type: landing

sections:
  - block: slider
    content:
      slides:
      - title: 空天地一体化网络
        content:  面向服务的空天地一体化异构异质网络资源调度策略 <br> 基于数字孪生的天地一体化网络管理架构


                
        align: left
        background:
          image:
            filename: coders.jpg
            filters:
              brightness: 0.7
          position: right
          color: '#666'
      - title: 车联网
        content:  面向自动驾驶任务的网络资源调度<br> 基于信息价值的多维资源协同调度<br> 车联网中视频流的自适应配置传输
        align: left
        background:
          image:
            filename: iov.png
            filters:
              brightness: 0.7
          position: center
          color: '#555'
      - title: 智能网络
        content: 分布式大模型训练与推理<br> 分布式韧性智能图计算<br> 可信高效联邦学习框架<br> 数字孪生辅助的快速强化学习
        align: left
        background:
          image:
            filename: ai.png
            filters:
              brightness: 0.5
          position: center
          color: '#333'
        link:
          icon: graduation-cap
          icon_pack: fas
          text: 加入我们
          url: ../contact/
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: '500px'
      is_fullscreen: false
      # Automatically transition through slides?
      loop: true
      # Duration of transition between slides (in ms)
      interval: 2000

  - block: portfolio

    # This file represents a page section.
    headless: false

    # Order that this section appears on the page.
    weight: 20

    title: 新闻


    content:
      # Page type to display. E.g. project.
      page_type: post

      # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
      filter_default: 0

    design:
      columns: '1'
      view: masonry
      flip_alt_rows: true
      background: {}
      #spacing: {padding: [0, 0, 0, 0]}
---

