from bs4 import BeautifulSoup

import os
from typing import Literal, Union

# * PATH CONFIG
# material paths
NORMAL_ROOT_PATH = os.path.realpath('./materials')
AI_ROOT_PATH = os.path.realpath('./AI_materials')

# final html path
HTML_PATH = os.path.realpath(
    '../seminar_list/content.txt'
)

# dir path of template of components
TEMPLATE_PATH = os.path.realpath('./templates')

# path for actual html parser in browser, used for download links
PARSE_NORMAL_PATH = '/seminar/materials'
PARSE_AI_PATH = 'seminar/AI_materials'


button_display_order = {        # display at the front for small value
    'PPT': 0,
    'Link': 1,
    'Note': 2
}



def get_AI_material_info():

    ret_list = []

    material_dir_list = os.listdir(AI_ROOT_PATH)
    material_dir_list.sort(reverse=True)

    for material_dir in material_dir_list:

        date = f"{material_dir[0:4]}-{material_dir[4:6]}-{material_dir[6:8]}"
        material_path = os.path.join(AI_ROOT_PATH, material_dir)
        filename_list = os.listdir(material_path)
        material_file_list = list(filter(
            lambda x: x == 'sort.dic' or 
                     (x.endswith(('.pdf', '.ppt', 'pptx', 'txt')) and x.find('_') != -1)
        , filename_list))

        # get the presenter list and title
        material_list = []
        title_list = []
        sort_list = []
        for material_file in material_file_list:

            button_list = []

            if material_file == 'sort.dic':
                with open(os.path.join(material_path, material_file), 'r', encoding='utf-8') as sort_file:
                    sort_list = sort_file.readline().split(' ')
                    # print(sort_list)

            elif material_file.endswith(('.pdf', '.ppt', 'pptx', 'txt')):
                title = (
                    ''.join((material_file.split('_')[1:]))         # remove the presenter name
                ).split('.')[:-1][0]                                # remove the file extension
                if title in title_list:
                    continue
                else:
                    title_list.append(title)
                
                extension = (material_file.split('.')[-1])
                presenter_list = material_file.split('_')[0].split('】')[-1].split('-')

                if material_file.endswith(('.pdf', '.ppt', 'pptx')):
                    button_list.append({
                        'type': 'PPT',
                        'path': f"{PARSE_AI_PATH}/{material_dir}/{material_file}"
                    })
                elif material_file.endswith('.txt'):
                    button_list.append({
                        'type': 'Link',
                        'path': f"{PARSE_AI_PATH}/{material_dir}/{material_file}"
                    })

                material_list.append({
                    'date': date,
                    'presenters': presenter_list,
                    'title': title,
                    'extension': extension,
                    'buttons': button_list
                })
        
        ret_list.append((material_list, sort_list))

    return ret_list


def get_normal_material_info():

    ret_list = []

    material_dir_list = os.listdir(NORMAL_ROOT_PATH)
    material_dir_list.sort(reverse=True)

    for material_dir in material_dir_list:

        date = f"{material_dir[0:4]}-{material_dir[4:6]}-{material_dir[6:8]}"
        material_path = os.path.join(NORMAL_ROOT_PATH, material_dir)
        filename_list = os.listdir(material_path)
        material_file_list = list(filter(
            lambda x: x == 'sort.dic' or 
                     (x.endswith(('.pdf', '.ppt', 'pptx', 'txt')) and x.find('_') != -1)
        , filename_list))
        note_list = list(filter(
            lambda x: x.endswith(('.doc', '.docx')) and x.find('_') != -1
        , filename_list))

        # get the presenter list and title
        material_list = []
        title_list = []
        sort_list = []
        for material_file in material_file_list:

            button_list = []

            if material_file == 'sort.dic':
                with open(os.path.join(material_path, material_file), 'r', encoding='utf-8') as sort_file:
                    sort_list = sort_file.readline().split(' ')
                    # print(sort_list)
            
            elif material_file.endswith(('.pdf', '.ppt', 'pptx', 'txt')):
                title = (
                    ''.join((material_file.split('_')[1:]))         # remove the presenter name
                ).split('.')[:-1][0]                                # remove the file extension
                if title in title_list:
                    continue
                else:
                    title_list.append(title)
                
                extension = (material_file.split('.')[-1])
                presenter_list = material_file.split('_')[0].split('】')[-1].split('-')

                if material_file.endswith(('.pdf', '.ppt', 'pptx')):
                    button_list.append({
                        'type': 'PPT',
                        'path': f"{PARSE_NORMAL_PATH}/{material_dir}/{material_file}"
                    })
                elif material_file.endswith('.txt'):
                    button_list.append({
                        'type': 'Link',
                        'path': f"{PARSE_NORMAL_PATH}/{material_dir}/{material_file}"
                    })
                
                if (f"{title}_会议纪要.docx" in note_list) or (f"{title}_会议纪要.doc" in note_list):
                    button_list.append({
                        'type': 'Note',
                        'path': f"{PARSE_NORMAL_PATH}/{material_dir}/{title}_会议纪要.docx" if f"{title}_会议纪要.docx" in note_list else f"{PARSE_NORMAL_PATH}/{material_dir}/{title}_会议纪要.doc"
                    })

                material_list.append({
                    'date': date,
                    'presenters': presenter_list,
                    'title': title,
                    'extension': extension,
                    'buttons': button_list
                })
        
        sort_list = None if len(sort_list) == 0 else sort_list
        ret_list.append((material_list, sort_list))
    
    return ret_list


