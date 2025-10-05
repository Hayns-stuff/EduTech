# DocumentSubmission.py
# Form implementation generated from DocumentSubmission.ui
# Modified to properly save student data

from PyQt6 import QtCore, QtGui, QtWidgets
from data_handler import save_student_data, show_message


class SaveWorker(QtCore.QObject):
    finished = QtCore.pyqtSignal(bool, str, object)  # success, message, last_id

    def __init__(self, student_data):
        super().__init__()
        self.student_data = student_data

    @QtCore.pyqtSlot()
    def run(self):
        import subprocess, json, sys
        try:
            proc = subprocess.Popen([sys.executable, "insert_student_cli.py"],
                                    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    text=True)
            stdin_data = json.dumps(self.student_data)
            out, err = proc.communicate(stdin_data, timeout=10)
            if err:
                # ignore non-critical stderr output
                pass
            # extract and parse JSON from stdout
            text = out.strip()
            json_start = text.rfind('{')
            json_text = text[json_start:] if json_start != -1 else text
            result = json.loads(json_text)
            success = result.get('success', False)
            message = result.get('message', '')
            last_id = result.get('last_id', None)
            self.finished.emit(success, message, last_id)
        except Exception:
            self.finished.emit(False, 'Subprocess error', None)


class Ui_docs(object):
    def setupUi(self, DocumentSubmission):
        DocumentSubmission.setObjectName("DocumentSubmission")
        DocumentSubmission.resize(800, 583)
        self.centralwidget = QtWidgets.QWidget(parent=DocumentSubmission)
        self.centralwidget.setObjectName("centralwidget")

        # Filipino requirements
        self.groupBoxFilipino = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxFilipino.setGeometry(QtCore.QRect(20, 20, 360, 220))
        self.groupBoxFilipino.setObjectName("groupBoxFilipino")

        self.label1 = QtWidgets.QLabel(parent=self.groupBoxFilipino)
        self.label1.setGeometry(QtCore.QRect(10, 30, 300, 16))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(parent=self.groupBoxFilipino)
        self.label2.setGeometry(QtCore.QRect(10, 55, 300, 16))
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(parent=self.groupBoxFilipino)
        self.label3.setGeometry(QtCore.QRect(10, 80, 300, 16))
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(parent=self.groupBoxFilipino)
        self.label4.setGeometry(QtCore.QRect(10, 105, 300, 16))
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(parent=self.groupBoxFilipino)
        self.label5.setGeometry(QtCore.QRect(10, 130, 300, 16))
        self.label5.setObjectName("label5")

        # Non-Filipino requirements
        self.groupBoxNonFilipino = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxNonFilipino.setGeometry(QtCore.QRect(400, 20, 360, 300))
        self.groupBoxNonFilipino.setObjectName("groupBoxNonFilipino")

        self.nlabel1 = QtWidgets.QLabel(parent=self.groupBoxNonFilipino)
        self.nlabel1.setGeometry(QtCore.QRect(10, 30, 330, 16))
        self.nlabel1.setObjectName("nlabel1")
        self.nlabel2 = QtWidgets.QLabel(parent=self.groupBoxNonFilipino)
        self.nlabel2.setGeometry(QtCore.QRect(10, 55, 330, 16))
        self.nlabel2.setObjectName("nlabel2")
        self.nlabel3 = QtWidgets.QLabel(parent=self.groupBoxNonFilipino)
        self.nlabel3.setGeometry(QtCore.QRect(10, 80, 330, 16))
        self.nlabel3.setObjectName("nlabel3")
        self.nlabel4 = QtWidgets.QLabel(parent=self.groupBoxNonFilipino)
        self.nlabel4.setGeometry(QtCore.QRect(10, 105, 330, 16))
        self.nlabel4.setObjectName("nlabel4")
        self.nlabel5 = QtWidgets.QLabel(parent=self.groupBoxNonFilipino)
        self.nlabel5.setGeometry(QtCore.QRect(10, 130, 330, 16))
        self.nlabel5.setObjectName("nlabel5")
        self.nlabel6 = QtWidgets.QLabel(parent=self.groupBoxNonFilipino)
        self.nlabel6.setGeometry(QtCore.QRect(10, 155, 330, 16))
        self.nlabel6.setObjectName("nlabel6")
        self.nlabel7 = QtWidgets.QLabel(parent=self.groupBoxNonFilipino)
        self.nlabel7.setGeometry(QtCore.QRect(10, 180, 330, 16))
        self.nlabel7.setObjectName("nlabel7")
        self.nlabel8 = QtWidgets.QLabel(parent=self.groupBoxNonFilipino)
        self.nlabel8.setGeometry(QtCore.QRect(10, 205, 330, 16))
        self.nlabel8.setObjectName("nlabel8")

        # Submit button
        self.submitButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(350, 500, 100, 32))
        self.submitButton.setObjectName("submitButton")

        # Terms box
        self.termsBox = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.termsBox.setGeometry(QtCore.QRect(20, 340, 740, 140))
        self.termsBox.setReadOnly(True)
        self.termsBox.setObjectName("termsBox")

        DocumentSubmission.setCentralWidget(self.centralwidget)

        self.retranslateUi(DocumentSubmission)
        QtCore.QMetaObject.connectSlotsByName(DocumentSubmission)

    def retranslateUi(self, DocumentSubmission):
        _translate = QtCore.QCoreApplication.translate
        DocumentSubmission.setWindowTitle(_translate("DocumentSubmission", "Document Submission"))
        self.groupBoxFilipino.setTitle(_translate("DocumentSubmission", "Required Documents (Filipino Applicants)"))
        self.label1.setText(_translate("DocumentSubmission", "1. Printed copy of the Notice of Acceptance"))
        self.label2.setText(_translate("DocumentSubmission", "2. Original High School Report Card – DepEd Form 138-A"))
        self.label3.setText(_translate("DocumentSubmission", "3. Certificate of Good Moral Character"))
        self.label4.setText(_translate("DocumentSubmission", "4. Two (2) 2×2” photos"))
        self.label5.setText(_translate("DocumentSubmission", "5. PSA Authenticated Birth Certificate"))
        self.groupBoxNonFilipino.setTitle(_translate("DocumentSubmission", "Required Documents (Non-Filipino Applicants)"))
        self.nlabel1.setText(_translate("DocumentSubmission", "1. Birth Certificate"))
        self.nlabel2.setText(_translate("DocumentSubmission", "2. Passport (Applicant - first & last page)"))
        self.nlabel3.setText(_translate("DocumentSubmission", "3. Passport (Parents/Guardians - first & last page)"))
        self.nlabel4.setText(_translate("DocumentSubmission", "4. Student Special Permit (SSP)"))
        self.nlabel5.setText(_translate("DocumentSubmission", "5. Alien’s Certificate of Registration (ACR/I-Card)"))
        self.nlabel6.setText(_translate("DocumentSubmission", "6. Junior High School Report Card (w/ English Translation)"))
        self.nlabel7.setText(_translate("DocumentSubmission", "7. Official Transcript of Records (Gr.7-10, English)"))
        self.nlabel8.setText(_translate("DocumentSubmission", "8. One recent 2×2” photograph"))
        self.submitButton.setText(_translate("DocumentSubmission", "Submit"))
        self.termsBox.setPlainText(_translate("DocumentSubmission",
            "Registration and Advance down payment are non-refundable.\n"
            "Credentials submitted for enrollment become a part of the senior high school and cannot be withdrawn after registration.\n"
            "Once registered a student is considered enrolled for the whole school year unless he/she is dropped or dismissed for cause.\n"
            "Student must notify the School Administration / Registrar the soonest time should he/she intends to drop the course.\n"
            "A student is considered enrolled once he/she submits his/her Report Card (Form 138) and other similar admission credentials and has made payment.\n"
            "Tuition fees and other financial obligations should be paid on or before the scheduled date. Otherwise, penalties will be imposed.\n"
            "The school reserves the right to deny admission to any course of those delinquent students."
        ))


# -----------------------
# Final submission window wrapper
# -----------------------

class DocumentSubmissionWindow(QtWidgets.QMainWindow):
    def __init__(self, student_data):
        super().__init__()
        self.ui = Ui_docs()
        self.ui.setupUi(self)
        self.student_data = student_data

        try:
            self.ui.submitButton.clicked.disconnect()
        except Exception:
            pass

        self.ui.submitButton.clicked.connect(self.submit_data)


    def submit_data(self):
        # run save in a background QThread
        self.ui.submitButton.setEnabled(False)
        self._thread = QtCore.QThread()
        self._worker = SaveWorker(self.student_data)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        self._worker.finished.connect(self._on_save_finished)
        self._worker.finished.connect(self._thread.quit)
        self._worker.finished.connect(self._worker.deleteLater)
        self._thread.finished.connect(self._thread.deleteLater)
        self._thread.start()

    def _on_save_finished(self, success, message, last_id):
        self.ui.submitButton.setEnabled(True)
        if success:
            show_message(self, "Success", f"Student data has been saved (id={last_id})")
            self.close()
        else:
            show_message(self, "Error", f"Failed to save student data: {message}",
                        QtWidgets.QMessageBox.Icon.Critical)
