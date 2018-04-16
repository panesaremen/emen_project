import os
import boto
import boto.s3.connection
from boto.s3.key import Key


def uploads3(request):
    conn = boto.s3.connect_to_region('ap-south-1',
    aws_access_key_id = 'AKIAI24J3HCOTFCO27FA',
    aws_secret_access_key = 'AKIAI24J3HCOTFCO27FA',
    host = 's3-website-ap-south-1.amazonaws.com',
    is_secure=True,               # uncomment if you are not using ssl
    calling_format = boto.s3.connection.OrdinaryCallingFormat(),
    )

    bucket = conn.get_bucket('emenpanesar')
    if request.method == 'POST':
         = UploadForm(request.POST, request.FILES)
        if uploads3Form.is_valid():
            uploads3Form.save()
            upload_to_youtube(os.path.join(settings.MEDIA_ROOT, 'mydocs/') + request.FILES['file'].name)
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('youtube_search'))


