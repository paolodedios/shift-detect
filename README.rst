===============================
Covariate shift estimator
===============================

Learns a covariate shift estimator for a given dataset via a kernel method using
the Relative Unconstrained Least-Squares Importance Fitting algorithm [1].

The RULSIF kernel method estimates the relative ratio of probability densities

P(X_reference) / (alpha * P(X_reference) + (1 - alpha) * P(X_test))

from samples:

X_test[i] | X_test[i] in R^{d}, with i=1 to X_test{N}

drawn independently from P(X_test)

and samples

X_reference[i] | X_reference[i] in R^{d}, with i=1 to X_reference{N}

drawn independently from P(X_reference)

Using relative density ratios allows the RULSIF method to calculate a divergence
score between a reference and test sample.


Usage
=====

::

    $ python
    >>> import numpy
    >>> from shift_detect import rulsif
    >>> estimator = RULSIF()

    # Acquire training data
    >>> X_reference_train = numpy.array([[-327.538995,1060.88410,-5135.11159], \
                                         [-6079.76383,4540.07072, 4683.89186], \
                                         [-519.485848,-65.427245,-460.108594], \
                                         [-102.050993,-486.05520,-373.829956]])

    >>> X_test_train      = numpy.array([[4968.97172, 3051.50683,-102.050991], \
                                         [-5501.4825,-1951.72530,-44.1323003], \
                                         [2872.91368,-555.026187, 1582.54918], \
                                         [-715.46199,-544.196344,-61.4378131]])

    # Train the model
    >>> estimator.train(X_reference_train, X_test_train)

    # Compare real data using the trained estimator
    >>> for (X_reference, X_test) in real_dataset :
    >>>    divergence_score = estimator.apply(X_reference, X_test)


Installation
============

::

    $ pip install shift-detect

Development
===========

To run the all tests run
::

    $ pyb run_unit_tests / $ pyb run_integration_tests

    or

    $ tox


References
==========

1. Relative Density-Ratio Estimation for Robust Distribution Comparison. Makoto Yamada,
   Taiji Suzuki, Takafumi Kanamori, Hirotaka Hachiya, and Masashi Sugiyama. NIPS,
   page 594-602. (2011)
