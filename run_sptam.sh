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

# python3 without_localmapping_ver2_sptam.py --path '/home/b08505024/stereo_ptam-master/dataset/KITTI/dataset/sequences/05' --no-viz
# echo "sequences/05 done"
# python3 without_localmapping_ver2_sptam.py --path '/home/b08505024/stereo_ptam-master/dataset/KITTI/dataset/sequences/06' --no-viz
# echo "sequences/06 done"
# python3 without_localmapping_ver2_sptam.py --path '/home/b08505024/stereo_ptam-master/dataset/KITTI/dataset/sequences/07' --no-viz
# echo "sequences/07 done"
# python3 without_localmapping_ver2_sptam.py --path '/home/b08505024/stereo_ptam-master/dataset/KITTI/dataset/sequences/08' --no-viz
# echo "sequences/08 done"
# python3 without_localmapping_ver2_sptam.py --path '/home/b08505024/stereo_ptam-master/dataset/KITTI/dataset/sequences/09' --no-viz
# echo "sequences/09 done"
# python3 without_localmapping_ver2_sptam.py --path '/home/b08505024/stereo_ptam-master/dataset/KITTI/dataset/sequences/10' --no-viz
# echo "sequences/10 done"



echo "run sptam for sequence 0-10 done! "



# python3 without_localmapping_ver2_sptam.py --path '/home/b08505024/stereo_ptam-master/dataset/KITTI/dataset/sequences/00' --no-viz