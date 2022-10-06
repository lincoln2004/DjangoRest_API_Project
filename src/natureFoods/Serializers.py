from rest_framework import serializers
import natureFoods.models as md 

class FruitSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = md.fruits
        
        exclude = ['id']
        

class VegetalSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = md.vegetals
        
        exclude = ['id']        