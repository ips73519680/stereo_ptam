import cv2 
# from SuperPoint.superpoint.superpoint_for_sptam import Superpoint  
from SuperGluePretrainedNetwork.models.superglue import SuperGlue
from match_module import Detecting
import torch

class Params(object):
    def __init__(self):
        
        self.pnp_min_measurements = 10
        self.pnp_max_iterations = 10
        self.init_min_points = 10

        self.local_window_size = 10
        self.ba_max_iterations = 10

        self.min_tracked_points_ratio = 0.5

        self.lc_min_inbetween_frames = 10   # frames
        self.lc_max_inbetween_distance = 3  # meters
        self.lc_embedding_distance = 22.0
        self.lc_inliers_threshold = 15
        self.lc_inliers_ratio = 0.5
        self.lc_distance_threshold = 2      # meters
        self.lc_max_iterations = 20

        self.ground = False

        self.view_camera_size = 1



class ParamsEuroc(Params):
    
    def __init__(self, config='GFTT-BRIEF'):
        super().__init__()

        if config == 'GFTT-BRIEF':
            self.feature_detector = cv2.GFTTDetector_create(
                maxCorners=1000, minDistance=15.0, 
                qualityLevel=0.001, useHarrisDetector=False)

            self.descriptor_extractor = cv2.BriefDescriptorExtractor_create(
                bytes=32, use_orientation=False)

        elif config == 'ORB-BRIEF':
            self.feature_detector = cv2.ORB_create(
                nfeatures=200, scaleFactor=1.2, nlevels=1, edgeThreshold=31)

            self.descriptor_extractor = cv2.BriefDescriptorExtractor_create(
                bytes=32, use_orientation=False)
            
        else:
            raise NotImplementedError

        self.descriptor_matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)

        self.matching_cell_size = 15   # pixels
        self.matching_neighborhood = 2
        self.matching_distance = 25

        self.frustum_near = 0.1  # meters
        self.frustum_far = 50.0

        self.lc_max_inbetween_distance = 4   # meters
        self.lc_distance_threshold = 1.5
        self.lc_embedding_distance = 22.0

        self.view_image_width = 400
        self.view_image_height = 250
        self.view_camera_width = 0.1
        self.view_viewpoint_x = 0
        self.view_viewpoint_y = -1
        self.view_viewpoint_z = -10
        self.view_viewpoint_f = 2000

    
class ParamsKITTI(Params):
    def __init__(self, config='GFTT-BRIEF'):
        super().__init__()

        if config == 'GFTT-BRIEF':
            self.feature_detector = cv2.GFTTDetector_create(
                maxCorners=1000, minDistance=12.0, 
                qualityLevel=0.001, useHarrisDetector=False)
            self.descriptor_extractor = cv2.xfeatures2d.BriefDescriptorExtractor_create()

        elif config == 'GFTT-BRISK':
            self.feature_detector = cv2.GFTTDetector_create(
                maxCorners=2000, minDistance=15.0, 
                qualityLevel=0.01, useHarrisDetector=False)

            self.descriptor_extractor = cv2.BRISK_create()

        elif config == 'ORB-ORB':
            self.feature_detector = cv2.ORB_create(
                nfeatures=1000, scaleFactor=1.2, nlevels=1, edgeThreshold=31)
            self.descriptor_extractor = self.feature_detector

        elif config == 'Superpoint-BRIEF':
            self.feature_detector = Superpoint(
                weights_name = 'sp_v6',keep_k_best=1000
            )
            self.descriptor_extractor = cv2.xfeatures2d.BriefDescriptorExtractor(
                bytes=32, use_orientation=False)

        elif config == 'Superpoint-Superpoint':
            # self.feature_detector = Superpoint(
            #     weights_name = 'sp_v6',keep_k_best=1000
            # )
            # self.descriptor_extractor = self.feature_detector  
            
            device = 'cuda' if torch.cuda.is_available()  else 'cpu'
            print('Running inference on device \"{}\"'.format(device))
            self.feature_detector = Detecting(device=device)
            self.descriptor_extractor = self.feature_detector             

        else:
            raise NotImplementedError


        if(config == 'Superpoint-Superpoint'):         
            # device = 'cuda' if torch.cuda.is_available()  else 'cpu'
            # print('Running inference on device \"{}\"'.format(device))
            # self.descriptor_matcher = Matching(device=device)
             
            self.descriptor_matcher = cv2.BFMatcher(cv2.NORM_L2, crossCheck=False)

        else:
            self.descriptor_matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)



        self.matching_cell_size = 15   # pixels
        self.matching_neighborhood = 3
        self.matching_distance = 30

        self.frustum_near = 0.1    # meters
        self.frustum_far = 1000.0

        self.ground = True

        self.lc_max_inbetween_distance = 50
        self.lc_distance_threshold = 15
        self.lc_embedding_distance = 20.0

        self.view_image_width = 400
        self.view_image_height = 130
        self.view_camera_width = 0.75
        self.view_viewpoint_x = 0
        self.view_viewpoint_y = -500   # -10
        self.view_viewpoint_z = -100   # -0.1
        self.view_viewpoint_f = 2000