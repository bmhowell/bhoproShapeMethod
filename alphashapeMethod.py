import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import time
import alphashape
from descartes import PolygonPatch

# https://stackoverflow.com/questions/23073170/calculate-bounding-polygon-of-alpha-shape-from-the-delaunay-triangulation


xplot = np.array([[-1.37333962e-03,  3.48250919e-05],
       [-2.20216449e-04,  3.45046320e-05],
       [-4.14149153e-06,  3.46502934e-05],
       [ 1.41709755e-04,  3.43686546e-05],
       [ 4.38119866e-04,  3.44618511e-05],
       [ 5.85102159e-04,  3.47951456e-05],
       [ 9.14618838e-04,  9.94948073e-05],
       [ 9.47185169e-04,  3.52290358e-05],
       [ 1.81885980e-03,  3.55145727e-05],
       [ 1.96897926e-03,  3.54098922e-05],
       [-6.51914363e-04,  3.43600272e-05],
       [-7.63986180e-05,  3.48065191e-05],
       [-7.23410335e-04,  3.42898090e-05],
       [ 2.89804718e-04,  3.41660757e-05],
       [ 5.11645818e-04,  3.47028971e-05],
       [ 1.05458341e-03,  9.76598156e-05],
       [ 8.03069113e-04,  3.52456483e-05],
       [ 1.01834332e-03,  3.54293553e-05],
       [ 1.89365813e-03,  3.54674262e-05],
       [ 2.19345033e-03,  3.52090532e-05],
       [-1.51586467e-03,  3.59095257e-05],
       [-2.08792383e-03,  9.73576849e-05],
       [-7.95426262e-04,  3.42324728e-05],
       [ 2.15711143e-04,  3.41766948e-05],
       [ 3.64244539e-04,  3.42727090e-05],
       [ 6.22265962e-04,  9.70566866e-05],
       [ 1.45259155e-03,  3.50371523e-05],
       [ 1.30875532e-03,  3.51422450e-05],
       [ 2.04451704e-03,  3.55833014e-05],
       [ 2.26795816e-03,  3.51253881e-05],
       [-1.95608652e-03,  3.48507798e-05],
       [-3.64365196e-04,  3.45817661e-05],
       [-1.22815949e-03,  3.47387560e-05],
       [ 1.79272359e-04,  9.48044288e-05],
       [ 4.01524035e-04,  9.51682188e-05],
       [ 1.56148802e-03,  9.68236913e-05],
       [ 1.23578124e-03,  3.50651870e-05],
       [ 3.43385815e-03,  9.55646167e-05],
       [ 2.11963446e-03,  3.57586248e-05],
       [ 2.34266229e-03,  3.48518805e-05],
       [-2.12335202e-03,  3.51375443e-05],
       [-1.80734205e-03,  3.56324501e-05],
       [-1.01181140e-03,  3.47989693e-05],
       [ 6.84004695e-05,  3.45247892e-05],
       [ 2.53291470e-04,  9.45449195e-05],
       [ 4.75023920e-04,  9.62028196e-05],
       [ 1.52509438e-03,  3.49033074e-05],
       [ 2.81687936e-03,  9.75193800e-05],
       [ 3.07435798e-03,  3.47299828e-05],
       [ 2.44400689e-03,  3.55128432e-05],
       [-4.64769568e-03,  1.85292319e-04],
       [-1.73315126e-03,  3.56260969e-05],
       [-1.84649746e-03,  1.00077819e-04],
       [-3.27920983e-04,  9.63163839e-05],
       [ 2.90563609e-04,  1.55644393e-04],
       [ 1.16286990e-03,  3.51090114e-05],
       [ 2.72027041e-03,  7.43677126e-05],
       [ 2.92740527e-03,  3.52128504e-05],
       [ 2.77985169e-03,  3.48367428e-05],
       [ 3.84506520e-03,  3.60449548e-05],
       [-2.26860205e-03,  3.59778345e-05],
       [-1.65973855e-03,  3.56831046e-05],
       [-5.45370304e-04,  9.68983543e-05],
       [ 3.27560524e-04,  9.44780107e-05],
       [ 1.93173336e-03,  9.86402565e-05],
       [ 3.00108165e-03,  3.52476750e-05],
       [ 3.62481030e-03,  3.56489287e-05],
       [ 3.77175997e-03,  3.60236532e-05],
       [ 2.66189705e-03,  3.46865734e-05],
       [-3.30672562e-03,  4.03554810e-05],
       [-2.85735578e-03,  3.50547386e-05],
       [-4.36595532e-04,  3.46069446e-05],
       [ 3.23625718e-05,  9.62586219e-05],
       [ 1.09067095e-03,  3.51105734e-05],
       [ 2.51687830e-03,  3.60126653e-05],
       [ 4.03316635e-03,  9.39481706e-05],
       [ 4.58626640e-03,  9.94541047e-05],
       [ 3.54956543e-03,  3.56167747e-05],
       [ 5.24467073e-03,  3.52566498e-05],
       [-5.77064553e-03,  5.21480426e-05],
       [-3.22997543e-03,  3.59031846e-05],
       [-1.44481786e-03,  3.50020266e-05],
       [-2.92215469e-04,  3.44904781e-05],
       [ 2.53023557e-04,  2.18219775e-04],
       [ 1.74517342e-03,  3.55364917e-05],
       [ 3.39277208e-03,  3.56532800e-05],
       [ 3.47556632e-03,  3.56476305e-05],
       [ 5.95442781e-03,  8.89175036e-05],
       [ 4.62260143e-03,  3.58780223e-05],
       [-3.69469975e-03,  8.81989913e-05],
       [-2.78374049e-03,  3.43110067e-05],
       [-9.04092080e-04,  9.67848602e-05],
       [-1.84443095e-04,  9.72016093e-05],
       [ 1.67268925e-03,  3.47195920e-05],
       [ 3.12100267e-03,  8.87511370e-05],
       [ 4.84419635e-03,  4.95461552e-05],
       [ 6.12962954e-03,  3.83234330e-05],
       [ 3.17029903e-03,  3.52200453e-05],
       [ 4.07631097e-03,  3.51710421e-05],
       [-2.63699139e-03,  3.51923067e-05],
       [-3.15445122e-03,  3.58478238e-05],
       [-2.56254018e-03,  3.50430647e-05],
       [-6.16526734e-04,  9.62475669e-05],
       [ 7.30680845e-04,  3.52192300e-05],
       [ 2.58928647e-03,  3.55757245e-05],
       [ 3.99254850e-03,  3.48784714e-05],
       [ 5.08882194e-03,  3.64866923e-05],
       [ 4.32477046e-03,  3.62092549e-05],
       [ 4.15729412e-03,  3.47814444e-05],
       [-3.42667926e-03,  7.22197440e-05],
       [-3.00516915e-03,  3.50513772e-05],
       [-1.58728274e-03,  3.56703547e-05],
       [ 2.16639759e-04,  1.56303608e-04],
       [ 3.65094836e-04,  1.56452501e-04],
       [ 2.00672710e-03,  9.94704124e-05],
       [ 4.20285402e-03,  9.15012754e-05],
       [ 6.41071965e-03,  5.22875334e-05],
       [ 5.63559164e-03,  5.41055257e-05],
       [ 6.04541118e-03,  8.26873880e-05],
       [-4.12821609e-03,  1.94575082e-04],
       [-3.07953777e-03,  3.56439225e-05],
       [-2.48798758e-03,  3.51158126e-05],
       [-5.80263517e-04,  3.45919174e-05],
       [ 1.05435302e-04,  9.56585382e-05],
       [ 2.89079741e-03,  9.83717905e-05],
       [ 3.24625919e-03,  3.51631796e-05],
       [ 4.24921592e-03,  3.53427834e-05],
       [ 6.94856915e-03,  1.14067082e-04],
       [ 7.65338760e-03,  1.25599518e-04],
       [-2.71042104e-03,  3.61741013e-05],
       [-8.67598476e-04,  3.46946256e-05],
       [-1.48461482e-04,  3.48509607e-05],
       [ 2.30634779e-03,  9.72878371e-05],
       [ 3.58716383e-03,  9.79930255e-05],
       [ 2.08183061e-03,  9.99923040e-05],
       [ 5.00939169e-03,  4.49815872e-05],
       [ 5.16537409e-03,  3.78235106e-05],
       [ 6.66883386e-03,  7.25346640e-05],
       [-3.78116208e-03,  5.10461382e-05],
       [-2.41388181e-03,  3.51839482e-05],
       [-1.41291579e-03,  9.91051300e-05],
       [-7.59647986e-04,  9.57631781e-05],
       [ 6.91907474e-05,  1.58420169e-04],
       [ 3.28525156e-04,  2.18365130e-04],
       [ 3.31936167e-03,  3.60448384e-05],
       [ 4.11874825e-03,  9.49831342e-05],
       [ 4.54880686e-03,  3.57002977e-05],
       [-2.93119482e-03,  3.67067786e-05],
       [-2.19589849e-03,  3.60352724e-05],
       [-9.39361099e-04,  3.46455188e-05],
       [-5.84946091e-04,  1.60205981e-04],
       [ 1.43266575e-04,  1.57476434e-04],
       [ 1.27317124e-03,  9.74937386e-05],
       [ 2.39288389e-03,  8.70286817e-05],
       [ 1.38051311e-03,  3.60707693e-05],
       [ 4.36405978e-03,  1.02339613e-04],
       [-6.87202766e-04,  9.65090993e-05],
       [-6.91052234e-03,  6.82747014e-05],
       [-2.60044400e-03,  9.75210463e-05],
       [-1.30109040e-03,  3.47461537e-05],
       [-5.08670671e-04,  3.46637949e-05],
       [-4.01506267e-05,  9.70685616e-05],
       [-1.12665707e-04,  9.74197195e-05],
       [ 3.95587726e-03,  9.82385062e-05],
       [ 3.69845472e-03,  3.56246519e-05],
       [-4.73233409e-04,  9.67884853e-05],
       [-2.44993400e-03,  9.79214740e-05],
       [-2.76081900e-03,  9.98495188e-05],
       [-2.52502340e-03,  9.74865283e-05],
       [-1.11871038e-03,  9.69698739e-05],
       [-4.00722799e-04,  9.63956280e-05],
       [-2.88563179e-04,  1.59373044e-04],
       [ 5.86962946e-04,  1.60535068e-04],
       [ 3.21015217e-03,  9.70890963e-05],
       [ 3.91827263e-03,  3.55410756e-05],
       [ 4.76977164e-03,  3.58049359e-05],
       [-2.03972743e-03,  1.52492226e-04],
       [-1.88175140e-03,  3.53812240e-05],
       [-1.15527235e-03,  3.47001968e-05],
       [-5.10863842e-04,  1.60397326e-04],
       [-3.26342676e-04,  2.21884552e-04],
       [ 3.03979657e-03,  9.84586975e-05],
       [ 1.59910993e-03,  3.48705293e-05],
       [ 4.28526651e-03,  1.01801854e-04],
       [-2.55670377e-04,  9.61552898e-05],
       [-1.92157917e-03,  9.92339906e-05],
       [-1.62155708e-03,  1.01016620e-04],
       [-9.76296429e-04,  9.67408487e-05],
       [-8.31655759e-04,  9.57707270e-05],
       [ 1.06596175e-04,  2.21454772e-04],
       [-1.51142095e-04,  1.61619656e-04],
       [ 2.62648666e-03,  9.86866448e-05],
       [ 4.69465959e-03,  4.17353112e-05],
       [ 4.07539292e-03,  1.53716567e-04],
       [-2.34123054e-03,  3.59833959e-05],
       [-1.26550781e-03,  9.65677135e-05],
       [-3.63666430e-04,  1.58812863e-04],
       [ 5.12169421e-04,  1.59839615e-04],
       [-4.37125896e-04,  1.60049585e-04],
       [ 4.38052959e-04,  1.59119625e-04],
       [-2.00086387e-03,  9.07066360e-05],
       [-1.04738198e-03,  9.92802642e-05],
       [-1.69743869e-03,  1.00611612e-04],
       [-7.24223975e-04,  1.58215602e-04],
       [ 1.29590065e-01,  3.91654687e-04],
       [ 7.67640926e-04,  9.88797773e-05],
       [ 4.92710860e-03,  3.33153908e-05],
       [ 1.19923803e-03,  9.74079892e-05],
       [-1.15528541e-03,  1.59446120e-04],
       [-1.33903479e-03,  9.69711170e-05],
       [-9.41924748e-04,  1.60349884e-04],
       [ 3.15996000e-03,  1.50348883e-04],
       [ 5.34005307e-03,  7.03202111e-05],
       [-1.08341694e-03,  3.51112530e-05],
       [-2.04814690e-03,  3.52503172e-05],
       [-8.66483612e-04,  1.59630046e-04],
       [ 1.59938075e-03,  1.59265605e-04],
       [ 4.40085089e-03,  3.55424700e-05],
       [ 5.72580546e-03,  1.03825380e-04],
       [-1.77231363e-03,  1.00497731e-04],
       [-1.19193034e-03,  9.65499461e-05],
       [ 6.94835055e-04,  9.87515059e-05],
       [ 1.63793202e-03,  9.67924291e-05],
       [ 5.43612990e-03,  4.47434802e-05],
       [ 6.58281355e-04,  3.49413158e-05],
       [ 2.75554246e-03,  1.37566399e-04],
       [ 5.48648595e-04,  9.67289209e-05],
       [ 1.34641336e-03,  1.02011765e-04],
       [ 2.23040879e-03,  9.74004133e-05],
       [ 1.48723673e-03,  9.81432161e-05],
       [-3.59596151e-03,  1.59570556e-04],
       [ 1.78001918e-03,  9.91055048e-05],
       [-3.77011676e-06,  1.60590065e-04],
       [ 2.96498216e-03,  9.84804835e-05],
       [ 4.47558259e-03,  3.57692698e-05],
       [ 8.40762018e-04,  9.90681605e-05],
       [-1.30219329e-03,  1.59157478e-04],
       [ 4.43656609e-03,  1.05013028e-04],
       [ 8.75327952e-04,  3.52915604e-05],
       [ 1.85680088e-03,  9.85377955e-05],
       [-7.72803067e-05,  1.61181836e-04],
       [ 1.00403291e-03,  1.48559003e-04],
       [ 2.85371811e-03,  3.50755929e-05],
       [ 1.23580820e-03,  1.60425577e-04],
       [ 1.12679097e-03,  9.88803889e-05]])

