import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch


def plot_figure1(x, y, tfa, asa, reg_asa, tilt, reg_tilt, vertices):

    fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(7, 10))

    ax[0][1].axis('off')

    v1 = np.linspace(min(tfa), max(tfa), 20, endpoint=True)
    v1_ = np.linspace(min(tfa), max(tfa), 5, endpoint=True)
    v2 = np.linspace(min(reg_asa * 1000), max(reg_asa * 1000), 20, endpoint=True)
    v2_ = np.linspace(min(reg_asa * 1000), max(reg_asa * 1000), 5, endpoint=True)
    v3 = np.linspace(min(reg_tilt), max(reg_tilt), 20, endpoint=True)
    v3_ = np.linspace(min(reg_tilt), max(reg_tilt), 5, endpoint=True)

    tmp1 = ax[0][0].tricontourf(y/1000, x/1000, tfa, 30, cmap='gist_ncar', levels=v1)
    tmp2 = ax[1][0].tricontourf(y/1000, x/1000, asa * 1000, 30, cmap='gist_ncar', levels=v2)
    tmp3 = ax[1][1].tricontourf(y/1000, x/1000, reg_asa * 1000, 30, cmap='gist_ncar', levels=v2)
    tmp4 = ax[2][0].tricontourf(y/1000, x/1000, tilt, 30, cmap='gist_ncar', levels=v3)
    tmp5 = ax[2][1].tricontourf(y/1000, x/1000, reg_tilt, 30, cmap='gist_ncar', levels=v3)


    plt.colorbar(tmp1, ax=ax[0][0], fraction=0.030, aspect=20, spacing='uniform', format='%.f', orientation='vertical',
                      ticks=v1_).set_label('(nT)', fontsize=10, labelpad=-20, y=-0.10, rotation=0)

    plt.colorbar(tmp2, ax=ax[1][0], fraction=0.030, aspect=20, spacing='uniform', format='%.f', orientation='vertical',
                      ticks=v2_).set_label('(nT/km)', fontsize=10, labelpad=-15, y=-0.10, rotation=0)

    plt.colorbar(tmp3, ax=ax[1][1], fraction=0.030, aspect=20, spacing='uniform', format='%.f', orientation='vertical',
                      ticks=v2_).set_label('(nT/km)', fontsize=10, labelpad=-15, y=-0.10, rotation=0)

    plt.colorbar(tmp4, ax=ax[2][0], fraction=0.030, aspect=20, spacing='uniform', format='%.1f', orientation='vertical',
                      ticks=v3_).set_label('(rad)', fontsize=10, labelpad=-20, y=-0.10, rotation=0)

    plt.colorbar(tmp5, ax=ax[2][1], fraction=0.030, aspect=20, spacing='uniform', format='%.1f', orientation='vertical',
                      ticks=v3_).set_label('(rad)', fontsize=10, labelpad=-20, y=-0.10, rotation=0)


    # Draw the polygons
    for b in vertices:
        path1 = Path(b)
        path2 = Path(b)
        path3 = Path(b)
        path4 = Path(b)
        path5 = Path(b)

        pathpatch1 = PathPatch(path1, facecolor='none', edgecolor='black', linewidth=1.5)
        pathpatch2 = PathPatch(path2, facecolor='none', edgecolor='black', linewidth=1.5)
        pathpatch3 = PathPatch(path3, facecolor='none', edgecolor='black', linewidth=1.5)
        pathpatch4 = PathPatch(path4, facecolor='none', edgecolor='black', linewidth=1.5)
        pathpatch5 = PathPatch(path5, facecolor='none', edgecolor='black', linewidth=1.5)

        ax[0][0].add_patch(pathpatch1)
        ax[1][0].add_patch(pathpatch2)
        ax[1][1].add_patch(pathpatch3)
        ax[2][0].add_patch(pathpatch4)
        ax[2][1].add_patch(pathpatch5)


    ax[0][0].set_xlabel('y (km)', fontsize=11)
    ax[1][0].set_xlabel('y (km)', fontsize=11)
    ax[1][1].set_xlabel('y (km)', fontsize=11)
    ax[2][0].set_xlabel('y (km)', fontsize=11)
    ax[2][1].set_xlabel('y (km)', fontsize=11)
    ax[0][0].set_ylabel('x (km)', fontsize=11)
    ax[1][0].set_ylabel('x (km)', fontsize=11)
    ax[2][0].set_ylabel('x (km)', fontsize=11)
    ax[1][1].set_ylabel('x (km)', fontsize=11)
    ax[2][1].set_ylabel('x (km)', fontsize=11)

    ax[0][0].text(1.2, 27, 'a)', fontsize=12, horizontalalignment='center', verticalalignment='center')
    ax[1][0].text(1.2, 27, 'b)', fontsize=12, horizontalalignment='center', verticalalignment='center')
    ax[1][1].text(1.2, 27, 'c)', fontsize=12, horizontalalignment='center', verticalalignment='center')
    ax[2][0].text(1.2, 27, 'd)', fontsize=12, horizontalalignment='center', verticalalignment='center')
    ax[2][1].text(1.2, 27, 'e)', fontsize=12, horizontalalignment='center', verticalalignment='center')

    ax[0][0].text(12, 21, 'A', fontsize=12, horizontalalignment='center', verticalalignment='center', weight='bold')
    ax[0][0].text(12, 13, 'B', fontsize=12, horizontalalignment='center', verticalalignment='center',  weight='bold')
    ax[0][0].text(20, 6, 'C', fontsize=12, horizontalalignment='center', verticalalignment='center',  weight='bold')
    ax[1][0].text(12, 21, 'A', fontsize=12, horizontalalignment='center', verticalalignment='center',  weight='bold')
    ax[1][0].text(12, 13, 'B', fontsize=12, horizontalalignment='center', verticalalignment='center',  weight='bold')
    ax[1][0].text(20, 6, 'C', fontsize=12, horizontalalignment='center', verticalalignment='center',  weight='bold')
    ax[1][1].text(12, 21, 'A', fontsize=12, horizontalalignment='center', verticalalignment='center',  weight='bold')
    ax[1][1].text(12, 13, 'B', fontsize=12, horizontalalignment='center', verticalalignment='center',  weight='bold')
    ax[1][1].text(20, 6, 'C', fontsize=12, horizontalalignment='center', verticalalignment='center',  weight='bold')
    ax[2][0].text(12, 21, 'A', fontsize=12, horizontalalignment='center', verticalalignment='center',  weight='bold')
    ax[2][0].text(12, 13, 'B', fontsize=12, horizontalalignment='center', verticalalignment='center',  weight='bold')
    ax[2][0].text(20, 6, 'C', fontsize=12, horizontalalignment='center', verticalalignment='center',  weight='bold')
    ax[2][1].text(12, 21, 'A', fontsize=12, horizontalalignment='center', verticalalignment='center',  weight='bold')
    ax[2][1].text(12, 13, 'B', fontsize=12, horizontalalignment='center', verticalalignment='center',  weight='bold')
    ax[2][1].text(20, 6, 'C', fontsize=12, horizontalalignment='center', verticalalignment='center',  weight='bold')

    ax[0][0].yaxis.set_ticks(np.arange(5, 30, step=5))
    ax[1][0].yaxis.set_ticks(np.arange(5, 30, step=5))
    ax[1][1].yaxis.set_ticks(np.arange(5, 30, step=5))
    ax[2][0].yaxis.set_ticks(np.arange(5, 30, step=5))
    ax[2][1].yaxis.set_ticks(np.arange(5, 30, step=5))
    ax[0][0].xaxis.set_ticks(np.arange(5, 30, step=5))
    ax[1][0].xaxis.set_ticks(np.arange(5, 30, step=5))
    ax[1][1].xaxis.set_ticks(np.arange(5, 30, step=5))
    ax[2][0].xaxis.set_ticks(np.arange(5, 30, step=5))
    ax[2][1].xaxis.set_ticks(np.arange(5, 30, step=5))

    ax[0][0].tick_params(axis='both', which='major', labelsize=10)
    ax[1][0].tick_params(axis='both', which='major', labelsize=10)
    ax[1][1].tick_params(axis='both', which='major', labelsize=10)
    ax[2][0].tick_params(axis='both', which='major', labelsize=10)
    ax[2][1].tick_params(axis='both', which='major', labelsize=10)

    plt.subplots_adjust(wspace=0.55, hspace=0.5)

    plt.savefig('figures/FIG1.png', bbox_inches='tight', dpi=600)
    plt.close('all')

    return



