from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Signal
import os,json,subprocess

from UI.MainWindow import Ui_MainWindow as Main_window
from Environment import path, dir_mix,next_,Show_bin


def message_info(type, title, msgs):
    msg = {
        'type': type,
        'title': title,
        'msg': msgs
    }
    return json.dumps(msg)
    # 包装message数据


class ReadConfig(QtCore.QThread):
    message = Signal(str)
    model_add = Signal(int, int, int)

    # 传参（传出）：x,y,ID

    def __init__(self):
        super().__init__()
        self.configs = []
        self.pkg_root = []

    def run(self) -> None:
        Path = None  # 图包父目录
        Child_path = None  # 图包文件夹目录名[list]
        # 遍历图包目录
        for paths, child_path, j in os.walk(path + next_+'Data'):
            Path = paths
            Child_path = child_path
            break

        now_Process = None
        try:
            for pkg_name in Child_path:
                now_Process = pkg_name
                config_file = dir_mix(
                    Path,
                    pkg_name,
                    'config.json'
                )
                # 合并多段数据 组成config文件的目录数据

                with open(config_file, 'r', encoding='utf-8') as f:
                    self.configs.append(json.loads(f.read()))

                    self.pkg_root.append(dir_mix(
                        Path,
                        pkg_name,
                    ))
        except:
            self.message.emit(message_info(type='wrong', title='error', msgs='包：[' + now_Process + ']异常'))
            # 回调，发送出错的包的名称
        All_model_count = len(self.configs)

        count = 0
        # print(int(All_model_count / 5))
        for y in range(1, 6):
            for x in range(1, 6):
                if count == All_model_count:
                    break
                # print(x,y,configs[count]["Name"],configs[count]["Description"])
                self.model_add.emit(x, y, count)
                count += 1


class window_main(QtWidgets.QMainWindow, Main_window):
    def __init__(self):
        super().__init__()
        self.checkBox = []
        self.label = []
        self.pixmap = []

        self.setupUi(self)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)

        # 设置滚动区域无边框

    def show(self) -> None:
        super().show()
        self.Add = ReadConfig()
        self.Add.message.connect(self.message)  # 绑定事件: message事件
        self.Add.model_add.connect(self.Create_model)
        self.Add.start()  # 启动图包加载线程

        # #人物计数器归零
        # for y in range(1,30):
        #     for x in range(1,6):
        #         self.Create_model(x,y)

    def message(self, msg):
        data = json.loads(msg)
        if data["type"] == "wrong":
            QtWidgets.QMessageBox.warning(self, data["title"], data["msg"], QtWidgets.QMessageBox.Yes)

    def Create_model(self, x, y, ID):
        name = self.configs[ID]["Name"]
        Description = self.configs[ID]["Description"]
        cover = dir_mix(self.pkg_root[ID], self.configs[ID]["cover"])
        list_length = 10 + 176 * y
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(760, list_length))
        x_label = 10 + 150 * (x - 1)
        y_label = 10 + 176 * (y - 1)

        self.label.append(QtWidgets.QLabel(self.scrollAreaWidgetContents))
        self.label[ID].setGeometry(QtCore.QRect(x_label, y_label, 140, 140))
        self.label[ID].setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label[ID].setToolTip(Description)

        pix = QtGui.QPixmap(cover)
        hight = pix.height()*140/pix.width()
        pix = pix.scaled(140, int(hight))  # 展示图片自适应

        self.pixmap.append(pix)
        self.label[ID].setPixmap(self.pixmap[ID])

        x_checkBox = 10 + 150 * (x - 1)
        y_checkBox = 10 + 150 * y + 26 * (y - 1)
        self.checkBox.append(QtWidgets.QCheckBox(self.scrollAreaWidgetContents))
        self.checkBox[ID].setGeometry(QtCore.QRect(x_checkBox, y_checkBox, 140, 16))

        self.checkBox[ID].setText(name)
        self.checkBox[ID].setToolTip(Description)

        self.label[ID].show()
        self.checkBox[ID].show()

    def About_Window(self):
        print('https://github.com/Cardinal-Designer')

    def MakePath(Show, Pkg_path):
        return Show + ' "' + Pkg_path + '"'

    # 避免出现因为路径中有空格导致的无法执行

    def Play_selected(self):
        self.selected = []  # 记录被选择的ID


        for i in range(0, len(self.configs)):
            if self.checkBox[i].isChecked():
                self.checkBox[i].setChecked(False)
                os.popen(self.MakePath(Show_bin,self.pkg_root[i]))
    def Play_all(self):
        for i in range(0, len(self.configs)):
            os.popen(self.MakePath(Show_bin, self.pkg_root[i]))
