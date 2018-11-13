from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import time

while True:
    try:

        # file reading-
        colorF = open("col.txt", "r")
        col = colorF.read()
        colorF.close()

        _format_ = open("format.txt", "r")
        frmt = _format_.read()
        _format_.close()

        Tranparency = open("transparency.txt", "r")
        trnprncy = Tranparency.read()
        Tranparency.close()

        tranLen = len(trnprncy)

        makeTrans = 3

        if tranLen is 3:
            makeTrans = 0.9
        elif tranLen is 2:
            makeTrans = 3.0

        # Window Config
        root = Tk()
        root.geometry('575x350')
        root.title("CPSC CALC")

        colLen = len(col)

        if colLen == 0:
            col = None

        root.attributes("-alpha", makeTrans)
        root.config(background=col)
        root.resizable(False, False)

        icon = PhotoImage(file='origin.ico')
        root.tk.call('wm', 'iconphoto', root._w, icon)

        # GUI
        heading = Label(root, text="CPSC CALC", bg='dark green', fg='light gray', font='times 15 bold').pack(fill='x')

        ct_marks = DoubleVar()
        ob_marks = DoubleVar()
        second_t = DoubleVar()
        subject = IntVar()
        gpa = IntVar()

        termEnd = DoubleVar()
        termEndMCQ = DoubleVar()
        ctMCQ = DoubleVar()
        ctCQ = DoubleVar()

        fPaperExmaMarks = StringVar()
        sPaperExmaMarks = StringVar()

        hExamMarks = StringVar()
        fExamMarks = StringVar()

        State = "normal"
        State2 = "disabled"
        num = 0

        Canvas(root, width=100, height=292, bg='light gray', highlightthickness=0).place(x=470, y=34)

        Canvas(root, width=1, height=292, bg='black', highlightthickness=0).place(x=466, y=34)
        Canvas(root, width=572, height=1, bg='black', highlightthickness=0).place(x=1, y=31)

        Label(root, text="Current Mode", bg="light gray", fg='dark green').place(x=482, y=270)
        Label(root, text="CPSC Mode", bg="light gray", fg='dark blue').place(x=487, y=290)

        Input = Label(root, text='Input', font='times 15', fg='dark blue', bg=col).place(x=30, y=45)
        Label(root, text="Output", fg="dark red", font='times 15', bg=col).place(x=30, y=220)

        Label(root, text='Enter Obtained Marks        ', font='times 13', bg=col).place(x=45, y=95)
        Label(root, text='Enter CT Marks\t         ', font='times 13', bg=col).place(x=45, y=120)
        Label(root, text='Enter Subject Code\t         ', font='times 13', bg=col, state='normal').place(x=45, y=70)
        Label(root, text='Enter 2nd Obtained Marks ', font='times 13', state=State2, bg=col).place(x=45, y=145)

        ttk.Entry(root, textvariable=ob_marks, width=23).place(x=265, y=97)
        ttk.Entry(root, textvariable=ct_marks, width=23, state=State).place(x=265, y=120)
        ttk.Entry(root, textvariable=subject, width=23, state='normal').place(x=265, y=74)
        ttk.Entry(root, textvariable=second_t, width=23, state=State2).place(x=265, y=145)

        Label(root, text="Final Marks: ", font='times 13', bg=col).place(x=40, y=250)
        entry = ttk.Entry(root, width=23, state="readonly")
        entry.place(x=135, y=252)

        Label(root, text="GPA            : ", font='times 13', bg=col).place(x=40, y=275)
        entry = ttk.Entry(root, width=23, state="readonly")
        entry.place(x=135, y=277)


        def canvases(command):
            Canvas(root, width=205, height=1, bg='black', highlightthickness=0).place(x=90, y=235)
            Canvas(root, width=1, height=77, bg='black', highlightthickness=0).place(x=295, y=235)
            Canvas(root, width=1, height=77, bg='black', highlightthickness=0).place(x=27, y=235)
            Canvas(root, width=269, height=1, bg='black', highlightthickness=0).place(x=27, y=312)

            Canvas(root, width=357, height=1, bg='black', highlightthickness=0).place(x=76, y=60)
            Canvas(root, width=1, height=130, bg='black', highlightthickness=0).place(x=433, y=60)
            Canvas(root, width=1, height=130, bg='black', highlightthickness=0).place(x=27, y=60)
            Canvas(root, width=170, height=1, bg='black', highlightthickness=0).place(x=27, y=190)
            Canvas(root, width=159, height=1, bg='black', highlightthickness=0).place(x=275, y=190)

            ttk.Button(root, text='Enter', command=command).place(x=198, y=177)

        def process():

            # Mainly makes overall marks with ct_marks & ob_marks
            
            while True:
                try:

                    total_marks = 0
                    exam_marks = 0
                    ct_process = 0

                    marks50_list = {154, 155, 148, 147, 102, 108}
                    marks100_list = {101, 107, 109, 127, 134, 151, 111, 112, 113, 114, 150}

                    if ob_marks.get() == 0:
                        final_marks = ct_marks.get() / 2
                    elif ct_marks.get() == 0:
                        final_marks = (ob_marks.get() * 90) / 100
                    else:
                        pass

                    if subject.get() in marks50_list:

                        total_marks += 50

                        exam_marks = ob_marks.get() * .9
                        ct_process = ct_marks.get() / 4

                    elif subject.get() in marks100_list:

                        total_marks += 100

                        _90_parct = total_marks - 10

                        exam_marks = (ob_marks.get() * _90_parct) / total_marks
                        ct_process = ct_marks.get() / 2

                    else:
                        tkinter.messagebox.showerror("CPSC CALC", "Subject you entered was not found in the dictionary")

                    final_marks = exam_marks + ct_process

                    parcentage = final_marks*100 / total_marks


                    if parcentage>=80:
                        n_gpa = 5
                    elif parcentage >= 70 and parcentage <= 79.9:
                        n_gpa = 4
                    elif parcentage >= 60 and parcentage <= 69.9:
                        n_gpa = 3.5
                    elif parcentage >= 50 and parcentage<= 59.9:
                        n_gpa = 3
                    elif parcentage >= 40 and parcentage <= 49.9:
                        n_gpa = 2
                    elif parcentage >= 33 and parcentage <= 39.9:
                        n_gpa = 1
                    else:
                        n_gpa = 0

                    if parcentage > 100:
                        final_marks = 0
                        n_gpa = 0

                    Label(root, text="Final Marks: ", font='times 13', bg=col).place(x=40, y=250)
                    _entry = ttk.Entry(root, width=23)
                    _entry.insert(0, str(final_marks))
                    _entry.configure(state="readonly")
                    _entry.place(x=135, y=252)

                    Label(root, text="GPA\t\t\t: ", font='times 13', bg=col).place(x=40, y=275)
                    _entry_ = ttk.Entry(root, width=23)
                    _entry_.insert(END, str(n_gpa))
                    _entry_.configure(state="readonly")
                    _entry_.place(x=135, y=277)

                    # file witting for history-

                    file_r = open("a.txt", "r")
                    text_r = file_r.read()
                    file_r.close()

                    history_list = []
                    history_list.append("Subject Code : " + str(subject.get()) + " ; Marks : " +
                                        str(final_marks) + " ; GPA : " + str(n_gpa) + ' ; Date: ' + str(time.asctime()) + "\n\n" + text_r)

                    history_list = history_list[::-1]

                    file = open("a.txt", 'w')
                    for element in history_list:
                        file.write(element)
                    file.close()

                    return final_marks, n_gpa
                    break

                except ZeroDivisionError:
                    pass
                    break

                except FileNotFoundError:
                    __file__ = open("a.txt", 'w')
                    __file__.write("Subject Code : " + str(subject.get()) + " ; Marks : " +
                                   str(final_marks) + " ; GPA : " + str(n_gpa) + ' ; Date: ' + str(time.asctime()))
                    __file__.close()
                    
                    break

                except ValueError:
                    tkinter.messagebox.showerror("CPSC CALC", "Invalid Input(Alpha)")
                    break


        def calculate():
            final_cq = (termEnd.get() * 90) / 100
            final_mcq = (termEndMCQ.get() * 90) / 100
            final_ctcq = (ctCQ.get() * 5) / 10
            final_ctmcq = (ctMCQ.get() * 5) / 10

            super_final_mcq = final_mcq + final_ctmcq
            super_final_cq = final_ctcq + final_cq

            mcq_perct = (super_final_mcq / 30) * 100
            cq_perct = (super_final_cq / 70) * 100

            ans = final_cq + final_mcq + final_ctcq + final_ctmcq


            n_gpa = 0

            if mcq_perct >= 45 and cq_perct >= 45:
                if ans >= 80:
                    n_gpa = 5
                elif ans >= 70 and ans <= 79.9:
                    n_gpa = 4
                elif ans >= 60 and ans <= 69.9:
                    n_gpa = 3.5
                elif ans >= 50 and ans <= 59.9:
                    n_gpa = 3
                elif ans >= 40 and ans <= 49.9:
                    n_gpa = 2
                elif ans >= 33 and ans <= 39.9:
                    n_gpa = 1
                else:
                    n_gpa = 0
            else:
                n_gpa = 0

            if termEnd.get() > 70 or termEndMCQ.get() > 30 or ctCQ.get() > 10 or ctMCQ.get() > 10:
                ans = 0
                n_gpa = 0

            result_entry = ttk.Entry(root, width=23)
            result_entry.insert(END, str(ans))
            result_entry.config(state='readonly')
            result_entry.place(x=135, y=252)

            result_entry_gpa = ttk.Entry(root, width=23)
            result_entry_gpa.insert(END, str(n_gpa))
            result_entry_gpa.config(state='readonly')
            result_entry_gpa.place(x=135, y=277)


        def averaging():

            #It is the function of the Average Mode.

            while True:
                try:

                    total_marks = 0
                    
                    average_marks = (ob_marks.get() + second_t.get()) / 2

                    if ob_marks.get() == 0 and second_t.get() == 0:
                        average_marks = 0

                    marks50_list = {154, 155, 148, 147, 102, 108}
                    marks100_list = {101, 107, 109, 127, 134, 151, 111, 112, 113, 114, 150}

                    if subject.get() in marks50_list:
                        total_marks += 50
                    elif subject.get() in marks100_list:
                        total_marks += 100
                    else:
                        tkinter.messagebox.showerror("CPSC CALC", "Subject you entered was not found in dictionary")

                    parcentage = average_marks*100 / total_marks

                    if parcentage >= 80:
                        n_gpa = 5
                    elif parcentage >= 70 and parcentage <= 79.9:
                        n_gpa = 4
                    elif parcentage>=60 and parcentage<=69.9:
                        n_gpa = 3.5
                    elif parcentage>=50 and parcentage<=59.9:
                        n_gpa = 3
                    elif parcentage>=40 and parcentage<=49.9:
                        n_gpa = 2
                    elif parcentage>=33 and parcentage<=39.9:
                        n_gpa = 1
                    else:
                        n_gpa = 0

                    if parcentage > 100:
                        average_marks = 0
                        n_gpa = 0
                        
                    Label(root, text="Final Marks: ", font='times 13', bg=col).place(x=40, y=250)
                    _entry = ttk.Entry(root, width=23)
                    _entry.insert(END, str(average_marks))
                    _entry.configure(state="readonly")
                    _entry.place(x=135, y=252)

                    Label(root, text="GPA            : ", font='times 13', bg=col).place(x=40, y=275)
                    _entry_ = ttk.Entry(root, width=23)
                    _entry_.insert(END, str(n_gpa))
                    _entry_.configure(state="readonly")
                    _entry_.place(x=135, y=277)
                    
                    _entry.place(x=135, y=252)

                    return average_marks, n_gpa
                    break
                except ValueError:
                    tkinter.messagebox.showerror("CPSC CALC", "Invalid Input(Alpha)")
                    break
                except ZeroDivisionError:
                    pass
                    break

        def addition():

            while True:

                try:
                
                    splitted_marks = hExamMarks.get().split()
                    listLen = len(splitted_marks)

                    fSplittedMarks = fExamMarks.get().split()
                    fListLen = len(fSplittedMarks)

                    fPaperSplitted = fPaperExmaMarks.get().split()
                    fPaperLen = len(fPaperSplitted)

                    sPaperSplitted = sPaperExmaMarks.get().split()
                    sPaperLen = len(sPaperSplitted)

                    fPSummation = 0
                    fPtotalGPA = 0

                    for fpNums in fPaperSplitted:

                        fPMakeFloat = float(fpNums)

                        fPSummation += fPMakeFloat

                        fPParcent = fPSummation*100 / 150

                        if fPParcent > 100:
                            fPSummation = 0
                            fPParcent = 0

                        if fPParcent >= 80:
                            fPtotalGPA = 5
                        elif fPParcent >= 70 and fPParcent <= 79.9:
                            fPtotalGPA = 4
                        elif fPParcent >= 60 and fPParcent <= 69.9:
                            fPtotalGPA = 3.5
                        elif fPParcent >= 50 and fPParcent <= 59.9:
                            fPtotalGPA = 3
                        elif fPParcent >= 40 and fPParcent <= 49.9:
                            fPtotalGPA = 2
                        elif fPParcent >= 33 and fPParcent <= 39.9:
                            fPtotalGPA = 1
                        else:
                            fPtotalGPA = 0

                    sPSummation = 0
                    sPtotalGPA = 0

                    for spNums in sPaperSplitted:
                        
                        sPMakeFloat = float(spNums)

                        sPSummation += sPMakeFloat

                        sPParcent =  sPSummation*100 / 150

                        if sPParcent > 100:
                            sPSummation = 0
                            sPParcent = 0

                        if sPParcent>=80:
                            sPtotalGPA = 5
                        elif sPParcent>=70 and sPParcent<=79.9:
                            sPtotalGPA = 4
                        elif sPParcent>=60 and sPParcent<=69.9:
                            sPtotalGPA = 3.5
                        elif sPParcent>=50 and sPParcent<=59.9:
                            sPtotalGPA = 3
                        elif sPParcent>=40 and sPParcent<=49.9:
                            sPtotalGPA = 2
                        elif sPParcent>=33 and sPParcent<=39.9:
                            sPtotalGPA = 1
                        else:
                            sPtotalGPA = 0

                    totalListLen = (listLen + fListLen + 2)

                    summation = 0
                    totalGPA = 0
                    totalPar = 0

                    for nums in splitted_marks:

                        makeInt = float(nums)

                        summation += makeInt

                        parcentage = makeInt*100 / 100

                        if parcentage > 100:
                            summation = 0
                            parcentage = 0

                        if parcentage >= 80:
                            n_gpa = 5
                        elif parcentage>=70 and parcentage<=79.9:
                            n_gpa = 4
                        elif parcentage>=60 and parcentage<=69.9:
                            n_gpa = 3.5
                        elif parcentage>=50 and parcentage<=59.9:
                            n_gpa = 3
                        elif parcentage>=40 and parcentage<=49.9:
                            n_gpa = 2
                        elif parcentage>=33 and parcentage<=39.9:
                            n_gpa = 1
                        else:
                            n_gpa = 0

                        totalGPA += n_gpa

                    fsummation = 0
                    ftotalGPA = 0

                    for fnums in fSplittedMarks:

                        fmakeInt = float(fnums)

                        fsummation += fmakeInt

                        parcentage = fmakeInt*100 / 50

                        if parcentage > 100:
                            fsummation = 0
                            parcentage = 0

                        if parcentage >= 80:
                            n_gpa = 5
                        elif parcentage>=70 and parcentage<=79.9:
                            n_gpa = 4
                        elif parcentage>=60 and parcentage<=69.9:
                            n_gpa = 3.5
                        elif parcentage>=50 and parcentage<=59.9:
                            n_gpa = 3
                        elif parcentage>=40 and parcentage<=49.9:
                            n_gpa = 2
                        elif parcentage>=33 and parcentage<=39.9:
                            n_gpa = 1
                        else:
                            n_gpa = 0

                        ftotalGPA += n_gpa

                    finalSum = fsummation + summation + sPSummation + fPSummation

                    FinalGPA = (ftotalGPA + totalGPA + sPtotalGPA + fPtotalGPA) / totalListLen

                    Label(root, text="Final Marks: ", font='times 13', bg=col).place(x=40, y=250)
                    _entry = ttk.Entry(root, width=23)
                    _entry.insert(END, str(finalSum))
                    _entry.configure(state="readonly")
                    _entry.place(x=135, y=252)

                    Label(root, text="GPA            : ", font='times 13', bg=col, state="normal").place(x=40, y=275)
                    entry = ttk.Entry(root, width=23, state="normal")
                    entry.insert(END, str(FinalGPA))
                    entry.configure(state="readonly")
                    entry.place(x=135, y=277)
                    
                    break

                except ValueError:
                    tkinter.messagebox.showerror("CPSC CALC", "Invalid Input(Alpha)")
                    break



        def _save():

            # Saving Function-
            
            marks = process()

            ave = averaging()

            subject_codes = {101, 107, 109, 127, 134, 151, 111, 150, 154, 155, 148, 147, 102, 108}

            while True:

                if subject.get() not in subject_codes:
                    tkinter.messagebox.showerror("CPSC CALC", "Your file cannot be saved!")
                    break

                file_ = open(str(subject.get()) + frmt, 'w')
                file_.write("Subject Code : " + str(subject.get()) + "\n" + "Marks & GPA in CPSC Mode: " + str(marks) +
                            "\n" + "Marks and GPA in Average Mode: " + str(ave))
                file_.close()

                tkinter.messagebox.showinfo("CPSC CALC", "Your file was saved successfully")
                break


        def _quit():

            # Quiting Function

            root.quit()
            quit()

        def sub_dic():

            # Subject Dictionary Function
            
            root = Tk()
            root.geometry("300x315")
            root.title("Subject Codes")
            root.config(background=col)
            root.attributes('-alpha', makeTrans)
            root.resizable(False, False)
            root.attributes("-toolwindow",1)

            Label(root, text="Subject Codes", font='times 13', fg='blue', bg=col).pack()
            Canvas(root, width=300, height=1, bg='black', highlightthickness=0).pack()

            Label(root, text="Bangla 1st         -        101", font='arial 9', bg=col).place(x=80, y=30)
            Label(root, text="Bangla 2nd        -        102", font='arial 9', bg=col).place(x=80, y=50)
            Label(root, text="English 1st        -        107", font='arial 9', bg=col).place(x=80, y=70)
            Label(root, text="English 2nd      -         108", font='arial 9', bg=col).place(x=80, y=90)
            Label(root, text="Math                   -         109", font='arial 9', bg=col).place(x=80, y=110)
            Label(root, text="Science             -         127", font='arial 9', bg=col).place(x=80, y=130)
            Label(root, text="BGS                   -         150", font='arial 9', bg=col).place(x=80, y=150)
            Label(root, text="Agriculture        -         134", font='arial 9', bg=col).place(x=80, y=170)
            Label(root, text="Home Science -         151", font='arial 9', bg=col).place(x=80, y=190)
            Label(root, text="Islam                 -          111", font='arial 9', bg=col).place(x=80, y=210)
            Label(root, text="Hinduism          -          112", font='arial 9', bg=col).place(x=80, y=230)
            Label(root, text="Christianity        -          114", font='arial 9', bg=col).place(x=80, y=250)
            Label(root, text="Buddhism         -          113", font='arial 9', bg=col).place(x=80, y=270)
            Label(root, text="ICT                     -          154", font='arial 9', bg=col).place(x=80, y=290)

            root.mainloop()

        def history():

            # History Function

            while True:
                try:
                    file = Tk()

                    file.geometry('430x250')
                    file.title("History")
                    file.attributes("-toolwindow",1)
                    file.attributes('-alpha', makeTrans)
                    file.config(background=col)
                    file.resizable(False, False)

                    _open = open("a.txt", 'r')
                    text = _open.read()

                    text_list = text.splitlines()

                    Label(file, text="History\n", fg='blue', font='arial 15', bg=col).pack(fill='x')

                    Canvas(file, width=430, height=1, bg='black', highlightthickness=0).place(x=0, y=32)

                    x = -50

                    if len(text_list) >= 6:
                        lines = 10
                    else:
                        lines = len(text_list)

                    for n in range(0, lines):
                        Label(file, text=text_list[n], font='arial 9', bg=col).place(y=x, anchor='center', relx=.5, rely=.5)
                        x += 15

                    def _clear():
                        __open = open("a.txt", 'w')

                        __open__ = open("a.txt", 'r')
                        _text_ = __open__.read()

                        Canvas(file, width=430, height=250, bg=col, highlightthickness=0).place(x=0, y=0)
                        Label(file, text="History\n", fg='blue', font='arial 15', bg=col).place(x=181, y=0)
                        ttk.Button(file, text="Clear All", state="disabled").place(x=320, y=3)
                        Canvas(file, width=430, height=1, bg='black', highlightthickness=0).place(x=0, y=32)
                        Label(file, text="History has been cleared!\n", fg='green', font='arial 15', bg=col).place(x=100, y=100)

                    ttk.Button(file, text="Clear All", command=_clear).place(x=320, y=3)

                    splitted = text.split()
                    counter = len(splitted)

                    if counter == 0:
                        ttk.Button(file, text="Clear All", state="disabled").place(x=320, y=3)
                        Label(file, text="There is no History yet!\n", fg='red', font='arial 15', bg=col).pack()

                    _open.close()

                    file.mainloop()
                    break

                except FileNotFoundError:
                    Label(file, text="History\n", fg='blue', font='arial 15', bg=col).pack()
                    ttk.Button(file, text="Clear All", state="disabled").place(x=320, y=3)
                    Canvas(file, width=430, height=1, bg='black', highlightthickness=0).place(x=0, y=32)
                    Label(file, text="There is no History yet!\n", fg='red', font='arial 15', bg=col).pack()
                    break

        def about_():

            # About Function
            
            root = Tk()
            root.geometry("400x260")
            root.title("About CPSC CALC")
            root.config(background=col)
            root.resizable(False, False)
            root.attributes("-toolwindow",1, '-alpha', makeTrans)
            
            root.iconbitmap("origin.ico")

            Label(root, text="\nCPSC CALC (Junior Version)\n", font='13', fg='blue', bg=col).pack()
            
            Label(root, text="Developer, Designer & Idea-", font='9', fg='green', bg=col).pack()
            Label(root, text="© Kazi Azmain Awsaf\n", font='9', fg='black', bg=col).pack()
            Label(root, text="Written in-", font='9', fg='green', bg=col).pack()
            Label(root, text="Python\n", font='9', fg='black', bg=col).pack()
            Label(root, text="Thanks to-", font='9', fg='green', bg=col).pack()
            Label(root, text="thenewboston", font='9', fg='black', bg=col).pack()

            root.mainloop()

        def color():

            # Settings Function

            color = Tk()
            color.title("Settings")
            color.resizable(False, False)
            color.config(background=col)
            color.attributes("-toolwindow", 1)
            color.attributes('-alpha', makeTrans)
            color.geometry("340x300")

            ivoryState = "normal"
            whiteState = "normal"
            grayState = "normal"

            txtState = "normal"
            xmlState = "normal"
            rtfState = "normal"

            tranStateT = "normal"
            tranStateO = "normal"

            if colLen == 0:
                ivoryState = "disabled"
            elif col == "white":
                whiteState = "disabled"
            elif col == "ivory3":
                grayState = "disabled"
            else:
                pass

            if frmt == ".txt":
                txtState = "disabled"
            elif frmt == ".xml":
                xmlState = "disabled"
            elif frmt == ".rtf":
                rtfState = "disabled"
            else:
                pass

            if tranLen is 3:
                tranStateT = "disabled"
            elif tranLen is 2:
                tranStateO = "disabled"

            Label(color, text="Settings", fg="grey", font="times 15", bg=col).pack()
            Canvas(color, width=540, height=1, bg='black', highlightthickness=0).pack()

            Label(color, text="Change Theme Color to", fg="gray", font="times 12", bg=col).place(x=8, y=50)

            Canvas(color, width=110, height=1, bg='black', highlightthickness=0).place(x=162, y=64)
            Canvas(color, width=1, height=57, bg='black', highlightthickness=0).place(x=272, y=64)
            Canvas(color, width=269, height=1, bg='black', highlightthickness=0).place(x=4, y=120)
            Canvas(color, width=1, height=57, bg='black', highlightthickness=0).place(x=4, y=64)

            Label(color, text="Change File Format to ", fg="gray", font="times 12", bg=col).place(x=8, y=130)

            Canvas(color, width=119, height=1, bg='black', highlightthickness=0).place(x=153, y=144)
            Canvas(color, width=1, height=57, bg='black', highlightthickness=0).place(x=272, y=144)
            Canvas(color, width=269, height=1, bg='black', highlightthickness=0).place(x=4, y=201)
            Canvas(color, width=1, height=57, bg='black', highlightthickness=0).place(x=4, y=144)

            Label(color, text="Make Window", fg="gray", font="times 12", bg=col).place(x=8, y=210)

            Canvas(color, width=1, height=57, bg='black', highlightthickness=0).place(x=4, y=224)
            Canvas(color, width=177, height=1, bg='black', highlightthickness=0).place(x=4, y=281)
            Canvas(color, width=1, height=57, bg='black', highlightthickness=0).place(x=180, y=224)
            Canvas(color, width=72, height=1, bg='black', highlightthickness=0).place(x=108, y=224)

            def ok():
                tkinter.messagebox.showinfo("CPSC CALC", "Please restart CPSC CALC to apply changes.")

            def ok_butt_function(state_):
                ok_butt = ttk.Button(color, text="Apply Changes", command=ok, state=state_).place(x=245, y=260)

            ok_butt_function("disabled")

            def color_save(col, file_name):
                color_file = open(file_name + ".txt", "w")
                color_file.write(col)
                color_file.close()

            def gray():
                color_ = "ivory3"
                color_save(color_, "col")
                ok_butt_function("active")

            def white():
                color_ = "white"
                color_save(color_, "col")
                ok_butt_function(state_="active")

            def default():
                color_ = ""
                color_save(str(color_), "col")
                ok_butt_function("active")

            def _txt():
                format_ = ".txt"
                color_save(format_, "format")
                ok_butt_function("active")
                
            def _xml():
                format_ = ".xml"
                color_save(format_, "format")
                ok_butt_function("active")

            def _rtf():
                format_ = ".rtf"
                color_save(format_, "format")
                ok_butt_function("active")

            def transparent_y():
                option = "yes"
                color_save(option, "transparency")
                ok_butt_function("active")

            def transparent_n():
                option = "no"
                color_save(option, "transparency")
                ok_butt_function("active")

            ttk.Button(color, text="Default", command=default, state=ivoryState).place(x=10, y=80)
            ttk.Button(color, text="Dark Ivory", command=gray, state=grayState).place(x=100, y=80)
            ttk.Button(color, text="White", command=white, state=whiteState).place(x=190, y=80)

            ttk.Button(color, text=".txt", command=_txt, state=txtState).place(x=10, y=160)
            ttk.Button(color, text=".xml", command=_xml, state=xmlState).place(x=100, y=160)
            ttk.Button(color, text=".rtf", command=_rtf, state=rtfState).place(x=190, y=160)

            ttk.Button(color, text="Transparent", command=transparent_y, state=tranStateT).place(x=10, y=240)
            ttk.Button(color, text="Opaque", command=transparent_n, state=tranStateO).place(x=100, y=240)

            color.mainloop()


        def ave_mf():

            Label(root, text='Enter Obtained Marks        ', font='times 13', bg=col, width=40).place(x=-44, y=95)
            Label(root, text='Enter CT Marks\t         ', font='times 13', bg=col, width=40, state="disabled")\
                .place(x=-45, y=120)
            Label(root, text='Enter Subject Code\t         ', font='times 13', bg=col, width=30, state='normal')\
                .place(x=0, y=70)
            Label(root, text='Enter 2nd Obtained Marks ', font='times 13', bg=col, width=30, state="normal")\
                .place(x=1, y=145)

            ttk.Entry(root, textvariable=ob_marks, width=23).place(x=265, y=97)
            ttk.Entry(root, textvariable=ct_marks, width=23, state="disabled").place(x=265, y=120)
            ttk.Entry(root, textvariable=subject, width=23, state='normal').place(x=265, y=74)
            ttk.Entry(root, textvariable=second_t, width=23, state="normal").place(x=265, y=145)

            Label(root, text="Final Marks: ", font='times 13', bg=col).place(x=40, y=250)
            entry = ttk.Entry(root, width=23, state="readonly")
            entry.place(x=135, y=252)

            Label(root, text="GPA            : ", font='times 13', bg=col).place(x=40, y=275)
            entry = ttk.Entry(root, width=23, state="readonly")
            entry.place(x=135, y=277)

            Label(root, text="Average Mode", height=2, bg="light gray", fg='dark red').place(x=482, y=283)
            Label(root, text="Current Mode", bg="light gray", fg='dark green').place(x=482, y=270)

            ttk.Button(root, text="CPSC Mode", command=cpsc_mf).place(x=484, y=38)
            ttk.Button(root, text="CPSC Mode\n  Class 9-10", command=calc_mf).place(x=484, y=113)
            ttk.Button(root, text="Summation\n     Mode", command=sum_mf).place(x=484, y=68)
            ttk.Button(root, text="Average Mode", command=ave_mf, state="disabled").place(x=479, y=158)

            canvases(averaging)


        def cpsc_mf():

            Label(root, text='Enter Obtained Marks        ', font='times 13', bg=col, width=40).place(x=-44, y=95)
            Label(root, text='Enter CT Marks\t         ', font='times 13', bg=col, width=40).place(x=-45, y=120)
            Label(root, text='Enter Subject Code\t         ', font='times 13', bg=col, state='normal', width=40).place(
                                                                                                            x=-45, y=70)
            Label(root, text='Enter 2nd Obtained Marks ', font='times 13', state=State2, bg=col, width=40).\
                place(x=-44, y=145)

            ttk.Entry(root, textvariable=ob_marks, width=23).place(x=265, y=97)
            ttk.Entry(root, textvariable=ct_marks, width=23, state="normal").place(x=265, y=120)
            ttk.Entry(root, textvariable=subject, width=23, state='normal').place(x=265, y=74)
            ttk.Entry(root, textvariable=second_t, width=23, state="disabled").place(x=265, y=145)

            Label(root, text="Final Marks: ", font='times 13', bg=col).place(x=40, y=250)
            ttk.Entry(root, width=23, state="readonly").place(x=135, y=252)

            Label(root, text="GPA            : ", font='times 13', bg=col).place(x=40, y=275)
            ttk.Entry(root, width=23, state="readonly").place(x=135, y=277)

            Label(root, bg="light gray", fg='dark blue', width=12, height=2, text="CPSC Mode").place(x=477, y=283)
            Label(root, text="Current Mode", bg="light gray", fg='dark green').place(x=482, y=270)

            ttk.Button(root, text="CPSC Mode", command=cpsc_mf, state="disabled").place(x=484, y=38)
            ttk.Button(root, text="CPSC Mode\n  Class 9-10", command=calc_mf).place(x=484, y=113)
            ttk.Button(root, text="Summation\n     Mode", command=sum_mf).place(x=484, y=68)
            ttk.Button(root, text="Average Mode", command=ave_mf).place(x=479, y=158)

            canvases(process)

        def sum_mf():

            Label(root, text='Enter Bangla Marks     ', font='times 13', bg=col, width=40).place(x=-58, y=95)
            Label(root, text='Enter 100 Exam Marks    ', font='times 13', bg=col, width=40).place(x=-48, y=120)
            Label(root, text='Enter English Marks       ', font='times 13', bg=col, width=30).place(x=-6, y=70)
            Label(root, text='Enter ICT Marks                 ', font='times 13', bg=col, width=30).place(x=1, y=145)

            ttk.Entry(root, textvariable=fPaperExmaMarks, width=23).place(x=265, y=97)
            ttk.Entry(root, textvariable=hExamMarks, width=23).place(x=265, y=120)
            ttk.Entry(root, textvariable=sPaperExmaMarks, width=23).place(x=265, y=74)
            ttk.Entry(root, textvariable=fExamMarks, width=23, state="normal").place(x=265, y=145)

            Label(root, text="Final Marks: ", font='times 13', bg=col).place(x=40, y=250)
            entry = ttk.Entry(root, width=23, state="readonly")
            entry.place(x=135, y=252)

            Label(root, text="GPA            : ", font='times 13', bg=col, state="normal").place(x=40, y=275)
            entry = ttk.Entry(root, width=23, state="readonly")
            entry.place(x=135, y=277)

            Label(root, text="Summation \nMode", bg="light gray", fg="gray", width=12).place(x=477, y=288)
            Label(root, text="Current Mode", bg="light gray", fg='dark green').place(x=482, y=270)

            ttk.Button(root, text="CPSC Mode", command=cpsc_mf).place(x=484, y=38)
            ttk.Button(root, text="CPSC Mode\n  Class 9-10", command=calc_mf).place(x=484, y=113)
            ttk.Button(root, text="Summation\n     Mode", command=sum_mf, state="disabled").place(x=484, y=68)
            ttk.Button(root, text="Average Mode", command=ave_mf).place(x=479, y=158)

            canvases(addition)

        def calc_mf():
            Label(text="Enter Term End CQ Marks ", fg="black", bg=col, font="times 13").place(x=45, y=70)
            Label(text="Enter Term End MCQ Marks ", fg="black", bg=col, font="times 13").place(x=45, y=95)
            Label(text="Enter Class Test CQ Marks ", fg="black", bg=col, font="times 13").place(x=45, y=120)
            Label(text="Enter Class Test MCQ Marks ", fg="black", bg=col, font="times 13").place(x=45, y=145)

            ttk.Entry(textvariable=termEnd, width=23).place(x=265, y=74)
            ttk.Entry(textvariable=termEndMCQ, width=23).place(x=265, y=97)
            ttk.Entry(textvariable=ctCQ, width=23).place(x=265, y=120)
            ttk.Entry(textvariable=ctMCQ, width=23).place(x=265, y=145)

            Label(root, text="Final Marks: ", font='times 13', bg=col).place(x=40, y=250)
            entry = ttk.Entry(root, width=23, state="readonly")
            entry.place(x=135, y=252)

            Label(root, text="GPA            : ", font='times 13', bg=col).place(x=40, y=275)
            entry = ttk.Entry(root, width=23, state="readonly")
            entry.place(x=135, y=277)

            Label(root, bg="light gray", fg='black', width=12, height=2, text="CPSC Mode\n Class 9-10")\
                .place(x=477, y=288)
            Label(root, text="Current Mode", bg="light gray", fg='dark green').place(x=482, y=270)

            ttk.Button(root, text="CPSC Mode", command=cpsc_mf).place(x=484, y=38)
            ttk.Button(root, text="CPSC Mode\n  Class 9-10", command=calc_mf, state="disabled").place(x=484, y=113)
            ttk.Button(root, text="Summation\n     Mode", command=sum_mf).place(x=484, y=68)
            ttk.Button(root, text="Average Mode", command=ave_mf).place(x=479, y=158)

            canvases(calculate)

        ttk.Button(root, text="CPSC Mode", command=cpsc_mf, state="disabled").place(x=484, y=38)
        ttk.Button(root, text="CPSC Mode\n  Class 9-10", command=calc_mf).place(x=484, y=113)
        ttk.Button(root, text="Summation\n     Mode", command=sum_mf).place(x=484, y=68)
        ttk.Button(root, text="Average Mode", command=ave_mf).place(x=479, y=158)

        canvases(process)

        menu = Menu(root)
        root.config(menu=menu)

        sub_menu = Menu(menu, tearoff=0)

        menu.add_cascade(label='Options', menu=sub_menu)

        sub_menu.add_command(label='Save', command=_save, state="normal")
        sub_menu.add_separator()
        sub_menu.add_command(label='History', command=history)
        sub_menu.add_command(label='Subject Codes', command=sub_dic)
        sub_menu.add_command(label='About CPSC CALC', command=about_)
        sub_menu.add_command(label='Settings', command=color)
        sub_menu.add_separator()
        sub_menu.add_command(label='Quit', command=_quit)

        root.mainloop()
        break

    except TclError:
        tkinter.messagebox.showerror("CPSC CALC", "Your program crashed")
        break

    except FileNotFoundError:
        tkinter.messagebox.showinfo("CPSC CALC", "Loading... Please restart the program")
        
        color_file = open("col.txt", "w")
        color_file.write("")
        color_file.close()

        format_file = open("format.txt", "w")
        format_file.write(".txt")
        format_file.close()

        format_file = open("transparency.txt", "w")
        format_file.write("no")
        format_file.close()
        
        break

# ____End____
