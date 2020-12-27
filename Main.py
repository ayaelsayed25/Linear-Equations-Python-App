from PyQt5 import QtCore, QtGui, QtWidgets
import gc
from JacobiGaussSeidel import *

dimension = 3
method = 0
readX = False


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(848, 584)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 248, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 248, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 248, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 248, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, MainWindow.width(), MainWindow.height()))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.title = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 0, 1, 1)
        self.toolsGrid = QtWidgets.QGridLayout()
        self.toolsGrid.setObjectName("toolsGrid")
        self.method_combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.method_combo.setModelColumn(0)
        self.method_combo.setObjectName("method_combo")
        self.method_combo.addItem("")
        self.method_combo.addItem("")
        self.method_combo.addItem("")
        self.method_combo.addItem("")
        self.method_combo.addItem("")
        self.method_combo.addItem("")
        self.method_combo.currentIndexChanged.connect(self.on_method_changed)
        self.toolsGrid.addWidget(self.method_combo, 1, 1, 1, 1)
        self.iterations_number = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.iterations_number.setProperty("value", 3)
        self.iterations_number.setObjectName("iterations_number")
        self.toolsGrid.addWidget(self.iterations_number, 7, 1, 1, 1)
        self.methods_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.methods_label.setObjectName("methods_label")
        self.toolsGrid.addWidget(self.methods_label, 1, 0, 1, 1)
        self.decomposition_method_combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.decomposition_method_combo.setObjectName("decomposition_method_combo")
        self.decomposition_method_combo.addItem("")
        self.decomposition_method_combo.addItem("")
        self.decomposition_method_combo.addItem("")
        self.toolsGrid.addWidget(self.decomposition_method_combo, 5, 1, 1, 1)
        self.significant_figures_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.significant_figures_label.setObjectName("significant_figures_label")
        self.toolsGrid.addWidget(self.significant_figures_label, 4, 0, 1, 1)
        self.paremters_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.paremters_label.setObjectName("paremters_label")
        self.toolsGrid.addWidget(self.paremters_label, 5, 0, 1, 1)
        self.absolute_erroe_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.absolute_erroe_label.setObjectName("absolute_erroe_label")
        self.toolsGrid.addWidget(self.absolute_erroe_label, 6, 0, 1, 1)
        self.significant_figures_spin = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.significant_figures_spin.setProperty("value", 3)
        self.significant_figures_spin.setObjectName("significant_figures_spin")
        self.toolsGrid.addWidget(self.significant_figures_spin, 4, 1, 1, 1)
        self.dimensionA_spin = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.dimensionA_spin.setProperty("value", 3)
        self.dimensionA_spin.setObjectName("dimensionA_spin")
        self.toolsGrid.addWidget(self.dimensionA_spin, 0, 1, 1, 1)
        self.matrixA_dimen = QtWidgets.QLabel(self.gridLayoutWidget)
        self.matrixA_dimen.setObjectName("matrixA_dimen")
        self.toolsGrid.addWidget(self.matrixA_dimen, 0, 0, 1, 1)
        self.iterations_number_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.iterations_number_label.setObjectName("iterations_number_label")
        self.toolsGrid.addWidget(self.iterations_number_label, 7, 0, 1, 1)
        self.absolute_relative_error_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.absolute_relative_error_text.setObjectName("absolute_relative_error_text")
        self.toolsGrid.addWidget(self.absolute_relative_error_text, 6, 1, 1, 1)
        self.gridLayout.addLayout(self.toolsGrid, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.calculate_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.calculate_button.setFont(font)
        self.calculate_button.setObjectName("calculate_button")
        self.calculate_button.clicked.connect(self.readMatrices)
        self.gridLayout_2.addWidget(self.calculate_button, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.MatricesGrid = QtWidgets.QHBoxLayout()
        self.MatricesGrid.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.MatricesGrid.setObjectName("MatricesGrid")
        self.matrixA_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.matrixA_label.setObjectName("matrixA_label")
        self.MatricesGrid.addWidget(self.matrixA_label)
        self.MatrixAGrid = QtWidgets.QGridLayout()
        self.MatrixAGrid.setObjectName("MatrixAGrid")
        self.A00 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.A00.setObjectName("A00")
        self.MatrixAGrid.addWidget(self.A00, 0, 0, 1, 1)
        self.A01 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.A01.setObjectName("A01")
        self.MatrixAGrid.addWidget(self.A01, 0, 1, 1, 1)
        self.A02 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.A02.setObjectName("A02")
        self.MatrixAGrid.addWidget(self.A02, 0, 2, 1, 1)

        self.A11 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.A11.setObjectName("A11")
        self.MatrixAGrid.addWidget(self.A11, 1, 1, 1, 1)
        self.A20 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.A20.setObjectName("A20")
        self.MatrixAGrid.addWidget(self.A20, 2, 0, 1, 1)

        self.A12 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.A12.setObjectName("A12")
        self.MatrixAGrid.addWidget(self.A12, 1, 2, 1, 1)
        self.A21 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.A21.setObjectName("A21")
        self.MatrixAGrid.addWidget(self.A21, 2, 1, 1, 1)
        self.A10 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.A10.setObjectName("A10")
        self.MatrixAGrid.addWidget(self.A10, 1, 0, 1, 1)
        self.A22 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.A22.setObjectName("A22")
        self.MatrixAGrid.addWidget(self.A22, 2, 2, 1, 1)
        self.MatricesGrid.addLayout(self.MatrixAGrid)
        self.matrixB_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.matrixB_label.setObjectName("matrixB_label")
        self.MatricesGrid.addWidget(self.matrixB_label)
        self.MatrixB_grid = QtWidgets.QVBoxLayout()
        self.MatrixB_grid.setObjectName("MatrixB_grid")
        self.B0 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.B0.setObjectName("B0")
        self.MatrixB_grid.addWidget(self.B0)
        self.B1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.B1.setObjectName("B1")
        self.MatrixB_grid.addWidget(self.B1)
        self.B2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.B2.setObjectName("B2")
        self.MatrixB_grid.addWidget(self.B2)
        self.MatricesGrid.addLayout(self.MatrixB_grid)
        self.matrixX_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.matrixX_label.setObjectName("matrixX_label")
        self.MatricesGrid.addWidget(self.matrixX_label)
        self.MatrixX_grid = QtWidgets.QVBoxLayout()
        self.MatrixX_grid.setObjectName("MatrixX_grid")
        self.X0 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.X0.setObjectName("X0")
        self.MatrixX_grid.addWidget(self.X0)
        self.X1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.X1.setObjectName("X1")
        self.MatrixX_grid.addWidget(self.X1)
        self.X2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.X2.setObjectName("X2")
        self.MatrixX_grid.addWidget(self.X2)
        self.MatricesGrid.addLayout(self.MatrixX_grid)
        self.gridLayout.addLayout(self.MatricesGrid, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        size = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, size.width() - 20, size.height() - 100))
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.showMaximized()
        self.reset()

        # MainWindow.setFixedSize(self.gridLayoutWidget.sizeHint())
        self.dimensionA_spin.valueChanged.connect(self.dimension_changed)
        self.newDimension = 3
        self.prevDimension = 3
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def reset(self):
        global readX
        readX = False
        self.decomposition_method_combo.setVisible(False)
        self.paremters_label.setVisible(False)
        self.absolute_erroe_label.setVisible(False)
        self.absolute_relative_error_text.setVisible(False)
        self.iterations_number.setVisible(False)
        self.iterations_number_label.setVisible(False)

    def on_method_changed(self, index):
        # number of method to be executed
        global method
        method = index
        if index == 3:
            self.reset()
            self.decomposition_method_combo.setVisible(True)
            self.paremters_label.setVisible(True)
        elif index == 4 or index == 5:
            self.reset()
            self.absolute_erroe_label.setVisible(True)
            self.absolute_relative_error_text.setVisible(True)
            self.iterations_number.setVisible(True)
            self.iterations_number_label.setVisible(True)
        else:
            self.reset()

    def dimension_changed(self):
        global dimension
        self.newDimension = self.dimensionA_spin.value()
        if self.newDimension > dimension:
            for i in range(0, self.newDimension):
                temp = QtWidgets.QLineEdit(self.gridLayoutWidget)
                temp.setObjectName("A" + str(i) + str(self.newDimension - 1))
                self.MatrixAGrid.addWidget(temp, i, self.newDimension - 1, 1, 1)

            for i in range(0, self.newDimension - 1):
                temp = QtWidgets.QLineEdit(self.gridLayoutWidget)
                temp.setObjectName("A" + str(self.newDimension - 1) + str(i))
                self.MatrixAGrid.addWidget(temp, self.newDimension - 1, i, 1, 1)
            temp = QtWidgets.QLineEdit(self.gridLayoutWidget)
            temp.setObjectName("B" + str(self.newDimension - 1))
            self.MatrixB_grid.addWidget(temp)
            temp = QtWidgets.QLineEdit(self.gridLayoutWidget)
            temp.setObjectName("X" + str(self.newDimension - 1))
            self.MatrixX_grid.addWidget(temp)
        else:
            for i in range(0, self.newDimension + 1):
                temp = self.gridLayoutWidget.findChild(QtWidgets.QLineEdit, "A" + str(i) + str(self.newDimension))
                temp.setParent(None)
                del temp

            for i in range(0, self.newDimension):
                temp = self.gridLayoutWidget.findChild(QtWidgets.QLineEdit, "A" + str(self.newDimension) + str(i))
                temp.setParent(None)
                del temp

            temp = self.gridLayoutWidget.findChild(QtWidgets.QLineEdit, "B" + str(self.newDimension))
            temp.setParent(None)
            del temp
            temp = self.gridLayoutWidget.findChild(QtWidgets.QLineEdit, "X" + str(self.newDimension))
            temp.setParent(None)
            del temp
            gc.collect()
        dimension = self.newDimension

    def readMatrices(self):
        global dimension
        self.matrixA = [[0 for x in range(dimension)] for y in range(dimension)]
        self.matrixB = [0 for x in range(dimension)]
        for i in range(0, dimension):
            for j in range(0, dimension):
                # print("A" + str(i) + str(j))
                temp = self.gridLayoutWidget.findChild(QtWidgets.QLineEdit, "A" + str(i) + str(j)).text()
                if temp != '':
                    self.matrixA[i][j] = int(temp)
        for i in range(0, dimension):
            temp = self.gridLayoutWidget.findChild(QtWidgets.QLineEdit, "B" + str(i)).text()
            if (temp != ''):
                self.matrixB[i] = int(temp)
        if method == 5 or method == 4:
            self.matrixX = [0 for x in range(dimension)]
            for i in range(0, dimension):
                self.matrixX[i] = int(
                    self.gridLayoutWidget.findChild(QtWidgets.QLineEdit, "X" + str(i)).text())
            # print(self.matrixX)
        self.executeMethod()

    def executeMethod(self):
        # if(method==0):
        # elif(method==1):
        # elif (method == 2):
        # elif (method == 3):
        numberOfIterations = self.iterations_number.value()
        if (method == 4):
            gauss_seidel(dimension, numberOfIterations, self.matrixA, self.matrixB, self.matrixX)
            show_result(numberOfIterations, dimension)

        elif (method == 5):
            jacobi(dimension, numberOfIterations, self.matrixA, self.matrixB, self.matrixX)
            show_result(numberOfIterations, dimension)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Solving System of Linear Equations"))
        self.method_combo.setCurrentText(_translate("MainWindow", "Gauss Elimination"))
        self.method_combo.setItemText(0, _translate("MainWindow", "Gauss Elimination"))
        self.method_combo.setItemText(1, _translate("MainWindow", "Gaus Jordan Elimination using pivoting"))
        self.method_combo.setItemText(2, _translate("MainWindow", "Gauss Jordan"))
        self.method_combo.setItemText(3, _translate("MainWindow", "LU Decompostion"))
        self.method_combo.setItemText(4, _translate("MainWindow", "Gauss Siedel"))
        self.method_combo.setItemText(5, _translate("MainWindow", "Jacobi Iteration"))
        self.methods_label.setText(_translate("MainWindow", "Method :"))
        self.decomposition_method_combo.setItemText(0, _translate("MainWindow", "Downlittle Form"))
        self.decomposition_method_combo.setItemText(1, _translate("MainWindow", "Crout Form"))
        self.decomposition_method_combo.setItemText(2, _translate("MainWindow", "Cholesky Form"))
        self.significant_figures_label.setText(_translate("MainWindow", "Number of Significant Figures :"))
        self.paremters_label.setText(_translate("MainWindow", "Method of decomposition :"))
        self.absolute_erroe_label.setText(_translate("MainWindow", "Absolute Relative Error :"))
        self.matrixA_dimen.setText(_translate("MainWindow", "Number of variables ( Dimension of A )"))
        self.iterations_number_label.setText(_translate("MainWindow", "Number of iterations :"))
        self.calculate_button.setText(_translate("MainWindow", "Calculate"))
        self.matrixA_label.setText(_translate("MainWindow", "Coefficient Matrix A :"))
        self.matrixB_label.setText(_translate("MainWindow", "Constant Matrix B :"))
        self.matrixX_label.setText(_translate("MainWindow", "Initial Guess X :"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
