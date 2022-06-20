import cv2
from SuperPoint.superpoint.superpoint_for_sptam import Superpoint  
import numpy as np

from SuperGluePretrainedNetwork.models.superglue import SuperGlue
from SuperGluePretrainedNetwork.models.superpoint import SuperPoint
from dataset import KITTIOdometry, EuRoCDataset

import torch

config = {
    'superpoint': {
        'descriptor_dim': 256,
        'nms_radius': 4,
        'keypoint_threshold': 0.005,
        'max_keypoints': -1,
        'remove_borders': 4,
    },
    'superglue': {
        'descriptor_dim': 256,
        'weights': 'indoor',
        'keypoint_encoder': [32, 64, 128, 256],
        'GNN_layers': ['self', 'cross'] * 9,
        'sinkhorn_iterations': 100,
        'match_threshold': 0.2,
    }
}

class Matching(torch.nn.Module):
    def __init__(self, config={},device='cuba'):
        super().__init__()
        self.superglue = SuperGlue(config.get('superglue', {})).to(device)

    def forward(self, descriptors0,descriptors1,keypoints0,keypoints1):

        descriptors0=np.expand_dims(np.transpose(descriptors0), axis = 0)
        descriptors1=np.expand_dims(np.transpose(descriptors1), axis = 0)
        keypoints0=np.expand_dims([keypoints0[idx].pt for idx in range(len(keypoints0)) ], axis = 0)
        keypoints1=np.expand_dims([keypoints1[idx].pt for idx in range(len(keypoints1)) ], axis = 0)
        data={'descriptors0':descriptors0,'descriptors1':descriptors1,'keypoints0':keypoints0,'keypoints1':keypoints1}

        pred = {**self.superglue(data)}
        
        pred = {k: v[0].cpu().numpy() for k, v in pred.items()}
        matches, conf = pred['matches0'], pred['matching_scores0']
        valid = matches > -1
        
        good_matches = [cv2.DMatch((100-conf), matches[valid],valid,None)  for idx in range(len(valid))]


        # mkpts0 = keypoints0[valid]
        # mkpts1 = keypoints1[matches[valid]]

        return good_matches

class Detecting(torch.nn.Module):
    def __init__(self,device='cuba', config={}):
        super().__init__()
        self.device=device
        self.superpoint = SuperPoint(config.get('superpoint', {})).to(device)

    def forward(self, image):
        frame_tensor = self.frame2tensor(image,self.device)
        pred0 = self.superpoint({'image':frame_tensor})
        
        keypoints=[p.detach().cpu().numpy() for p in pred0['keypoints']]
        descriptors=[p.detach().cpu().numpy() for p in pred0['descriptors']]
        keypoints = [cv2.KeyPoint(p[0], p[1], 1) for p in np.array(keypoints)[0]]
        descriptors=np.transpose(descriptors[0])
        
        
        return keypoints,descriptors

    
    def frame2tensor(self,frame,device):
        return torch.from_numpy(frame/255.).float()[None, None].to(device)




