from rest_framework import serializers
from .models import *
class TaxiFareSerializer(serializers.Serializer):
    dep_lat = serializers.FloatField()
    dep_lng = serializers.FloatField()
    arr_lat = serializers.FloatField()
    arr_lng = serializers.FloatField()


class Navigationdata(serializers.ModelSerializer):
    class Meta:
        model=Naviagtion_bar
        fields='__all__'
class Carouseldata(serializers.ModelSerializer):
    class Meta:
        model=Home_carousel
        fields='__all__'


########################  flights    ################################
        
from rest_framework import serializers
from .models import *

class flights_serialization(serializers.ModelSerializer):
    class Meta:
        model=flights_offercards
        fields="__all__"

class kotak_serialization(serializers.ModelSerializer):
    class Meta:
        model=flights_kotak_offer
        fields="__all__"

class kotakterms_serialization(serializers.ModelSerializer):
    class Meta:
        model=flights_kotak_terms
        fields="__all__" 

class kotakpolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=flights_policy
        fields="__all__" 

class kotakpolicy1_serialization(serializers.ModelSerializer):
    class Meta:
        model=flights_policy1
        fields="__all__"

class kotak_serialization1(serializers.ModelSerializer):
    class Meta:
        model=flights_kotak_offer1
        fields="__all__"        

## first booking ##

class flight_firstser(serializers.ModelSerializer):
    class Meta:
        model=flight_offer_first
        fields="__all__"

class flight_first1ser(serializers.ModelSerializer):
    class Meta:
        model=flight_offer_first1
        fields="__all__"


# ..................card1 serialization Yes Bank....................
class card1_offers_serialization(serializers.ModelSerializer):
    class Meta:
        model=card1_offers
        fields="__all__"

class card1_offerdetailes_serialization(serializers.ModelSerializer):
    class Meta:
        model=card1_offerdetailes
        fields="__all__"

class card1_terms_conditions_serialization(serializers.ModelSerializer):
    class Meta:
        model=card1_terms_conditions
        fields="__all__"

## FAQ ##
        
class flightfaqs_serialization(serializers.ModelSerializer):
    class Meta:
        model=faqs
        fields='__all__'   
        
#................100% Refund card...........

from .models import  Zero_cancellation_offer,Zero_cancellation_terms

class ZC_offer_serialization(serializers.ModelSerializer):
    class Meta:
        model=Zero_cancellation_offer
        fields="__all__"

class zc_terms_serialization(serializers.ModelSerializer):
    class Meta:
        model=Zero_cancellation_terms
        fields="__all__"           

#....why choose us...#

class why_chooseser(serializers.ModelSerializer):
    class Meta:
        model=why_choose
        fields="__all__"

#....question...#
        
class content_serialization(serializers.ModelSerializer):
    class Meta:
        model=choosing_content
        fields="__all__"

#....icic...#
        
class icic_serialization(serializers.ModelSerializer):
    class Meta:
        model=icic_offer
        fields="__all__"

class icici_serialization(serializers.ModelSerializer):
    class Meta:
        model=icic_terms
        fields="__all__"    

#...................sbi card......................

class sbiimage_serialization(serializers.ModelSerializer):
    class Meta:
        model=sbiimage
        fields="__all__"

class sbioffer_serialization(serializers.ModelSerializer):
    class Meta:
        model=sbioffer
        fields="__all__"

class sbiterms_serialization(serializers.ModelSerializer):
    class Meta:
        model=sbiterms
        fields="__all__"            

#...................hdfc card......................
        
class hdfc_logoser(serializers.ModelSerializer):
    class Meta:
        model=hdfc_logo
        fields="__all__"             
class hdfc_offerser(serializers.ModelSerializer):
    class Meta:
        model=hdfc_offer
        fields="__all__"         
      
#......................HOTELS...........................#
  

from .models import *
from rest_framework import serializers



class cardsserializationclass(serializers.ModelSerializer):
    class Meta:
        model=hotel_cards
        fields= ['title', 'content', 'image', 'url']
        extra_kwargs = {
            'title': {'required': False},
            'content': {'required': False},
            'image': {'required': False},
            'url': {'required': False}
        } 

