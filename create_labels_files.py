# -*-coding:utf-8-*-
"""
    @Project: googlenet_classification
    @File   : create_labels_files.py
    @Author : panjq
    @E-mail : pan_jinquan@163.com
    @Date   : 2018-08-11 10:15:28
"""

import os
import os.path


def write_txt(content, filename, mode='w'):
    """保存txt数据
    :param content:需要保存的数据,type->list
    :param filename:文件名
    :param mode:读写模式:'w' or 'a'
    :return: void
    """
    with open(filename, mode) as f:
        for line in content:
            str_line = ""
            for col, data in enumerate(line):
                if not col == len(line) - 1:
                    # 以空格作为分隔符
                    str_line = str_line + str(data) + " "
                else:
                    # 每行最后一个数据用换行符“\n”
                    str_line = str_line + str(data) + "\n"
            f.write(str_line)


def get_files_list(dir):
    '''
    实现遍历dir目录下,所有文件(包含子文件夹的文件)
    :param dir:指定文件夹目录
    :return:包含所有文件的列表->list
    '''
    # parent:父目录, filenames:该目录下所有文件夹,filename:该目录下的文件名
    files_list = []
    print(dir)
    for parent, dirnames, filenames in os.walk(dir):

        print('filenames=',filenames)
        if filenames != ".DS_Store":
            
            for filename in filenames:
                if filename != ".DS_Store":
                # print("parent is: " + parent)
                # print("filename is: " + filename)
                # print(os.path.join(parent, filename))  # 输出rootdir路径下所有文件（包含子文件）信息
                    print('filename', filename)
                    curr_file = parent.split(os.sep)[-1]
                    #print(os.path.split(dirnames))
                    if curr_file == 'a':
                        labels = 0
                    elif curr_file == 'b':
                        labels = 1
                    elif curr_file == 'c':
                        labels = 2
                    elif curr_file == 'd':
                        labels = 3
                    elif curr_file == 'e':
                        labels = 4

                    files_list.append([os.path.join(curr_file, filename), labels])
    return files_list


if __name__ == '__main__':
    train_dir = '/Users/xuezhouwen/Desktop/tensorflow_models_learning/dataset/train'
    train_txt = 'dataset/train.txt'
    train_data = get_files_list(train_dir)
    write_txt(train_data, train_txt, mode='w')

    val_dir = '/Users/xuezhouwen/Desktop/tensorflow_models_learning/dataset/val'
    val_txt = 'dataset/val.txt'
    val_data = get_files_list(val_dir)
    write_txt(val_data, val_txt, mode='w')

