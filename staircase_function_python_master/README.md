# Python programs to apply regularized derivatives in the magnetic tilt derivative and gradient intensity data processing: a graphical procedure to choose the regularization parameter

by
Janaína A. Melo, Carlos A. Mendonça and Yara R. Marangoni 


## About

This paper has been submitted in the *Applied Computing and Geosciences*. Melo, J.A., Mendonça, C.A, Marangoni, Y.R., 2023. Python programs to apply regularized derivatives in the magnetic tilt derivative and gradient intensity data processing: a graphical procedure to choose the regularization parameter.

This repository contains the source code to perform the synthetic test and real data presented. The codes 'filtering.py', 'synthetic_data.py', 'real_data.py', and  'plot_figure.py' generate the results related to our methodology.

These programs are compatible with both Python 2.7 and Python 3.7 programming language.


## Abstract

The Tikhonov regularization parameter is a key parameter conditioning the smoothness degree of model parameters and associated model response in regularized inversion. Usual methods to determine a proper parameter (L-curve or the discrepancy principle, for example) are not readily applicable to the evaluation of regularized derivatives, since this formulation does not make explicit a set of model parameters that are necessary to implement these methods. We develop a procedure for the determination of the regularization parameter based on the graphical construction of a characteristic “staircase” function associated with the Euclidean norm of the regularized derivatives for a set of trial regularization parameters. This function is independent of model parameters and presents a smooth and monotonic variation. The regularization parameters at the upper step (low values) of the ''staircase'' function provide equivalent results to the non-regularized derivative, the parameters at the lower step (high values) leading to over-smoothed derivatives.  For the evaluated data sets, the proper regularization parameter is located in the slope connecting these two flat end-members of the staircase curve, thus balancing noise amplification against the amplitude loss in the transformed fields. A set of Python programs are presented to evaluate the regularization procedure in a well-known synthetic model composed of multiple (bulk and elongated) magnetic sources. This numerical approach also is applied in gridded aeromagnetic data covering high-grade metamorphic terrains of the Anápolis-Itauçu Complex in the Brasília Fold Belt central portion of Tocantins Province, central Brazil, characterized by multiple magnetic lineaments with different directions and intersections which are associated with shear zones, geologic faults, and intrusive bodies. The results obtained from the regularization procedure show efficiency in improving the maps of filtered fields, better tracking the continuity of magnetic lineaments and general geological trends. The results from the application in the Brasília Fold Belt enhance the importance and broader coverage of Pirineus Zone of High Strain.


## Content

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
	
Test data:

- synthetic_data.dat:
		Synthetic total-field anomaly data are available by Uieda et al. (2014) at 
		http://github.com/pinga-lab/paper-tle-euler-tutorial.	

- real_data.xyz:
		Real total-field anomaly database with code 3013 is requested for academic 
		purposes from the State of Goiás Division for Geology and Mining Affairs. 

Complementary files:

- batholith_vertices: 
		x and y coordinates of the batholith vertices to plot on synthetic data 
                figures.

- dike_vertices: 
		x and y coordinates of the dike vertices to plot on synthetic data 
		figures.

- sill_vertices: 
		x and y coordinates of the sill vertices to plot on synthetic data 
		figures.


## Getting the code

You can download a copy of all the files in this repository by cloning the
[git](https://git-scm.com/) repository:

    git clone https://github.com/janainaanjos/Staircase_Function.git

or [download a zip archive](https://github.com/janainaanjos/Staircase_Function/archive/master.zip).


## Dependencies

The Python program "filtering.py" requires the Python packages "numpy" and "sklearn", the 
scripts "synthetic_data.py" and "real_data.py" require the Python package "numpy", and the script 
"plot_figure.py" requires the Python packages "numpy" and "matplotlib". 
The easier way to get Python and all libraries installed is through the Anaconda Python 
distribution (https://www.anaconda.com/distribution/). After installed Anaconda, install the libraries 
by running the following command in your terminal:

	conda install numpy matplotlib sklearn


## Reproducing the results

For the synthetic and real data, the results are reproducible from the folder '/results' and the figures 
are found in the folder '/figures'. Running the codes 'synthetic_data.py' and 'real_data.py' will allow 
the reproduction of the results of our methodology. For more information read the file 'README.md'or 
'README.txt' in the folder '/code'.


## License

All source code is made available under a MIT license. You can freely use 
and modify the code, without warranty, so long as you provide attribution
to the authors. See 'LICENSE.md' for the full license text.

The manuscript text is open source. The authors reserve the rights to the 
article content, which is currently submitted for publication in the
*Applied Computing and Geosciences*.
