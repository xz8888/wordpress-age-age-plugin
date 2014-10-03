from boto.s3.bucket import Bucket
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from lib.zencoder.zencoder import Zencoder
import os
import settings

class Encode(object):
	def __init__(self):
		pass

	def upload_aws_s3(self, local_video, upload_path):
		conn = S3Connection(settings.AWS_ACCESS_KEY, settings.AWS_SECRET_KEY)
		bucket = Bucket(conn, settings.AWS_BUCKET)

		self.aws_file_key = ('/' + settings.AWS_STATE + '/' + upload_path)

		#print self.aws_file_key

		self.local_file = str(settings.MEDIA_ROOT + local_video)

		key = Key(bucket)
		key.key = self.aws_file_key + '.mp4'
		key.set_metadata('Expires', '3600')
		key.set_metadata("Content-Type", 'video/mp4')
		
		key.set_contents_from_filename(self.local_file, cb=self.percent_cb, num_cb=10)
		key.set_acl('public-read')

	def percent_cb(self, complete, total):
		complete = float(complete)
		total = float(total)
		perc = float(complete/total)
		#print perc
		
		if perc == 1.0:
			self.upload_aws_s3_complete()

	def upload_aws_s3_complete(self):
		self.create_zencoder_job()

		try:
			os.remove(self.local_file)
		except:
			pass

	def create_zencoder_job(self):
		zen = Zencoder(settings.ZENCODER_API_KEY)

		web_m = {	
			"headers": {
		        "Expires": "3600"
		      },	
				
			'label': 'web_m',
			'url': 's3://' + settings.AWS_BUCKET + self.aws_file_key + '.webm',
			'quality': 3,
			'speed': 3,
			'video_codec': 'vp8',
			'public': 1
		}

		ogg_theora = {
			"headers": {
		        "Expires": "3600"
		      },			
					
			'label': 'ogg_theora',
			'url': 's3://' + settings.AWS_BUCKET + self.aws_file_key + '.theora.ogv',
			'quality': 3,
			'speed': 3,
			'video_codec': 'theora',
			'public': 1
		}

		three_gp = {
			"headers": {
		        "Expires": "3600"
		      },		
				
			'label': '3gp',
			'url': 's3://' + settings.AWS_BUCKET + self.aws_file_key + '.3gp',
			'video_codec': 'mpeg4',
			'width': 320,
			'height': 240,
			'aspect_mode': 'pad',
			'frame_rate': 15,
			'upscale': 'true',
			'video_bitrate': 192,
			'bitrate_cap': 192,
			'audio_bitrate': 24,
			'audio_channels': 1,
			'audio_sample_rate': 16000,
			'public': 1
		}

		outputs = (web_m, ogg_theora, three_gp)

		job_file = (
			settings.AWS_URL + settings.AWS_BUCKET +
			self.aws_file_key  + '.mp4'
		)

		zen.job.create(job_file, outputs=outputs)