#...Axis...#

class hotel_axis_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_axisoffer
        fields= ['image']
        extra_kwargs = {
            'image': {'required': False} 
        } 



class hotel_axispolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_axispolicy
        fields = ['content', 'content1', 'content2', 'content3', 'content4']
        extra_kwargs = {
            'content': {'required': False},
            'content1': {'required': False},
            'content2': {'required': False},
            'content3': {'required': False},
            'content4': {'required': False}
            
        } 

class hotel_axisserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_axisoffer1
        fields= ['product', 'offer']
        extra_kwargs = {
            'product': {'required': False},
            'offer': {'required': False}
        }         

#...icici...#
        
class hotel_icici_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_icicioffer
        fields= ['image', 'title', 'couponcode']
        extra_kwargs = {
            'image': {'required': False},
            'title': {'required': False},
            'couponcode': {'required': False}
        } 



class hotel_icicipolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_icicipolicy
        fields = ['content', 'content1', 'content2', 'content3', 'content4']
        extra_kwargs = {
            'content': {'required': False},
            'content1': {'required': False},
            'content2': {'required': False},
            'content3': {'required': False},
            'content4': {'required': False}
            
        } 

class hotel_iciciserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_icicioffer1
        fields= ['applicable', 'offer']
        extra_kwargs = {
            'applicable': {'required': False},
            'offer': {'required': False}
        }           

#...HSBC...#

class hotel_hsbc_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_hsbcoffer
        fields= ['image', 'title', 'couponcode']
        extra_kwargs = {
            'image': {'required': False},
            'title': {'required': False},
            'couponcode': {'required': False}
        }



class hotel_hsbcpolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_hsbcpolicy
        fields = ['data', 'data1', 'data2', 'data3', 'data4']
        extra_kwargs = {
            'data': {'required': False},
            'data1': {'required': False},
            'data2': {'required': False},
            'data3': {'required': False},
            'data4': {'required': False} 
        } 

class hotel_hsbcserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_hsbcoffer1
        fields= ['applicable', 'offer']
        extra_kwargs = {
            'applicable': {'required': False},
            'offer': {'required': False}
        }                  

#...SBI....#
        
class hotel_sbi_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_sbioffer
        fields= ['image', 'title', 'couponcode']
        extra_kwargs = {
            'image': {'required': False},
            'title': {'required': False},
            'couponcode': {'required': False}
        }



class hotel_sbipolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_sbipolicy
        fields = ['cnt', 'cnt1', 'cnt2', 'cnt3', 'cnt4']
        extra_kwargs = {
            'cnt': {'required': False},
            'cnt1': {'required': False},
            'cnt2': {'required': False},
            'cnt3': {'required': False},
            'cnt4': {'required': False} 
        }  

class hotel_sbiserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_sbioffer1
        fields= ['applicable', 'offer']
        extra_kwargs = {
            'applicable': {'required': False},
            'offer': {'required': False}
        }                 

#...KOTAK...#
        

class hotel_kotak_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_kotakoffer
        fields= ['image', 'title', 'couponcode']
        extra_kwargs = {
            'image': {'required': False},
            'title': {'required': False},
            'couponcode': {'required': False}
        }


class hotel_kotakpolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_kotakpolicy
        fields = ['cntnt', 'cntnt1', 'cntnt2', 'cntnt3']
        extra_kwargs = {
            'cntnt': {'required': False},
            'cntnt1': {'required': False},
            'cntnt2': {'required': False},
            'cntnt3': {'required': False}  
        } 

class hotel_kotakserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_kotakoffer1
        fields= ['applicable', 'offer']
        extra_kwargs = {
            'applicable': {'required': False},
            'offer': {'required': False}
        }         

#.....BOB.....#
        

class hotel_bob_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_boboffer
        fields= ['photo', 'title', 'cpncode']
        extra_kwargs = {
            'photo': {'required': False},
            'title': {'required': False},
            'cpncode': {'required': False}
        }

