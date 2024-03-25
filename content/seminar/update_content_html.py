import os

MATERIAL_ROOT_PATH = os.path.realpath('./materials')
HTML_PATH = os.path.realpath(
    os.path.join(MATERIAL_ROOT_PATH, '../../seminar_list/content.html')
)
print(HTML_PATH)


def get_material_list():
    
    ret_list = []

    material_dir_list = os.listdir(MATERIAL_ROOT_PATH)
    material_dir_list.sort(reverse=True)
    for material_dir in material_dir_list:

        material_path = os.path.join(MATERIAL_ROOT_PATH, material_dir)
        filename_list = os.listdir(material_path)
        material_file_list = list(filter(lambda x: x.endswith(('.pdf', '.ppt', 'pptx', 'txt', 'zip')) and x.find('_') != -1, filename_list))
        for material_file in material_file_list:
            presenter_list = material_file.split('_')[0].split('-')
            title = (
                ''.join((material_file.split('_')[1:]))         # remove the presenter name
            ).split('.')[:-1]                                   # remove the file extension
            if material_file.endswith('.txt'):
                material_type = 'Link'
            elif material_file.endswith('.zip'):
                material_type = 'ZIP'
            elif material_file.endswith(('.pdf', '.ppt', 'pptx')):
                material_type = 'PDF'
            else:
                raise ValueError(f'Unknown material type: {material_file}')
            ret_list.append((material_dir, presenter_list, title, material_file, material_type))
            print(ret_list[-1])
    # print(ret_list)
    return ret_list


def generate_html(html_text):
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="Access-Control-Allow-Origin" content="unicxidian.com" />
    <title>Document</title>
</head>
<body>
    <div class="universal-wrapper">
        <div class="row">
            <div class="col-lg-12">
                <!-- <div>
                    <input type="search" class="filter-search form-control form-control-sm" 
                        placeholder="Search..." autocapitalize="off" autocomplete="off" 
                        autocorrect="off" role="textbox" spellcheck="false"
                    />
                </div> -->
                <!-- <div class="form-row mb-4">
                    <div class="col-auto">
                        <input type="search" class="filter-search form-control form-control-sm" 
                            placeholder="Search..." autocapitalize="off" autocomplete="off" 
                            autocorrect="off" role="textbox" spellcheck="false"
                        />
                    </div>
                     <div class="col-auto">
                        <select class="pub-filters pubtype-select form-control form-control-sm" 
                            data-filter-group="pubtype"
                        >
                            <option value="*">Type</option>
                            <option value=".pubtype-1">
                                Conference paper
                            </option>
                            <option value=".pubtype-2">
                                Journal article
                            </option>
                        </select>
                    </div> 
                    <div class="col-auto">
                        <select class="pub-filters form-control form-control-sm" 
                            data-filter-group="year"
                        >
                            <option value="*">Date</option>
                            <option value=".year-2024">2024</option>
                            <option value=".year-2023">2023</option>
                            <option value=".year-2022">2022</option>
                            <option value=".year-2021">2021</option>
                        </select>
                    </div>
                </div> -->
                
                <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="Access-Control-Allow-Origin" content="unicxidian.com" />
    <title>Document</title>
