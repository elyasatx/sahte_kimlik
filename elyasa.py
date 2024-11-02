import random
import datetime
import os

# Kullanıcı bilgileri
instagram_account = "elyasatx"
github_account = "elyasatx"

# İsim, soyisim, meslek, üniversite, şehir ve suç kaydı listeleri
erkek_isimleri =  ["Ahmet", "Mehmet", "Yusuf", "Mustafa", "Ali", "Hasan", "Hüseyin", "İbrahim", "Ömer", "Mahmut",
    "Kemal", "Ayhan", "Sinan", "Murat", "Aykut", "Eren", "Burak", "Can", "Emre", "Erhan",
    "Serkan", "Levent", "Gökhan", "Hakan", "Volkan", "Kaan", "Tolga", "Rıza", "Taner", "Tuncay",
    "Cenk", "Cem", "Tamer", "Veli", "Barış", "Ersin", "Yunus", "Kürşat", "Bora", "Ziya",
    "Recep", "İsa", "Melih", "Kerim", "Tuğrul", "Doğan", "Kadir", "Fırat", "Özcan", "Halil",
    "Bekir", "Salih", "Alper", "Nedim", "Engin", "Fatih", "Umut", "Bülent", "Gökçe", "Serhat",
    "Sefa", "Erdem", "Ferhat", "Turgut", "Ramazan", "Veysel", "İhsan", "Koray", "Berk", "Oğuzhan",
    "Adnan", "Utku", "Cihan", "Batuhan", "Ertuğrul", "Hidayet", "Baran", "Şahin", "Şeref", "Ercan",
    "Ertan", "Giray", "Göktuğ", "Burhan", "Arda", "Çetin", "Ferdi", "Mesut", "Kemalettin", "Orhan",
    "Faruk", "Tahsin", "İskender", "Hakkı", "Server", "Erkan", "Evren", "Güven", "Çağrı", "Tuna",
    "Talat", "Adil", "Okan", "Ufuk", "Selçuk", "Seyfi", "Şerif", "Tayfur", "Tolunay", "Seçkin",
    "Eşref", "İdris", "Tan", "Cüneyt", "Cemil", "Hayati", "Vedat", "Mete", "Burçin", "Tufan",
    "Tuna", "Devrim", "Cemal", "Refik", "Ender", "Fuat", "Selim", "İlker", "Mert", "Tarık",
    "Timur", "Cüneyt", "Doğuş", "Hikmet", "Rasim", "Nazmi", "Muhammed", "Fikret", "Korhan", "Caner",
    "Tanju", "Güvenç", "Tolgahan", "Engin", "Vefa", "Taha", "Tayfun", "Tevfik", "Eray", "Cüneyt",
    "Suat", "Atilla", "Bayram", "Timur", "Nevzat", "Halim", "Remzi", "Yücel", "Oktay", "Alpaslan",
    "Kemalettin", "Aziz", "Levent", "Oktay", "Sabri", "Çetin", "Baki", "Alaattin", "Muammer", "Erdal",
    "Saim", "Rıdvan", "Demir", "Tahir", "Adnan", "Namık", "Bora", "Ethem", "Rüstem", "Serdar",
    "Erdoğan", "İlter", "Yasin", "Ege", "Gani", "Müfit", "Gürbüz", "Dinçer", "Ünal", "Süleyman",
    "Umur", "Tuncer", "Altan", "Ergin", "Ozan", "Nihat", "Soner", "Çağdaş", "Murathan", "Emir"]
