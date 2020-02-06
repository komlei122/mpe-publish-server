# -*- coding: utf-8 -*-
"""
desc:自己用来对blog中文件夹、文件名中特殊不合法名称剔除
"""
import sys
import os

reload(sys)

sys.setdefaultencoding('utf8')


replace_syx={
        "(":"[",
        ")":"]",
        "（":"[",
        "）":"]",
        " ":"_",
        "&":"与",
}

def fix_name(name):
    """
    名称替换
    """
    new_name=name
    for item in replace_syx:
        if item in name:
            new_name=new_name.replace(item,replace_syx[item])
    if name==new_name:
        new_name=''
    return new_name

def rename_file(path_dir):
    """
    修改文件名字
    """
    for lists in os.listdir(path_dir):
        path_file = os.path.join(path_dir, lists)
        # 文件
        if os.path.isfile(path_file):
            file_name=os.path.basename(path_file)
            #  只对md格式文件编译
            if file_name[-3:] == '.md':
                new_name=fix_name(file_name)
                if new_name:
                    full_file_name=os.path.join(path_dir, file_name)
                    full_new_name=os.path.join(path_dir, new_name)
                    os.rename(full_file_name, full_new_name)
                    print "file_name:%s ||  new_name: %s "%(full_file_name,full_new_name)
        # 文件夹
        else:
            rename_file(path_file)

def rename_dir(path_dir):
    """
    修改文件夹名字
    """
    for lists in os.listdir(path_dir):
        path_file = os.path.join(path_dir, lists)
        # 文件
        if os.path.isfile(path_file):
            pass
            # file_name=os.path.basename(path_file)
            #  只对md格式文件编译
        # 文件夹
        else:
            final_name=os.path.basename(path_file)
            new_name=fix_name(final_name)
            if new_name:
                full_file_name=os.path.join(path_dir, final_name)
                full_new_name=os.path.join(path_dir, new_name)
                print "mv %s %s "%(full_file_name,full_new_name)
                os.rename(full_file_name, full_new_name)
            else:
                full_new_name=path_file
            rename_dir(full_new_name)


if __name__ == '__main__':
    root_dir = "../docs"
    rename_dir(os.path.abspath(root_dir))
    rename_file(os.path.abspath(root_dir))