def plot_figure2(alpha, norm_sol_dx, norm_sol_dy, norm_sol_dz, alpha_vector):

    fig, ax = plt.subplots(figsize=(4, 3))

    ax.plot(np.log10(alpha), norm_sol_dx, '-', color='blue', markersize=6, label='S$_x$')
    ax.plot(np.log10(alpha), norm_sol_dy, color='red', markersize=6, label='S$_y$')
    ax.plot(np.log10(alpha), norm_sol_dz, color='green', markersize=6, label='S$_z$')

    ax.set_ylabel('S$_\mu(\u03B1)$', color='black', fontsize=11)
    ax.set_xlabel('log$_{10}$($\u03B1$)', fontsize=11)
    ax.xaxis.set_ticks(np.arange(min(np.log10(alpha)), max(np.log10(alpha)), step=3))

    ax.text(4.5, -0.01, '$\u03B1_{x}$', fontsize=7, color='blue', horizontalalignment='center', verticalalignment='center')
    ax.text(6.5, -0.015, '$\u03B1_{y}$', fontsize=7, color='red', horizontalalignment='center', verticalalignment='center')
    ax.text(5.60, -0.01, '$\u03B1_{z}$', fontsize=7, color='green', horizontalalignment='center', verticalalignment='center')

    ax.yaxis.set_ticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])

    ax.hlines(0.5, -6, 14, colors='black', linestyles='dashed')
    ax.vlines(np.round(alpha_vector[0], 1), 0, 0.5, colors = 'blue', linestyles = 'dashed')
    ax.vlines(np.round(alpha_vector[1], 1), 0, 0.5, colors = 'red', linestyles = 'dashed')
    ax.vlines(np.round(alpha_vector[2], 1), 0, 0.5, colors = 'green', linestyles = 'dashed')

    ax.tick_params(axis='both', which='major', labelsize=8)
    ax.legend(loc='best', fontsize=8, edgecolor='black')

    plt.savefig('figures/FIG2.png', bbox_inches='tight', dpi=600)
    plt.close('all')

    return



