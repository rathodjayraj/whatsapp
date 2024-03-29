from whatsapp_app.views.files_import import * 
import requests
from requests.exceptions import RequestException, JSONDecodeError
from json.decoder import JSONDecodeError
from selenium import webdriver



def templatelist(request):

    #api_url = "https://society.gujjucode.com/api/wpbox/getTemplates?token=SLiwZiw4xgAHce1k4Y6TAW79XxoHxasyPj8nWrW18aa594b5"
    api_url = "https://society.gujjucode.com/api/wpbox/getTemplates?token=IcPk9Flec3oHtfcI9nLu4npOVGXBV7DVsx6z6KD43eabe511"
    #api_url = "https://developers.facebook.com/2252914984814495/message_templates"
    response = requests.get(api_url)
    data=response.json()


    baseurl = "https://graph.facebook.com/v19.0/242783256342267/message_templates?access_token=EAAJMcXGQBO8IRURFZCcOS7BonRZCZBpCkaZAlU7GgZBwvMTIZAQcWfnMIzizPluT9LdM3pa1TKvtXbQLcDqXnttZAu0WaQPjCcqQLP2ZC7iPs0fO7pgfgWY8cnu4wxqo8Ya1CZB8PunHqeX7HOf3uzkDigulmAELKbjqqWnuwQudrVHe7pT4cE4ZCJyAQO5ZBW6rhoSqjS3ZCR88zMN28ssOc2GtM3J2fCqSNvmZArq9n4j0Cs1Fp4&debug=all&format=json&method=get&origin_graph_explorer=1&pretty=0&suppress_http_code=1&transport=cors"

    return render(request,"adminTemplate/templatelist/templatelist.html",{"data":data['templates']})




def contactlist(request):

    api_url = "https://society.gujjucode.com/api/wpbox/getContacts?token=IcPk9Flec3oHtfcI9nLu4npOVGXBV7DVsx6z6KD43eabe511"
    response = requests.get(api_url)
    data=response.json()
    data = data['contacts']
    reversed_entries = data[::-1]

    # api_url2 = "https://society.gujjucode.com/api/wpbox/chat/3?token=IcPk9Flec3oHtfcI9nLu4npOVGXBV7DVsx6z6KD43eabe511"
    # response2 = requests.get(api_url2)
    # data2=response2.json()
    # print(data2,'jjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
    # reversed_entries2 = data2[::-1]


    email ="info@gujjucode.com"
    password="Jayraj@2015"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    URL="https://society.gujjucode.com/login" 
    
    data= {
        email:email,
        password:password
        
    } 
    r=requests.post(url=URL, data=data,headers={ 'user-agent': 'I am a BOT script' }) 
    print(r,"dsdsdsdsdsd")
   # print(r.json()) 

    context= {
        "data" : reversed_entries,
        # "data2":reversed_entries2
    }

    return render(request,"adminTemplate/templatelist/contactlist.html",context)

def campainlist(request):

    
    api_url = "https://society.gujjucode.com/campaigns/18/show?token=IcPk9Flec3oHtfcI9nLu4npOVGXBV7DVsx6z6KD43eabe511&type=1"
    response = requests.get(api_url)
    response.raise_for_status()  # Check for HTTP errors
    data=reversed(response.json())


    return render(request,"adminTemplate/templatelist/campainlist.html",{"data":data})


def category(request):
    try:
        username_id=get_user_details(request)
        data=Category.objects.filter(user_details_id=username_id).order_by('-createDate')
        return render(request,"posTemplate/product_management/categorylist.html",{"data":data})
    except Exception as e:
        print(e,"in category function")
        return redirect('error')

def addcategory(request):
    try:
        if(request.method=="POST"):
            if(request.POST['cat_id']==''):
                print("inside add ")
                username_id=get_user_details(request)
                cat_name=request.POST['cat_name']
                cat_code=request.POST['cat_code']
                
                desc=request.POST['desc']
                ###########################
                cat_obj=Category()
                cat_obj.category_name=cat_name
                if(cat_code!=""):
                    cat_obj.category_code=cat_code
                cat_obj.category_desc=desc
                try:
                    cat_img=request.FILES['cat_img']
                    cat_obj.category_image=cat_img
                except:
                    pass
                cat_obj.user_details_id=username_id
                cat_obj.created_by = loginuserdetail(request)
                cat_obj.save()        
                return redirect('category')
            else:
                print("inside update")

                cat_name=request.POST['cat_name']
                cat_code=request.POST['cat_code']
                
                desc=request.POST['desc']
                ###########################
                cat_obj=Category.objects.get(id=request.POST['cat_id'])
                cat_obj.category_name=cat_name
                if(cat_code!=""):
                    cat_obj.category_code=cat_code
                cat_obj.category_desc=desc
                cat_obj.created_by = loginuserdetail(request)
                cat_obj.updateDate=date.today()
                try:
                    cat_img=request.FILES['cat_img']
                    cat_obj.category_image=cat_img
                except:
                    pass
                cat_obj.save()    
                return redirect('category')
                

        else:
            return render(request,"posTemplate/product_management/addcategory.html",{"data":"Add","data2":"Create new product Category"})
    
    except Exception as e:
        print(e,"in addcategory function")
        return redirect('error')
    
def updatecategory(request,id):
    try:
        cat_obj=Category.objects.get(id=id)
        return render(request,"posTemplate/product_management/addcategory.html",{"cat_obj":cat_obj,"data":"Update","data2":"Update existing product Category "})
    
    except Exception as e:
        print(e,"in updatecategory function")
        return redirect('error')
    
def deletecategory(request,id):
    try:
        cat_obj=Category.objects.get(id=id)
        try:
            if cat_obj.category_image.name!="img/noimage.png":
                os.remove(cat_obj.category_image.path)
        except:
            pass
        cat_obj.delete()
        return redirect('category')
    except Exception as e:
        print(e,"in deletecategory function")
        return redirect('error')

####################################### status category #########################################

def change_state_category(request,id):
    try:
        p_t_m_obj=Category.objects.get(id=id)
        if(p_t_m_obj.category_status=="Active"):
            p_t_m_obj.category_status="InActive"
        else:
            p_t_m_obj.category_status="Active"
        p_t_m_obj.save()
        return redirect('category')
    except Exception as e:
        print(e,"in change_state_category function")
        return redirect('error')