class Category:
    def __init__(self,cat_name,sub_category):
        self.cat_name=cat_name
        self.sub_category=sub_category
      
class Product:
    def __init__(self,p_name,category):
        self.p_name=p_name
        self.category = category

    def display(self):
        # print(self.category.sub_category[0].cat_name)
        temp = self.category.sub_category
   
        print(self.category.cat_name ,end='->')
        while len(temp):
            
            print(temp[0].cat_name,end='->')
            temp = temp[0].sub_category
        print(self.p_name)
            
        

        
                
            
       
       
            
        
        
        
#Laptop
M1 = Category("M1", [])
M2 = Category("M2", [])
mac = Category("mac",[M1,M2])

w11=Category("w11",[])
w12=Category("w12",[])
windows=Category("windows",[w11,w12])

laptop = Category("laptop", [mac,windows])

#mobile
iphone15=Category('iphone15',[])
iphone16=Category('iphone16',[])
iphone=Category("iphone",[iphone15,iphone16])

m32=Category("m32",[])
m31=Category("m31",[])
android=Category("android",[m32,m31])

mobile=Category("mobile",[android,iphone])
#earpods
airdrops=Category("airdrops",[])
wireless=Category("wireless",[])
earpods=Category("earpods",[wireless])
electronics=Category('electronics',[laptop,earpods,mobile])

product=Product('product',electronics)
# product2=Product(M1,electronics)
product.display()

# Category-[electronics,..]
# sub-cat;[mobile,laptop],[],[]
# producut-[m32,z5]