def plot_figure3(x, y, tfa, asa, reg_asa, tilt, reg_tilt):

    fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(7, 10))

    ax[0][1].axis('off')

    v1 = np.linspace(min(tfa), max(tfa), 25, endpoint=True)
    v1_ = np.linspace(min(tfa), max(tfa), 5, endpoint=True)
    v2 = np.linspace(min(reg_asa * 1000), max(reg_asa * 1000), 25, endpoint=True)
    v2_ = np.linspace(min(reg_asa * 1000), max(reg_asa * 1000), 5, endpoint=True)
    v3 = np.linspace(min(reg_tilt), max(reg_tilt), 25, endpoint=True)
    v3_ = np.linspace(min(reg_tilt), max(reg_tilt), 5, endpoint=True)

    tmp1 = ax[0][0].tricontourf(x/1000, y/1000, tfa, 30, cmap='gist_ncar', levels=v1)
    tmp2 = ax[1][0].tricontourf(x/1000, y/1000, asa * 1000, 30, cmap='binary', levels=v2)
    tmp3 = ax[1][1].tricontourf(x/1000, y/1000, reg_asa * 1000, 30, cmap='binary', levels=v2)
    tmp4 = ax[2][0].tricontourf(x/1000, y/1000, tilt, 30, cmap='gist_gray', levels=v3)
    tmp5 = ax[2][1].tricontourf(x/1000, y/1000, reg_tilt, 30, cmap='gist_gray', levels=v3)


    plt.colorbar(tmp1, ax=ax[0][0], fraction=0.030, aspect=20, spacing='uniform', format='%.f', orientation='vertical',
                      ticks=v1_).set_label('(nT)', fontsize=10, labelpad=-20, y=-0.10, rotation=0)

    plt.colorbar(tmp2, ax=ax[1][0], fraction=0.030, aspect=20, spacing='uniform', format='%.f', orientation='vertical',
                      ticks=v2_).set_label('(nT/km)', fontsize=10, labelpad=-15, y=-0.10, rotation=0)

    plt.colorbar(tmp3, ax=ax[1][1], fraction=0.030, aspect=20, spacing='uniform', format='%.f', orientation='vertical',
                      ticks=v2_).set_label('(nT/km)', fontsize=10, labelpad=-15, y=-0.10, rotation=0)

    plt.colorbar(tmp4, ax=ax[2][0], fraction=0.030, aspect=20, spacing='uniform', format='%.1f', orientation='vertical',
                      ticks=v3_).set_label('(rad)', fontsize=10, labelpad=-20, y=-0.10, rotation=0)

    plt.colorbar(tmp5, ax=ax[2][1], fraction=0.030, aspect=20, spacing='uniform', format='%.1f', orientation='vertical',
                      ticks=v3_).set_label('(rad)', fontsize=10, labelpad=-20, y=-0.10, rotation=0)


    ax[0][0].set_xlabel('y (km)')
    ax[1][0].set_xlabel('y (km)')
    ax[1][1].set_xlabel('y (km)')
    ax[2][0].set_xlabel('y (km)')
    ax[2][1].set_xlabel('y (km)')
    ax[0][0].set_ylabel('x (km)')
    ax[1][0].set_ylabel('x (km)')
    ax[2][0].set_ylabel('x (km)')
    ax[1][1].set_ylabel('x (km)')
    ax[2][1].set_ylabel('x (km)')

    ax[0][0].yaxis.set_ticks([8265, 8280, 8295])
    ax[1][0].yaxis.set_ticks([8265, 8280, 8295])
    ax[1][1].yaxis.set_ticks([8265, 8280, 8295])
    ax[2][0].yaxis.set_ticks([8265, 8280, 8295])
    ax[2][1].yaxis.set_ticks([8265, 8280, 8295])
    ax[0][0].xaxis.set_ticks([-20, 0, 20])
    ax[1][0].xaxis.set_ticks([-20, 0, 20])
    ax[1][1].xaxis.set_ticks([-20, 0, 20])
    ax[2][0].xaxis.set_ticks([-20, 0, 20])
    ax[2][1].xaxis.set_ticks([-20, 0, 20])

    ax[0][0].tick_params(axis='y', labelrotation=90)
    ax[1][0].tick_params(axis='y', labelrotation=90)
    ax[1][1].tick_params(axis='y', labelrotation=90)
    ax[2][0].tick_params(axis='y', labelrotation=90)
    ax[2][1].tick_params(axis='y', labelrotation=90)

    ax[0][0].text(-37.5, 8312, 'a)', fontsize=14, horizontalalignment='center', verticalalignment='center')
    ax[1][0].text(-37.5, 8312, 'b)', fontsize=14, horizontalalignment='center', verticalalignment='center')
    ax[1][1].text(-37.5, 8312, 'c)', fontsize=14, horizontalalignment='center', verticalalignment='center')
    ax[2][0].text(-37.5, 8312, 'd)', fontsize=14, horizontalalignment='center', verticalalignment='center')
    ax[2][1].text(-37.5, 8312, 'e)', fontsize=14, horizontalalignment='center', verticalalignment='center')

    plt.subplots_adjust(wspace=0.6, hspace=0.5)

    plt.savefig('figures/FIG3.png', bbox_inches='tight', dpi=600)
    plt.close('all')

    return



