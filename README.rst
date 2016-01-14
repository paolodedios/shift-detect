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
