import numpy as np
import matplotlib.pyplot as plt



def plot_figure1(x, y, tfa, asa, reg_asa, tilt, reg_tilt):

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

    ax[0][0].set_title('TFA')
    ax[1][0].set_title('ASA')
    ax[1][1].set_title('REG ASA')
    ax[2][0].set_title('TDR')
    ax[2][1].set_title('REG TDR')

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

    plt.savefig('figures/FIG1.png', bbox_inches='tight', dpi=600)
    plt.close('all')

    return



def plot_figure2(alpha, norm_sol_dx, norm_sol_dy, norm_sol_dz,  alpha_vector):

    fig, ax = plt.subplots(figsize=(4, 3))

    ax.plot(np.log10(alpha), norm_sol_dx, '-', color='blue', markersize=6, label='$x$')
    ax.plot(np.log10(alpha), norm_sol_dy, color='red', markersize=6, label='$y$')
    ax.plot(np.log10(alpha), norm_sol_dz, color='green', markersize=6, label='$z$')

    ax.set_ylabel('||$\phi_\mu$($\u03B1$)$||_2$', color='black', fontsize=11)
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

    plt.savefig('figures/FIG2.png', bbox_inches='tight', dpi=600)
    plt.close('all')

    return