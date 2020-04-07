from predict import predict_image
import time
url='/home/bavya/dataset/images/char-4-epoch-1/test/'
images=['bdip_8393caeb-25f5-4d8b-8ba8-434aa718655d.png','bigm_4a3889ca-59da-4b0c-9136-65b858c1cc08.png','bght_4fee7d67-458c-4c4f-a469-989b1167fe74.png','avdq_8bf6ec31-9169-410f-a0dd-a9760fb9106a.png','agvx_ca7f3aa5-9c13-4a90-bc58-881d300a9415.png','btqy_664630aa-368a-4912-a691-6a98d38c9784.png','aymt_c9daf9d3-38ee-4e6f-ae73-292f2a7d54dc.png','aryd_e29b0b46-c3c2-476d-b281-6a16b4960641.png']


for img in images:
    print("actual output:   ",predict_image(url+img))
    print("expected output:  ",img[0:4])
    
   