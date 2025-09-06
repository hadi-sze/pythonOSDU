from django.shortcuts import render
import json
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from .models import Tempwell,NIOC_Production
from .models import POOL_TYPE,R_WELL_STATUS,R_WELL_STATUS_TYPE
from .serializers import wellSerializer
from django.core.exceptions import ObjectDoesNotExist
 
Well={
    'name':"Wall1",
    'soild':10,
    'water':"40%",
    'OnService':"Yes"
}

well1 = {
  "name": "John",
  "age": 30,
  "Active": True,
  "Ofshore": False,
  "children": ("osc1","nioc2"),
  "pets": None,
  "Pipelining": [
    {"model": "marshal 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

def test(request):
    return HttpResponse("Hello world!")

def wellreport(request):
    return JsonResponse(Well)

def wellreport1(request):
    return JsonResponse(well1)

def getallwell(respone):
           if respone.method == 'GET':
            items = list(POOL_TYPE.objects.all())
            return JsonResponse(items, safe=False) 



@csrf_exempt
def create_well(respone):
     if respone.method == 'POST':
        data = json.loads(respone.body)
        item = Tempwell.objects.create(id=data['id'], wellname=data['wellname'],componyname=data['componyname'] , amount=data['amount'] )
        return JsonResponse({'id': item.id, 'wellname': item.wellname, 'componyname': item.componyname,'amount':item.amount
                             
                             
                             }, status=201) # 201 Created
     return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def delete_byid(request):
    try:
        _id=request.GET.get('id', None)
        int_id=int(_id)
        _getwell=Tempwell.objects.get(id=int_id)
        _getwell.delete()
        return JsonResponse({'well': "was removed"}, safe=False, )
    except Tempwell.DoesNotExist as e :
        return JsonResponse ({'error': str(e)}, status=403)



@csrf_exempt
def addwell(respone):
    # /payload = json.loads(respone.GET)
    id1=respone.GET.get('id', None)
    wellname1=respone.GET.get('wellname', None)
    componyname1=respone.GET.get('componyname', None)
    amount1=respone.GET.get('amount', None)
    _wlllnew=Tempwell.objects.create( id=id1, wellname=wellname1,componyname=componyname1,
            amount=amount1 )
 
    return JsonResponse({'wells': "OK Aded"}, safe=False, )
     
    
    # return JsonResponse({'wells': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    # except ObjectDoesNotExist as e:
    #     return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    # except Exception:
    #     return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Create your views here.≈


def getProduction(respons):
     if respons.method == 'GET':
       items = list(NIOC_Production.objects.all().values('id', 'title', 'amount'))
       return JsonResponse(items, safe=False) 
     return JsonResponse({{'error': 'empty'}}, safe=False) 

 

 # //////////////       POOL View.       //////////////////

def GetPooType(respone):
   if respone.method == 'GET':
            items = list(POOL_TYPE.objects.all().values())
            return JsonResponse(items, safe=False)
   




 # //////////////       Well View.       //////////////////
def GetWELL_STATUS(respone):
   if respone.method == 'GET':
            items = list(R_WELL_STATUS.objects.all().values())
            return JsonResponse(items, safe=False)
         

def GetWELLSTATUSTYPE(respone):
        if respone.method == 'GET':
            items = list(R_WELL_STATUS_TYPE.objects.all().values())
            return JsonResponse(items, safe=False)
         
         