</head>
<body>
    <div class="universal-wrapper">
        <div class="row">
            <div class="col-lg-12">
                <!-- <div>
                    <input type="search" class="filter-search form-control form-control-sm" 
                        placeholder="Search..." autocapitalize="off" autocomplete="off" 
                        autocorrect="off" role="textbox" spellcheck="false"
                    />
                </div> -->
                <!-- <div class="form-row mb-4">
                    <div class="col-auto">
                        <input type="search" class="filter-search form-control form-control-sm" 
                            placeholder="Search..." autocapitalize="off" autocomplete="off" 
                            autocorrect="off" role="textbox" spellcheck="false"
                        />
                    </div>
                     <div class="col-auto">
                        <select class="pub-filters pubtype-select form-control form-control-sm" 
                            data-filter-group="pubtype"
                        >
                            <option value="*">Type</option>
                            <option value=".pubtype-1">
                                Conference paper
                            </option>
                            <option value=".pubtype-2">
                                Journal article
                            </option>
                        </select>
                    </div> 
                    <div class="col-auto">
                        <select class="pub-filters form-control form-control-sm" 
                            data-filter-group="year"
                        >
                            <option value="*">Date</option>
                            <option value=".year-2024">2024</option>
                            <option value=".year-2023">2023</option>
                            <option value=".year-2022">2022</option>
                            <option value=".year-2021">2021</option>
                        </select>
                    </div>
                </div> -->
                
                <div id="container-publications" style="position: relative; left: -7.5%; font-size: 1rem; width: 115%;">
                    <div class="grid-sizer col-lg-12 isotope-item year-2024" 
                        style="position: absolute; top: 0px; width: 100%;">
                        <div class="pub-list-item view-citation" style="margin-bottom: 1rem; width: 100%;">
                            <table id="item-table-content" rules="none" align="center" style="width: 100%; font-size: 12pt;">
                                <tbody>
                                    {html_text}
                                </tbody>
                            </table>
                            <!-- <p> -->
                                
                                <!-- <a href="#" class="btn btn-outline-primary btn-page-header btn-sm js-cite-modal" 
                                    data-filename="/publication/value_matters_a_novel_value_of_information-based_resource_sche/cite.bib">
                                    Cite
                                </a>
                                <a class="btn btn-outline-primary btn-page-header btn-sm" href="https://doi.org/10.1109/TVT.2024.3355119" target="_blank" rel="noopener">DOI</a>
                                <a class="btn btn-outline-primary btn-page-header btn-sm" href="https://ieeexplore.ieee.org/document/10402048" target="_blank" rel="noopener">IEEE Link</a> -->
                            <!-- </p> -->
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
    """

def table_head(material_list):
    date_list = [material_tuple[0] for material_tuple in material_list]
    year_list = list(set([date[:4] for date in date_list]))
    year_list.sort(reverse=True)
    class_name = ' '.join([f'year-{year}' for year in year_list])
    return f"""
    <tr class="{class_name}">
        <td style="position: relative; width: 15%; text-align: center; padding-bottom: 0.2rem;">
            <span class="article-metadata li-cite-author" 
                style="width: 100%; text-align: center; font-weight: bold; font-size: 15pt;">
                <span>汇报日期</span>
            </span>
        </td>
        <td style="position: relative; width: 12%; text-align: center; padding-bottom: 0.2rem;">
            <span class="article-metadata li-cite-author" 
                style="width: 100%; text-align: center; font-weight: bold; font-size: 15pt;">
                <span>汇报人</span>
            </span>
        </td>
        <td style="position: relative; width: 73%; text-align: center; padding-bottom: 0.2rem;">
            <span class="article-metadata li-cite-author" 
                style="width: 100%; text-align: center; font-weight: bold; font-size: 15pt;">
                <span>汇报主题</span>
            </span>
        </td>
    </tr>
"""

def material_item_html(material_tuple):
    # material tuple: (date, presenter_list, title, material_file, 'Link'/'PPT')
    year_class = f'year-{(material_tuple[0])[:4]}'
    date_str = material_tuple[0]
    date_html_str = f'{date_str[0:4]}-{date_str[4:6]}-{date_str[6:8]}'
    presenter_html_str = '<span>' + \
        "</span>、<span>".join(material_tuple[1]) + \
        '</span>'
    relative_download_path = f"{material_tuple[0]}/{material_tuple[3]}"
    button_name = material_tuple[4]
    presentation_title = material_tuple[2][0]
    return (TABLE_ITEM := f"""
    <tr class="{year_class}">
        <td style="position: relative; width: 15%; text-align: center;">
            <span class="article-metadata li-cite-author" 
                style="width: 100%; text-align: center;">
                <span>{date_html_str}</span>
        </span>
        </td>
        <td style="position: relative; width: 12%; text-align: center;">
            <span class="article-metadata li-cite-author" 
                style="width: 100%; text-align: center;">
                {presenter_html_str}
            </span>
        </td>
        <td style="position: relative; width: 73%; text-align: left; vertical-align: middle;">
            <p style="display: inline-block; margin: 0;"
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            </p>
            <p style="display: inline-block; margin: 0;">
                <a class="btn btn-outline-primary btn-page-header btn-sm" 
                    href="/seminar/materials/{relative_download_path}" 
                    target="_blank" rel="noopener"
                    style="vertical-align: middle; margin-left: 1.5rem;">
                    {button_name}
                </a>
            </p>
            <p style="text-align: left; display: inline-block; width: 85%; vertical-align: middle;">
                <span>{presentation_title}</span>
            </p>
        </td>
    </tr>
    """)


if __name__ == '__main__':
    material_list = get_material_list()
    html_text = table_head(material_list)
    for material_tuple in material_list:
        html_text += material_item_html(material_tuple)
    html_text = generate_html(html_text)
    with open(HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(html_text)