class hotel_bobpolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_bobpolicy
        fields = ['term', 'term1', 'term2', 'term3']
        extra_kwargs = {
            'term': {'required': False},
            'term1': {'required': False},
            'term2': {'required': False},
            'term3': {'required': False} 
        } 

class hotel_bobserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_boboffer1
        fields = ['category', 'couponcode', 'offer']
        extra_kwargs = {
            'category': {'required': False},
            'couponcode': {'required': False},
            'offer': {'required': False}
        }            


#...FEDERAL...#  


class hotel_federal_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_federaloffer
        fields= ['image', 'title', 'couponcode']
        extra_kwargs = {
            'image': {'required': False},
            'title': {'required': False},
            'couponcode': {'required': False}
        }



class hotel_federalpolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_federalpolicy
        fields = ['cntnt', 'cntnt1']
        extra_kwargs = {
            'cntnt': {'required': False},
            'cntnt1': {'required': False}
        }  

class hotel_federalserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_federaloffer1
        fields= ['applicable', 'offer']
        extra_kwargs = {
            'applicable': {'required': False},
            'offer': {'required': False}
        }  



        
                      
#################################  cabs #############################
from rest_framework import serializers
from .models import *

class cab_serialization(serializers.ModelSerializer):
    class Meta:
        model = cab_cards
        fields = ['title', 'description', 'photo', 'code', 'Link']
        extra_kwargs = {
            
            'title': {'required': False},
            'description': {'required': False},
            'photo': {'required': False},
            'code': {'required': False},
            'Link': {'required': False}
        }


###############  2nd page for 1st card ##########

class festive_serialization(serializers.ModelSerializer):
    class Meta:
        model = cab_festive
        fields = ['photo', 'title', 'point1', 'point2', 'point3', 'point4', 'point5', 'point6', 'point7', 'point8', 'point9', 'point10', 'point11', 'point12']
        extra_kwargs = {

            'photo': {'required': False},
            'title': {'required': False},
            'point1': {'required': False},
            'point2': {'required': False},
            'point3': {'required': False},
            'point4': {'required': False},
            'point5': {'required': False},
            'point6': {'required': False},
            'point7': {'required': False},
            'point8': {'required': False},
            'point9': {'required': False},
            'point10': {'required': False},
            'point11': {'required': False},
            'point12': {'required': False}

        }



###############  2nd page for 2nd card ##########

class rental_serialization(serializers.ModelSerializer):
    class Meta:
        model = cab_rental
        fields = ['photo', 'title', 'point1', 'point2', 'point3', 'point4', 'point5', 'point6', 'point7', 'point8', 'point9', 'point10', 'point11', 'point12']
        extra_kwargs = {

            'photo': {'required': False},
            'title': {'required': False},
            'point1': {'required': False},
            'point2': {'required': False},
            'point3': {'required': False},
            'point4': {'required': False},
            'point5': {'required': False},
            'point6': {'required': False},
            'point7': {'required': False},
            'point8': {'required': False},
            'point9': {'required': False},
            'point10': {'required': False},
            'point11': {'required': False},
            'point12': {'required': False}
        }
###############  2nd page for 3rd card ##########

class anytime_serialization(serializers.ModelSerializer):
    class Meta:
        model = cab_anytime
        fields = ['photo', 'heading', 'content', 'title', 'point1', 'point2', 'point3', 'point4', 'point5', 'point6', 'point7', 'point8', 'point9', 'point10', 'point11', 'point12']
        extra_kwargs = {

            'photo': {'required': False},
            'heading': {'required': False},
            'content': {'required': False},
            'title': {'required': False},
            'point1': {'required': False},
            'point2': {'required': False},
            'point3': {'required': False},
            'point4': {'required': False},
            'point5': {'required': False},
            'point6': {'required': False},
            'point7': {'required': False},
            'point8': {'required': False},
            'point9': {'required': False},
            'point10': {'required': False},
            'point11': {'required': False},
            'point12': {'required': False}
        }




