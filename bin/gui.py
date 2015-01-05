__author__ = 'CAVPP'
#!/usr/bin/python

import sys
from PySide.QtCore import *
from PySide.QtGui import *
import time

from driveSummary.driveSummary import *




class WindowForm(QDialog):

    def generate_report(self):

        if self.data["audio_counter"] != 0:

            if self.data["mp3_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Audio", "MPEG-2 Audio Layer III", ".mp3", str(self.data["mp3_counter"])]))
                # self.stats.addItem("mp3: " + str(self.data["mp3_counter"]))


            if self.data["m4a_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Audio", "", ".m4a", str(self.data["m4a_counter"])]))

            if self.data["mpc_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Audio", "Musepack", ".mpc", str(self.data["mpc_counter"])]))

            if self.data["wave_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Audio", "Waveform Audio File", ".wav", str(self.data["wave_counter"])]))

            if self.data["flac_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Audio", "Free Lossless Audio Codec", ".flac", str(self.data["flac_counter"])]))

            if self.data["ogg_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Audio", "Ogg", ".ogg", str(self.data["ogg_counter"])]))

            if self.data["wma_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Audio", "Windows Media Audio", ".wma", str(self.data["wma_counter"])]))
        if self.data["video_counter"] != 0:
            if self.data["avi_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Video", "Audio Video Interleave", ".avi", str(self.data["avi_counter"])]))

            if self.data["dv_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Video", "DV", ".dv", str(self.data["dv_counter"])]))

            if self.data["mov_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Video", "QuickTime", ".mov", str(self.data["mov_counter"])]))

            if self.data["mp4_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Video", "MPEG-4 Part 14", ".mp4", str(self.data["mp4_counter"])]))

            if self.data["m4v_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Video", "M4V", ".m4v", str(self.data["m4v_counter"])]))

        if self.data["image_counter"] != 0:
            if self.data["tiff_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Image", "Tagged Image File Format", ".tif", str(self.data["tiff_counter"])]))

            if self.data["jpeg_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Image", "JPEG", ".jpg", str(self.data["jpeg_counter"])]))

            if self.data["bmp_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Image", "BMP", ".bmp", str(self.data["bmp_counter"])]))

            if self.data["gif_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Image", "Graphics Interchange Format", ".gif", str(self.data["gif_counter"])]))

            if self.data["png_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Image", "Portable Network Graphics", ".png", str(self.data["png_counter"])]))

        if self.data["document_counter"] != 0:
            if self.data["excel_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Document", "Excel", ".xlsx or .xls", str(self.data["excel_counter"])]))

            if self.data["rtf_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Document", "Rich Text Format", ".rtf", str(self.data["rtf_counter"])]))

            if self.data["txt_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Document", "Text", ".txt", str(self.data["txt_counter"])]))

            if self.data["doc_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Document", "Doc", ".doc", str(self.data["doc_counter"])]))

            if self.data["pdf_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Document", "Portable Document Format", ".pdf", str(self.data["pdf_counter"])]))

    def populate_data(self):
        self.other_files, self.data = get_data("/Volumes/DPLA0002")
        self.generate_report()
        for item in self.stat_items:
            self.stats.addTopLevelItem(item)

        for file_name in self.other_files:
            self.other_files_list.addItem(file_name)

    def __init__(self, parent=None):
        super(WindowForm, self).__init__(parent)
        self.stat_items = []

        self.stats_label = QLabel("Audio, Video, Image, Document Files")
        self.stats = QTreeWidget()
        self.stats.setColumnCount(2)
        self.stats.setHeaderLabels(["Type", "Format", "File Extension", "Number of Files"])

        self.other_files_list = QListWidget()
        self.line_edit = QLineEdit("Here is the Summary of the drive")
        self.other_files_label = QLabel("Non-AV or Image Files")

        layout = QVBoxLayout()
        layout.addWidget(self.stats_label)
        layout.addWidget(self.stats)
        layout.addWidget(self.other_files_label)
        layout.addWidget(self.other_files_list)
        layout.addWidget(self.line_edit)

        self.setLayout(layout)
        self.setWindowTitle("Summary")
        self.populate_data()


def main():
    # app = QApplication(sys.argv)
    #
    # label = QLabel("Hello World")
    # label.setWindowFlags(Qt.SplashScreen)
    # label.show()
    # QTimer.singleShot(10000, app.quit)
    # # time.sleep(2)
    # app.exec_()

    app = QApplication(sys.argv)
    main_window = WindowForm()
    main_window.show()
    app.exec_()


if __name__ == "__main__":
    main()