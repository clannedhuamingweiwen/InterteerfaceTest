from utility.enhance import Tokenhander
from Settings import cofig
from utility.enhance import Tokenhander,Sender
from Settings import urls


#parent
class p(Tokenhander.tokenMamagement):
    def __init__(self):
        self.p_token =Tokenhander.tokenMamagement.get_token(cofig.Parent,cofig.parent_dict)


    def test(self):
        pp=Tokenhander.tokenMamagement.get_token(cofig.Parent, cofig.parent_dict)  #get token
        print pp
        print "%%%%%%%%%%%"
     #   print "pp is ",type(pp)
        result =Tokenhander.tokenMamagement.Ins2(urls.PARENT_URLS["loc_url"],urls.loc_params).sendPost(urls.PARENT_URLS["loc_url"],urls.loc_params,**pp)

      #  print "result is",result
        return result



x =p()
print x.test()