points2d = [(-1.37333962e-03,  3.48250919e-05),
       (-2.20216449e-04,  3.45046320e-05),
       (-4.14149153e-06,  3.46502934e-05),
       ( 1.41709755e-04,  3.43686546e-05),
       ( 4.38119866e-04,  3.44618511e-05),
       ( 5.85102159e-04,  3.47951456e-05),
       ( 9.14618838e-04,  9.94948073e-05),
       ( 9.47185169e-04,  3.52290358e-05),
       ( 1.81885980e-03,  3.55145727e-05),
       ( 1.96897926e-03,  3.54098922e-05),
       (-6.51914363e-04,  3.43600272e-05),
       (-7.63986180e-05,  3.48065191e-05),
       (-7.23410335e-04,  3.42898090e-05),
       ( 2.89804718e-04,  3.41660757e-05),
       ( 5.11645818e-04,  3.47028971e-05),
       ( 1.05458341e-03,  9.76598156e-05),
       ( 8.03069113e-04,  3.52456483e-05),
       ( 1.01834332e-03,  3.54293553e-05),
       ( 1.89365813e-03,  3.54674262e-05),
       ( 2.19345033e-03,  3.52090532e-05),
       (-1.51586467e-03,  3.59095257e-05),
       (-2.08792383e-03,  9.73576849e-05),
       (-7.95426262e-04,  3.42324728e-05),
       ( 2.15711143e-04,  3.41766948e-05),
       ( 3.64244539e-04,  3.42727090e-05),
       ( 6.22265962e-04,  9.70566866e-05),
       ( 1.45259155e-03,  3.50371523e-05),
       ( 1.30875532e-03,  3.51422450e-05),
       ( 2.04451704e-03,  3.55833014e-05),
       ( 2.26795816e-03,  3.51253881e-05),
       (-1.95608652e-03,  3.48507798e-05),
       (-3.64365196e-04,  3.45817661e-05),
       (-1.22815949e-03,  3.47387560e-05),
       ( 1.79272359e-04,  9.48044288e-05),
       ( 4.01524035e-04,  9.51682188e-05),
       ( 1.56148802e-03,  9.68236913e-05),
       ( 1.23578124e-03,  3.50651870e-05),
       ( 3.43385815e-03,  9.55646167e-05),
       ( 2.11963446e-03,  3.57586248e-05),
       ( 2.34266229e-03,  3.48518805e-05),
       (-2.12335202e-03,  3.51375443e-05),
       (-1.80734205e-03,  3.56324501e-05),
       (-1.01181140e-03,  3.47989693e-05),
       ( 6.84004695e-05,  3.45247892e-05),
       ( 2.53291470e-04,  9.45449195e-05),
       ( 4.75023920e-04,  9.62028196e-05),
       ( 1.52509438e-03,  3.49033074e-05),
       ( 2.81687936e-03,  9.75193800e-05),
       ( 3.07435798e-03,  3.47299828e-05),
       ( 2.44400689e-03,  3.55128432e-05),
       (-4.64769568e-03,  1.85292319e-04),
       (-1.73315126e-03,  3.56260969e-05),
       (-1.84649746e-03,  1.00077819e-04),
       (-3.27920983e-04,  9.63163839e-05),
       ( 2.90563609e-04,  1.55644393e-04),
       ( 1.16286990e-03,  3.51090114e-05),
       ( 2.72027041e-03,  7.43677126e-05),
       ( 2.92740527e-03,  3.52128504e-05),
       ( 2.77985169e-03,  3.48367428e-05),
       ( 3.84506520e-03,  3.60449548e-05),
       (-2.26860205e-03,  3.59778345e-05),
       (-1.65973855e-03,  3.56831046e-05),
       (-5.45370304e-04,  9.68983543e-05),
       ( 3.27560524e-04,  9.44780107e-05),
       ( 1.93173336e-03,  9.86402565e-05),
       ( 3.00108165e-03,  3.52476750e-05),
       ( 3.62481030e-03,  3.56489287e-05),
       ( 3.77175997e-03,  3.60236532e-05),
       ( 2.66189705e-03,  3.46865734e-05),
       (-3.30672562e-03,  4.03554810e-05),
       (-2.85735578e-03,  3.50547386e-05),
       (-4.36595532e-04,  3.46069446e-05),
       ( 3.23625718e-05,  9.62586219e-05),
       ( 1.09067095e-03,  3.51105734e-05),
       ( 2.51687830e-03,  3.60126653e-05),
       ( 4.03316635e-03,  9.39481706e-05),
       ( 4.58626640e-03,  9.94541047e-05),
       ( 3.54956543e-03,  3.56167747e-05),
       ( 5.24467073e-03,  3.52566498e-05),
       (-5.77064553e-03,  5.21480426e-05),
       (-3.22997543e-03,  3.59031846e-05),
       (-1.44481786e-03,  3.50020266e-05),
       (-2.92215469e-04,  3.44904781e-05),
       ( 2.53023557e-04,  2.18219775e-04),
       ( 1.74517342e-03,  3.55364917e-05),
       ( 3.39277208e-03,  3.56532800e-05),
       ( 3.47556632e-03,  3.56476305e-05),
       ( 5.95442781e-03,  8.89175036e-05),
       ( 4.62260143e-03,  3.58780223e-05),
       (-3.69469975e-03,  8.81989913e-05),
       (-2.78374049e-03,  3.43110067e-05),
       (-9.04092080e-04,  9.67848602e-05),
       (-1.84443095e-04,  9.72016093e-05),
       ( 1.67268925e-03,  3.47195920e-05),
       ( 3.12100267e-03,  8.87511370e-05),
       ( 4.84419635e-03,  4.95461552e-05),
       ( 6.12962954e-03,  3.83234330e-05),
       ( 3.17029903e-03,  3.52200453e-05),
       ( 4.07631097e-03,  3.51710421e-05),
       (-2.63699139e-03,  3.51923067e-05),
       (-3.15445122e-03,  3.58478238e-05),
       (-2.56254018e-03,  3.50430647e-05),
       (-6.16526734e-04,  9.62475669e-05),
       ( 7.30680845e-04,  3.52192300e-05),
       ( 2.58928647e-03,  3.55757245e-05),
       ( 3.99254850e-03,  3.48784714e-05),
       ( 5.08882194e-03,  3.64866923e-05),
       ( 4.32477046e-03,  3.62092549e-05),
       ( 4.15729412e-03,  3.47814444e-05),
       (-3.42667926e-03,  7.22197440e-05),
       (-3.00516915e-03,  3.50513772e-05),
       (-1.58728274e-03,  3.56703547e-05),
       ( 2.16639759e-04,  1.56303608e-04),
       ( 3.65094836e-04,  1.56452501e-04),
       ( 2.00672710e-03,  9.94704124e-05),
       ( 4.20285402e-03,  9.15012754e-05),
       ( 6.41071965e-03,  5.22875334e-05),
       ( 5.63559164e-03,  5.41055257e-05),
       ( 6.04541118e-03,  8.26873880e-05),
       (-4.12821609e-03,  1.94575082e-04),
       (-3.07953777e-03,  3.56439225e-05),
       (-2.48798758e-03,  3.51158126e-05),
       (-5.80263517e-04,  3.45919174e-05),
       ( 1.05435302e-04,  9.56585382e-05),
       ( 2.89079741e-03,  9.83717905e-05),
       ( 3.24625919e-03,  3.51631796e-05),
       ( 4.24921592e-03,  3.53427834e-05),
       ( 6.94856915e-03,  1.14067082e-04),
       ( 7.65338760e-03,  1.25599518e-04),
       (-2.71042104e-03,  3.61741013e-05),
       (-8.67598476e-04,  3.46946256e-05),
       (-1.48461482e-04,  3.48509607e-05),
       ( 2.30634779e-03,  9.72878371e-05),
       ( 3.58716383e-03,  9.79930255e-05),
       ( 2.08183061e-03,  9.99923040e-05),
       ( 5.00939169e-03,  4.49815872e-05),
       ( 5.16537409e-03,  3.78235106e-05),
       ( 6.66883386e-03,  7.25346640e-05),
       (-3.78116208e-03,  5.10461382e-05),
       (-2.41388181e-03,  3.51839482e-05),
       (-1.41291579e-03,  9.91051300e-05),
       (-7.59647986e-04,  9.57631781e-05),
       ( 6.91907474e-05,  1.58420169e-04),
       ( 3.28525156e-04,  2.18365130e-04),
       ( 3.31936167e-03,  3.60448384e-05),
       ( 4.11874825e-03,  9.49831342e-05),
       ( 4.54880686e-03,  3.57002977e-05),
       (-2.93119482e-03,  3.67067786e-05),
       (-2.19589849e-03,  3.60352724e-05),
       (-9.39361099e-04,  3.46455188e-05),
       (-5.84946091e-04,  1.60205981e-04),
       ( 1.43266575e-04,  1.57476434e-04),
       ( 1.27317124e-03,  9.74937386e-05),
       ( 2.39288389e-03,  8.70286817e-05),
       ( 1.38051311e-03,  3.60707693e-05),
       ( 4.36405978e-03,  1.02339613e-04),
       (-6.87202766e-04,  9.65090993e-05),
       (-6.91052234e-03,  6.82747014e-05),
       (-2.60044400e-03,  9.75210463e-05),
       (-1.30109040e-03,  3.47461537e-05),
       (-5.08670671e-04,  3.46637949e-05),
       (-4.01506267e-05,  9.70685616e-05),
       (-1.12665707e-04,  9.74197195e-05),
       ( 3.95587726e-03,  9.82385062e-05),
       ( 3.69845472e-03,  3.56246519e-05),
       (-4.73233409e-04,  9.67884853e-05),
       (-2.44993400e-03,  9.79214740e-05),
       (-2.76081900e-03,  9.98495188e-05),
       (-2.52502340e-03,  9.74865283e-05),
       (-1.11871038e-03,  9.69698739e-05),
       (-4.00722799e-04,  9.63956280e-05),
       (-2.88563179e-04,  1.59373044e-04),
       ( 5.86962946e-04,  1.60535068e-04),
       ( 3.21015217e-03,  9.70890963e-05),
       ( 3.91827263e-03,  3.55410756e-05),
       ( 4.76977164e-03,  3.58049359e-05),
       (-2.03972743e-03,  1.52492226e-04),
       (-1.88175140e-03,  3.53812240e-05),
       (-1.15527235e-03,  3.47001968e-05),
       (-5.10863842e-04,  1.60397326e-04),
       (-3.26342676e-04,  2.21884552e-04),
       ( 3.03979657e-03,  9.84586975e-05),
       ( 1.59910993e-03,  3.48705293e-05),
       ( 4.28526651e-03,  1.01801854e-04),
       (-2.55670377e-04,  9.61552898e-05),
       (-1.92157917e-03,  9.92339906e-05),
       (-1.62155708e-03,  1.01016620e-04),
       (-9.76296429e-04,  9.67408487e-05),
       (-8.31655759e-04,  9.57707270e-05),
       ( 1.06596175e-04,  2.21454772e-04),
       (-1.51142095e-04,  1.61619656e-04),
       ( 2.62648666e-03,  9.86866448e-05),
       ( 4.69465959e-03,  4.17353112e-05),
       ( 4.07539292e-03,  1.53716567e-04),
       (-2.34123054e-03,  3.59833959e-05),
       (-1.26550781e-03,  9.65677135e-05),
       (-3.63666430e-04,  1.58812863e-04),
       ( 5.12169421e-04,  1.59839615e-04),
       (-4.37125896e-04,  1.60049585e-04),
       ( 4.38052959e-04,  1.59119625e-04),
       (-2.00086387e-03,  9.07066360e-05),
       (-1.04738198e-03,  9.92802642e-05),
       (-1.69743869e-03,  1.00611612e-04),
       (-7.24223975e-04,  1.58215602e-04),
       ( 1.29590065e-01,  3.91654687e-04),
       ( 7.67640926e-04,  9.88797773e-05),
       ( 4.92710860e-03,  3.33153908e-05),
       ( 1.19923803e-03,  9.74079892e-05),
       (-1.15528541e-03,  1.59446120e-04),
       (-1.33903479e-03,  9.69711170e-05),
       (-9.41924748e-04,  1.60349884e-04),
       ( 3.15996000e-03,  1.50348883e-04),
       ( 5.34005307e-03,  7.03202111e-05),
       (-1.08341694e-03,  3.51112530e-05),
       (-2.04814690e-03,  3.52503172e-05),
       (-8.66483612e-04,  1.59630046e-04),
       ( 1.59938075e-03,  1.59265605e-04),
       ( 4.40085089e-03,  3.55424700e-05),
       ( 5.72580546e-03,  1.03825380e-04),
       (-1.77231363e-03,  1.00497731e-04),
       (-1.19193034e-03,  9.65499461e-05),
       ( 6.94835055e-04,  9.87515059e-05),
       ( 1.63793202e-03,  9.67924291e-05),
       ( 5.43612990e-03,  4.47434802e-05),
       ( 6.58281355e-04,  3.49413158e-05),
       ( 2.75554246e-03,  1.37566399e-04),
       ( 5.48648595e-04,  9.67289209e-05),
       ( 1.34641336e-03,  1.02011765e-04),
       ( 2.23040879e-03,  9.74004133e-05),
       ( 1.48723673e-03,  9.81432161e-05),
       (-3.59596151e-03,  1.59570556e-04),
       ( 1.78001918e-03,  9.91055048e-05),
       (-3.77011676e-06,  1.60590065e-04),
       ( 2.96498216e-03,  9.84804835e-05),
       ( 4.47558259e-03,  3.57692698e-05),
       ( 8.40762018e-04,  9.90681605e-05),
       (-1.30219329e-03,  1.59157478e-04),
       ( 4.43656609e-03,  1.05013028e-04),
       ( 8.75327952e-04,  3.52915604e-05),
       ( 1.85680088e-03,  9.85377955e-05),
       (-7.72803067e-05,  1.61181836e-04),
       ( 1.00403291e-03,  1.48559003e-04),
       ( 2.85371811e-03,  3.50755929e-05),
       ( 1.23580820e-03,  1.60425577e-04),
       ( 1.12679097e-03,  9.88803889e-05)]

