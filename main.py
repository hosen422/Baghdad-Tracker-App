from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from plyer import gps
import math

class BaghdadTrackerApp(App):
    def build(self):
        self.clients = {
            "مجمع المنصور التجاري": {"lat": 33.325, "lon": 44.345},
            "أسواق الشورجة (جملة)": {"lat": 33.338, "lon": 44.398},
            "شركة الكرادة للمواد الغذائية": {"lat": 33.310, "lon": 44.422}
        }
        self.agent_lat = 33.326 
        self.agent_lon = 44.346

        try:
            gps.configure(on_location=self.on_gps_location, on_status=self.on_gps_status)
            gps.start(minTime=1000, minDistance=1)
        except NotImplementedError:
            print("GPS Not Supported on this platform")

        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        layout.add_widget(Label(
            text="📍 نظام 'مُتحقِّق' الذكي للمناديب", 
            font_size=22, size_hint_y=0.08, color=(0, 0.8, 1, 1), bold=True
        ))
        
        self.status_image = Image(
            source='target_zone.png', 
            size_hint_y=0.2,
            allow_stretch=True
        )
        layout.add_widget(self.status_image)
        
        layout.add_widget(Label(text="اسم المندوب الميداني:", font_size=14, size_hint_y=0.04))
        self.agent_name_input = TextInput(
            text="حسين البرمجي", 
            multiline=False, 
            size_hint_y=0.07,
            halign="center",
            font_size=16
        )
        layout.add_widget(self.agent_name_input)
        
        layout.add_widget(Label(text="اختر المحل أو الزبون المستهدف للزيارة:", font_size=14, size_hint_y=0.04))
        self.client_spinner = Spinner(
            text='--- قائمة الوجهات اليومية ---',
            values=list(self.clients.keys()),
            size_hint_y=0.08
        )
        layout.add_widget(self.client_spinner)
        
        verify_btn = Button(
            text="🔒 إثبات حضور (تحقق جغرافي)", 
            font_size=18, background_color=(0, 0.6, 0.3, 1), size_hint_y=0.1, bold=True
        )
        verify_btn.bind(on_press=self.verify_location)
        layout.add_widget(verify_btn)
        
        scroll = ScrollView(size_hint_y=0.45)
        self.report_label = Label(
            text="بانتظار اختيار الوجهة والضغط على التحقق لضمان عدم تلاعب المندوب...", 
            font_size=15, size_hint_y=None, halign="center", color=(0.9, 0.9, 0.9, 1)
        )
        self.report_label.bind(texture_size=self.report_label.setter('size'))
        scroll.add_widget(self.report_label)
        layout.add_widget(scroll)
        
        layout.add_widget(Label(
            text="⚙️ تطوير: حسين - نظام المراقبة الميداني المتقدم © 2026", 
            font_size=11, size_hint_y=0.05, color=(0.5, 0.5, 0.5, 1)
        ))
        
        return layout

    def on_gps_location(self, **kwargs):
        self.agent_lat = kwargs.get('lat', self.agent_lat)
        self.agent_lon = kwargs.get('lon', self.agent_lon)

    def on_gps_status(self, stype, status):
        pass

    def verify_location(self, instance):
        selected_client = self.client_spinner.text
        agent_name = self.agent_name_input.text.strip()
        
        if not agent_name:
            self.report_label.text = "⚠️ يرجى كتابة اسم المندوب أولاً!"
            return

        if selected_client == '--- قائمة الوجهات اليومية ---':
            self.report_label.text = "⚠️ يرجى اختيار اسم المحل!"
            return
            
        client_coords = self.clients[selected_client]
        distance = self.calculate_distance(self.agent_lat, self.agent_lon, client_coords["lat"], client_coords["lon"])
        
        if distance <= 200:
            self.report_label.text = (
                f"✅ [تم إثبات الزيارة بنجاح]\n\n"
                f"👤 المندوب: {agent_name}\n"
                f"🏪 الزبون: {selected_client}\n"
                f"🎯 النطاق: متواجد على بعد {int(distance)} متر."
            )
        else:
            self.report_label.text = (
                f"❌ [فشل التحقق - خارج النطاق]\n\n"
                f"🚨 تنبيه: المندوب {agent_name} يحاول إثبات الحضور عن بُعد!\n"
                f"📍 المسافة الحالية هي {distance:.1f} كيلومتر."
            )

    def calculate_distance(self, lat1, lon1, lat2, lon2):
        R = 6371.0
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c * 1000

