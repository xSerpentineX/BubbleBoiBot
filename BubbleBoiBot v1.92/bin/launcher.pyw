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
        BubbleBoiLauncher.resize(950, 700)
        BubbleBoiLauncher.setMinimumSize(QtCore.QSize(950, 700))
        BubbleBoiLauncher.setMaximumSize(QtCore.QSize(950, 700))
        self.centralwidget = QtWidgets.QWidget(BubbleBoiLauncher)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 951, 701))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 928, 2092))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.bot_name_text = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.bot_name_text.setObjectName("bot_name_text")
        self.bot_name_text.setPlainText(name)
        self.gridLayout.addWidget(self.bot_name_text, 36, 0, 1, 1)
        self.spam_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.spam_label.setObjectName("spam_label")
        self.gridLayout.addWidget(self.spam_label, 52, 0, 1, 1)
        self.randomAvatar_checkbox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.randomAvatar_checkbox.setObjectName("randomAvatar_checkbox")
        if random_avatar:
            self.randomAvatar_checkbox.setChecked(True)
        self.gridLayout.addWidget(self.randomAvatar_checkbox, 44, 0, 1, 1)
        self.port5003_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.port5003_radio.setObjectName("port5003_radio")
        if port == 5003:
            self.port5003_radio.setChecked(True)
        self.port_group = QtWidgets.QButtonGroup(BubbleBoiLauncher)
        self.port_group.setObjectName("port_group")
        self.port_group.addButton(self.port5003_radio)
        self.gridLayout.addWidget(self.port5003_radio, 42, 0, 1, 1)
        self.one_start_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.one_start_radio.setObjectName("one_start_radio")
        if start_times == 1:
            self.one_start_radio.setChecked(True)
        self.start_times_group = QtWidgets.QButtonGroup(BubbleBoiLauncher)
        self.start_times_group.setObjectName("start_times_group")
        self.start_times_group.addButton(self.one_start_radio)
        self.gridLayout.addWidget(self.one_start_radio, 15, 0, 1, 1)
        self.start_times_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.start_times_label.setFont(font)
        self.start_times_label.setObjectName("start_times_label")
        self.gridLayout.addWidget(self.start_times_label, 13, 0, 1, 1)
        self.delay500_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.delay500_radio.setObjectName("delay500_radio")
        if delay == 500:
            self.delay500_radio.setChecked(True)
        self.delay_group = QtWidgets.QButtonGroup(BubbleBoiLauncher)
        self.delay_group.setObjectName("delay_group")
        self.delay_group.addButton(self.delay500_radio)
        self.gridLayout.addWidget(self.delay500_radio, 5, 0, 1, 1)
        self.four_start_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.four_start_radio.setObjectName("four_start_radio")
        if start_times == 4:
            self.four_start_radio.setChecked(True)
        self.start_times_group.addButton(self.four_start_radio)
        self.gridLayout.addWidget(self.four_start_radio, 18, 0, 1, 1)
        self.delay1250_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.delay1250_radio.setObjectName("delay1250_radio")
        if delay == 1250:
            self.delay1250_radio.setChecked(True)
        self.delay_group.addButton(self.delay1250_radio)
        self.gridLayout.addWidget(self.delay1250_radio, 8, 0, 1, 1)
        self.hidden_mode_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.hidden_mode_label.setFont(font)
        self.hidden_mode_label.setObjectName("hidden_mode_label")
        self.gridLayout.addWidget(self.hidden_mode_label, 10, 0, 1, 1)
        self.title_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
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
        self.gridLayout.addWidget(self.title_label, 0, 0, 1, 1)
        self.two_start_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.two_start_radio.setObjectName("two_start_radio")
        if start_times == 2:
            self.two_start_radio.setChecked(True)
        self.start_times_group.addButton(self.two_start_radio)
        self.gridLayout.addWidget(self.two_start_radio, 16, 0, 1, 1)
        self.delay1000_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.delay1000_radio.setObjectName("delay1000_radio")
        if delay == 1000:
            self.delay1000_radio.setChecked(True)
        self.delay_group.addButton(self.delay1000_radio)
        self.gridLayout.addWidget(self.delay1000_radio, 7, 0, 1, 1)
        self.colour_themes_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.colour_themes_label.setFont(font)
        self.colour_themes_label.setObjectName("colour_themes_label")
        self.gridLayout.addWidget(self.colour_themes_label, 22, 0, 1, 1)
        self.six_start_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.six_start_radio.setObjectName("six_start_radio")
        if start_times == 6:
            self.six_start_radio.setChecked(True)
        self.start_times_group.addButton(self.six_start_radio)
        self.gridLayout.addWidget(self.six_start_radio, 20, 0, 1, 1)
        self.delay_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.delay_label.setFont(font)
        self.delay_label.setObjectName("delay_label")
        self.gridLayout.addWidget(self.delay_label, 2, 0, 1, 1)
        self.emerald_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.emerald_radio.setObjectName("emerald_radio")
        if colour_theme == 'emerald':
            self.emerald_radio.setChecked(True)
        self.colour_themes_group = QtWidgets.QButtonGroup(BubbleBoiLauncher)
        self.colour_themes_group.setObjectName("colour_themes_group")
        self.colour_themes_group.addButton(self.emerald_radio)
        self.gridLayout.addWidget(self.emerald_radio, 25, 0, 1, 1)
        self.ocean_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.ocean_radio.setObjectName("ocean_radio")
        if colour_theme == 'ocean':
            self.ocean_radio.setChecked(True)
        self.colour_themes_group.addButton(self.ocean_radio)
        self.gridLayout.addWidget(self.ocean_radio, 26, 0, 1, 1)
        self.three_start_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.three_start_radio.setObjectName("three_start_radio")
        if start_times == 3:
            self.three_start_radio.setChecked(True)
        self.start_times_group.addButton(self.three_start_radio)
        self.gridLayout.addWidget(self.three_start_radio, 17, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 9, 0, 1, 1)
        self.five_start_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.five_start_radio.setObjectName("five_start_radio")
        if start_times == 5:
            self.five_start_radio.setChecked(True)
        self.start_times_group.addButton(self.five_start_radio)
        self.gridLayout.addWidget(self.five_start_radio, 19, 0, 1, 1)
        self.candy_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.candy_radio.setObjectName("candy_radio")
        if colour_theme == 'cadny':
            self.candy_radio.setChecked(True)
        self.colour_themes_group.addButton(self.candy_radio)
        self.gridLayout.addWidget(self.candy_radio, 29, 0, 1, 1)
        self.fire_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.fire_radio.setObjectName("fire_radio")
        if colour_theme == 'fire':
            self.fire_radio.setChecked(True)
        self.colour_themes_group.addButton(self.fire_radio)
        self.gridLayout.addWidget(self.fire_radio, 24, 0, 1, 1)
        self.desert_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.desert_radio.setObjectName("desert_radio")
        if colour_theme == 'gold':
            self.desert_radio.setChecked(True)
        self.colour_themes_group.addButton(self.desert_radio)
        self.gridLayout.addWidget(self.desert_radio, 28, 0, 1, 1)
        self.delay250_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.delay250_radio.setObjectName("delay250_radio")
        if delay == 250:
            self.delay250_radio.setChecked(True)
        self.delay_group.addButton(self.delay250_radio)
        self.gridLayout.addWidget(self.delay250_radio, 4, 0, 1, 1)
        self.delay750_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.delay750_radio.setObjectName("delay750_radio")
        if delay == 750:
            self.delay750_radio.setChecked(True)
        self.delay_group.addButton(self.delay750_radio)
        self.gridLayout.addWidget(self.delay750_radio, 6, 0, 1, 1)
        self.storm_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.storm_radio.setObjectName("storm_radio")
        if colour_theme == 'storm':
            self.storm_radio.setChecked(True)
        self.colour_themes_group.addButton(self.storm_radio)
        self.gridLayout.addWidget(self.storm_radio, 27, 0, 1, 1)
        self.yliluoma_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.yliluoma_radio.setObjectName("yliluoma_radio")
        if drawing_algorithm == 'yliluoma':
            self.yliluoma_radio.setChecked(True)
        self.algorithm_group = QtWidgets.QButtonGroup(BubbleBoiLauncher)
        self.algorithm_group.setObjectName("algorithm_group")
        self.algorithm_group.addButton(self.yliluoma_radio)
        self.gridLayout.addWidget(self.yliluoma_radio, 63, 0, 1, 1)
        self.plain_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.plain_radio.setObjectName("plain_radio")
        if colour_theme == 'plain':
            self.plain_radio.setChecked(True)
        self.colour_themes_group.addButton(self.plain_radio)
        self.gridLayout.addWidget(self.plain_radio, 30, 0, 1, 1)
        self.cluster_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.cluster_radio.setObjectName("cluster_radio")
        if drawing_algorithm == 'cluster':
            self.cluster_radio.setChecked(True)
        self.algorithm_group.addButton(self.cluster_radio)
        self.gridLayout.addWidget(self.cluster_radio, 62, 0, 1, 1)
        self.dark_checkbox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.dark_checkbox.setObjectName("dark_checkbox")
        if dark_mode == 'dim':
            self.dark_checkbox.setChecked(True)
        self.gridLayout.addWidget(self.dark_checkbox, 31, 0, 1, 1)
        self.port5001_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.port5001_radio.setObjectName("port5001_radio")
        if port == 5001:
            self.port5001_radio.setChecked(True)
        self.port_group.addButton(self.port5001_radio)
        self.gridLayout.addWidget(self.port5001_radio, 40, 0, 1, 1)
        self.port5002_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.port5002_radio.setObjectName("port5002_radio")
        if port == 5002:
            self.port5002_radio.setChecked(True)
        self.port_group.addButton(self.port5002_radio)
        self.gridLayout.addWidget(self.port5002_radio, 41, 0, 1, 1)
        self.search_checkbox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.search_checkbox.setObjectName("search_checkbox")
        if only_user == True:
            self.search_checkbox.setChecked(True)
        self.gridLayout.addWidget(self.search_checkbox, 67, 0, 1, 1)
        self.search_settings_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.search_settings_label.setFont(font)
        self.search_settings_label.setObjectName("search_settings_label")
        self.gridLayout.addWidget(self.search_settings_label, 65, 0, 1, 1)
        self.image_path_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.image_path_label.setObjectName("image_path_label")
        self.gridLayout.addWidget(self.image_path_label, 59, 0, 1, 1)
        self.portAll_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.portAll_radio.setObjectName("portAll_radio")
        if port_all:
            self.portAll_radio.setChecked(True)
            self.port5001_radio.setChecked(False)
            self.port5003_radio.setChecked(False)
            self.port5002_radio.setChecked(False)
        self.port_group.addButton(self.portAll_radio)
        self.gridLayout.addWidget(self.portAll_radio, 43, 0, 1, 1)
        self.port_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.port_label.setObjectName("port_label")
        self.gridLayout.addWidget(self.port_label, 39, 0, 1, 1)
        self.doSpam_checkbox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.doSpam_checkbox.setObjectName("doSpam_checkbox")
        if spam_server:
            self.doSpam_checkbox.setChecked(True)
        self.gridLayout.addWidget(self.doSpam_checkbox, 50, 0, 1, 1)
        self.join_text = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.join_text.setObjectName("join_text")
        self.join_text.setPlainText(join)
        self.gridLayout.addWidget(self.join_text, 46, 0, 1, 1)
        self.join_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.join_label.setObjectName("join_label")
        self.gridLayout.addWidget(self.join_label, 45, 0, 1, 1)
        self.linkFilter_checkbox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.linkFilter_checkbox.setObjectName("linkFilter_checkbox")
        if automatic_formatting:
            self.linkFilter_checkbox.setChecked(True)
        self.gridLayout.addWidget(self.linkFilter_checkbox, 51, 0, 1, 1)
        self.randomImage_checkbox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.randomImage_checkbox.setObjectName("randomImage_checkbox")
        if random_image:
            self.randomImage_checkbox.setChecked(True)
        self.gridLayout.addWidget(self.randomImage_checkbox, 58, 0, 1, 1)
        self.shuffle_checkbox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.shuffle_checkbox.setObjectName("shuffle_checkbox")
        if shuffle:
            self.shuffle_checkbox.setChecked(True)
        self.gridLayout.addWidget(self.shuffle_checkbox, 57, 0, 1, 1)
        self.spam_text = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.spam_text.setObjectName("spam_text")
        self.spam_text.setPlainText(spam_message)
        self.gridLayout.addWidget(self.spam_text, 53, 0, 1, 1)
        self.bot_name_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.bot_name_label.setObjectName("bot_name_label")
        self.gridLayout.addWidget(self.bot_name_label, 35, 0, 1, 1)
        self.language_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.language_label.setObjectName("language_label")
        self.gridLayout.addWidget(self.language_label, 37, 0, 1, 1)
        self.image_path_text = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.image_path_text.setObjectName("image_path_text")
        self.image_path_text.setPlainText(image_path)
        self.gridLayout.addWidget(self.image_path_text, 60, 0, 1, 1)
        self.language_text = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.language_text.setObjectName("language_text")
        self.language_text.setPlainText(language)
        self.gridLayout.addWidget(self.language_text, 38, 0, 1, 1)
        self.join_settings_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.join_settings_label.setFont(font)
        self.join_settings_label.setObjectName("join_settings_label")
        self.gridLayout.addWidget(self.join_settings_label, 33, 0, 1, 1)
        self.draw_settings_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.draw_settings_label.setFont(font)
        self.draw_settings_label.setObjectName("draw_settings_label")
        self.gridLayout.addWidget(self.draw_settings_label, 55, 0, 1, 1)
        self.spam_settings_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.spam_settings_label.setFont(font)
        self.spam_settings_label.setObjectName("spam_settings_label")
        self.gridLayout.addWidget(self.spam_settings_label, 48, 0, 1, 1)
        self.username_text = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.username_text.setObjectName("username_text")
        self.username_text.setPlainText(only_username)
        self.gridLayout.addWidget(self.username_text, 69, 0, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout.addWidget(self.line_9, 70, 0, 1, 1)
        self.algorithm_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.algorithm_label.setObjectName("algorithm_label")
        self.gridLayout.addWidget(self.algorithm_label, 61, 0, 1, 1)
        self.username_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.username_label.setObjectName("username_label")
        self.gridLayout.addWidget(self.username_label, 68, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 21, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 47, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 12, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 32, 0, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout.addWidget(self.line_8, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 54, 0, 1, 1)
        self.start_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.gridLayout.addWidget(self.start_button, 71, 0, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout.addWidget(self.line_7, 64, 0, 1, 1)
        self.hidden_mode_checkbox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.hidden_mode_checkbox.setText("")
        self.hidden_mode_checkbox.setObjectName("hidden_mode_checkbox")
        if hidden:
            self.hidden_mode_checkbox.setChecked(True)
        self.gridLayout.addWidget(self.hidden_mode_checkbox, 11, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        BubbleBoiLauncher.setCentralWidget(self.centralwidget)
        self.start_button.clicked.connect(self.launched)

        self.retranslateUi(BubbleBoiLauncher)
        QtCore.QMetaObject.connectSlotsByName(BubbleBoiLauncher)

    def retranslateUi(self, BubbleBoiLauncher):
        _translate = QtCore.QCoreApplication.translate
        BubbleBoiLauncher.setWindowTitle(_translate("BubbleBoiLauncher", "BubbleBoiBot v1.92 - Launcher"))
        self.spam_label.setText(_translate("BubbleBoiLauncher", "Message:"))
        self.randomAvatar_checkbox.setText(_translate("BubbleBoiLauncher", "Random Avatar"))
        self.port5003_radio.setText(_translate("BubbleBoiLauncher", "5003"))
        self.one_start_radio.setText(_translate("BubbleBoiLauncher", "1"))
        self.start_times_label.setText(_translate("BubbleBoiLauncher", "Start Times:"))
        self.delay500_radio.setText(_translate("BubbleBoiLauncher", "500ms"))
        self.four_start_radio.setText(_translate("BubbleBoiLauncher", "4"))
        self.delay1250_radio.setText(_translate("BubbleBoiLauncher", "1250ms"))
        self.hidden_mode_label.setText(_translate("BubbleBoiLauncher", "Hidden Mode (Hide tasks in Task Manager):"))
        self.title_label.setText(_translate("BubbleBoiLauncher", "BubbleBoiBot v1.92"))
        self.two_start_radio.setText(_translate("BubbleBoiLauncher", "2"))
        self.delay1000_radio.setText(_translate("BubbleBoiLauncher", "1000ms"))
        self.colour_themes_label.setText(_translate("BubbleBoiLauncher", "Colour Theme:"))
        self.six_start_radio.setText(_translate("BubbleBoiLauncher", "6"))
        self.delay_label.setText(_translate("BubbleBoiLauncher", "Delay (No less than 1000ms for proper chat-log!):"))
        self.emerald_radio.setText(_translate("BubbleBoiLauncher", "Emerald"))
        self.ocean_radio.setText(_translate("BubbleBoiLauncher", "Ocean"))
        self.three_start_radio.setText(_translate("BubbleBoiLauncher", "3"))
        self.five_start_radio.setText(_translate("BubbleBoiLauncher", "5"))
        self.candy_radio.setText(_translate("BubbleBoiLauncher", "Candy"))
        self.fire_radio.setText(_translate("BubbleBoiLauncher", "Fire"))
        self.desert_radio.setText(_translate("BubbleBoiLauncher", "Desert"))
        self.delay250_radio.setText(_translate("BubbleBoiLauncher", "250ms"))
        self.delay750_radio.setText(_translate("BubbleBoiLauncher", "750ms"))
        self.storm_radio.setText(_translate("BubbleBoiLauncher", "Storm"))
        self.yliluoma_radio.setText(_translate("BubbleBoiLauncher", "Yliluoma (Very slow, higher quality)"))
        self.plain_radio.setText(_translate("BubbleBoiLauncher", "Plain"))
        self.cluster_radio.setText(_translate("BubbleBoiLauncher", "Cluster"))
        self.dark_checkbox.setText(_translate("BubbleBoiLauncher", "Dark Mode"))
        self.port5001_radio.setText(_translate("BubbleBoiLauncher", "5001"))
        self.port5002_radio.setText(_translate("BubbleBoiLauncher", "5002"))
        self.search_checkbox.setText(_translate("BubbleBoiLauncher", "Search"))
        self.search_settings_label.setText(_translate("BubbleBoiLauncher", "Search Settings:"))
        self.image_path_label.setText(_translate("BubbleBoiLauncher", "Image path:"))
        self.portAll_radio.setText(_translate("BubbleBoiLauncher", "All"))
        self.port_label.setText(_translate("BubbleBoiLauncher", "Port to attack:"))
        self.doSpam_checkbox.setText(_translate("BubbleBoiLauncher", "Spam Server"))
        self.join_label.setText(_translate("BubbleBoiLauncher", "Join Code (For Private Games):"))
        self.linkFilter_checkbox.setText(_translate("BubbleBoiLauncher", "Link Message Filter (Convert any periods to commas)"))
        self.randomImage_checkbox.setText(_translate("BubbleBoiLauncher", "Random image from images folder"))
        self.shuffle_checkbox.setText(_translate("BubbleBoiLauncher", "Shuffle"))
        self.bot_name_label.setText(_translate("BubbleBoiLauncher", "Bot Name:"))
        self.language_label.setText(_translate("BubbleBoiLauncher", "Language:"))
        self.join_settings_label.setText(_translate("BubbleBoiLauncher", "Join Settings:"))
        self.draw_settings_label.setText(_translate("BubbleBoiLauncher", "Drawing Settings:"))
        self.spam_settings_label.setText(_translate("BubbleBoiLauncher", "Spam Settings:"))
        self.algorithm_label.setText(_translate("BubbleBoiLauncher", "Drawing algorithm:"))
        self.username_label.setText(_translate("BubbleBoiLauncher", "Username to find:"))
        self.start_button.setText(_translate("BubbleBoiLauncher", "Launch"))


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
                    cmd = "loop5001.bat"
                    for x in range(start_times):
                        SW_MINIMIZE = 6
                        info = subprocess.STARTUPINFO()
                        info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                        info.wShowWindow = SW_MINIMIZE
                        subprocess.Popen(cmd, startupinfo=info)
                        t.sleep((delay/1000))
                    cmd = "loop5002.bat"
                    for x in range(start_times):
                        SW_MINIMIZE = 6
                        info = subprocess.STARTUPINFO()
                        info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                        info.wShowWindow = SW_MINIMIZE
                        subprocess.Popen(cmd, startupinfo=info)
                        t.sleep((delay/1000))
                    cmd = "loop5003.bat"
                    for x in range(start_times):
                        SW_MINIMIZE = 6
                        info = subprocess.STARTUPINFO()
                        info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                        info.wShowWindow = SW_MINIMIZE
                        subprocess.Popen(cmd, startupinfo=info)
                        t.sleep((delay/1000))
                else:
                    cmd = "loop5001.bat"
                    for x in range(start_times):
                        SW_HIDE = 0
                        info = subprocess.STARTUPINFO()
                        info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                        info.wShowWindow = SW_HIDE
                        subprocess.Popen(cmd, startupinfo=info)
                        t.sleep((delay/1000))
                    cmd = "loop5002.bat"
                    for x in range(start_times):
                        SW_HIDE = 0
                        info = subprocess.STARTUPINFO()
                        info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                        info.wShowWindow = SW_HIDE
                        subprocess.Popen(cmd, startupinfo=info)
                        t.sleep((delay/1000))
                    cmd = "loop5003.bat"
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
                        cmd = "loop5001.bat"
                        for x in range(start_times):
                            SW_MINIMIZE = 6
                            info = subprocess.STARTUPINFO()
                            info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                            info.wShowWindow = SW_MINIMIZE
                            subprocess.Popen(cmd, startupinfo=info)
                            t.sleep((delay/1000))
                    else:
                        cmd = "loop5001.bat"
                        for x in range(start_times):
                            SW_HIDE = 0
                            info = subprocess.STARTUPINFO()
                            info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                            info.wShowWindow = SW_HIDE
                            subprocess.Popen(cmd, startupinfo=info)
                            t.sleep((delay/1000))
                if SETTINGS["Port"] == 5002:
                    if not hidden:
                        cmd = "loop5002.bat"
                        for x in range(start_times):
                            SW_MINIMIZE = 6
                            info = subprocess.STARTUPINFO()
                            info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                            info.wShowWindow = SW_MINIMIZE
                            subprocess.Popen(cmd, startupinfo=info)
                            t.sleep((delay/1000))
                    else:
                        cmd = "loop5002.bat"
                        for x in range(start_times):
                            SW_HIDE = 0
                            info = subprocess.STARTUPINFO()
                            info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                            info.wShowWindow = SW_HIDE
                            subprocess.Popen(cmd, startupinfo=info)
                            t.sleep((delay/1000))
                if SETTINGS["Port"] == 5003:
                    if not hidden:
                        cmd = "loop5003.bat"
                        for x in range(start_times):
                            SW_MINIMIZE = 6
                            info = subprocess.STARTUPINFO()
                            info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                            info.wShowWindow = SW_MINIMIZE
                            subprocess.Popen(cmd, startupinfo=info)
                            t.sleep((delay/1000))
                    else:
                        cmd = "loop5003.bat"
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


# [New] Python programmed by KyleJamesCatterall#0989.
# GUI Base code generated by pycui5 (pycui5 -x Launcher.ui -o launcher.pyw).

