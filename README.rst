===============================
Covariate shift estimator
===============================

Learns a covariate shift estimator for a given dataset via Relative
Unconstrained Least-Squares Importance Fitting (with leave-one-out cross
validation)

The RULSIF method estimates the relative ratio of probability densities

P(Numerator[x]) / (alpha * P(Numerator[x]) + (1 - alpha) * P(Denominator[x]))

from samples:

Denominator[x_i] | Denominator[x_i] in R^{d}, with i=1 to Denominator{N}

drawn independently from P(Denominator[x])

and samples

Numerator[x_i] | Numerator[x_i] in R^{d}, with i=1 to Numerator{N}

drawn independently from P(Numerator[x])

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
