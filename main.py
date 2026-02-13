import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt
from Ui_main import Ui_Form

class GenesysTool(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.setFixedSize(self.width(), self.height())
        
        self.toggle_string_group()
        
        self.ui.customized_string.stateChanged.connect(self.toggle_string_group)
        self.ui.generatedbutton.clicked.connect(self.generate_eep)

        self.card_type_map = {
            "MS (Memory Stick)": 0x80,
            "SD / MMC / EMMC": 0x40,
            "CF (Compact Flash)": 0x10,
            "microSD": 0x04,
            "M2 (Memory Stick Micro)": 0x08,
            "xD (Extreme Digital)": 0x01,
            "None": 0x00
        }
        
        self.ui.label_19.setEnabled(False)
        self.ui.lun5_assignment.setEnabled(False)

    def toggle_string_group(self):
        is_active = self.ui.customized_string.isChecked()
        self.ui.groupBox_4.setEnabled(is_active)

    def generate_eep(self):
        try:
            vid = self.ui.vid.text().upper()
            pid = self.ui.pid.text().upper()
            
            reg_power = f"{(self.ui.usb_power_setting.value() // 8):02X}"

            pcs_val = 0
            if self.ui.pcs_ms.isChecked(): pcs_val |= 0x80
            if self.ui.pcs_sd.isChecked(): pcs_val |= 0x40
            if self.ui.pcs_cf.isChecked(): pcs_val |= 0x10
            if self.ui.pcs_msd.isChecked(): pcs_val |= 0x04
            if self.ui.pcs_m2.isChecked(): pcs_val |= 0x08
            if self.ui.pcs_xd.isChecked(): pcs_val |= 0x01
            reg_pcs = f"{pcs_val:02X}"

            reg_lun = f"{(self.ui.spinBox.value() - 1):02X}"

            i0 = f"{self.card_type_map[self.ui.lun0_assignment.currentText()]:02X}"
            i1 = f"{self.card_type_map[self.ui.lun1_assignment.currentText()]:02X}"
            i2 = f"{self.card_type_map[self.ui.lun2_assignment.currentText()]:02X}"
            i3 = f"{self.card_type_map[self.ui.lun3_assignment.currentText()]:02X}"
            i4 = f"{self.card_type_map[self.ui.lun4_assignment.currentText()]:02X}"

            c2_val = 0
            if self.ui.readonly.isChecked(): c2_val |= (1 << 7)
            if self.ui.ltm.isChecked(): c2_val |= (1 << 6)
            if self.ui.sd2_wp_enabled.isChecked(): c2_val |= (1 << 4)
            if self.ui._3233_pin_defined.currentIndex() == 1: c2_val |= (1 << 3)
            reg_c2 = f"{c2_val:02X}"

            c1_val = 0
            is_custom = self.ui.customized_string.isChecked()
            if not self.ui.mmc_support.isChecked(): c1_val |= 0x01
            if is_custom: c1_val |= (1 << 1)
            if self.ui.power_saving_mode.isChecked(): c1_val |= (1 << 3)
            if self.ui.remote_wakeup.isChecked(): c1_val |= (1 << 4)
            if self.ui.ssc.isChecked(): c1_val |= (1 << 5)
            if self.ui.lpm.isChecked(): c1_val |= (1 << 6)
            reg_c1 = f"{c1_val:02X}"

            if not is_custom:
                v_s, p_s, s_s, card_s = "", "", "", ""
            else:
                v_s, p_s, s_s = self.ui.v_str.text(), self.ui.p_str.text(), self.ui.s_str.text()
                c_list = [self.ui.c_str_0.text().strip(), self.ui.c_str_1.text().strip(), 
                          self.ui.c_str_2.text().strip(), self.ui.c_str_3.text().strip()]
                card_s = ",".join([s for s in c_list if s])

            output = (
                f"[START]\n"
                f"{vid}        #00h Vendor ID\n"
                f"{pid}        #01h Product ID\n"
                f"{reg_power}{reg_pcs}        #02h Power/CardType\n"
                f"00{reg_lun}        #03h LUN Count\n"
                f"0000        #04h String offsets\n"
                f"0000        #05h Configuration 3\n"
                f"{i1}{i0}        #06h ICON 1/0\n"
                f"{i2}{i3}        #07h ICON 3/2\n"
                f"{reg_c2}{i4}        #08h Configuration 2/ICON4\n"
                f"00{reg_c1}        #09h Checksum(00)/Configuration 1\n\n"
                f"[V-STR]\n\"{v_s}\"\n\n[P-STR]\n\"{p_s}\"\n\n"
                f"[S-STR]\n\"{s_s}\"\n\n[Card-STR]\n\"{card_s}\"\n"
            )

            f_path, _ = QFileDialog.getSaveFileName(self, "Save EEP", "", "EEP Files (*.eep)")
            if f_path:
                with open(f_path, "w", encoding="utf-8") as f:
                    f.write(output)
                QMessageBox.information(self, "Success", f"EEP File Generated!\nFile saved to: {f_path}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GenesysTool()
    window.show()
    sys.exit(app.exec())