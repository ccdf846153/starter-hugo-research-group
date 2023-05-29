---
title: My page
type: landing

sections:
  - block: markdown
    content:
      title:
      subtitle: ''
      text: <div class="row">
<a href="https://github.com/wowchemy/wowchemy-hugo-modules" target="_blank" rel="noopener">wowchemy/wowchemy-hugo-modules</a>
<img src=https://img.shields.io/github/stars/wowchemy/wowchemy-hugo-modules.svg alt="Github stars" title="Github stars"/>
<img src=https://img.shields.io/github/languages/top/wowchemy/wowchemy-hugo-modules.svg alt="Language" title="Language"/>
<img src=https://img.shields.io/github/v/tag/wowchemy/wowchemy-hugo-modules.svg?sort=semver alt="Last Tag" title="Last Tag"/>
<img src=https://img.shields.io/github/last-commit/wowchemy/wowchemy-hugo-modules.svg alt="Last Commit" title="Last Commit"/>
</div>
    design:
      columns: '1'
    
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen
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
