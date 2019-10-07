# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Launcher.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import subprocess
import time as t
import os
import commentjson
import json
from PyQt5 import QtCore, QtGui, QtWidgets

start_times = 3
delay = 1250
hidden = False
colour_theme = 'plain'
dark_mode = 'bright'
name = 'BubblyBoiBot'
language = 'English'
port = 5001
join = ''
random_avatar = False
spam_server = True
spam_message = 'Replace this text with spam.'
automatic_formatting = False
shuffle = False
random_image = False
image_path = 'BubbleBoiBotLogo.jpg'
drawing_algorithm = 'cluster'
only_user = False
only_username = ''
X = 3
Y = 4
port_all = False


def check_and_load_settings():
    global start_times
    global delay
    global hidden
    global colour_theme
    global dark_mode
    global name
    global language
    global port
    global join
    global random_avatar
    global spam_server
    global spam_message
    global automatic_formatting
    global shuffle
    global random_image
    global image_path
    global drawing_algorithm
    global only_user
    global only_username
    global X
    global Y
    global port_all

    if os.path.isfile('settings.json'):
        with open('settings.json', 'r') as settings_file:
            SETTINGS = commentjson.load(settings_file)
            start_times = SETTINGS["start_times"]
            delay = SETTINGS["delay"]
            hidden = SETTINGS["hidden"]
            colour_theme = SETTINGS["ColourTheme"]
            dark_mode = SETTINGS["BrightOrDim"]
            name = SETTINGS["BotName"]
            port = SETTINGS["Port"]
            language = SETTINGS["Language"]
            join = SETTINGS["Join"]
            random_avatar = SETTINGS["RandomAvatar"]
            spam_server = SETTINGS["SpamServer"]
            spam_message = SETTINGS["SpamMessage"]
            automatic_formatting = SETTINGS["AutomaticFormatting"]
            shuffle = SETTINGS["Shuffle"]
            random_image = SETTINGS["RandomImage"]
            image_path = SETTINGS["ImageToDraw"]
            drawing_algorithm = SETTINGS["Algorithm"]
            only_user = SETTINGS["OnlyUser"]
            only_username = SETTINGS["OnlyUserName"]
            port_all = SETTINGS["portAll"]
            X = SETTINGS["X"]
            Y = SETTINGS["Y"]

    else:
        default_settings = {'delay': delay, 'hidden': hidden, 'start_times': start_times, 'ColourTheme': colour_theme, 'BrightOrDim': dark_mode, 'BotName': name, 'Language': language, 'Port': port, 'Join': join, 'RandomAvatar': random_avatar, 'SpamServer': spam_server,
                            'SpamMessage': spam_message, 'AutomaticFormatting': automatic_formatting, 'Shuffle': shuffle, 'RandomImage': random_image, 'ImageToDraw': image_path, 'Algorithm': drawing_algorithm, 'OnlyUser': only_user, 'OnlyUserName': only_username, 'portAll': port_all, 'X': X, 'Y': Y}
        settings = json.dumps(default_settings)
        with open('settings.json', 'w') as file:
            file.write(settings)
            file.close()
        check_and_load_settings()


check_and_load_settings()