kadın_isimleri = ["Ayşe", "Fatma", "Zeynep", "Elif", "Meryem", "Hatice", "Emine", "Kübra", "Sevgi", "Funda",
    "Gül", "Havva", "Melis", "Deniz", "Esra", "Merve", "Derya", "Büşra", "Seda", "Sibel",
    "Aylin", "Ebru", "Gizem", "Bahar", "Ceyda", "Dilek", "Ece", "Filiz", "Gonca", "Hande",
    "İpek", "Jale", "Kader", "Lale", "Mine", "Nazan", "Özge", "Pelin", "Rabia", "Selin",
    "Tuba", "Ülkü", "Vildan", "Yasemin", "Zehra", "Aysel", "Banu", "Ceren", "Duygu", "Elvan",
    "Fatoş", "Gülşah", "Hülya", "İnci", "Jülide", "Kezban", "Leyla", "Mina", "Nergis", "Özlem",
    "Perihan", "Rana", "Sevil", "Tülay", "Ümran", "Vesile", "Yelda", "Zeliha", "Alev", "Berrin",
    "Cansu", "Derya", "Elif", "Figen", "Gülcan", "Hacer", "İlknur", "Jale", "Kader", "Leman",
    "Melek", "Nihal", "Özden", "Pelin", "Rukiye", "Safiye", "Tijen", "Ülkü", "Vildan", "Yasemin",
    "Zehra", "Aysun", "Bahar", "Ceylan", "Dilek", "Eda", "Fatoş", "Gülşen", "Hülya", "İpek",
    "Jülide", "Kezban", "Leyla", "Mina", "Nergis", "Özlem", "Perihan", "Rana", "Sevil", "Tülay",
    "Ümran", "Vesile", "Yelda", "Zeliha", "Alev", "Berrin", "Cansu", "Derya", "Elif", "Figen",
    "Gülcan", "Hacer", "İlknur", "Jale", "Kader", "Leman", "Melek", "Nihal", "Özden", "Pelin",
    "Rukiye", "Safiye", "Tijen", "Ülkü", "Vildan", "Yasemin", "Zehra", "Aysun", "Bahar", "Ceylan",
    "Dilek", "Eda", "Fatoş", "Gülşen", "Hülya", "İpek", "Jülide", "Kezban", "Leyla", "Mina",
    "Nergis", "Özlem", "Perihan", "Rana", "Sevil", "Tülay", "Ümran", "Vesile", "Yelda", "Zeliha",
    "Alev", "Berrin", "Cansu", "Derya", "Elif", "Figen", "Gülcan", "Hacer", "İlknur", "Jale",
    "Kader", "Leman", "Melek", "Nihal", "Özden", "Pelin", "Rukiye", "Safiye", "Tijen", "Ülkü",
    "Vildan", "Yasemin", "Zehra", "Aysun", "Bahar", "Ceylan", "Dilek", "Eda", "Fatoş", "Gülşen"]
