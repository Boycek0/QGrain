import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler

import qtawesome as qta
from PySide2.QtCore import QTranslator
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication

from QGrain import QGRAIN_ROOT_PATH, QGRAIN_VERSION
from QGrain.ui.ConsolePanel import ConsolePanel


def getdirsize(dir):
    size = 0
    for root, _, files in os.walk(dir):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size

def create_necessary_folders():
    necessary_folders = (os.path.join(os.path.expanduser("~"), "QGrain"), os.path.join(os.path.expanduser("~"), "QGrain", "logs"))
    for folder in necessary_folders:
        if not os.path.exists(folder):
            os.mkdir(folder)

def setup_language(app: QApplication):
    lang = "en"
    trans = QTranslator(app)
    trans.load(os.path.join(QGRAIN_ROOT_PATH, "assets", lang))
    app.installTranslator(trans)

def setup_logging():
    format_str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    file_handler = TimedRotatingFileHandler(os.path.join(os.path.expanduser("~"), "QGrain", "logs", "qgrain.log"), when="D", backupCount=8, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(format_str))
    logging.basicConfig(level=logging.DEBUG, format=format_str)
    logging.getLogger("matplotlib").setLevel(logging.WARNING)
    logging.getLogger().addHandler(file_handler)

def setup_app():
    import matplotlib.pyplot as plt
    # import qtawesome as qta
    from PySide2.QtCore import Qt
    from PySide2.QtGui import QColor
    from PySide2.QtWidgets import QApplication, QSplashScreen, QStyleFactory

    app = QApplication(sys.argv)
    splash = QSplashScreen()
    pixmap = QPixmap(os.path.join(QGRAIN_ROOT_PATH, "assets", "icon.png"))
    pixmap.setDevicePixelRatio(1.0)
    splash.setPixmap(pixmap)
    splash.show()
    # splash.showMessage("Starting QGrain App", Qt.AlignCenter, color=QColor(0x000000))
    create_necessary_folders()
    app.setWindowIcon(qta.icon("fa5s.rocket"))
    app.setApplicationDisplayName(f"QGrain ({QGRAIN_VERSION})")
    app.setApplicationVersion(QGRAIN_VERSION)
    app.setStyle(QStyleFactory.create("Fusion"))
    app.setStyleSheet("""* {font-family:Tahoma,Verdana,Arial,Georgia,"Microsoft YaHei","Times New Roman";
                      color:#000000;background-color:#c4cbcf;alternate-background-color:#b2bbbe;
                      selection-color:#ffffff;selection-background-color:#555f69}""")

    plt.set_cmap("tab10")
    plt.rcParams["axes.facecolor"] = "#c4cbcf"
    plt.rcParams["figure.facecolor"] = "#c4cbcf"
    plt.rcParams["savefig.dpi"] = 300.0
    plt.rcParams["savefig.facecolor"] = "white"
    plt.rcParams["savefig.transparent"] = True
    plt.rcParams["figure.max_open_warning"] = False

    setup_language(app)
    setup_logging()

    return app, splash

def qgrain_console():
    app, splash = setup_app()
    main = ConsolePanel()
    main.show()
    splash.finish(main)
    sys.exit(app.exec_())

if __name__ == "__main__":
    qgrain_console()
