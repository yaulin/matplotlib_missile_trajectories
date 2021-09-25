#!/usr/bin/env python

from trajectory_classes import *

dir1 = "WorkPackageM-20210521T090339Z-001/WorkPackageM/"

tdir = trajectory_dir(dir1)

palette1 = ['midnightblue','navy','darkblue','blue','slateblue','deepskyblue','cyan','fuchsia','orchid']
sns.set_palette(palette1)

tdir.plot_combined_xt(save = True)
tdir.plot_combined_yt(save = True)
tdir.plot_combined_zt(save = True)

tdir.plot_combined_grt(save = True)
tdir.plot_combined_alt(save = True)
tdir.plot_combined_drt(save = True)
tdir.plot_combined_crt(save = True)

tdir.plot_combined_vt(save = True)
tdir.plot_combined_at(save = True)
tdir.plot_combined_axt(save = True)
tdir.plot_combined_ayt(save = True)
tdir.plot_combined_azt(save = True)

tdir.plot_combined_pat(save = True)
tdir.plot_combined_hat(save = True)

tdir.plot_combined_mt(save = True)

tdir.plot_combined_am(save = True)

tdir.plot_combined_av(save = True)

tdir.plot_combined_agr(save = True)

tdir.plot_combined_xyz(save = True)
tdir.plot_combined_3D(save = True)

tdir.plot_combined_end_2D(save = True)

tdir.plot_combined_end_xyz(save = True)


