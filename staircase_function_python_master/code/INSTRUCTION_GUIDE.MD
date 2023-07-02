# Python programs to apply regularized derivatives in the magnetic tilt derivative and gradient intensity data processing: a graphical procedure to choose the regularization parameter

by Janaína A. Melo (IAG-USP), Carlos A. Mendonça (IAG-USP) and Yara R. Marangoni (IAG-USP) (2023)

Email: janaina.melo@usp.br (J.A. Melo); carlos.mendonca@iag.usp.br (C.A. Mendonça); yaramaran@usp.br. (Y.R. Marangoni)

This repository contains several Python codes and synthetic and real data examples for a paper about the open-source package staircase function. The synthetic and real example data reproduce the results and figures shown in the publication. The codes 'filtering.py', 'synthetic_data.py', 'real_data.py', and 'plot_figure.py' are compatible with both Python 2.7 and Python 3.7 programming languages. To run the main programs "synthetic_data.py" and "real_data.py", the numpy library is required. In addition, the numpy and sklearn.linear_model libraries are necessary to run the complementary code "filtering.py"  and the matplotlib and numpy libraries are required to run the script "plot_figure.py".


1 - Abstract

2 - Content

3 - Prerequisites

4 - Parameterization

5 - Running the files

6 - License

===============================================================================


1 - Abstract
----------------------
The Tikhonov regularization parameter is a key parameter conditioning the smoothness degree of model parameters and associated model response in regularized inversion. Usual methods to determine a proper parameter (L-curve or the discrepancy principle, for example) are not readily applicable to the evaluation of regularized derivatives, since this formulation does not make explicit a set of model parameters that are necessary to implement these methods. We develop a procedure for the determination of the regularization parameter based on the graphical construction of a characteristic “staircase” function associated with the Euclidean norm of the regularized derivatives for a set of trial regularization parameters. This function is independent of model parameters and presents a smooth and monotonic variation. The regularization parameters at the upper step (low values) of the ''staircase'' function provide equivalent results to the non-regularized derivative, the parameters at the lower step (high values) leading to over-smoothed derivatives.  For the evaluated data sets, the proper regularization parameter is located in the slope connecting these two flat end-members of the staircase curve, thus balancing noise amplification against the amplitude loss in the transformed fields. A set of Python programs are presented to evaluate the regularization procedure in a well-known synthetic model composed of multiple (bulk and elongated) magnetic sources. This numerical approach also is applied in gridded aeromagnetic data covering high-grade metamorphic terrains of the Anápolis-Itauçu Complex in the Brasília Fold Belt central portion of Tocantins Province, central Brazil, characterized by multiple magnetic lineaments with different directions and intersections which are associated with shear zones, geologic faults, and intrusive bodies. The results obtained from the regularization procedure show efficiency in improving the maps of filtered fields, better tracking the continuity of magnetic lineaments and general geological trends. The results from the application in the Brasília Fold Belt enhance the importance and broader coverage of Pirineus Zone of High Strain.


2 - Content
----------------------

Python codes:

	- filtering.py:
		General Python module containing the functions to compute the non-regularized and 
        	regularized directional first-order derivatives, S-function of the regularized 
		directional first-order derivatives, regularization parameters, analytical signal 
		amplitude and tilt derivative.
	
	- synthetic_data.py:
		Python script to generate the synthetic results. The script loads the total-field 
		anomaly of a synthetic model from the file "synthetic_data.dat" and computes the 
		non-regularized and regularized first-order derivatives, S-function of the regularized 
		first-order derivatives, regularization parameters, analytical signal amplitude and 
		tilt derivative using the functions in "filtering.py". The figures are generated using 
		the function "plot_figure.py". 

	- real_data.py:
		Python script to generate the real results. The script loads the total-field 
		anomaly of a real data from the file "real_data.xyz" and computes the non-regularized 
		and regularized first-order derivatives, S-function of the regularized first-order 
		derivatives, regularization parameters, analytical signal amplitude and tilt derivative 
		using the functions in "filtering.py". The figures are generated using the function 
		"plot_figure.py". 
	
	- plot_figure.py:
		Python script to generate the figures of the synthetic and real data.
	
