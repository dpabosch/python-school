# coding=utf-8

from robot.api import TestSuiteBuilder
from robot.api import ResultWriter
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from threading import Thread
import time


class RFListener:
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self, master):
        self.hold = True
        self.master = master
        self.kw_level = 0

    def hold_execution(self):
        self.hold = True
        while self.hold:
            time.sleep(0.1)

    def start_test(self, name, attributes):
        self.master.print_output("Starte Test '" + name + "'")
        self.hold_execution()

    def end_test(self, name, attributes):
        self.master.print_output("fertig mit Test '" + name + "' (" + str(attributes['elapsedtime']) + "ms)")

    def start_keyword(self, name, attributes):
        self.kw_level = self.kw_level + 1
        self.master.print_output(("++"*self.kw_level) + " Starte Keyword '" + name + "'")
        self.hold_execution()

    def end_keyword(self, name, attributes):
        self.master.print_output(("--"*self.kw_level) + " fertig mit Keyword '" + name + "' (" + str(attributes['elapsedtime']) + "ms)")
        self.kw_level = self.kw_level - 1


class Hangar(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        self.suite_filename = None
        self.suite = None
        self.result = None
        self.robot_listener = RFListener(self)
        self.output_name = 'output.xml'

        load_btn = Button(root, text='Test Suite laden', command=self.load_suite)
        load_btn.grid(column=0, row=1)
        self.suite_name_lbl = Label(root, text="(keine Suite geladen)")
        self.suite_name_lbl.grid(column=1, row=1)
        start_btn = Button(root, text='Start', command=self.run_suite_thread)
        start_btn.grid(column=0, row=2)
        step_btn_lbl = Button(root, text='Step', command=self.continue_suite)
        step_btn_lbl.grid(column=1, row=2)
        stop_btn_lbl = Button(root, text='Stop')
        stop_btn_lbl.grid(column=2, row=2)

        save_report_btn = Button(root, text='Report', command=self.save_report)
        save_report_btn.grid(column=0, row=3)
        self.report_name_lbl = Label(root, text="robot_hangar_report.html")
        self.report_name_lbl.grid(column=1, row=3)

        save_log_btn = Button(root, text='Log', command=self.save_log)
        save_log_btn.grid(column=0, row=4)
        self.log_name_lbl = Label(root, text="robot_hangar_log.html")
        self.log_name_lbl.grid(column=1, row=4)

        save_xunit_btn = Button(root, text='XUnit', command=self.save_xunit)
        save_xunit_btn.grid(column=0, row=5)
        self.xunit_name_lbl = Label(root, text="robot_hangar_xunit.xml")
        self.xunit_name_lbl.grid(column=1, row=5)

        save_results_btn = Button(root, text='Save Results', command=self.save_results)
        save_results_btn.grid(column=0, row=6)

        self.output_text = Text(root, height=20, width=120)
        self.output_text.grid(column=0, row=7, columnspan=4, rowspan=12)

    def load_suite(self):
        selected_filename = askopenfilename(filetypes=(
            ("Robot Framework", "*.robot"),
            ("Text File", "*.txt"),
            ("Alles", "*.*")
        ))
        if selected_filename:
            self.suite_filename = selected_filename
            self.suite_name_lbl['text'] = self.suite_filename
            self.suite = TestSuiteBuilder().build(r'listener_test.robot')

    def run_suite_thread(self):
        t = Thread(target=self.run_suite)
        t.start()

    def run_suite(self):
        self.result = self.suite.run(critical='smoke',
                                output=self.output_name,
                                listener=self.robot_listener,
                                console='quiet')

    def continue_suite(self):
        self.robot_listener.hold = False

    def save_report(self):
        filename = asksaveasfilename()
        if filename:
            self.report_name_lbl['text'] = filename

    def save_log(self):
        filename = asksaveasfilename()
        if filename:
            self.log_name_lbl['text'] = filename

    def save_xunit(self):
        filename = asksaveasfilename()
        if filename:
            self.xunit_name_lbl['text'] = filename

    def save_results(self):
        ResultWriter(self.output_name).write_results(
            report=self.report_name_lbl['text'],
            log=self.log_name_lbl['text'],
            xunit=self.xunit_name_lbl['text']
        )

    def print_output(self, output_text):
        self.output_text.insert(END, output_text + '\n')


if __name__ == '__main__':
    root = Tk()
    application = Hangar(root)
    application.mainloop()
