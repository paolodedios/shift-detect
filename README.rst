===============================
Covariate shift estimator
===============================

Learns a covariate shift estimator for a given dataset via Relative
Unconstrained Least-Squares Importance Fitting (with leave-one-out cross
validation)

The RULSIF method estimates the relative ratio of probability densities

P(X_reference) / (alpha * P(X_reference) + (1 - alpha) * P(X_test))

from samples:

X_test[i] | X_test[i] in R^{d}, with i=1 to X_test{N}

drawn independently from P(X_test)

and samples

X_reference[i] | X_reference[i] in R^{d}, with i=1 to X_reference{N}

drawn independently from P(X_reference)

Using relative density ratios allows the RULSIF method to calculate a divergence
score between a reference and test sample

Usage
=====

 $ python
    >>> import numpy
    >>> from change_detect import rulsif
    >>> estimator = RULSIF()

    >>> X_reference_train = numpy.array([[-327.538995628852,1060.88410310621,-5135.11159167599], \
                                         [-6079.76383170992,4540.07072474003, 4683.89186361784], \
                                         [-519.48584881375 ,-65.427245639234,-460.108594708504], \
                                        [-102.050993806512,-486.055204138377,-373.829956812207]])

    >>> X_test_train      = numpy.array([[4968.97172846034 ,3051.50683649008 ,-102.050993806512], \
                                         [-5501.48250592865,-1951.72530129918,-44.1323008447163], \
                                         [2872.91368914527 ,-555.026187729457, 1582.54918268909], \
                                         [-715.46199368274 ,-544.196344693367, -61.437813172935]])

    >>> estimator.train(X_reference_train, X_test_train)    # Train the model

    >>> for (X_reference, X_test) in real_dataset :         # Compare real data using the trained estimator
    >>>    divergence_score = estimator.apply(X_reference, X_test)


Installation
============

::

    $ pip install change-detect

Development
===========

To run the all tests run::

    $ pyb run_unit_tests / $ pyb run_integration_tests

    or

    $ tox