# plot orginal data points
plt.figure(figsize=(10,10))
plt.scatter(xplot[:, 0], xplot[:, 1])
plt.xlim(-0.015/2, 0.015/2)
plt.ylim(0, 0.001)
plt.savefig('final_state.png')


def alpha_shape(points, alpha, only_outer=True):
    """
    Compute the alpha shape (concave hull) of a set of points.
    :param points: np.array of shape (n,2) points.
    :param alpha: alpha value.
    :param only_outer: boolean value to specify if we keep only the outer border
    or also inner edges.
    :return: set of (i,j) pairs representing edges of the alpha-shape. (i,j) are
    the indices in the points array.
    """
    assert points.shape[0] > 3, "Need at least four points"

    def add_edge(edges, i, j):
        """
        Add a line between the i-th and j-th points,
        if not in the list already
        """
        if (i, j) in edges or (j, i) in edges:
            # already added
            assert (j, i) in edges, "Can't go twice over same directed edge right?"
            if only_outer:
                # if both neighboring triangles are in shape, it is not a boundary edge
                edges.remove((j, i))
            return
        edges.add((i, j))

    tri = Delaunay(points)
    edges = set()
    # Loop over triangles:
    # ia, ib, ic = indices of corner points of the triangle
    for ia, ib, ic in tri.simplices:
        pa = points[ia]
        pb = points[ib]
        pc = points[ic]
        # Computing radius of triangle circumcircle
        # www.mathalino.com/reviewer/derivation-of-formulas/derivation-of-formula-for-radius-of-circumcircle
        a = np.sqrt((pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2)
        b = np.sqrt((pb[0] - pc[0]) ** 2 + (pb[1] - pc[1]) ** 2)
        c = np.sqrt((pc[0] - pa[0]) ** 2 + (pc[1] - pa[1]) ** 2)
        s = (a + b + c) / 2.0
        area = np.sqrt(s * (s - a) * (s - b) * (s - c))
        circum_r = a * b * c / (4.0 * area)
        if circum_r < alpha:
            add_edge(edges, ia, ib)
            add_edge(edges, ib, ic)
            add_edge(edges, ic, ia)
    return edges

# Computing the alpha shape via Delauney alpha shape method
startTime = time.time()
edges = alpha_shape(xplot, alpha=5, only_outer=True)
print('edges: ', (edges))
endTime = time.time()
print('Delauney alpha shape method: ', endTime - startTime)

# Plotting the output
plt.figure()
plt.axis('equal')
plt.xlim(-0.015/2, 20 * 0.015/2)
plt.ylim(0, 0.000005)

plt.plot(xplot[:, 0], xplot[:, 1], '.')
print('test1 = ', xplot[[157, 79], 0])
print('test2 = ', xplot[[157, 79], 1])
print('type(xplot): ', type(xplot))
print('xplot.shape: ', xplot.shape)


print('')
for i, j in edges:
       print('i = {}, j = {}'.format(i, j))
       plt.plot(xplot[[i, j], 0], xplot[[i, j], 1])
plt.savefig('delauneyShape.png')

# Computing the alpha shape via alphashape package:

startTime = time.time()
alpha_shape = alphashape.alphashape(points2d, 0.2)
endTime = time.time()
print('alphashape package time: ', endTime - startTime)

fig, ax = plt.subplots()
ax.scatter(*zip(*points2d))
ax.add_patch(PolygonPatch(alpha_shape, alpha=0.2))
plt.savefig('alphashapePackage.png')


