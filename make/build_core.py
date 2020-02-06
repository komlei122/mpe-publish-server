# -*- coding: utf-8 -*-
"""
desc:调起mume_parse 解析markdown文件
"""
import sys
import os

reload(sys)

sys.setdefaultencoding('utf8')


def parse_build(path_file):
    full_cmd = run_cmd + path_file
    os.system(full_cmd)
    print(path_file + " has build to html file !")


def md_remove(path_file):
    os.remove(path_file)
    print(path_file + " has been removed !")


def search_file(path_dir, run_func):
    for lists in os.listdir(path_dir):
        path_file = os.path.join(path_dir, lists)
        # 文件
        if os.path.isfile(path_file):
            #  只对md格式文件编译
            if path_file[-3:] == u'.md':
                run_func(path_file)
        # 文件夹
        else:
            search_file(path_file, run_func)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        root_dir = sys.argv[1]
        js_file = sys.argv[2]
        node_cmd = sys.argv[3]
        # 包含node命令路径、执行核心编译的js代码
        run_cmd = "{node_cmd} {js_file} ".format(
            node_cmd=node_cmd, js_file=js_file)
        print("root_path is:" + root_dir)
        search_file(os.path.abspath(root_dir), parse_build)
        search_file(os.path.abspath(root_dir), md_remove)
    else:
        exit("参数有误编译停止")
