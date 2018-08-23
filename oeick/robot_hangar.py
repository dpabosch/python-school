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
        self.hold, self.autohold = False, False
        self.master = master
        self.kw_level = 0

    def conditional_hold_execution(self):
        self.hold = True if self.autohold else self.hold
        while self.hold:
            time.sleep(0.1)

    def start_test(self, name, attributes):
        self.master.print_output("Starte Test '" + name + "'")
        self.conditional_hold_execution()

    def end_test(self, name, attributes):
        self.master.print_output("[" + attributes['status'] + "] fertig mit Test '" + name + "' (" + str(attributes['elapsedtime']) + "ms)")

    def start_keyword(self, name, attributes):
        self.kw_level = self.kw_level + 1
        self.master.print_output(("++"*self.kw_level) + " Starte Keyword '" + name + "'")
        if name == self.master.breakpoint_name.get():
            self.hold = True
            if len(attributes['args']) > 0:
                if attributes['args'][0] == 'Step':
                    self.autohold = True
        self.conditional_hold_execution()

    def end_keyword(self, name, attributes):
        self.master.print_output(("--"*self.kw_level) + " [" + attributes['status'] + "] fertig mit Keyword '" +
                                 name + "' (" + str(attributes['elapsedtime']) + "ms)")
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

        run_frame = Frame(root)
        run_frame.grid(column=0, row=2, columnspan=3)

        start_btn = Button(run_frame, text='Start', command=self.run_suite_thread)
        start_btn.grid(column=0, row=0)

        step_btn = Button(run_frame, text='Step', command=self.continue_suite)
        step_btn.grid(column=1, row=0)

        stop_btn = Button(run_frame, text='Stop')
        stop_btn.grid(column=2, row=0)

        self.breakpoint_name = Entry(run_frame)
        self.breakpoint_name.insert(0, 'Breakpoint')
        self.breakpoint_name.grid(column=3, row=0)

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

        self.output_text = Text(root, height=30, width=120)
        self.output_text.grid(column=0, row=7, columnspan=4)

        output_scroller = Scrollbar(root, command=self.output_text.yview)
        self.output_text['yscrollcommand'] = output_scroller.set
        output_scroller.grid(column=4, row=7, sticky='nsew')

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
            self.print_output("Test Suite '{}' geladen".format(self.suite_filename))
            self.print_output("    beinhaltet folgende Tests:")
            for t in self.suite.tests:
                self.print_output("      - '{}'".format(t))

    def run_suite_thread(self):
        t = Thread(target=self.run_suite)
        t.start()
        self.print_output('Bearbeitung der Suite gestartet.')

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
