from window_main import window_main
from PySide2 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

main = window_main()
main.show()

sys.exit(app.exec_())
