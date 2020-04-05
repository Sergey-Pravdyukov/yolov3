from models import attempt_download

if __name__=='__main__':
	attempt_download('weights/yolov3.pt')
	attempt_download('weights/yolov3-spp.pt')

