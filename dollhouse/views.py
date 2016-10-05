import os

from django.http import HttpResponse
from django.shortcuts import render_to_response

import utils.classify_image as cfi

# index page
def home(request):
	return render_to_response('index.html')

# image_sniffer page
def image_sniffer(request):
	return render_to_response('image_sniffer.html')

# At first upload , then handle file and return result
def upload_and_handle(request):
	if request.method == 'POST':
		filename = str(request.FILES['file'])
		# 1. ipload
		handle_uploaded_file(request.FILES['file'], filename)
		# 2. handle
		cfi.maybe_download_and_extract()
		image = (cfi.FLAGS.image_file if cfi.FLAGS.image_file else 
				os.path.join(cfi.FLAGS.model_dir, filename))
		ret_list = cfi.run_inference_on_image(image)
		# 3. return
		return render_to_response('classify_image.html', {'ret_list': ret_list, 'length': len(ret_list), 'filename': filename})
	return render_to_response('http404.html')

# upload handler
def handle_uploaded_file(file, filename):
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media/images/'+filename), 'wb+') as destination:
		for chunk in file.chunks():
			destination.write(chunk)