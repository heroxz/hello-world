#!/usr/bin/python -u

import json
from urllib import request

DIRECT_API = ('http://gql-cpbu.svc.eng.vmware.com/datadirect?'
'query=%7B%0A%20%20getLatestSmokeCfRecommendation(input%3A%20%'
'7BBRANCH%3A%20%22main%22%2C%20PIPELINE_NAME%3A%20%22smoke%22%7'
'D)%20%7B%0A%20%20%20%20ESX_CLN%0A%20%20%20%20ESX_BUILD_ID%0A%20%'
'20%20%20VC_CLN%0A%20%20%20%20VC_BUILD_ID%0A%20%20%7D%0A%7D%0A')

def getBuildInfo():
   res = request.urlopen(DIRECT_API)
   api_output = res.read().decode('utf-8')
   raw_data = json.loads(api_output)
   recommended_build = raw_data['data']['getLatestSmokeCfRecommendation']
   VC_BUILD_ID = recommended_build['VC_BUILD_ID']
   VC_CLN = recommended_build['VC_CLN']
   ESX_BUILD_ID = recommended_build['ESX_BUILD_ID']
   ESX_CLN = recommended_build['ESX_CLN']
   return VC_BUILD_ID, VC_CLN, ESX_BUILD_ID, ESX_CLN

if __name__ == '__main__':

   vc_build_id, vc_cln, esx_build_id, esx_cln = getBuildInfo()
   #print('VC_BUILD_ID=%s' % vc_build_id)
   #print('VC_CLN=%s' % vc_cln)
   print('%s' % esx_build_id)
   #print('ESX_CLN=%s' % esx_cln)







