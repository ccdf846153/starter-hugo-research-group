---
title: Tour
date: 2022-10-24

type: landing

sections:
  - block: slider
    content:
      slides:
      - title: 空天地一体化网络
        content: \item 面向服务的空天地一体化异构异质网络资源调度策略  \item 基于数字孪生的天地一体化网络管理架构 \item 知识驱动的多场景按需服务支持技术


                
        align: left
        background:
          image:
            filename: coders.jpg
            filters:
              brightness: 0.7
          position: right
          color: '#666'
      - title: Lunch & Learn ☕️
        content: 'Share your knowledge with the group and explore exciting new topics together!'
        align: left
        background:
          image:
            filename: iov.png
            filters:
              brightness: 0.7
          position: center
          color: '#555'
      - title: World-Class Semiconductor Lab
        content: 'Just opened last month!'
        align: right
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
          text: Join Us
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

