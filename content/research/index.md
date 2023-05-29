---
title: My page
type: landing

sections:
  - block: markdown
    content:
      title: Gallery
      subtitle: ''
      text: <center><img src="./fangxiang/fl.png" width="30%" />&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<img src="./fangxiang/kg.png" width="30%" /><br/><font color="AAAAAA">001.jpg</font>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<font color="AAAAAA">002.jpg</font></center><br/>
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
