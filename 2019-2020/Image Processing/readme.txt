öncelikle yarattığımız karmaşadan ve düzensizlikten ötürü özür dileriz :dd

evet, biliyorum, çok korkunç duruyor, ama açıklayayım;

yarışmada çalışan 2 kodumuz vardı, bunlar "otonom_1_25092020.py" ve "otonom_2_26092020.py"

kodların içerisinde start ve deneme fonksiyonlarını göreceksiniz
deneme1 ve deneme2 bulunuyor, bir tanesi araç havuzun sağ tarafından, diğeri de sol tarafından bırakılmasına göre
yazılmış, aracın kendini toplaması için bir algoritma. açıklaması biraz karışık ama nihai olarak
araç kendini çemberin ekseniyle çalıştırıyor, yani havuza dik bir şekilde, uzunlamasına, bakıyor.

işin ilginç yanı deneme 1 veya 2 olması çok da değiştirmedi, iki türlü de araç kendini toparladı

start ise biraz ilerleyip havuzu genel olarak görmesi için yazıldı

sonrası arama, konumlama ve güdümleme algoritmalarını içeriyor

arama algoritması ile çemberi bulmaya çalışıyor (çemberi bulamadığı durum yok gibi bişi, yoksa da kendi var gibi davranıyor)
konumlama algoritmasında 2 boyutlu kartezyende aracımız orjinde, çember ise 1.2.3. veya 4. bölgede, bu ikisini çakıştırmak için
çeşitli hareketler yapıyoruz motorlarla
güdümleme algoritmasında ise artık çemberi bulmuşuz, karşısına geçmişiz, aracımızı ortalamışız, artık içerisinden geçeceğiz

the end