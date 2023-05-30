---
title: My page
type: landing

sections:
  - block: markdown
    content:
      title: 研究方向
      subtitle: ''
      text: <table rules="none" align="center"><tr><td><center><img src="./fangxiang/fl.png" width="250%" /><br/><font color="AAAAAA">研究方向1</font></center></td><td><center><img src="./fangxiang/kg.png" width="250%" ><br/><font color="AAAAAA">研究方向2</font></center></td><td><center><img src="./fangxiang/ktd.png" width="250%" /><br/><font color="AAAAAA">研究方向3</font></center></td><td><center><img src="./fangxiang/v2x.png" width="250%" /><br/><font color="AAAAAA">研究方向4</font></center></tr></table>
    design:
      columns: '1'
  - block: collection
    content:
      title: <div style="margin-bottom:1em; margin-top:-0.5em;"><a href="../work/" style="color:black; text-decoration:inherit;">科研成果</a></div>
      # Choose how many pages you would like to display (0 = all pages)
      count: 3
      # Filter on criteria
      filters:
        # The folders to display content from
        folders:
          - work
        author: ""
        category: ""
        tag: ""
        publication_type: ""
        featured_only: false
        exclude_featured: false
        exclude_future: false
        exclude_past: false
      # Choose how many pages you would like to offset by
      # Useful if you wish to show the first item in the Featured widget
      offset: 0
      # Field to sort by, such as Date or Title
      sort_by: 'content_id'
      sort_ascending: true

    design:
      # Choose a listing view
      view: Showcase
      # Choose single or dual column layout
      columns: '1'
      flip_alt_rows: false
---
