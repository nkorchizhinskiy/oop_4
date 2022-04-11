from PyQt5.QtWidgets import QDialog, \
                            QTableWidget, \
                            QSpinBox, \
                            QLabel, \
                            QAbstractItemView, \
                            QTableWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox
from decimal import Decimal




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
        
        self.table_1.cellChanged.connect(self.get_values_in_table_1)
        self.table_2.cellChanged.connect(self.get_values_in_table_2)
        

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
    
    def get_values_in_table_1(self, row: int, column: int):
        self.check_values_from_table(self.table_1, row, column)    
        
    def get_values_in_table_2(self, row: int, column: int):
        self.check_values_from_table(self.table_2, row, column)             
     
    def check_values_from_table(self, table_name: object, row: int, column: int):
        if table_name.item(row, column).text() == '':
            pass
        elif table_name.item(row, column).text()[0] == '-':
            try:
                print(float(table_name.item(row, column).text()))
            except Exception as e:
                self.erroneous_input(table_name, row, column)
        else:
            try:
                print(float(table_name.item(row, column).text()))
            except Exception as e:
                self.erroneous_input(table_name, row, column)
        self.is_not_empty_table()
    
    def erroneous_input(self, table_name: object, row: int, column: int):
        '''Method. which operate mistakes from person's input'''
        QMessageBox.warning(self, 'Ошибка!', 'Введите число!')
        table_name.setItem(row, column, QTableWidgetItem(''))
    
    def is_not_empty_table(self):
        empty = False
        for row in range(self.spin_box_row.value()):
            for column in range(self.spin_box_column.value()):
                try:
                    print(self.table_1.item(row, column).text())
                    if self.table_1.item(row, column).text() == '':
                        empty = True
                except AttributeError:
                    empty = True
            print('\n')
        print('\n\n\n')
        for row in range(self.spin_box_row.value()):
            for column in range(self.spin_box_column.value()):
                try:
                    print(self.table_2.item(row, column).text())
                    if self.table_2.item(row, column).text() == '':
                        empty = True
                except AttributeError:
                    empty = True
            print('\n')
        
        if not empty:
            self.count_values_in_tables()
    
    def count_values_in_tables(self):
        for row in range(self.spin_box_row.value()):
            for column in range(self.spin_box_column.value()):
                temp_value = Decimal(self.table_1.item(row, column).text()) + \
                             Decimal(self.table_2.item(row, column).text())
                self.table_3.setItem(row, column, QTableWidgetItem(str(temp_value)))
                
        
        
        
        