class Ui_BubbleBoiLauncher(object):
    def setupUi(self, BubbleBoiLauncher):
        BubbleBoiLauncher.setObjectName("BubbleBoiLauncher")
        BubbleBoiLauncher.resize(500, 900)
        BubbleBoiLauncher.setMinimumSize(QtCore.QSize(500, 900))
        BubbleBoiLauncher.setMaximumSize(QtCore.QSize(500, 900))
        self.centralwidget = QtWidgets.QWidget(BubbleBoiLauncher)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(119, 0, 281, 111))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.delay_label = QtWidgets.QLabel(self.centralwidget)
        self.delay_label.setGeometry(QtCore.QRect(10, 90, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.delay_label.setFont(font)
        self.delay_label.setObjectName("delay_label")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(34, 737, 430, 131))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.hidden_mode_label = QtWidgets.QLabel(self.centralwidget)
        self.hidden_mode_label.setGeometry(QtCore.QRect(10, 140, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.hidden_mode_label.setFont(font)
        self.hidden_mode_label.setObjectName("hidden_mode_label")
        self.hidden_mode_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.hidden_mode_checkbox.setGeometry(QtCore.QRect(400, 168, 81, 20))
        self.hidden_mode_checkbox.setText("")
        self.hidden_mode_checkbox.setObjectName("hidden_mode_checkbox")
        if hidden:
            self.hidden_mode_checkbox.setChecked(True)
        self.start_times_label = QtWidgets.QLabel(self.centralwidget)
        self.start_times_label.setGeometry(QtCore.QRect(10, 190, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.start_times_label.setFont(font)
        self.start_times_label.setObjectName("start_times_label")
        self.one_start_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.one_start_radio.setGeometry(QtCore.QRect(140, 218, 31, 20))
        self.one_start_radio.setObjectName("one_start_radio")
        if start_times == 1:
            self.one_start_radio.setChecked(True)
        self.start_times_group = QtWidgets.QButtonGroup(BubbleBoiLauncher)
        self.start_times_group.setObjectName("start_times_group")
        self.start_times_group.addButton(self.one_start_radio)
        self.two_start_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.two_start_radio.setGeometry(QtCore.QRect(180, 218, 31, 20))
        self.two_start_radio.setObjectName("two_start_radio")
        if start_times == 2:
            self.two_start_radio.setChecked(True)
        self.start_times_group.addButton(self.two_start_radio)
        self.three_start_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.three_start_radio.setGeometry(QtCore.QRect(220, 218, 31, 20))
        self.three_start_radio.setObjectName("three_start_radio")
        if start_times == 3:
            self.three_start_radio.setChecked(True)
        self.start_times_group.addButton(self.three_start_radio)
        self.four_start_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.four_start_radio.setGeometry(QtCore.QRect(260, 218, 31, 20))
        self.four_start_radio.setObjectName("four_start_radio")
        if start_times == 4:
            self.four_start_radio.setChecked(True)
        self.start_times_group.addButton(self.four_start_radio)
        self.five_start_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.five_start_radio.setGeometry(QtCore.QRect(300, 218, 31, 20))
        self.five_start_radio.setObjectName("five_start_radio")
        if start_times == 5:
            self.five_start_radio.setChecked(True)
        self.start_times_group.addButton(self.five_start_radio)
        self.six_start_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.six_start_radio.setGeometry(QtCore.QRect(340, 218, 31, 20))
        self.six_start_radio.setObjectName("six_start_radio")
        if start_times == 6:
            self.six_start_radio.setChecked(True)
        self.start_times_group.addButton(self.six_start_radio)
        self.colour_themes_label = QtWidgets.QLabel(self.centralwidget)
        self.colour_themes_label.setGeometry(QtCore.QRect(10, 240, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.colour_themes_label.setFont(font)
        self.colour_themes_label.setObjectName("colour_themes_label")
        self.emerald_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.emerald_radio.setGeometry(QtCore.QRect(165, 268, 71, 20))
        self.emerald_radio.setObjectName("emerald_radio")
        if colour_theme == 'emerald':
            self.emerald_radio.setChecked(True)
        self.colour_themes_group = QtWidgets.QButtonGroup(BubbleBoiLauncher)
        self.colour_themes_group.setObjectName("colour_themes_group")
        self.colour_themes_group.addButton(self.emerald_radio)
        self.fire_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.fire_radio.setGeometry(QtCore.QRect(245, 268, 51, 20))
        self.fire_radio.setObjectName("fire_radio")
        if colour_theme == 'fire':
            self.fire_radio.setChecked(True)
        self.colour_themes_group.addButton(self.fire_radio)
        self.ocean_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.ocean_radio.setGeometry(QtCore.QRect(303, 268, 61, 20))
        self.ocean_radio.setObjectName("ocean_radio")
        if colour_theme == 'ocean':
            self.ocean_radio.setChecked(True)
        self.colour_themes_group.addButton(self.ocean_radio)
        self.storm_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.storm_radio.setGeometry(QtCore.QRect(375, 268, 61, 20))
        self.storm_radio.setObjectName("storm_radio")
        if colour_theme == 'storm':
            self.storm_radio.setChecked(True)
        self.colour_themes_group.addButton(self.storm_radio)
        self.candy_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.candy_radio.setGeometry(QtCore.QRect(10, 300, 61, 20))
        self.candy_radio.setObjectName("candy_radio")
        if colour_theme == 'candy':
            self.candy_radio.setChecked(True)
        self.colour_themes_group.addButton(self.candy_radio)
        self.desert_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.desert_radio.setGeometry(QtCore.QRect(80, 300, 61, 20))
        self.desert_radio.setObjectName("desert_radio")
        if colour_theme == 'gold':
            self.desert_radio.setChecked(True)
        self.colour_themes_group.addButton(self.desert_radio)
        self.plain_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.plain_radio.setGeometry(QtCore.QRect(152, 300, 61, 20))
        self.plain_radio.setObjectName("plain_radio")
        if colour_theme == 'plain':
            self.plain_radio.setChecked(True)
        self.colour_themes_group.addButton(self.plain_radio)
        self.dark_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.dark_checkbox.setGeometry(QtCore.QRect(215, 300, 91, 20))
        self.dark_checkbox.setObjectName("dark_checkbox")
        if dark_mode == 'dim':
            self.dark_checkbox.setChecked(True)
        self.join_settings_label = QtWidgets.QLabel(self.centralwidget)
        self.join_settings_label.setGeometry(QtCore.QRect(10, 320, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.join_settings_label.setFont(font)
        self.join_settings_label.setObjectName("join_settings_label")
        self.bot_name_label = QtWidgets.QLabel(self.centralwidget)
        self.bot_name_label.setGeometry(QtCore.QRect(10, 375, 61, 16))
        self.bot_name_label.setObjectName("bot_name_label")
        self.bot_name_text = QtWidgets.QTextEdit(self.centralwidget)
        self.bot_name_text.setGeometry(QtCore.QRect(80, 376, 141, 16))
        self.bot_name_text.setObjectName("bot_name_text")
        self.bot_name_text.setPlainText(name)
        self.port_label = QtWidgets.QLabel(self.centralwidget)
        self.port_label.setGeometry(QtCore.QRect(10, 405, 91, 16))
        self.port_label.setObjectName("port_label")
        self.port5001_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.port5001_radio.setGeometry(QtCore.QRect(100, 403, 51, 20))
        self.port5001_radio.setObjectName("port5001_radio")
        if port == 5001:
            self.port5001_radio.setChecked(True)
        self.port_group = QtWidgets.QButtonGroup(BubbleBoiLauncher)
        self.port_group.setObjectName("port_group")
        self.port_group.addButton(self.port5001_radio)
        self.port5002_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.port5002_radio.setGeometry(QtCore.QRect(160, 403, 51, 20))
        self.port5002_radio.setObjectName("port5002_radio")
        if port == 5002:
            self.port5002_radio.setChecked(True)
        self.port_group.addButton(self.port5002_radio)
        self.port5003_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.port5003_radio.setGeometry(QtCore.QRect(220, 403, 51, 20))
        self.port5003_radio.setObjectName("port5003_radio")
        if port == 5003:
            self.port5003_radio.setChecked(True)
        self.port_group.addButton(self.port5003_radio)
        self.portAll_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.portAll_radio.setGeometry(QtCore.QRect(280, 403, 51, 20))
        self.portAll_radio.setObjectName("portAll_radio")
        if port_all:
            self.portAll_radio.setChecked(True)
            self.port5001_radio.setChecked(False)
            self.port5003_radio.setChecked(False)
            self.port5002_radio.setChecked(False)
        self.port_group.addButton(self.portAll_radio)
        self.join_label = QtWidgets.QLabel(self.centralwidget)
        self.join_label.setGeometry(QtCore.QRect(10, 435, 181, 16))
        self.join_label.setObjectName("join_label")
        self.join_text = QtWidgets.QTextEdit(self.centralwidget)
        self.join_text.setGeometry(QtCore.QRect(200, 436, 141, 16))
        self.join_text.setObjectName("join_text")
        self.join_text.setPlainText(join)
        self.language_label = QtWidgets.QLabel(self.centralwidget)
        self.language_label.setGeometry(QtCore.QRect(235, 375, 61, 16))
        self.language_label.setObjectName("language_label")
        self.language_text = QtWidgets.QTextEdit(self.centralwidget)
        self.language_text.setGeometry(QtCore.QRect(305, 376, 101, 16))
        self.language_text.setObjectName("language_text")
        self.language_text.setPlainText(language)
        self.randomAvatar_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.randomAvatar_checkbox.setGeometry(QtCore.QRect(360, 434, 111, 21))
        self.randomAvatar_checkbox.setObjectName("randomAvatar_checkbox")
        if random_avatar:
            self.randomAvatar_checkbox.setChecked(True)
        self.spam_settings_label = QtWidgets.QLabel(self.centralwidget)
        self.spam_settings_label.setGeometry(QtCore.QRect(10, 450, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.spam_settings_label.setFont(font)
        self.spam_settings_label.setObjectName("spam_settings_label")
        self.doSpam_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.doSpam_checkbox.setGeometry(QtCore.QRect(172, 478, 101, 21))
        self.doSpam_checkbox.setObjectName("doSpam_checkbox")
        if spam_server:
            self.doSpam_checkbox.setChecked(True)
        self.spam_text = QtWidgets.QTextEdit(self.centralwidget)
        self.spam_text.setGeometry(QtCore.QRect(360, 475, 131, 61))
        self.spam_text.setObjectName("spam_text")
        self.spam_text.setPlainText(spam_message)
        self.spam_label = QtWidgets.QLabel(self.centralwidget)
        self.spam_label.setGeometry(QtCore.QRect(295, 481, 61, 16))
        self.spam_label.setObjectName("spam_label")
        self.linkFilter_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.linkFilter_checkbox.setGeometry(QtCore.QRect(10, 510, 331, 21))
        self.linkFilter_checkbox.setObjectName("linkFilter_checkbox")
        if automatic_formatting:
            self.linkFilter_checkbox.setChecked(True)
        self.draw_settings_label = QtWidgets.QLabel(self.centralwidget)
        self.draw_settings_label.setGeometry(QtCore.QRect(10, 530, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.draw_settings_label.setFont(font)
        self.draw_settings_label.setObjectName("draw_settings_label")
        self.shuffle_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.shuffle_checkbox.setGeometry(QtCore.QRect(200, 558, 71, 21))
        self.shuffle_checkbox.setObjectName("shuffle_checkbox")
        if shuffle:
            self.shuffle_checkbox.setChecked(True)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 535, 501, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 454, 501, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 323, 501, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 241, 501, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 190, 501, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(0, 140, 501, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.randomImage_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.randomImage_checkbox.setGeometry(QtCore.QRect(270, 558, 231, 21))
        self.randomImage_checkbox.setObjectName("randomImage_checkbox")
        if random_image:
            self.randomImage_checkbox.setChecked(True)
        self.image_path_text = QtWidgets.QTextEdit(self.centralwidget)
        self.image_path_text.setGeometry(QtCore.QRect(89, 586, 401, 31))
        self.image_path_text.setObjectName("image_path_text")
        self.image_path_text.setPlainText(image_path)
        self.image_path_label = QtWidgets.QLabel(self.centralwidget)
        self.image_path_label.setGeometry(QtCore.QRect(10, 592, 71, 16))
        self.image_path_label.setObjectName("image_path_label")
        self.algorithm_label = QtWidgets.QLabel(self.centralwidget)
        self.algorithm_label.setGeometry(QtCore.QRect(10, 626, 111, 16))
        self.algorithm_label.setObjectName("algorithm_label")
        self.cluster_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.cluster_radio.setGeometry(QtCore.QRect(125, 625, 71, 20))
        self.cluster_radio.setObjectName("cluster_radio")
        if drawing_algorithm == 'cluster':
            self.cluster_radio.setChecked(True)
        self.algorithm_group = QtWidgets.QButtonGroup(BubbleBoiLauncher)
        self.algorithm_group.setObjectName("algorithm_group")
        self.algorithm_group.addButton(self.cluster_radio)
        self.yliluoma_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.yliluoma_radio.setGeometry(QtCore.QRect(199, 625, 231, 20))
        self.yliluoma_radio.setObjectName("yliluoma_radio")
        if drawing_algorithm == 'yliluoma':
            self.yliluoma_radio.setChecked(True)
        self.algorithm_group.addButton(self.yliluoma_radio)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(0, 645, 501, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(0, 93, 501, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.search_settings_label = QtWidgets.QLabel(self.centralwidget)
        self.search_settings_label.setGeometry(QtCore.QRect(10, 641, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.search_settings_label.setFont(font)
        self.search_settings_label.setObjectName("search_settings_label")
        self.search_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.search_checkbox.setGeometry(QtCore.QRect(182, 669, 71, 21))
        self.search_checkbox.setObjectName("search_checkbox")
        if only_user:
            self.search_checkbox.setChecked(True)
        self.username_text = QtWidgets.QTextEdit(self.centralwidget)
        self.username_text.setGeometry(QtCore.QRect(358, 672, 131, 16))
        self.username_text.setObjectName("username_text")
        self.username_text.setPlainText(only_username)
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(251, 670, 111, 20))
        self.username_label.setObjectName("username_label")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(0, 697, 501, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.delay250_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.delay250_radio.setGeometry(QtCore.QRect(80, 118, 71, 20))
        self.delay250_radio.setObjectName("delay250_radio")
        if delay == 250:
            self.delay250_radio.setChecked(True)
        self.delay_group = QtWidgets.QButtonGroup(BubbleBoiLauncher)
        self.delay_group.setObjectName("delay_group")
        self.delay_group.addButton(self.delay250_radio)
        self.delay500_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.delay500_radio.setGeometry(QtCore.QRect(150, 118, 71, 20))
        self.delay500_radio.setObjectName("delay500_radio")
        if delay == 500:
            self.delay500_radio.setChecked(True)
        self.delay_group.addButton(self.delay500_radio)
        self.delay750_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.delay750_radio.setGeometry(QtCore.QRect(220, 118, 71, 20))
        self.delay750_radio.setObjectName("delay750_radio")
        if delay == 750:
            self.delay750_radio.setChecked(True)
        self.delay_group.addButton(self.delay750_radio)
        self.delay1000_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.delay1000_radio.setGeometry(QtCore.QRect(290, 118, 71, 20))
        self.delay1000_radio.setObjectName("delay1000_radio")
        if delay == 1000:
            self.delay1000_radio.setChecked(True)
        self.delay_group.addButton(self.delay1000_radio)
        self.delay1250_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.delay1250_radio.setGeometry(QtCore.QRect(370, 118, 71, 20))
        self.delay1250_radio.setObjectName("delay1250_radio")
        if delay == 1250:
            self.delay1250_radio.setChecked(True)
        self.delay_group.addButton(self.delay1250_radio)
        BubbleBoiLauncher.setCentralWidget(self.centralwidget)
        self.start_button.clicked.connect(self.launched)

        self.retranslateUi(BubbleBoiLauncher)
        QtCore.QMetaObject.connectSlotsByName(BubbleBoiLauncher)

    def retranslateUi(self, BubbleBoiLauncher):
        _translate = QtCore.QCoreApplication.translate
        BubbleBoiLauncher.setWindowTitle(_translate(
            "BubbleBoiLauncher", "BubbleBoiBot v1.8 - Launcher"))
        self.title_label.setText(_translate(
            "BubbleBoiLauncher", "BubbleBoiBot v1.8"))
        self.delay_label.setText(_translate("BubbleBoiLauncher", "Delay:"))
        self.start_button.setText(_translate("BubbleBoiLauncher", "Launch"))
        self.hidden_mode_label.setText(_translate(
            "BubbleBoiLauncher", "Hidden (Hide tasks in Task Manager):"))
        self.start_times_label.setText(
            _translate("BubbleBoiLauncher", "Start Times:"))
        self.one_start_radio.setText(_translate("BubbleBoiLauncher", "1"))
        self.two_start_radio.setText(_translate("BubbleBoiLauncher", "2"))
        self.three_start_radio.setText(_translate("BubbleBoiLauncher", "3"))
        self.four_start_radio.setText(_translate("BubbleBoiLauncher", "4"))
        self.five_start_radio.setText(_translate("BubbleBoiLauncher", "5"))
        self.six_start_radio.setText(_translate("BubbleBoiLauncher", "6"))
        self.colour_themes_label.setText(
            _translate("BubbleBoiLauncher", "Colour Theme:"))
        self.emerald_radio.setText(_translate("BubbleBoiLauncher", "Emerald"))
        self.fire_radio.setText(_translate("BubbleBoiLauncher", "Fire"))
        self.ocean_radio.setText(_translate("BubbleBoiLauncher", "Ocean"))
        self.storm_radio.setText(_translate("BubbleBoiLauncher", "Storm"))
        self.candy_radio.setText(_translate("BubbleBoiLauncher", "Candy"))
        self.desert_radio.setText(_translate("BubbleBoiLauncher", "Desert"))
        self.plain_radio.setText(_translate("BubbleBoiLauncher", "Plain"))
        self.dark_checkbox.setText(_translate(
            "BubbleBoiLauncher", "Dark Mode"))
        self.join_settings_label.setText(
            _translate("BubbleBoiLauncher", "Join Settings:"))
        self.bot_name_label.setText(
            _translate("BubbleBoiLauncher", "Bot Name:"))
        self.port_label.setText(_translate(
            "BubbleBoiLauncher", "Port to attack:"))
        self.port5001_radio.setText(_translate("BubbleBoiLauncher", "5001"))
        self.port5002_radio.setText(_translate("BubbleBoiLauncher", "5002"))
        self.port5003_radio.setText(_translate("BubbleBoiLauncher", "5003"))
        self.portAll_radio.setText(_translate("BubbleBoiLauncher", "All"))
        self.join_label.setText(_translate(
            "BubbleBoiLauncher", "Join Code (For Private Games):"))
        self.language_label.setText(
            _translate("BubbleBoiLauncher", "Language:"))
        self.randomAvatar_checkbox.setText(
            _translate("BubbleBoiLauncher", "Random Avatar"))
        self.spam_settings_label.setText(
            _translate("BubbleBoiLauncher", "Spam Settings:"))
        self.doSpam_checkbox.setText(_translate(
            "BubbleBoiLauncher", "Spam Server"))
        self.spam_label.setText(_translate("BubbleBoiLauncher", "Message:"))
        self.linkFilter_checkbox.setText(_translate(
            "BubbleBoiLauncher", "Link Message Filter (Convert any periods to commas)"))
        self.draw_settings_label.setText(_translate(
            "BubbleBoiLauncher", "Drawing Settings:"))
        self.shuffle_checkbox.setText(
            _translate("BubbleBoiLauncher", "Shuffle"))
        self.randomImage_checkbox.setText(_translate(
            "BubbleBoiLauncher", "Random image from images folder"))
        self.image_path_label.setText(
            _translate("BubbleBoiLauncher", "Image path:"))
        self.algorithm_label.setText(_translate(
            "BubbleBoiLauncher", "Drawing algorithm:"))
        self.cluster_radio.setText(_translate("BubbleBoiLauncher", "Cluster"))
        self.yliluoma_radio.setText(_translate(
            "BubbleBoiLauncher", "Yliluoma (Very slow, higher quality)"))
        self.search_settings_label.setText(
            _translate("BubbleBoiLauncher", "Search Settings:"))
        self.search_checkbox.setText(_translate("BubbleBoiLauncher", "Search"))
        self.username_label.setText(_translate(
            "BubbleBoiLauncher", "Username to find:"))
        self.delay250_radio.setText(_translate("BubbleBoiLauncher", "250ms"))
        self.delay500_radio.setText(_translate("BubbleBoiLauncher", "500ms"))
        self.delay750_radio.setText(_translate("BubbleBoiLauncher", "750ms"))
        self.delay1000_radio.setText(_translate("BubbleBoiLauncher", "1000ms"))
        self.delay1250_radio.setText(_translate("BubbleBoiLauncher", "1250ms"))

    def launched(self):
        global start_times
        global delay
        global hidden
        global colour_theme
        global dark_mode
        global name
        global language
        global port
        global join
        global random_avatar
        global spam_server
        global spam_message
        global automatic_formatting
        global shuffle
        global random_image
        global image_path
        global drawing_algorithm
        global only_user
        global only_username
        global X
        global Y
        global port_all

        if self.delay250_radio.isChecked():
            delay = 250
        if self.delay500_radio.isChecked():
            delay = 500
        if self.delay750_radio.isChecked():
            delay = 750
        if self.delay1000_radio.isChecked():
            delay = 1000
        if self.delay1250_radio.isChecked():
            delay = 1250
        if self.hidden_mode_checkbox.isChecked():
            hidden = True
        else:
            hidden = False
        if self.one_start_radio.isChecked():
            start_times = 1
        if self.two_start_radio.isChecked():
            start_times = 2
        if self.three_start_radio.isChecked():
            start_times = 3
        if self.four_start_radio.isChecked():
            start_times = 4
        if self.five_start_radio.isChecked():
            start_times = 5
        if self.six_start_radio.isChecked():
            start_times = 6
        if self.emerald_radio.isChecked():
            colour_theme = 'emerald'
        if self.fire_radio.isChecked():
            colour_theme = 'fire'
        if self.ocean_radio.isChecked():
            colour_theme = 'ocean'
        if self.storm_radio.isChecked():
            colour_theme = 'storm'
        if self.candy_radio.isChecked():
            colour_theme = 'candy'
        if self.desert_radio.isChecked():
            colour_theme = 'gold'
        if self.plain_radio.isChecked():
            colour_theme = 'plain'
        name = self.bot_name_text.toPlainText()
        language = self.language_text.toPlainText()
        if self.port5001_radio.isChecked():
            port = 5001
            port_all = False
        if self.port5002_radio.isChecked():
            port = 5002
            port_all = False
        if self.port5003_radio.isChecked():
            port = 5003
            port_all = False
        if self.portAll_radio.isChecked():
            port = 5001
            port_all = True
        else:
            port_all = False
        join = self.join_text.toPlainText()
        if self.randomAvatar_checkbox.isChecked():
            random_avatar = True
        else:
            random_avatar = False
        if self.dark_checkbox.isChecked():
            dark_mode = 'dim'
        else:
            dark_mode = 'bright'
        if self.doSpam_checkbox.isChecked():
            spam_server = True
        else:
            spam_server = False
        if self.linkFilter_checkbox.isChecked():
            automatic_formatting = True
        else:
            automatic_formatting = False
        spam_message = self.spam_text.toPlainText()
        if self.shuffle_checkbox.isChecked():
            shuffle = True
        else:
            shuffle = False
        if self.randomImage_checkbox.isChecked():
            random_image = True
        else:
            random_image = False
        image_path = self.image_path_text.toPlainText()
        if self.cluster_radio.isChecked():
            drawing_algorithm = 'cluster'
        else:
            drawing_algorithm = 'yliluoma'
        if self.search_checkbox.isChecked():
            only_user = True
        else:
            only_user = False
        only_username = self.username_text.toPlainText()

        BubbleBoiLauncher.close()

        changed_settings = {'delay': delay, 'hidden': hidden, 'start_times': start_times, 'ColourTheme': colour_theme, 'BrightOrDim': dark_mode, 'BotName': name, 'Language': language, 'Port': port, 'Join': join, 'RandomAvatar': random_avatar, 'SpamServer': spam_server,
                            'SpamMessage': spam_message, 'AutomaticFormatting': automatic_formatting, 'Shuffle': shuffle, 'RandomImage': random_image, 'ImageToDraw': image_path, 'Algorithm': drawing_algorithm, 'OnlyUser': only_user, 'OnlyUserName': only_username, 'portAll': port_all, 'X': X, 'Y': Y}
        new_settings = json.dumps(changed_settings)
        os.remove('settings.json')
        with open('settings.json', 'w') as file:
            file.write(new_settings)
            file.close()

            with open('settings.json', 'r') as settings_file:
                SETTINGS = commentjson.load(settings_file)

            if SETTINGS["portAll"]:
                if not hidden:
                    cmd = "exec\loop5001.bat"
                    for x in range(start_times):
                        SW_MINIMIZE = 6
                        info = subprocess.STARTUPINFO()
                        info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                        info.wShowWindow = SW_MINIMIZE
                        subprocess.Popen(cmd, startupinfo=info)
                        t.sleep((delay/1000))
                    cmd = "exec\loop5002.bat"
                    for x in range(start_times):
                        SW_MINIMIZE = 6
                        info = subprocess.STARTUPINFO()
                        info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                        info.wShowWindow = SW_MINIMIZE
                        subprocess.Popen(cmd, startupinfo=info)
                        t.sleep((delay/1000))
                    cmd = "exec\loop5003.bat"
                    for x in range(start_times):
                        SW_MINIMIZE = 6
                        info = subprocess.STARTUPINFO()
                        info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                        info.wShowWindow = SW_MINIMIZE
                        subprocess.Popen(cmd, startupinfo=info)
                        t.sleep((delay/1000))
                else:
                    cmd = "exec\loop5001.bat"
                    for x in range(start_times):
                        SW_HIDE = 0
                        info = subprocess.STARTUPINFO()
                        info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                        info.wShowWindow = SW_HIDE
                        subprocess.Popen(cmd, startupinfo=info)
                        t.sleep((delay/1000))
                    cmd = "exec\loop5002.bat"
                    for x in range(start_times):
                        SW_HIDE = 0
                        info = subprocess.STARTUPINFO()
                        info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                        info.wShowWindow = SW_HIDE
                        subprocess.Popen(cmd, startupinfo=info)
                        t.sleep((delay/1000))
                    cmd = "exec\loop5003.bat"
                    for x in range(start_times):
                        SW_HIDE = 0
                        info = subprocess.STARTUPINFO()
                        info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                        info.wShowWindow = SW_HIDE
                        subprocess.Popen(cmd, startupinfo=info)
                        t.sleep((delay/1000))
            else:
                if SETTINGS["Port"] == 5001:
                    if not hidden:
                        cmd = "exec\loop5001.bat"
                        for x in range(start_times):
                            SW_MINIMIZE = 6
                            info = subprocess.STARTUPINFO()
                            info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                            info.wShowWindow = SW_MINIMIZE
                            subprocess.Popen(cmd, startupinfo=info)
                            t.sleep((delay/1000))
                    else:
                        cmd = "exec\loop5001.bat"
                        for x in range(start_times):
                            SW_HIDE = 0
                            info = subprocess.STARTUPINFO()
                            info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                            info.wShowWindow = SW_HIDE
                            subprocess.Popen(cmd, startupinfo=info)
                            t.sleep((delay/1000))
                if SETTINGS["Port"] == 5002:
                    if not hidden:
                        cmd = "exec\loop5002.bat"
                        for x in range(start_times):
                            SW_MINIMIZE = 6
                            info = subprocess.STARTUPINFO()
                            info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                            info.wShowWindow = SW_MINIMIZE
                            subprocess.Popen(cmd, startupinfo=info)
                            t.sleep((delay/1000))
                    else:
                        cmd = "exec\loop5002.bat"
                        for x in range(start_times):
                            SW_HIDE = 0
                            info = subprocess.STARTUPINFO()
                            info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                            info.wShowWindow = SW_HIDE
                            subprocess.Popen(cmd, startupinfo=info)
                            t.sleep((delay/1000))
                if SETTINGS["Port"] == 5003:
                    if not hidden:
                        cmd = "exec\loop5003.bat"
                        for x in range(start_times):
                            SW_MINIMIZE = 6
                            info = subprocess.STARTUPINFO()
                            info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                            info.wShowWindow = SW_MINIMIZE
                            subprocess.Popen(cmd, startupinfo=info)
                            t.sleep((delay/1000))
                    else:
                        cmd = "exec\loop5003.bat"
                        for x in range(start_times):
                            SW_HIDE = 0
                            info = subprocess.STARTUPINFO()
                            info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                            info.wShowWindow = SW_HIDE
                            subprocess.Popen(cmd, startupinfo=info)
                            t.sleep((delay/1000))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BubbleBoiLauncher = QtWidgets.QMainWindow()
    ui = Ui_BubbleBoiLauncher()
    ui.setupUi(BubbleBoiLauncher)
    BubbleBoiLauncher.show()
    sys.exit(app.exec_())