soyadlar = ["Yılmaz", "Kaya", "Demir", "Şahin", "Çelik", "Kılıç", "Arslan", "Öz", "Can", "Baş",
    "Ekinci", "Polat", "Duran", "Karaca", "Güven", "Koç", "Güler", "Aslan", "Kurt", "Baysal",
    "Aydın", "Tan", "Atalay", "Ak", "Acar", "Akyüz", "Bal", "Baran", "Başar", "Bayram",
    "Bircan", "Bulut", "Candan", "Cebeci", "Ceylan", "Çetin", "Çiftçi", "Çınar", "Deniz", "Dinç",
    "Doğan", "Duman", "Durmaz", "Dursun", "Erol", "Esen", "Fidan", "Gök", "Gökçe", "Görkem",
    "Gül", "Güzel", "Hakan", "Hancı", "Hızır", "Işık", "Işıklı", "Kalkın", "Kar", "Karataş",
    "Kara", "Karaoğlu", "Karaman", "Karan", "Kartal", "Kaya", "Kazan", "Kızıl", "Koç", "Kök",
    "Köse", "Kurt", "Kuş", "Kurtoğlu", "Mercan", "Mutlu", "Narin", "Nazar", "Odabaşı", "Öktem",
    "Ökmen", "Önder", "Öztürk", "Pala", "Palalı", "Polat", "Sağlam", "Sarı", "Savaş", "Seçkin",
    "Sevim", "Sezer", "Sönmez", "Şahin", "Şener", "Şimşek", "Taş", "Taşkın", "Tekin", "Telli",
    "Temiz", "Temizkan", "Terzi", "Toprak", "Toraman", "Türkmen", "Uçar", "Ülker", "Ülkü", "Yalçın","Yaman", "Yardımcı", "Yavuz", "Yazıcı", "Yıldız", "Yılmaz", "Yol", "Yurdakul", "Zafer", "Zengin","Zırhlı", "Aral", "Aslan", "Atlı", "Ay", "Ayan", "Aygün", "Balcı", "Baş", "Başar",
    "Baydar", "Baykal", "Bekar", "Berber", "Bilge", "Bilgin", "Bozkurt", "Bulut", "Çakır", "Çalışkan",
    "Çatal", "Çetin", "Demirci", "Dinçer", "Durmaz", "Düşün", "Ece", "Ekici", "Ekinci", "Elmas",
    "Ergin", "Erkan", "Erol", "Gökçe", "Gönül", "Görkem", "Güçlü", "Güler", "Güven", "Hakan",
    "Hazar", "Ilıcalı", "Işık", "Kaptan", "Kara", "Karagöz", "Kaya", "Keleş", "Kibar", "Koç",
    "Konak", "Koray", "Korkmaz", "Köse", "Kurt", "Kurtoğlu", "Kuş", "Mercan", "Meşe", "Nacar",
    "Narin", "Ocak", "Oflaz", "Oral", "Orhan", "Osman", "Otağ", "Önder", "Özcan", "Özel",
    "Özkan", "Pala", "Paker", "Polat", "Sağır", "Sarı", "Sarıkaya", "Savaş", "Seçgin", "Sezer",
    "Sökmen", "Şahin", "Şeker", "Şen", "Şener", "Şimşek", "Tamer", "Tan", "Tuna", "Turan",
    "Türkmen", "Tütüncü", "Ulus", "Ulusoy", "Üçer", "Ülker", "Ünal", "Üzüm", "Yalçın", "Yaman",
    "Yardımcı", "Yavuz", "Yayla", "Yazıcı", "Yıldız", "Yılmaz", "Yol", "Yurdakul", "Zafer", "Zengin",
    "Zırhlı", "Aral", "Aslan", "Atlı", "Ay", "Ayan", "Aygün", "Balcı", "Baş", "Başar",
    "Baydar", "Baykal", "Bekar", "Berber", "Bilge", "Bilgin", "Bozkurt", "Bulut", "Çakır", "Çalışkan",
    "Çatal", "Çetin", "Demirci", "Dinçer", "Durmaz", "Düşün", "Ece", "Ekici", "Ekinci", "Elmas",
    "Ergin", "Erkan", "Erol", "Gökçe", "Gönül", "Görkem", "Güçlü", "Güler", "Güven", "Hakan",
    "Hazar", "Ilıcalı", "Işık", "Kaptan", "Kara", "Karagöz", "Kaya", "Keleş", "Kibar", "Koç",
    "Konak", "Koray", "Korkmaz", "Köse", "Kurt", "Kurtoğlu", "Kuş", "Mercan", "Meşe", "Nacar",
    "Narin", "Ocak", "Oflaz", "Oral", "Orhan", "Osman", "Otağ", "Önder", "Özcan", "Özel",
    "Özkan", "Pala", "Paker", "Polat", "Sağır", "Sarı", "Sarıkaya", "Savaş", "Seçgin", "Sezer",
    "Sökmen", "Şahin", "Şeker", "Şen", "Şener", "Şimşek", "Tamer", "Tan", "Tuna", "Turan",
    "Türkmen", "Tütüncü", "Ulus", "Ulusoy", "Üçer", "Ülker", "Ünal", "Üzüm", "Yalçın", "Yaman",
    "Yardımcı", "Yavuz", "Yayla", "Yazıcı", "Yıldız", "Yılmaz", "Yol", "Yurdakul", "Zafer", "Zengin",
    "Zırhlı", "Aral", "Aslan", "Atlı", "Ay", "Ayan", "Aygün", "Balcı", "Baş", "Başar",
    "Baydar", "Baykal", "Bekar", "Berber", "Bilge", "Bilgin", "Bozkurt", "Bulut", "Çakır", "Çalışkan",
    "Çatal", "Çetin", "Demirci", "Dinçer", "Durmaz", "Düşün", "Ece", "Ekici", "Ekinci", "Elmas",
    "Ergin", "Erkan", "Erol", "Gökçe", "Gönül", "Görkem", "Güçlü", "Güler", "Güven", "Hakan",
    "Hazar", "Ilıcalı", "Işık", "Kaptan", "Kara", "Karagöz", "Kaya", "Keleş", "Kibar", "Koç",
    "Konak", "Koray", "Korkmaz", "Köse", "Kurt", "Kurtoğlu", "Kuş", "Mercan", "Meşe", "Nacar",
    "Narin", "Ocak", "Oflaz", "Oral", "Orhan", "Osman", "Otağ", "Önder", "Özcan", "Özel",
    "Özkan", "Pala", "Paker", "Polat", "Sağır", "Sarı", "Sarıkaya", "Savaş", "Seçgin", "Sezer",
    "Sökmen", "Şahin", "Şeker", "Şen", "Şener", "Şimşek", "Tamer", "Tan", "Tuna", "Turan",
    "Türkmen", "Tütüncü", "Ulus", "Ulusoy", "Üçer", "Ülker", "Ünal", "Üzüm", "Yalçın", "Yaman",
    "Yardımcı", "Yavuz", "Yayla", "Yazıcı", "Yıldız", "Yılmaz", "Yol", "Yurdakul", "Zafer", "Zengin"]
