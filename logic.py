from PyQt5.QtWidgets import QDialog, \
                            QTableWidget, \
                            QSpinBox, \
                            QLabel, \
                            QAbstractItemView
from PyQt5.QtGui import QFont




class MainWindow(QDialog):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1600, 800)
        self.setWindowTitle('Лабораторная 3')
        self.font_label = QFont('Times New Roman', 14)

        # // Create Labels
        self.label_spin_box_row = QLabel('Количество строк', self)
        self.label_spin_box_column = QLabel('Количество столбцов', self)
        # // Moving Labels
        self.label_spin_box_row.move(30, 30)
        self.label_spin_box_column.move(200, 30)
        # // Set fonts to labels
        self.label_spin_box_row.setFont(self.font_label)
        self.label_spin_box_column.setFont(self.font_label)

        # // Create Spin-boxes
        self.spin_box_row = QSpinBox(self)
        self.spin_box_column = QSpinBox(self)
        self.spin_box_row.setMaximum(10)
        self.spin_box_column.setMaximum(10)
        # // Moved Spin-boxes
        self.spin_box_row.move(30, 50)
        self.spin_box_column.move(200, 50)

        # // Tables
        self.table_1 = QTableWidget(self)
        self.table_2 = QTableWidget(self)
        self.table_3 = QTableWidget(self)
        self.table_3.setEditTriggers(QAbstractItemView.EditTrigger(0))# > No Edit Mode

        self.table_1.resize(420, 260)
        self.table_2.resize(420, 260)
        self.table_3.resize(420, 260)

        # // Moving tables
        self.table_1.move(80, 200)
        self.table_2.move(600, 200)
        self.table_3.move(1120, 200)

        # // SIGNALS
        self.spin_box_row.valueChanged.connect(self.editing_tables)
        self.spin_box_column.valueChanged.connect(self.editing_tables)


    def editing_tables(self):
        """Set rows/columns values 0-10 (maximum in spin-box)"""
        self.table_1.setColumnCount(self.spin_box_column.value())
        self.table_1.setRowCount(self.spin_box_row.value())
        self.resize_cells(self.table_1)
        
        self.table_2.setColumnCount(self.spin_box_column.value())
        self.table_2.setRowCount(self.spin_box_row.value())
        self.resize_cells(self.table_2)
        
        self.table_3.setColumnCount(self.spin_box_column.value())
        self.table_3.setRowCount(self.spin_box_row.value())
        self.resize_cells(self.table_3)

    def resize_cells(self, table_name: object):
        for row in range(10):
            table_name.setRowHeight(row, 3)
        for column in range(10):
            table_name.setColumnWidth(column, 3)
                
     