###############  2nd page for 4th card ##########

class ride_serialization(serializers.ModelSerializer):
    class Meta:
        model = cab_ride
        fields = ['photo', 'title', 'point1', 'point2', 'point3', 'point4', 'point5', 'point6', 'point7', 'point8', 'point9', 'point10', 'point11', 'point12']
        extra_kwargs = {

            'photo': {'required': False},
            'title': {'required': False},
            'point1': {'required': False},
            'point2': {'required': False},
            'point3': {'required': False},
            'point4': {'required': False},
            'point5': {'required': False},
            'point6': {'required': False},
            'point7': {'required': False},
            'point8': {'required': False},
            'point9': {'required': False},
            'point10': {'required': False},
            'point11': {'required': False},
            'point12': {'required': False}
        }
    


###############  2nd page for 5th card ##########


class familyfun_serialization(serializers.ModelSerializer):
    class Meta:
        model = cab_familyfun
        fields = ['photo', 'heading', 'content', 'title', 'point1', 'point2', 'point3', 'point4', 'point5', 'point6', 'point7', 'point8', 'point9', 'point10', 'point11', 'point12']
        extra_kwargs = {

            'photo': {'required': False},
            'heading': {'required': False},
            'content': {'required': False},
            'title': {'required': False},
            'point1': {'required': False},
            'point2': {'required': False},
            'point3': {'required': False},
            'point4': {'required': False},
            'point5': {'required': False},
            'point6': {'required': False},
            'point7': {'required': False},
            'point8': {'required': False},
            'point9': {'required': False},
            'point10': {'required': False},
            'point11': {'required': False},
            'point12': {'required': False}
        }




###############  2nd page for 6th card ##########

class easy_serialization(serializers.ModelSerializer):
    class Meta:
        model = cab_easy
        fields = ['photo', 'title', 'point1', 'point2', 'point3', 'point4', 'point5', 'point6', 'point7', 'point8', 'point9', 'point10', 'point11', 'point12']
        extra_kwargs = {

            'photo': {'required': False},
            'title': {'required': False},
            'point1': {'required': False},
            'point2': {'required': False},
            'point3': {'required': False},
            'point4': {'required': False},
            'point5': {'required': False},
            'point6': {'required': False},
            'point7': {'required': False},
            'point8': {'required': False},
            'point9': {'required': False},
            'point10': {'required': False},
            'point11': {'required': False},
            'point12': {'required': False}
        }





###############  2nd page for 7th card ##########

class offer15_serialization(serializers.ModelSerializer):
    class Meta:
        model = cab_offer_card
        fields = ['photo', 'title', 'point1', 'point2', 'point3', 'point4', 'point5', 'point6', 'point7', 'point8', 'point9', 'point10', 'point11', 'point12']
        extra_kwargs = {

            'photo': {'required': False},
            'title': {'required': False},
            'point1': {'required': False},
            'point2': {'required': False},
            'point3': {'required': False},
            'point4': {'required': False},
            'point5': {'required': False},
            'point6': {'required': False},
            'point7': {'required': False},
            'point8': {'required': False},
            'point9': {'required': False},
            'point10': {'required': False},
            'point11': {'required': False},
            'point12': {'required': False}
        }



###############  2nd page for 8th card ##########

class paytm_card_serialization(serializers.ModelSerializer):
    class Meta:
        model = cab_paytm_card
        fields = ['photo', 'title', 'point1', 'point2', 'point3', 'point4', 'point5', 'point6', 'point7', 'point8', 'point9', 'point10', 'point11', 'point12']
        extra_kwargs = {

            'photo': {'required': False},
            'title': {'required': False},
            'point1': {'required': False},
            'point2': {'required': False},
            'point3': {'required': False},
            'point4': {'required': False},
            'point5': {'required': False},
            'point6': {'required': False},
            'point7': {'required': False},
            'point8': {'required': False},
            'point9': {'required': False},
            'point10': {'required': False},
            'point11': {'required': False},
            'point12': {'required': False}
        }

