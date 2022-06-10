#!/bin/bash

cd ./eval
python3 eval_odom.py --result ../result/
cd ..

echo "run eval done!"