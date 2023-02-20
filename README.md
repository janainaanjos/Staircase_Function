# Python programs to apply regularized derivatives in the magnetic tilt derivative and gradient intensity data processing: a graphical procedure to choose the regularization parameter

by
Janaína A. Melo, Carlos A. Mendonça and Yara R. Marangoni 

## About

This paper has been published in the *Computers & Geosciences*. Melo, J.A., Mendonça, C.A, Marangoni, Y.R., 2023. Python programs to apply regularized derivatives in the magnetic tilt derivative and gradient intensity data processing: a graphical procedure to choose the regularization parameter. Computers & Geosciences.

This repository contains the source code to perform the synthetic test and real data presented. The codes 'filtering.py', 'synthetic_data.py', 'real_data.py' and the code 'plot_figure.py' to generate the results related to our methodology.

These programs are compatible with both Python 2.7 and Python 3.7 programming language.

## Abstract

The Tikhonov regularization parameter is a key parameter conditioning the smoothness degree of model parameters and associated model response in regularized inversion. Usual methods to determine a proper parameter as L-curve or the discrepancy principle, for example, are not readily applicable to the evaluation of regularized derivatives since this formulation does not make explicit a set of model parameters, which are necessary to implement these methods. We develop an iterative procedure for the determination of the regularization parameter based on the graphical construction of a characteristic “staircase” function associated with the Euclidean norm of the regularized derivative for a set of trial regularization parameters. This function is independent of model parameters and presents a smooth and monotonic variation, where the regularization parameters at the upper step (low values) of the ''staircase'' function provide equivalent results to the non-regularized derivative and the regularization parameters at the lower step (high values) of the stair over-smooth the derivative. The proper regularization parameter is located in the slope connecting these two flat end-members of the curve, balancing the noise amplification against amplitude reduction in transformed fields. A set of Python programs are presented to evaluate the regularization procedure in a well-known synthetic model composed of different magnetic sources. This numerical approach also is applied in gridded aeromagnetic data covering the Pirineus Syntax in the Brasília Fold Belt central portion of Tocantins Province, state of Goiás, characterized by multiple magnetic lineaments with different directions and intersections which are associated with shear zones, geologic faults, and intrusive bodies. The results obtained from the regularization procedure show efficiency in improving quality filtered fields, enhancing the continuity of magnetic lineaments and general trends.

## Content

- filtering.py:
	General Python module containing the functions to compute the non-regularized and 
        regularized directional derivatives, S-function, S-function values linear model, 
        and analytical signal amplitude and slope.
	
- synthetic_data.py:
	Python script to generate the synthetic results. The script loads the total-field 
	anomaly of a synthetic model from the file "synthetic_data.dat" and computes the 
	non-regularized and regularized directional derivatives, S-function, S-function 
	values linear model, and analytical signal amplitude and slope using the functions 
	in "filtering.py". The results are generated using the function "plot_figure.py" 
	for the plots.

- real_data.py:
	Python script to generate the real results. The script loads the total-field 
	anomaly of a real data from the file "real_data.xyz" and computes the 
	non-regularized and regularized directional derivatives, S-function, S-function 
	values linear model, and analytical signal amplitude and slope using the functions 
	in "filtering.py". The results are generated using the function "plot_figure.py" 
	for the plots.
	
- plot_figure.py:
	Python script to generate the figures of the synthetic and real data.
	
Test data:

- synthetic_data.dat:
		Synthetic total-field anomaly data are available by Uieda et al. (2014) at 
		http://github.com/pinga-lab/paper-tle-euler-tutorial.	

- real_data.xyz:
		Real total-field anomaly database with code 3013 is requested for academic 
		purposes from the State of Goiás Division for Geology and Mining Affairs. 

## Getting the code

You can download a copy of all the files in this repository by cloning the
[git](https://git-scm.com/) repository:

    git clone https://github.com/janainaanjos/Staircase_Function.git

or [download a zip archive](https://github.com/janainaanjos/Staircase_Function/archive/master.zip).


## Dependencies

The Python program "filtering.py" requires the Python packages "numpy" and "sklearn.linear_model", and 
the scripts "synthetic_data.py" and "real_data.py" require the Python package "numpy", and the script 
"plot_figure.py" requires the Python packages "numpy" and "matplotlib". 
The easier way to get Python and all libraries installed is through the Anaconda Python 
distribution (https://www.anaconda.com/distribution/). After installed Anaconda, install the libraries 
by running the following command in your terminal:

	conda install numpy matplotlib

## Reproducing the results

For the synthetic and real data, the results are reproducible from the folder '/results' and the figures 
are found in the folder '/figures'. Running the codes 'synthetic_data.py' and 'real_data.py' will allow 
the reproduction of the results of our methodology. For more information read the file 'README.md'or 
'README.txt' in the folder '/code'.


## License

All source code is made available under a MIT license. You can freely use 
and modify the code, without warranty, so long as you provide attribution
to the authors. See 'LICENSE.md' for the full license text.

The manuscript text is not open source. The authors reserve the rights to 
the article content, which is currently submitted for publication in the
*Computers & Geosciences*.
