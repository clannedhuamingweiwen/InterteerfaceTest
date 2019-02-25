#coding:utf-8



#老师端忘记密码
ele1_list={
    "username":"id>edu.yjyx.teacher:id/userEdit",

    "t_forget":"edu.yjyx.teacher:id/forgetPsw_tv",

    "phone":"edu.yjyx.teacher:id/find_password_user_name",

    "submit":"edu.yjyx.teacher:id/find_password_confirm",

    "sms_reback":"edu.yjyx.teacher:id/find_password_confirm",

    "verfcode":"",

    "pwd1":"edu.yjyx.teacher:id/reset_password_new_password",

    "pwd2":"edu.yjyx.teacher:id/reset_password_new_password_confirm"
}



#老师端登录主流程
login_list ={
    "username":["id>edu.yjyx.teacher:id/userEdit","15067118599"],
    "password":["id>edu.yjyx.teacher:id/pwdEdit","888888"],
    "btn":"id>edu.yjyx.teacher:id/submit"
}

ex='xpath>//*[@text="我的"]'


#老师端-身份认证case1
auth_list={
    "mine":'xpath>//*[@text="我的"]',
    "auth":"id>edu.yjyx.teacher:id/view_identification",
    "name":["id>edu.yjyx.teacher:id/input_name","call you tonight"],
    "idCard":["id>edu.yjyx.teacher:id/input_number","231121199309250034"],
    "pos":"id>edu.yjyx.teacher:id/positive_place_img",
    "chooseStyle":"id>edu.yjyx.teacher:id/textView_select_local",
    "upload":"id>com.miui.gallery:id/pick_num_indicator",
    "success":"id>com.miui.gallery:id/ok",

    "back":"id>edu.yjyx.teacher:id/frame_view_back",
    "upload2":"id>com.miui.gallery:id/pick_num_indicator",
    "finish":"id>edu.yjyx.teacher:id/confirm_commit"

}





