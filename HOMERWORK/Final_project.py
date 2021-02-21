# Resül ŞAHİN 
# Global Ai HUB final projet 21/02/2021


class YemekYapımı(): 
    def __init__(self,yemekAdi): 
        self.yemekAdi=yemekAdi

    def malzemeler(self,malzeme):
        self.malzeme=malzeme
        print("\nMALZEMELER:")

    def hazirlanisi(self,hazirlanis):
        self.hazirlanis=hazirlanis
        print("\nHAZIRLANIŞI:")


class Menemen(YemekYapımı):
    def __init__(self,yemekAdi):
        yemekAdi="Menemen"
        super().__init__(yemekAdi)
        print("Menemen yapımı:")
    
    def malzemeler(self):
        malzeme="2 yemek kaşığı sıvı yağ, 3 adet yeşil biber (Sap ve çekirdekleri temizledikten sonra, ince doğranmış), 3 orta boy domates, , 1/2 çay kaşığı tuz. 3 adet yumurta. "
        super().malzemeler(malzeme)
        print(f"{self.malzeme}")
        

    def hazirlanisi(self):
        hazirlanis=" Sıvı yağı ve biberleri tavaya alarak biberlerin rengi dönünceye kadar kavurun. Üzerine kabukları soyulup küçük küçük doğranmış domatesleri ilave edin. Kısık ocakta tavanın kapağını kapatarak domateslerin iyice pişmesini bekleyin. Domatesler çok suyu değil, tavaya yapışıyorsa birazcık kaynar su ekleyebilirsiniz. Genellikle de bu duruma gerek kalmayacaktır. Fotoğraftaki gibi domatesler piştikten sonra yumurtaları kırabilirsiniz. Yumurtaları ister ayrı bir kapta çırpıp ekleyin isterseniz de benim gibi tavaya kırıp tavada karıştırabilirsiniz Menemeni sıcak olarak servis yapın. "
        super().hazirlanisi(hazirlanis)
        print(f"{self.hazirlanis}")


class Karniyarik(YemekYapımı):
    def __init__(self,yemekAdi):
        yemekAdi="Karnıyarık"
        super().__init__(yemekAdi)
        print("\nKarnıyarık Tarifi")
    
    def malzemeler(self):
        malzeme="6 adetorta boy patlıcan, 3 yemek kaşığızeytinyağı, 1 adetbüyük boy kuru soğan, 2 adetyeşil biber(iç harcı için), 350 gramkıyma, 2 dişsarımsak, 1/2 tatlı kaşığıbiber salçası, 1/2 tatlı kaşığıdomates salçası, 1 çay kaşığıtuz, 1 çay kaşığıkarabiber, 2 adetdomates,  6 adetorta boy yeşil sivri biber, 1 avuçmaydanoz"
        super().malzemeler(malzeme)
        print(f"{self.malzeme}")

    def hazirlanisi(self):
        hazirlanis="Bol suda yıkadığınız patlıcanları, pijamalı şekilde soyun ve tuzlu suda bekletin, Yemek kaşığı zeytinyağını bir tavada kızdırın. Yemeklik doğradığınız 1 adet soğanı da üzerine ekleyip pembeleşene kadar kavurun. 2 adet doğranmış yeşil biberi ilave edip kavurmaya devam edin. 350 gram orta yağlı kıymayı da ekleyin ve kavrulmakta olan soğanlarla birlikte renk alıp, suyunu çekene kadar pişirin.  Aralarda karıştırıp pişirme işlemine devam ederek sırasıyla; 2 diş sarımsak, yarım tatlı kaşığı domates salçası, yarım tatlı kaşığı biber salçası eleyin.  2 adet küp doğranmış domatesi ekleyin, 5 dakika kadar pişirdikten sonra ocağın altını kısın ve bir avuç doğranmış maydanozu ekleyip son kez karıştırarak ocaktan alın. Acısını alıp, pijamalı soyduğunuz 6 adet patlıcanı kızartın , Fırına dayanıklı bir kaba yerleştirin , Orta kısımlarından patlıcanları yarın. Hazırladığınız iç harçtan bol bol ekleyin.  Patlıcanların üzerine birer cherry domates ve biber dilimleri ekleyin. Karnıyarıkları önceden ısıtılmış 170 derece fırında 20-25 dakika kadar pişirdikten sonra, sıcak olarak, dilerseniz tereyağlı pirinç pilavı eşliğinde servis edin, afiyet olsun! " 
        super().hazirlanisi(hazirlanis)
        print(f"{self.hazirlanis}")
        

class Sütlac(YemekYapımı):
    def __init__(self,yemekAdi):
        yemekAdi="Sütlaç"
        super().__init__(yemekAdi)
        print("\nSütlaç Tarifi:")
    
    def malzemeler(self):
        malzeme="1 lt süt, 2 çay bardağı pirinç, 1 litre su, 3 yemek kaşığı pirinç unu, 1,5 -2 su bardağı toz şeker (eğer çok şekerli sevmiyorsanız 1,5 bardak kullanabilirsiniz) , 1 su bardağı süt, tarçın"
        super().malzemeler(malzeme)
        print(f"{self.malzeme}")
        
    def hazirlanisi(self):
        hazirlanis="Sütlaç yapmak için öncelikle pirinci yıkayıp su ile ateşe koyun., Pirinçler uzayıp suyu çekene kadar kaynatın, soğuk sütü ekleyin. ,1-2 defa karıştırıp, kaynamasını bekleyin., Bu arada bir kasede pirinç ununu 1 su bardağı soğuk süt ile ezin. , Tencerede kaynamakta olan sütten 1-2 kepçe alıp kaseye ekleyin. (pirinç unu ılınmış olmalı)., Pirinç ununu tencereye ekleyin, ara sıra karıştırarak 10 dakika kadar pişirin., Toz şekeri ilave edip karıştırın ve 1-2 taşım kaynatın., Sütlacı kaselere paylaştırın., Soğuyunca sütlaçların üzerlerine tarçın serperek servis edebilirsiniz. Afiyet olsun."
        super().hazirlanisi(hazirlanis)
        print(f"{self.hazirlanis}")

      
ana_yemek = YemekYapımı("Menemen")

# yemek 1 menemen
yemek1 = Menemen("Menemen")
yemek1.malzemeler()
yemek1.hazirlanisi()

#yemek 2 karniyariki
yemek2 = Karniyarik("Karnıyarık")
yemek2.malzemeler()
yemek2.hazirlanisi()



# yemek 3 sütlaç
yemek3=Sütlac("Sütlaç")
yemek3.malzemeler()
yemek3.hazirlanisi()

