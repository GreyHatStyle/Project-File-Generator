from tkinter import messagebox
from Format_Control import Main_Format_Handle
from PyQt6.QtWidgets import QFileDialog,QWidget,QLabel,QProgressBar
from time import sleep

from docx import Document
class Ui_util_Handle:
    def __init__(self, detail_txt: list, system_dct: dict):

        self.index = 0
        self.FilesList = []
        self.address = ""
        self.list_size = 0
        self.detail_listTxt = detail_txt
        self.sys_dct = system_dct
        self.document = Document()

        # Start
        self.startDoc = Main_Format_Handle(doc=self.document, 
                                        BefIpList=[system_dct['bef_ip'][0],system_dct['bef_op'][0]], 
                                        GenFont=[system_dct['gen_font'][0],system_dct['gen_font'][1],False], 
                                        headFootList=[system_dct['header_footer'][0],system_dct['header_footer'][1]])
        


    def next_data_transfer_util(self, details_pg3: list, bold_lst :list, label: QLabel, pg_bar: QProgressBar, mode: str):
        """
        Essential role:
        - Takes files list, and **display it on label** on by one.
        - After taking input of first file, it will display next file.
        - Sends data to "Main_Format_Handle" class, for further execution
        - Increase *progress bar* value.
        - Display "Completed" message, after all files are done is list.

        """
        # details list: ['ques','ip', 'freq', 'font']

        file = self.FilesList[self.index]


        # To display Label
        if (self.index + 1 != self.list_size):
            lst = self.FilesList[self.index+1].split("\\")
            label.setText(lst[-1])

        
        print(f"self.index: {self.index}, self.listsize: {self.list_size} CURRENT INDEX")
        pg_bar.setValue(80)

        self.startDoc.NextQues_PushB_Func(
            detail_list=self.detail_listTxt, 
            detail_fsty=self.sys_dct['gen_font'][0], detail_fsize=self.sys_dct['gen_font'][1], detail_boldd=bold_lst[0],
            bef_ip_fsize=self.sys_dct['bef_ip'][1], bef_ip_bold=bold_lst[1],
            file_address=file,
            bef_op_fsize=self.sys_dct['bef_op'][1], bef_op_bold=bold_lst[2],
            count=int(details_pg3[2]), 
            ipString=details_pg3[1], 
            opc_fSize=details_pg3[-1], opc_bold=bold_lst[3], question_=details_pg3[0],
            pg_bar2=pg_bar,
            mode = mode
        )

        self.index += 1

        
        sleep(0.1)
        pg_bar.setValue(90)
        if self.index == self.list_size:
            print(f"self.index: {self.index}, self.listsize: {self.list_size} STOPPEd!")
            messagebox.showinfo("Completed!", "All files in folders are completed!\nClick on 'Create' button")
            return True
        
        return False
    
    def save_file_1(self):
        
        file, _ = QFileDialog.getSaveFileName(QWidget(), "Save File Window title", 
                                              f"{self.address}\\{self.detail_listTxt[0]} DMP.docx", "Docx Files (*.docx)")
        if file=="":
            messagebox.showerror("Error!", "No path selected")
            return
        
        self.startDoc.Save_File_Func(file)
        



        
        