Outputs (folders): 
 
	- figures - figures of the real and synthetic data will be saved in this folder. The figures 
		    generated may differ from the publication and can be adapted in the script 
		    'plot_figure.py'.
						 
	- results - xyz files of regularized and non-regularized analytical signal amplitude and 
                    regularized and non-regularized tilt derivative.

Test data:

	- input/synthetic_data.dat
		    Synthetic total-field anomaly data are available by Uieda et al. (2014) at 
		    http://github.com/pinga-lab/paper-tle-euler-tutorial.	

	- input/real_data.xyz
		    Real total-field anomaly database with code 3013 is requested for academic 
		    purposes from the State of Goiás Division for Geology and Mining Aff.

Complementary files:

	- input/batholith_vertices: 
		    x and y coordinates of the batholith vertices to plot on synthetic data 
		    figures.
  
	- input/dike_vertices: 
		    x and y coordinates of the dike vertices to plot on synthetic data 
		    figures.

	- input/sill_vertices: 
		    x and y coordinates of the sill vertices to plot on synthetic data 
		    figures.


3 - Prerequisites
----------------------
The Python program "filtering.py" requires the Python packages "numpy" and "sklearn.linear_model", and 
the scripts "synthetic_data.py" and "real_data.py" require the Python package "numpy", and the script 
"plot_figure.py" requires the Python packages "numpy" and "matplotlib". 
The easier way to get Python and all libraries installed is through the Anaconda Python 
distribution (https://www.anaconda.com/distribution/). After installed Anaconda, install the libraries 
by running the following command in your terminal:

	conda install numpy matplotlib sklearn.linear_model

 
4 - Parameterization
----------------------
To construct the S-function, the user must configure the parameter 'alpha_test' that corresponds 
to the variation range of the trial regularization parameters to calculate the Euclidean norm of 
the regularized derivatives.

To determine the regularization parameter associated with the Euclidean norm specific-value in 
the slope of the S-function, the user must configure two parameters: 'inferior_limit' and 
'upper_limit'. These parameters represent the interval limits in which the S-function presents a 
linear variation.


5 - Running the files
----------------------
After Anaconda and the libraries are installed, you need to run 
the codes 'synthetic_data.py' and 'real_data.py' to generate the 
synthetic and real data results, respectively.
There are two easy ways to run:

1. Via command line: 

	1.1 On linux based systems open the command prompt windows (terminal), and run the command:
	
	On Python 2.7: python synthetic_data.py 
	On Python 2.7: python real_data.py 

	On Python 3.7: python3 synthetic_data.py 
	On Python 3.7: python3 real_data.py 

	1.2 On windows based systems open the Iphyton console (Python 2.7) or 
	Anaconda Navigator and then Jupyter QtConsole (Python 3.7), and run the command:

	run synthetic_data.py
	run real_data.py

2. Open the PyCharm program that comes with the Ananconda installation. In the PyCharm, open
the example script "synthetic_data.py" or "real_data.py" and click in "Run" inside the PyCharm
to execute it.

If everything runs ok, the figures and results will be saved, respectively, in the folders: 
'/figures' and '/results'.


6 - License
----------------------
The following legal note is restricted solely to the content of the named files. It cannot
overrule licenses from the Python standard distribution modules, which are imported and
used therein.

The 'filtering.py', 'synthetic_data.py', 'real_data.py' and 'plot_figure.py' files are 
distributed under the following license agreement:

MIT license

Copyright (c) 2023 Janaína A. Melo, Carlos A. Mendonça and Yara R. Marangoni.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
* Neither the names of the copyright holders nor the names of any contributors
  may be used to endorse or promote products derived from this software
  without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
