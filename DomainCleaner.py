import re

def basic_cleaner(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'(©.*)$', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def detik_cleaner(text):
    text = str(text).lower()
    text = text.replace('advertisement', ' ')
    text = text.replace('scroll to continue with content', ' ')
    text = re.sub(r'(saksikan live detikpagi.*)', ' ', text)
    text = re.sub(r'(baca info lengkapnya di sini.*)', ' ', text)
    text = re.sub(r'(simak (juga )?video.*)', ' ', text)
    text = re.sub(r'(simak selengkapnya di halaman berikutnya.*)', ' ', text)
    text = re.sub(r'(lihat juga video.*)', ' ', text)
    text = re.sub(r'(untuk menampilkan video ini.*)', ' ', text)
    text = re.sub(r'(\[gambas.*\])', ' ', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def cnn_cleaner(text):
    text = str(text).lower()
    text = text.replace('advertisement', ' ')
    text = text.replace('scroll to continue with content', ' ')
    text = re.sub(r'(\[gambas.*\])', ' ', text)
    text = re.sub(r'\xa0', ' ', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def bisnis_cleaner(text):
    text = str(text).lower()
    text = text.replace('bisnis.com', ' ')
    text = text.replace('advertisement', ' ')
    text = text.replace('nyaman tanpa iklan. langganan bisnispro', ' ')
    text = re.sub(r'(news dan wa channel.*)', ' ', text)
    text = re.sub(r'(cek berita dan artikel yang lain.*)', ' ', text)
    text = re.sub(r'\xa0', ' ', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def bareksa_cleaner(text):
    text = str(text).lower()
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'(kamu bisa mulai dari nama produk investasi.*daftar ke akun bareksa bisnis)', ' ', text)
    text = re.sub(r'(kamu bisa mulai dari nama produk investasi.*organisasi berbadan hukum & memiliki rekening a\/n perusahaan)', ' ', text)
    text = re.sub(r'(beli saham\, klik di sini.*bareksa whatsapp telegram twitter facebook linkedin email salin tautan)', ' ', text)
    text = re.sub(r'(bareksa whatsapp.*email salin tautan)', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def berita_satu_cleaner(text):
    text = str(text).lower()
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'(terkini.*wib jakarta, beritasatu\.com - )', ' ', text)
    text = re.sub(r'(simak berita dan artikel lainnya di google news ikuti terus berita terhangat dari beritasatu.com.*)', ' ', text)
    text = text.replace('jakarta, beritasatu.com - ', ' ')
    text = text.replace('belum punya akun? klik di sini. lupa password', ' ')
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def viva_cleaner(text):
    text = str(text).lower()
    text = re.sub(r'(artikel ini telah ditayangkan di.*)', ' ', text)
    text = re.sub(r'\xa0', ' ', text)
    text = text.replace('advertisement', ' ')
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def liputan6_cleaner(text):
    text = str(text).lower()
    text = text.replace('advertisement', ' ')
    text = re.sub(r'(fakta atau hoaks\? untuk mengetahui kebenaran informasi yang beredar.*baca juga)', ' ', text)
    text = re.sub(r'( liputan6.*wib liputan6\.com\, )', ' ', text)
    text = re.sub(r'(disclaimer\:.*timbul dari keputusan investasi)', ' ', text)
    text = re.sub(r'(follow official whatsapp channel liputan6\.com.*dengan mengklik tautan ini\.)', ' ', text)
    text = re.sub(r'\xa0', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = text.replace('liputan6.com, ', ' ')
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def kontan_cleaner(text):
    text = str(text).lower()
    text = re.sub(r'(ilustrasi.*kontan\.co\.id \- )', ' ', text)
    text = re.sub(r'(reporter.*kontan\.co\.id \- )', ' ', text)
    text = re.sub(r'(penulis.*kontan\.co\.id \- )', ' ', text)
    text = re.sub(r'(agar bisa lanjut membaca sampai tuntas artikel ini.*menyetujui syarat dan ketentuan atau gopay ovo linkaja dana)', ' ', text)
    text = text.replace('cek berita dan artikel yang lain di google news', ' ')
    text = text.replace('momsmoney\.id \- ', ' ')
    text = text.replace('jakarta. ', ' ')
    text = re.sub(r'\xa0', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def kompas_cleaner(text):
    text = str(text).lower()
    text = re.sub(r'\n', ' ', text)
    text = text.replace('\xa0', ' ')
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub(r'(penulis.*kompas\.com \-)', ' ', text)
    text = re.sub(r'(editor.*kompas\.com \-)', ' ', text)
    text = re.sub(r'(tim redaksi.*kompas\.com \-)', ' ', text)
    text = re.sub(r'(.*kompas\.tv \-)', ' ', text)
    text = re.sub(r'(.*kompas\.tv\-)', ' ', text)
    text = re.sub(r'(selengkapnya.*update berita terbaru dan terpercaya\.)', ' ', text)
    text = re.sub(r'(mari bergabung di kanal whatsapp kompastekno.*aplikasi whatsapp terlebih dulu di ponsel\.)', ' ', text)
    text = re.sub(r'(copyright.*all rights reserved\.)', ' ', text)
    text = re.sub(r'(gabung ke channel whatsapp.*terbaru dan terpercaya\.)', ' ', text)
    text = re.sub(r'(kirimkan komentar anda.*)$', ' ', text)
    text = re.sub(r'(dapatkan segera buku.*melalui gramedia\.com\.)$', ' ', text)
    text = re.sub(r'(versi cetak artikel ini terbit di harian kompas.*)$', ' ', text)
    text = re.sub(r'(simak selengkapnya di sini.*)$', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def tribun_cleaner(text):
    text = str(text).lower()
    text = re.sub(r'\n', ' ', text)
    text = text.replace('\xa0', ' ')
    text = text.replace('medium large larger', ' ')
    text = text.replace('ikuti kami di', ' ')
    text = re.sub(r'(halo\,  profile kirim images.*android \& ios)', ' ', text)
    text = re.sub(r'(di playstore atau.*pengalaman baru)', ' ', text)
    text = re.sub(r'(artikel ini telah tayang di.*di google news)', ' ', text)
    text = re.sub(r'(baca berita.*lainnya di google news)', ' ', text)
    text = re.sub(r'(ikuti.*di google news)', ' ', text)
    text = re.sub(r'(baca wartakotalive\.com.*di google news)', ' ', text)
    text = re.sub(r'(dapatkan informasi lain.*whatsapp \: di sini)', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def tempo_cleaner(text):
    text = str(text).lower()
    text = re.sub(r'\n', ' ', text)
    text = text.replace('\xa0', ' ')
    text = re.sub(r'(lupa kata sandi.*belum memiliki akun)', ' ', text)
    text = re.sub(r'(daftar di sini.*sudah memiliki akun)', ' ', text)
    text = re.sub(r'(konfirmasi email kami.*koran dan majalah tempo)', ' ', text)
    text = re.sub(r'(jika anda tidak menerima.*kirimkan lagi sekarang)', ' ', text)
    text = re.sub(r'(menu utama daftar.*sudah memiliki akun\?)', ' ', text)
    text = text.replace('masuk di sini', ' ')
    text = re.sub(r'(pencarian terpopuler.*bagikan)', ' ', text)
    text = re.sub(r'(terkini.*unduh aplikasi tempo)$', ' ', text)
    text = re.sub(r'(berita selanjutnya.*)$', ' ', text)
    text = re.sub(r'(pilihan editor.*)$', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def idn_cleaner(text):
    text = str(text).lower()
    text = re.sub(r'(follow idn times.*klik untuk follow)', ' ', text)
    text = re.sub(r'\n', ' ', text)
    text = text.replace('- scroll untuk melanjutkan', ' ')
    text = text.replace('channels', ' ')
    text = text.replace('regional', ' ')
    text = text.replace('kategori', ' ')
    text = text.replace('event', ' ')
    text = text.replace('download idn app sekarang!', ' ')
    text = text.replace('whatsapp channel &', ' ')
    text = text.replace('google news', ' ')
    text = text.replace('scroll untuk melanjutkan', ' ')
    text = text.replace('iklan', ' ')
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def bloomberg_cleaner(text):
    text = str(text).lower()
    text = re.sub(r'(hak cipta ©.*berita mediatama indonesia)$', ' ', text)
    text = re.sub(r'(bloomberg.* \-)', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def okezone_cleaner(text):
    text = str(text).lower()
    text = re.sub(r'(lihat juga.*)', ' ', text)
    text = text.replace('follow berita okezone di google news', ' ')
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'(dapatkan berita up to date.*nantikan kejutan menarik lainnya)', ' ', text)
    text = re.sub(r'(berita terkait.*all rights reserved)', ' ', text)
    text = re.sub(r'(2007.*all rights reserved)', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def investor_cleaner(text):
    text = str(text).lower()
    text = text.replace('\xa0', ' ')
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'(untuk masuk dan daftar.*investor daily)', ' ', text)
    text = re.sub(r'(editor.*)$', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def tv_one_cleaner(text):
    text = str(text).lower()
    text = re.sub(r'(.*tvonenews\.com \-)', ' ', text)
    text = text.replace('load more', ' ')
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def disway_cleaner(text):
    text = str(text).lower()
    text = re.sub(r'(baca juga:.*)', ' ', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'(.*diswayjateng \-)', ' ', text)
    text = re.sub(r'(.*disway jateng \-)', ' ', text)
    text = re.sub(r'(.*disway.id \-)', ' ', text)
    text = re.sub(r'(.*disway.id\-\-)', ' ', text)
    text = re.sub(r'(.*harian disway \-)', ' ', text)
    text = re.sub(r'(.*disway.id)', ' ', text)
    text = text.replace('advertisement', ' ')
    text = text.replace('cek berita dan artikel yang lain di google news', ' ')
    text = re.sub(r'(sumber:.*)$', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def idx_cleaner(text):
    text = str(text).lower()
    text = text.replace('\xa0', ' ')
    text = text.replace('scan this qr or download app from:', ' ')
    text = text.replace('idxchannel -', ' ')
    text = text.replace('idxchannel', ' ')
    text = re.sub(r'(disclaimer.*tangan investor\.)', ' ', text)
    text = re.sub(r'(informasi ekonomi.*dalam satu aplikasi\.)', ' ', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def republika_cleaner(text):
    text = str(text).lower()
    text = text.replace('\xa0', ' ')
    text = re.sub(r'(.*republika\.co\.id\,)', ' ', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'(gunakan google.*)$', ' ', text)
    text = re.sub(r'(gunakan facebook.*)$', ' ', text)
    text = re.sub(r'(\(qs\. al\-baqarah ayat 66\).*)$', ' ', text)
    text = re.sub(r'(\(qs\. al\-an\'am ayat 37\).*)$', ' ', text)
    text = re.sub(r'(\(qs\. al\-naml ayat 41\).*)$', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def cnbc_cleaner(text):
    text = str(text)
    text = text.replace('CNBC INDONESIA RESEARCH', ' ')
    text = re.sub(r'(CNBC Indonesia Research research@cnbcindonesia\.com.*)$', ' ', text)
    text = text.lower()
    text = text.replace('\xa0', ' ')
    text = re.sub(r'(.*cnbc indonesia \-)', ' ', text)
    text = re.sub(r'\n', ' ', text)
    text = text.replace('ikuti kami', ' ')
    text = text.replace('advertisement', ' ')
    text = text.replace('scroll to continue with content', ' ')
    text = text.replace('scroll to resume content', ' ')
    text = re.sub(r'(ikuti kami.*a transmedia company)$', ' ', text)
    text = re.sub(r'(research@cnbcindonesia\.com.*)$', ' ', text)
    text = re.sub(r'(download aplikasi cnbc indonesia.*a transmedia company)$', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def inews_cleaner(text):
    text = str(text).lower()
    text = re.sub(r'(.*inews\.id \-)', ' ', text)
    text = re.sub(r'(.*inews\.id)', ' ', text)
    text = re.sub(r'\n', ' ', text)
    text = text.replace('advertisement', ' ')
    text = re.sub(r'(editor.*)$', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def jpnn_cleaner(text):
    text = str(text).lower()
    text = re.sub(r'(silakan baca konten menarik lainnya.*)$', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def gridoto_cleaner(text):
    text = str(text).lower()
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'(sobat bisa berlangganan tabloid.*)$', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def bbc_cleaner(text):
    text = str(text).lower()
    text = text.replace('\xa0', ' ')
    text = text.replace('sumber gambar,', ' ')
    text = text.replace('getty images', ' ')
    text = re.sub(r'(kami melakukan sejumlah perubahan penting.*bagi anda dan data anda\.)', ' ', text)
    text = re.sub(r'(©.*)$', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

def otodriver_cleaner(text):
    text = str(text).lower()
    text = re.sub(r'(.*otodriver \-)', ' ', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'(mari bergabung di channel telegram otodriver.*)$', ' ', text)
    text = re.sub(r'(dapatkan update berita.*otodriver\.com\.)', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s.%$,(\/)\';:\-"]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text