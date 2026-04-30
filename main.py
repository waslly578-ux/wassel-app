from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import OneLineListItem, MDList
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
import sqlite3
import webbrowser

class AlWaselPro(MDApp):
    def build(self):
        # إعداد سمة التطبيق (الألوان)
        self.theme_cls.primary_palette = "Blue"
        screen = MDScreen()
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=10)

        # خانات إدخال البيانات
        self.name = MDTextField(hint_text="اسم الزبون", mode="outline")
        self.phone = MDTextField(hint_text="رقم الهاتف", mode="outline")
        self.amount = MDTextField(hint_text="المبلغ", mode="outline")
        self.note = MDTextField(hint_text="ملاحظات", mode="outline")

        # زر الحفظ
        btn_save = MDRaisedButton(
            text="حفظ الحساب", 
            pos_hint={'center_x': 0.5}, 
            on_release=self.add_transaction
        )
        
        # قائمة لعرض الحسابات المسجلة
        self.scroll = ScrollView()
        self.list_view = MDList()
        self.scroll.add_widget(self.list_view)

        # إضافة العناصر إلى الواجهة
        layout.add_widget(self.name)
        layout.add_widget(self.phone)
        layout.add_widget(self.amount)
        layout.add_widget(self.note)
        layout.add_widget(btn_save)
        layout.add_widget(self.scroll)
        
        screen.add_widget(layout)
        
        # تشغيل قاعدة البيانات وتحميل البيانات القديمة إن وجدت
        self.init_db()
        self.load_data()
        return screen

    def init_db(self):
        conn = sqlite3.connect('alwasel_pro.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS shop_accounts 
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT, amount REAL, note TEXT)''')
        conn.commit()
        conn.close()

    def add_transaction(self, instance):
        if self.name.text and self.amount.text:
            conn = sqlite3.connect('alwasel_pro.db')
            c = conn.cursor()
            c.execute("INSERT INTO shop_accounts (name, phone, amount, note) VALUES (?, ?, ?, ?)", 
                      (self.name.text, self.phone.text, self.amount.text, self.note.text))
            conn.commit()
            conn.close()
            self.load_data()
            # مسح الخانات بعد الحفظ
            self.name.text = ""; self.phone.text = ""; self.amount.text = ""; self.note.text = ""

    def load_data(self):
        self.list_view.clear_widgets()
        conn = sqlite3.connect('alwasel_pro.db')
        c = conn.cursor()
        c.execute("SELECT name, phone, amount, note FROM shop_accounts")
        for row in c.fetchall():
            # عند الضغط على أي اسم في القائمة سيفتح تطبيق الرسائل تلقائياً
            item = OneLineListItem(
                text=f"{row[0]} - {row[2]} RY", 
                on_release=lambda x, p=row[1], n=row[0], a=row[2]: self.send_sms(p, n, a)
            )
            self.list_view.add_widget(item)
        conn.close()

    def send_sms(self, phone, name, amount):
        message = f"إشعار من الواصل برو\nالزبون: {name}\nالمبلغ: {amount}"
        sms_url = f"sms:{phone}?body={message}"
        webbrowser.open(sms_url)

if __name__ == "__main__":
    AlWaselPro().run()
