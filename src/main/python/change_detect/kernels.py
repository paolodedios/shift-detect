#!/usr/bin/env python
# -*- c-file-style: "sourcery" -*-
#
# Use and distribution of this software and its source code is governed
# by the terms and conditions defined in the "LICENSE" file that is part
# of this source code package.
#
"""
Kernel interfaces
"""
from __future__             import print_function

import numpy     as numpy


class Estimator :
    """
    Marker interface for all Estimators. Provides basic apply() style
    interface and a show() method for debugging
    """
    def apply(self, samples=None) :
        self.show("Missing Implementation", samples)


    def show(self, displayName=None, estimate=None, title=None) :
        print("[" + title + "]")
        print(displayName + " : " + str(estimate) + "\n")
        print("---------------")


class Vector :
    @classmethod
    def show(cls, displayName=None, vector=None, options=None) :
        if options["--debug"] is None :
            return

        print("[" + displayName + "]")
        print("elements : " + str(numpy.size(vector)) + "\n")
        print(str(vector) + "\n")
        print("---------------")


class Matrix(Vector) :
    @classmethod
    def show(cls, displayName=None, matrix=None, options=None) :
        if options["--debug"] is None :
                return

        print("[" + displayName + "]")
        print("(rows, cols) : " + str(matrix.shape) + "\n")
        print(str(matrix) + "\n")
        print("---------------")


class Kernel(Matrix) :
    def apply(self, samples=None) :
        self.show("Missing Implementation", samples)

    def show(self, results=None, displayName=None, options=None) :
        Matrix.show(displayName, results)


class GaussianKernel(Kernel) :

    sigmaWidth = None


    def __init__(self, sigma=1.0) :
        self.sigmaWidth = sigma


    def computeDistance(self, samples=None, sampleMeans=None) :
        """
        Compute the distances between points in the sample's feature space
        to points along the center of the distribution
        """
        (sampleRows, sampleCols) = samples.shape
        (meanRows  , meanCols  ) = sampleMeans.shape

        squaredSamples = sum(samples**2, 0)
        squaredMeans   = sum(sampleMeans**2, 0)

        return numpy.tile(squaredMeans, (sampleCols, 1)) + numpy.tile(squaredSamples[:, None], (1, meanCols)) - 2 * numpy.dot(samples.T, sampleMeans)


    def apply(self, samples=None, sampleMeans=None) :
        """
        Computes an n-dimensional Gaussian/RBF kernel matrix by taking points
        in the sample's feature space and maps them to kernel coordinates in
        Hilbert space by calculating the distance to each point in the sample
        space and taking the Gaussian function of the distances.

           K(X,Y) = exp( -(|| X - Y ||^2) / (2 * sigma^2) )

        where X is the matrix of data points in the sample space,
              Y is the matrix of gaussian centers in the sample space
             sigma is the width of the gaussian function being used
        """
        squaredDistance = self.computeDistance(samples, sampleMeans)
        return numpy.exp(-squaredDistance / ( 2 * (self.sigmaWidth**2) ))
