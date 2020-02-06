# -*- coding: utf-8 -*-
"""
desc:拷贝docs下的文件到release/books下，并为每个文件夹创建对应的index.html
"""
import time
import sys
import os
from shutil import copyfile

reload(sys)

sys.setdefaultencoding('utf8')

# --------------------------------------------------HTML模版-------------------------------------------------------------------------
index_html_model_head = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title> Read Index </title>
  <style type="text/css">
        table
        {
            border-collapse: collapse;
            margin: 0 auto;
            text-align: left;
        }
        table td, table th
        {
            border: 1px solid #cad9ea;
            color: #666;
            height: 30px;
        }
        table thead th
        {
            background-color: #CCE8EB;
            width: 100px;
        }
        table tr:nth-child(odd)
        {
            background: #fff;
        }

        table tr:nth-child(even)
        {
            background: #F5FAFA;
        }
    </style>
 </head>
 """

index_html_model_body = """
 <body>
     <img src="https://www-eu.apache.org/icons/back.gif" alt="[PARENTDIR]"/> <a href="{parent_dir}">Parent Directory</a>
  <table width="90%" class="table">
   <caption>
    <h2> Index of {title} </h2>
    <br>
   </caption>
   <thead>
    <tr>
     <th> Name </th>
     <th> Last modified </th>
     <th> Description </th>
    </tr>
   </thead>
   <tbody>
     {line_infos}
   </tbody>
  </table>
 </body>
</html>
"""

line_info = """
<tr>
    <td> <img src="https://www-eu.apache.org/icons/folder.gif" alt="[DIR]" /> <a href="{path}">{name}/</a> </td>
    <td> {mtime} </td>
    <td> - </td>
</tr>
"""

index_ignore = ['_images', '_core_data', '.images', 'image', '.core_data']


# ----------------------------------------------------------------------------------------------------------------------------------

def advance_copy(source_dir, dist_dir):
    """
    :param source_dir: "./docs"
    :param dist_dir:  "./release/books"
    :return:
    """
    # 递归调用生成root子目录得index、并copy src的文件
    for file in os.listdir(source_dir):
        src_path_file = os.path.join(source_dir, file)
        dist_path_file = os.path.join(dist_dir, file)

        # 判断是文件、文件夹：
        # 1、文件
        if os.path.isfile(src_path_file):
            copyfile(src_path_file, dist_path_file)
        # 2、文件夹
        else:
            # 创建文件夹
            os.makedirs(dist_path_file)
            cur_dir_name = os.path.basename(src_path_file)
            # 对非如下类型文件夹创建index.md
            if cur_dir_name not in index_ignore:
                deep_build_index(dist_path_file, src_path_file)
            # 递归调用
            advance_copy(src_path_file, dist_path_file)


def deep_build_index(dist_path_file, src_path_file, index_file_name='index.html'):
    """
    创建当前dir的index.md文件，内容为下一层得文件
    :param index_file_name:
    :param dist_path_file: 目标路径
    :param src_path_file: 原始路径
    :return:
    """
    # 给文件夹创建index
    index_file = open(os.path.join(dist_path_file, index_file_name), 'w')
    parent_name = os.path.basename(src_path_file)
    # 只遍历一层
    true_line_infos = []
    for deep_file_name in os.listdir(src_path_file):
        abs_deep_file_name = os.path.join(src_path_file, deep_file_name)
        # 1、子file是markdown文件
        if os.path.isfile(abs_deep_file_name) and abs_deep_file_name[-3:] == '.md':
            may_index_name = os.path.basename(abs_deep_file_name)
            path = may_index_name.replace(".md", ".html")
            name = may_index_name.replace(".md", "")
            mtime = os.path.getmtime(abs_deep_file_name)
            mtime_str = time.strftime("%Y-%m-%d\t%H:%M:%S", time.localtime(mtime))
            true_line_info = line_info.format(path=path, name=name, mtime=mtime_str)
            true_line_infos.append(true_line_info)
        # 2、不再重复遍历刚生成的index.md文件
        elif os.path.isfile(abs_deep_file_name) and abs_deep_file_name[-8:] == index_file_name:
            pass
        # 3、子file是目录
        elif os.path.isdir(abs_deep_file_name) and deep_file_name not in index_ignore:
            path = os.path.join(deep_file_name, index_file_name)
            name = path.replace("/" + index_file_name, "")
            mtime = os.path.getmtime(abs_deep_file_name)
            mtime_str = time.strftime("%Y-%m-%d\t%H:%M:%S", time.localtime(mtime))
            true_line_info = line_info.format(path=path, name=name, mtime=mtime_str)
            true_line_infos.append(true_line_info)
    # 创建的html完整内容写入index文件
    if true_line_infos:
        line_infos_str = "\n".join(true_line_infos)
        index_html = index_html_model_head + index_html_model_body.format(title=parent_name, parent_dir='../index.html',
                                                                          line_infos=line_infos_str)
        index_file.write(index_html)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        src_dir = sys.argv[1]
        dist_dir = sys.argv[2]
        # root 目录需要单独调用一次创建index
        deep_build_index(dist_dir, src_dir)
        # 递归创建
        advance_copy(os.path.abspath(src_dir), os.path.abspath(dist_dir))
    else:
        exit("参数有误编译停止")