def plot_figure4(alpha, norm_sol_dx, norm_sol_dy, norm_sol_dz,  alpha_vector):

    fig, ax = plt.subplots(figsize=(4, 3))

    ax.plot(np.log10(alpha), norm_sol_dx, '-', color='blue', markersize=6, label='S$_x$')
    ax.plot(np.log10(alpha), norm_sol_dy, color='red', markersize=6, label='S$_y$')
    ax.plot(np.log10(alpha), norm_sol_dz, color='green', markersize=6, label='S$_z$')

    ax.set_ylabel('S$_\mu(\u03B1)$', color='black', fontsize=11)
    ax.set_xlabel('log$_{10}$($\u03B1$)', fontsize=11)
    ax.xaxis.set_ticks(np.arange(min(np.log10(alpha)), max(np.log10(alpha)), step=3))

    ax.text(5.2, 0.013, '$\u03B1_{x}$', fontsize=7, color='blue', horizontalalignment='center', verticalalignment='center')
    ax.text(2.8, 0.01, '$\u03B1_{y}=\u03B1_{z}$', fontsize=7, color='green', horizontalalignment='center', verticalalignment='center')

    ax.yaxis.set_ticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])

    ax.hlines(0.5, -6, 14, colors='black', linestyles='dashed')
    ax.vlines(np.round(alpha_vector[0], 1), 0, 0.5, colors='blue', linestyles='dashed')
    ax.vlines(np.round(alpha_vector[1], 1), 0, 0.5, colors='red', linestyles='dashed')
    ax.vlines(np.round(alpha_vector[2], 1), 0, 0.5, colors='green', linestyles='dashed')

    ax.tick_params(axis='both', which='major', labelsize=8)
    ax.legend(loc='best', fontsize=8, edgecolor='black')

    plt.savefig('FIG4.png', bbox_inches='tight', dpi=600)
    plt.close('all')

    return