meslekler = ["Doktor", "Mühendis", "Öğretmen", "Avukat", "Hemşire", "Polis", "Mimar", "Eczacı", "Bilgisayar Programcısı", "Grafik Tasarımcı",
    "Muhasebeci", "Psikolog", "Sosyolog", "Ekonomist", "Gazeteci", "Yazar", "Çevirmen", "Pilot", "Hostes", "Diş Hekimi",
    "Veteriner", "Fizyoterapist", "Diyetisyen", "Spor Antrenörü", "Sanatçı", "Müzisyen", "Oyuncu", "Yönetmen", "Prodüktör", "Editör",
    "Fotoğrafçı", "Reklamcı", "Pazarlamacı", "Satış Temsilcisi", "İnsan Kaynakları Uzmanı", "İşletmeci", "Bankacı", "Sigortacı", "Yatırım Danışmanı", "Gayrimenkul Danışmanı",
    "Turizm Rehberi", "Aşçı", "Garson", "Barista", "Kuaför", "Güzellik Uzmanı", "Moda Tasarımcısı", "Tekstil Mühendisi", "Makine Mühendisi", "Elektrik Mühendisi",
    "Elektronik Mühendisi", "İnşaat Mühendisi", "Çevre Mühendisi", "Kimya Mühendisi", "Endüstri Mühendisi", "Jeoloji Mühendisi", "Maden Mühendisi", "Ziraat Mühendisi", "Orman Mühendisi", "Gıda Mühendisi",
    "Su Ürünleri Mühendisi", "Biyolog", "Kimyager", "Fizikçi", "Matematikçi", "Astronom", "Jeofizikçi", "Meteorolog", "Arkeolog", "Antropolog",
    "Tarihçi", "Filolog", "Felsefeci", "Teolog", "Siyaset Bilimci", "Uluslararası İlişkiler Uzmanı", "Sosyal Hizmet Uzmanı", "Kütüphaneci", "Arşivci", "Müzeci",
    "Restoratör", "Konservatör", "Sanat Tarihçisi", "Eğitim Bilimci", "Rehber Öğretmen", "Özel Eğitim Uzmanı", "Dil ve Konuşma Terapisti", "Ergoterapist", "Odyolog", "Optisyen",
    "Radyoloji Teknisyeni", "Anestezi Teknisyeni", "Laboratuvar Teknisyeni", "Paramedik", "Ambulans Şoförü", "Yangın Söndürme Uzmanı", "İtfaiyeci", "Güvenlik Görevlisi", "Asker", "Subay"]
