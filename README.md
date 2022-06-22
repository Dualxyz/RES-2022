# RES - dokumentacija
## 1.Writer
Writer komponenta sluzi za uspostavljanje TCP konekcije sa **Replicatoru_sender **– om I salje mu automatski izgenerisanu poruku. Poruka se sastoji od dve stavke, koda I vrednosti. Writer komponenta se sastoji iz dve stavke Writer.py I WRITER_CLASS.py.
##### 1.1Writer.py
Writer.py se koristi kao vrsta meni-a gde korisnik odabirom jedne od tri opcije moze da manipulise radom writer komponenti:
   SLIKAAA
Ako izabere opciju jedan (1.) uz pomoc WRITER_CLASS.py će se kreirati novi writer. Ako se izabere opcija dva(2.) unosenjem odredjene istance cemo unistiti odredjen writer koja pripada toj instanci. Odabirom trece opcije(3.) izlazimo iz menija gde se automatiski sve instance writera unistavaju.
  SLIKAA
  ##### 1.2WRITER_CLASS.py
  Sluzi za kreiranje writera-a koji ce na svakih dve sekunde slati odredjenu poruku. Poruka se sastoji iz dva dela, Koda I Vrednosti. Kod je jedna od 6 vrednosti koje se nalaze u** CODE_LIST.py.**
  SLIKAA
   Vrednost je bilo koji broj od 1 do 100.Poruka se Kreira tako sto se nasumično uzme jedna od 6 vrednosti iz** CODE_LIST.py**  I nasumično izabere jedan celobrojan broj u intervalu od 1 do 100. Tako izgenerisana poruka se salje ** Replicatoru_senderu **– u.
   ## 2.Replicator-Sender
   Replicator_sender je komponenta koja prima poruku od Writer-a I nakon toga je prosleđuje** Replicator_receiver**-u. Sastoji se iz tri stavke: ReplicatorSender.py,REPLICATOR_RECEIVE_FROM_CLASS.py,REPLICATOR_SEND_TO_CLASS.py.
   ##### 2.1REPLICATOR_RECEIVE_FROM_CLASS.py
   Klasa koja se koristi za uspostavljanje veze sa **Writer**-om I primanje poruke od istog. Ukoliko poruka koja je primljena nije prazna ona se ispisuje u konzolu I  stavlja u buffer.
   SLIKAA
   ##### 2.2REPLICATOR_SEND_TO_CLASS.py
   Klasa koja se koristi za uspostavljanje veze sa **Replicator-receiver**-om I slanje poruke istom. Poruka koja se salje se uzima sa buffera, koju je tu stavio instanca klase REPLICATOR_RECEIVE_FROM_CLASS.py, ukoliko sam buffer nije prazan. poruka se zatim salje **Replicator-receiver**-u I pop-uje se iz buffer-a.
   SLIKAA
   ##### 2.3ReplicatorSender.py
   Klasa u kojoj se inicijalizuju instance prethodno opisanih klasa I u kojoj se inicijalizuje buffer. Koristi se za pokretanje samog** Replicator-sender**-a kao celine uz pomoc thread-ova.
   SLIKAA
   ## 3.Replicator-Receiver
   Replicator receiver je komponenta koja prima poruku od **Replicator-sender**-a I zatim je od zavisnosti sadrzaja poruke prosledjuje istu odredjenom **Reader**-u. Sastoji se od sledecih komponenti: RECEIVER_RECEIVE_FROM_CLASS.py, RECEIVER_SEND_TO_CLASS.py, Struct.py, ReplicatorReceiver.py.
   ##### 3.1ReplicatorSender.py
   Klasa REPLICATOR_RECEIVE_FROM se koristi za uspostavljanje konekcije sa Replicator-sender-om nakon cega prima poruku koju mu je poslao I nju stavlja u buffer.
   SLIKAA
##### 3.2Struct.py
Klasa Collection_Description koja se nalazi u Struct.py se koristi za odredjivanje DATASET-a kojem poruka pripada u zavisnosti od koda poruke.
SLIIKAA
##### 3.3RECEIVER_SEND_TO_CLASS.py
Klasa RECEIVER_SEND_TO se koristi za uspostavljanje veze sa **Reader**-om I slanje poruke istom.
SLIIKAA
##### 3.4ReplicatorReceiver.py
Klasa u kojoj se inicijalizuju instance prethodno opisanih klasa I u kojoj se inicijalizuje buffer. Sa njom se pokrece sam Replicator-receiver. Radi na način tako sto se instance klase REPLICATOR_RECEIVER_FROM pokrece u tredu. Nakon toga proverava da li u buffer ima poruka I ako ima uzima poruku i split –uje je u dve promenjive nakon cega se potiva klasa Collection_Description kako bi se odredio DATASET za tu poruku.
SLIKAAA
Nakon odredjivanja DATASETA-a poruka se salje salje odredjenom tipu Readera u zavisnosti od vrste DATASETA-a kojoj poruka pripada. Nakon slanja poruke ona se pop-uje sa buffera.
SLIKAA
   ## 4.Reader
   Reader je komponenta koja prima poruku **Replicator-receiver**-a I nakon toga poruku upisuje u database. Postoje 4 vrste Reader-a za svaki tip DATASET-a. Svaki od njih radi po istom principu I sastoje se od istih komponenti: READER_OOP.py, READER_RECEIVE_CLASS.py, Reader_n.py
   ##### 4.1READER_RECEIVE_CLASS.py
   Klasa READER_RECEIVE se koristi za uspostavljanje konekcije sa **Replicator-receiverom**-om nakon cega prima poruku koju mu je poslao I nju stavlja u buffer.
   SLIKEE
   ##### 4.2READER_OOP.py
   Klasa READER_TO_DB sluzi da uzme poruku koju je instanca READER_RECEIVE klase stavio u buffer I nakon toga je upise u database.
   SLIKAA
   Ona takodje vrsi proveru poruke. Ako je kod poruke tipa CODE_DIGITAL poruka ce se automatski upisati u database. Ukoliko je kod bilo kog drugog tipa onda ce se vrednost poruke poredeti sa drugim vrednostima koji su upisanu u database I imaju isti kod I ako je razlika izmedju njih veca od 2% poruka će moci  da se upise u database. U suprotnom se poruka neće upisati.
   SLIKAA
   ##### 4.3Reader_n.py
   Slovo n predstavlja jedan od 4 vrste readera. Ovde se incijalizuju buffer I  instance ostalih klasa  koje se stavljaju u thread-ove , samim tim sluzi za pokretanje samog Reader-a.
   SLIKAA
   
   ## 5.Logger
   SEND_TO_LOG ima klasu LOG koja se implementira nad svakoj klasi kako bi mogle slati poruke logeru o trenutnim aktivnostima.Logger.py je server koji prima poruke poslate putem send_to_log I upisuje ih file.
   SLIKAA
