from django.shortcuts import render,HttpResponse
from app01.models import *
from app01.algorithm.main import *

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

caseName=""
materialName=""
case_list=0
editedVideo=0
shot_list=[]
startShot=0
endShot=0
# Create your views here.

def index(req):
    return render(req,"index.html")

def repo_base(req):
    #读取所有的视频文件 model 检索功能
    video_list = CVE_Case.objects.all()
    flag=False
    search = ""
    if req.method == "POST":
        search=req.POST.get("search")
        flag=True



    return render(req, "repo_base.html", locals())



#-----
def repo_1(req):
    #只针对该功能的检索视频结果展示
    video_list=CVE_Case_Tags.objects.order_by('product_type')
    video_list2 = CVE_Case.objects.all()
    return render(req,"repo_1.html",locals())

def repo_2(req):
    #只针对该功能的检索视频结果展示
    video_list = CVE_Case_Tags.objects.order_by('product_style')
    video_list2 = CVE_Case.objects.all()
    return render(req,"repo_2.html",locals())

def repo_3(req):
    #只针对该功能的检索视频结果展示
    video_list = CVE_Case_Tags.objects.order_by('busi_orientation')
    video_list2 = CVE_Case.objects.all()
    return render(req,"repo_3.html",locals())

def repo_4(req):
    #只针对该功能的检索视频结果展示
    video_list = CVE_Case_Tags.objects.order_by('media')
    video_list2 = CVE_Case.objects.all()
    return render(req,"repo_4.html",locals())

def repo_5(req):
    #只针对该功能的检索视频结果展示
    video_list = CVE_Case_Tags.objects.order_by('year')
    video_list2 = CVE_Case.objects.all()
    return render(req,"repo_5.html",locals())

def repo_6(req):
    #只针对该功能的检索视频结果展示
    video_list = CVE_Case_Tags.objects.order_by('consumer')
    video_list2 = CVE_Case.objects.all()
    return render(req,"repo_6.html",locals())
#-----



def case_change(req):
    # 这里req的内容 应该是从之前提交过来的
    # 这里直接写死 name和id
    videoId=1
    videoName="video1.avi"
    # 根据内容去数据库里面取
    video=CVE_Case.objects.filter(case_id=videoId)
    shot_list=CVE_Shot.objects.filter(case_id=videoId)
    return render(req,"case_change.html",locals())

def upload_material(req):
    caseId=0
    case=0
    caseName=""
    materialName=""
    if  req.method == 'GET':
        caseId=req.GET.get("id")
        print(caseId)
        case=CVE_Case.objects.filter(case_id=caseId)
        caseName=case[0].name
        return render(req,"upload_material.html",locals())
    elif req.method == "POST":
        obj=req.FILES.get("fileUpload")
        caseName=req.POST.get("caseName")
        materialName=obj.name
        f=open(os.path.join(BASE_DIR,'templates','pic',obj.name),'wb')
        for line in obj.chunks():
            f.write(line)
        f.close()
        return render(req,"upload_material.html",locals())

def analyzing(req):
    return render(req,"analyzing.html",locals())




def display_case_parameter(req):
    global caseName
    global case_list
    global editedVideo
    global shot_list
    global startShot
    global endShot
    global materialName

    if req.method == 'GET':
        caseName=req.GET.get("caseName")
        materialName=req.GET.get("materialName")
        print("casename:" + caseName)
        case_list=CVE_Case.objects.filter(name=caseName)
    elif req.method == 'POST':
        ans=VideoMerge(materialName,0,EditedVideo)
        return render(req,"download_material.html",locals())


    if len(case_list) ==0: #说明不在库里面 需要重新分析并且上传到库文件
        pass
    elif len(case_list)>0: #直接从库里面取出来就可以了
        caseId=case_list[0].case_id
        shots=CVE_Shot.objects.filter(case_id=caseId)
        startShot=shots[0]
        endShot=shots[len(shots)-1]
        # print(type(startShot))
        # print(len(shots))
        for shot in shots:
            shot_list.append(ShotElement(shot.shot_id,shot.start,shot.end,shot.during,shot.speed,shot.position,shot.craMotion,shot.color,shot.shotSize))
        editedVideo=EditedVideo(case_list[0].case_id,case_list[0].name,case_list[0].jumpArg,case_list[0].speedArg,case_list[0].positionArg,case_list[0].cramArg,case_list[0].colorArg,shot_list)
        

    return render(req, "display_case_parameter.html", globals())