universiteler = ["Boğaziçi Üniversitesi", "İstanbul Teknik Üniversitesi", "Orta Doğu Teknik Üniversitesi", "Hacettepe Üniversitesi", "Ankara Üniversitesi", "İstanbul Üniversitesi", "Ege Üniversitesi", "Dokuz Eylül Üniversitesi", "Gazi Üniversitesi", "Marmara Üniversitesi",
    "Yıldız Teknik Üniversitesi", "Sabancı Üniversitesi", "Koç Üniversitesi", "Bilkent Üniversitesi", "İzmir Yüksek Teknoloji Enstitüsü", "Çukurova Üniversitesi", "Uludağ Üniversitesi", "Akdeniz Üniversitesi", "Karadeniz Teknik Üniversitesi", "Selçuk Üniversitesi",
    "Atatürk Üniversitesi", "Erciyes Üniversitesi", "Fırat Üniversitesi", "İnönü Üniversitesi", "Ondokuz Mayıs Üniversitesi", "Süleyman Demirel Üniversitesi", "Pamukkale Üniversitesi", "Kocaeli Üniversitesi", "Sakarya Üniversitesi", "Dumlupınar Üniversitesi",
    "Gaziantep Üniversitesi", "Mersin Üniversitesi", "Muğla Sıtkı Koçman Üniversitesi", "Nevşehir Hacı Bektaş Veli Üniversitesi", "Niğde Ömer Halisdemir Üniversitesi", "Osmaniye Korkut Ata Üniversitesi", "Sivas Cumhuriyet Üniversitesi", "Trakya Üniversitesi", "Uşak Üniversitesi", "Yalova Üniversitesi",
    "Yüzüncü Yıl Üniversitesi", "Zonguldak Bülent Ecevit Üniversitesi", "Adnan Menderes Üniversitesi", "Afyon Kocatepe Üniversitesi", "Aksaray Üniversitesi", "Amasya Üniversitesi", "Anadolu Üniversitesi", "Balıkesir Üniversitesi", "Bartın Üniversitesi", "Batman Üniversitesi",
    "Bayburt Üniversitesi", "Bingöl Üniversitesi", "Bitlis Eren Üniversitesi", "Bolu Abant İzzet Baysal Üniversitesi", "Burdur Mehmet Akif Ersoy Üniversitesi", "Bursa Teknik Üniversitesi", "Çanakkale Onsekiz Mart Üniversitesi", "Çankırı Karatekin Üniversitesi", "Düzce Üniversitesi", "Eskişehir Osmangazi Üniversitesi",
    "Giresun Üniversitesi", "Hakkari Üniversitesi", "Hatay Mustafa Kemal Üniversitesi", "Iğdır Üniversitesi", "Isparta Uygulamalı Bilimler Üniversitesi", "İstanbul Medeniyet Üniversitesi", "İstanbul Sabahattin Zaim Üniversitesi", "İstanbul Şehir Üniversitesi", "İstanbul Ticaret Üniversitesi", "İstanbul Üniversitesi-Cerrahpaşa",
    "İzmir Demokrasi Üniversitesi", "İzmir Ekonomi Üniversitesi", "Kadir Has Üniversitesi", "Kafkas Üniversitesi", "Kahramanmaraş Sütçü İmam Üniversitesi", "Kastamonu Üniversitesi", "Kırıkkale Üniversitesi", "Kırklareli Üniversitesi", "Kilis 7 Aralık Üniversitesi", "Kocaeli Sağlık ve Teknoloji Üniversitesi",
    "Konya Gıda ve Tarım Üniversitesi", "KTO Karatay Üniversitesi", "Malatya Turgut Özal Üniversitesi", "Manisa Celal Bayar Üniversitesi", "Mardin Artuklu Üniversitesi", "Mehmet Akif Ersoy Üniversitesi", "Mimar Sinan Güzel Sanatlar Üniversitesi", "Nişantaşı Üniversitesi", "Nuh Naci Yazgan Üniversitesi", "Ordu Üniversitesi"]
sehirler = ["Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir",
    "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli",
    "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari",
    "Hatay", "Isparta", "Mersin", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir",
    "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir",
    "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat",
    "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman",
    "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"]