def txt_to_html(path: str, encoding: Union[str, None] = None) -> BeautifulSoup:

    with open(path, 'r', encoding=encoding) as file:
        soup = BeautifulSoup(file, 'html.parser')
    return soup


def set_seminar_table_html(info_list: list) -> BeautifulSoup:

    ret_html = table_head = txt_to_html(f"{TEMPLATE_PATH}\\seminar_table-head.txt", encoding='utf-8')
    table_row_temp = txt_to_html(f"{TEMPLATE_PATH}\\seminar_table-row.txt", encoding='utf-8')
    table_button_temp = txt_to_html(f"{TEMPLATE_PATH}\\seminar_table-button.txt", encoding='utf-8')

    ret_html.append(ret_html.new_tag('tbody'))

    # using `sort_list` to set display order in same seminar dir
    def material_sort_arg(sorted_list: list, kwd_list: list):
        # print(sorted_list, kwd_list)
        # print([[(kwd in x['presenters']) for x in sorted_list] for kwd in kwd_list])
        return [[(kwd in x['presenters']) for x in sorted_list].index(True) for kwd in kwd_list]

    # set the width of the title column, defined by trials
    title_width = lambda button_num: 93 - 8 * button_num

    table = ret_html.find('tbody')
    for material_list, sort_list in info_list:

        # sort the material list by the sort list if exists
        if sort_list is not None:
            material_list = [material_list[idx] for idx in material_sort_arg(material_list, sort_list)]
        for material in material_list:

            table_row = table_row_temp.__copy__()
            table_row.find('tr').attrs['class'] = "year-{}".format(material['date'].split('-')[0])

            table_row.find('span', {'class': 'seminar-date'}).string = material['date']
            table_row.find('span', {'class': 'seminar-presenter'}).string = '、'.join(material['presenters'])
            table_row.find('span', {'class': 'seminar-title'}).string = material['title']
            table_row.find('span', {'class': 'seminar-title'}).parent.attrs['style'].replace(
                'max-width: {width}%', 
                f"max-width: {title_width(len(material['buttons']))}%"
            )

            for button in sorted(material['buttons'], key=lambda x: button_display_order[x['type']]):
                table_button = table_button_temp.__copy__()
                table_button.find('a').attrs['href'] = button['path']
                table_button.find('a').string = button['type']

                table_row.find('td', {'class': 'seminar-topic'}).insert(-2, table_button)
            
            table.append(table_row)
    
    return ret_html
                
    
def set_html(normal_info: list, AI_info: list):

    container = txt_to_html(f"{TEMPLATE_PATH}\\seminar_container.txt", encoding='utf-8')

    normal_table = set_seminar_table_html(normal_info)
    AI_table = set_seminar_table_html(AI_info)

    container.find('table', {'id': 'normal-item-table-content'}).append(normal_table)
    container.find('table', {'id': 'ai-item-table-content'}).append(AI_table)

    return container  


def save_html(html: BeautifulSoup, path: str, encoding: Union[str, None] = None):

    with open(path, 'w', encoding=encoding) as file:
        file.write(str(html))


if __name__ == "__main__":

    normal_info = get_normal_material_info()
    AI_info = get_AI_material_info()

    html = set_html(normal_info, AI_info)
    save_html(html, HTML_PATH, encoding='utf-8')

