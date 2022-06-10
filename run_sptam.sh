#!/bin/bash

python3 sptam.py --path '/home/b08505024/stereo_ptam-master/dataset/KITTI/dataset/sequences/00' --no-viz
echo "sequences/00 done"
python3 sptam.py --path '/home/b08505024/stereo_ptam-master/dataset/KITTI/dataset/sequences/01' --no-viz
echo "sequences/01 done"
python3 sptam.py --path '/home/b08505024/stereo_ptam-master/dataset/KITTI/dataset/sequences/02' --no-viz
echo "sequences/02 done"
python3 sptam.py --path '/home/b08505024/stereo_ptam-master/dataset/KITTI/dataset/sequences/03' --no-viz
echo "sequences/03 done"
python3 sptam.py --path '/home/b08505024/stereo_ptam-master/dataset/KITTI/dataset/sequences/04' --no-viz
echo "sequences/04 done"
echo "run sptam for sequence 0-4 done! "