suç_kayıtları = ["Hırsızlık", "Dolandırıcılık", "Kasten Adam Öldürme", "Yaralama", "Uyuşturucu Ticareti", "Cinsel Saldırı", "Tehdit", "Hakaret", "Şantaj", "Rüşvet",
    "İhaleye Fesat Karıştırma", "Görevi Kötüye Kullanma", "Zimmet", "İrtikap", "Trafik Güvenliğini Tehlikeye Sokma", "Kasten Yaralama", "Taksirle Yaralama", "Taksirle Öldürme", "Kasten Öldürme", "İşkence",
    "Eziyet", "Hürriyeti Tahdit", "Konut Dokunulmazlığını İhlal", "Haberleşmenin Gizliliğini İhlal", "Kişisel Verilerin Kaydedilmesi", "Kişisel Verilerin Hukuka Aykırı Olarak Verilmesi", "Kişisel Verilerin Yok Edilmemesi", "Özel Hayatın Gizliliğini İhlal", "Cinsel Taciz", "Çocukların Cinsel İstismarı",
    "Reşit Olmayanla Cinsel İlişki", "Cinsel Saldırı", "Cinsel Taciz", "Çocuğun Kaçırılması ve Alıkonulması", "Çocuğun Fuhşa Teşviki", "Çocuğun Fuhşa Zorlanması", "Çocuğun Fuhşa Aracılık Edilmesi", "Çocuğun Fuhşa Teşvik Edilmesi", "Çocuğun Fuhşa Zorlanması", "Çocuğun Fuhşa Aracılık Edilmesi",
    "Çocuğun Fuhşa Teşvik Edilmesi", "Çocuğun Fuhşa Zorlanması", "Çocuğun Fuhşa Aracılık Edilmesi", "Çocuğun Fuhşa Teşvik Edilmesi", "Çocuğun Fuhşa Zorlanması", "Çocuğun Fuhşa Aracılık Edilmesi", "Çocuğun Fuhşa Teşvik Edilmesi", "Çocuğun Fuhşa Zorlanması", "Çocuğun Fuhşa Aracılık Edilmesi", "Çocuğun Fuhşa Teşvik Edilmesi"]
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def kimlik_olustur(cinsiyet):
    if cinsiyet == 'erkek':
        isim = random.choice(erkek_isimleri)
    else:
        isim = random.choice(kadın_isimleri)
    soyisim = random.choice(soyadlar)
    meslek = random.choice(meslekler)
    üniversite = random.choice(universiteler)
    şehir = random.choice(sehirler)
    suç = random.choice(suç_kayıtları)
    dob = datetime.datetime(random.randint(1970, 2000), random.randint(1, 12), random.randint(1, 28))
    yaş = datetime.datetime.now().year - dob.year
    
    kimlik = {
        "İsim": isim,
        "Soyisim": soyisim,
        "Meslek": meslek,
        "Suç Kaydı": suç,
        "Üniversite": üniversite,
        "Şehir": şehir,
        "Doğum Tarihi": dob.strftime("%Y-%m-%d"),
        "Yaş": yaş,
    }
    
    return kimlik

def main_menu():
    clear_terminal()
    while True:
        print(f"--- Elyasa Sahte Kimlik Oluşturucu ---")
        print(f"Instagram: {instagram_account}")
        print(f"GitHub: {github_account}\n")
        print("1. Erkek Kimlik Oluştur")
        print("2. Kadın Kimlik Oluştur")
        print("3. Rastgele Cinsiyet Kimlik Oluştur")
        print("4. Çıkış")
        
        secim = input("\nSeçiminizi yapın (1/2/3/4): ")

        if secim in ['1', '2', '3']:
            adet = int(input("Kaç kimlik oluşturulsun? "))
            for _ in range(adet):
                cinsiyet = 'erkek' if secim == '1' else 'kadın' if secim == '2' else random.choice(['erkek', 'kadın'])
                kimlik = kimlik_olustur(cinsiyet)
                
                print("\n--- Oluşturulan Kimlik ---")
                for key, value in kimlik.items():
                    print(f"{key}: {value}")

                # Veriyi dosyaya kaydet
                with open('kullanici_verileri.txt', 'a') as f:
                    f.write(f"{kimlik}\n")

            print("\nKullanıcı verileri başarıyla oluşturuldu. @elyasatx")

        elif secim == '4':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main_menu()